import os
import anthropic
from pathlib import Path
import time
import httpx

def translate_essay(client, content, is_summary=False, max_retries=3):
    """Translate essay to Korean using Claude API with timeout and retry."""
    if is_summary:
        prompt = f"""다음 요약문을 자연스러운 한국어로 번역해주세요.

{content}

번역:"""
    else:
        # For full essays, translate in chunks if too long
        max_chars = 8000
        if len(content) > max_chars:
            # Translate first part
            content = content[:max_chars]
            print(f"    (Warning: Content truncated to {max_chars} characters)")

        prompt = f"""다음 에세이를 자연스러운 한국어로 번역해주세요. 제목도 함께 번역하고, 원문의 톤과 뉘앙스를 최대한 살려주세요.

{content}

번역:"""

    # Retry logic with timeout
    for attempt in range(max_retries):
        try:
            message = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                timeout=120.0,  # 120 second timeout
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            translation = message.content[0].text.strip()
            return translation

        except httpx.TimeoutException:
            print(f"    ⚠ Timeout (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retry
                continue
            else:
                print(f"    ✗ Failed after {max_retries} attempts (timeout)")
                return None
        except Exception as e:
            print(f"    ✗ Error translating: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            else:
                return None

    return None

def translate_original_essays():
    """Translate all original essays to Korean."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        return

    client = anthropic.Anthropic(api_key=api_key)

    original_dir = Path('essays/original')
    translated_dir = Path('essays/translated')
    translated_dir.mkdir(parents=True, exist_ok=True)

    essay_files = sorted(original_dir.glob('*.md'))
    total = len(essay_files)

    print(f"Translating {total} original essays to Korean...")

    successful = 0
    failed = 0

    for i, filepath in enumerate(essay_files, 1):
        try:
            # Check if translation already exists
            translated_path = translated_dir / filepath.name
            if translated_path.exists():
                print(f"[{i}/{total}] Skipped (already exists): {filepath.name}")
                successful += 1
                continue

            # Read original essay
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"[{i}/{total}] Translating: {filepath.name}")

            # Translate
            translation = translate_essay(client, content, is_summary=False)

            if translation:
                # Save translation
                with open(translated_path, 'w', encoding='utf-8') as f:
                    f.write(translation)

                print(f"  ✓ Saved: {translated_path.name}")
                successful += 1
            else:
                failed += 1

            # Rate limiting
            if i < total:
                time.sleep(0.5)

        except Exception as e:
            print(f"  ✗ Error processing {filepath.name}: {str(e)}")
            failed += 1

    print(f"\n=== Original Essays Translation Summary ===")
    print(f"Total: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

def translate_summary_essays():
    """Translate all summary essays to Korean."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        return

    client = anthropic.Anthropic(api_key=api_key)

    summary_dir = Path('essays/original/summary')
    translated_summary_dir = Path('essays/translated/summary')
    translated_summary_dir.mkdir(parents=True, exist_ok=True)

    if not summary_dir.exists():
        print(f"Summary directory does not exist: {summary_dir}")
        return

    summary_files = sorted(summary_dir.glob('*.md'))
    total = len(summary_files)

    print(f"\nTranslating {total} summary essays to Korean...")

    successful = 0
    failed = 0

    for i, filepath in enumerate(summary_files, 1):
        try:
            # Check if translation already exists
            translated_path = translated_summary_dir / filepath.name
            if translated_path.exists():
                print(f"[{i}/{total}] Skipped (already exists): {filepath.name}")
                successful += 1
                continue

            # Read summary
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"[{i}/{total}] Translating summary: {filepath.name}")

            # Translate
            translation = translate_essay(client, content, is_summary=True)

            if translation:
                # Save translation
                with open(translated_path, 'w', encoding='utf-8') as f:
                    f.write(translation)

                print(f"  ✓ Saved: {translated_path.name}")
                successful += 1
            else:
                failed += 1

            # Rate limiting
            if i < total:
                time.sleep(0.5)

        except Exception as e:
            print(f"  ✗ Error processing {filepath.name}: {str(e)}")
            failed += 1

    print(f"\n=== Summary Essays Translation Summary ===")
    print(f"Total: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == "original":
            translate_original_essays()
        elif mode == "summary":
            translate_summary_essays()
        else:
            print("Usage: python translate_essays.py [original|summary]")
    else:
        print("Translating both original and summary essays...")
        translate_original_essays()
        translate_summary_essays()
