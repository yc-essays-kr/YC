import os
import anthropic
from pathlib import Path
import time

def summarize_essay(client, title, content):
    """Summarize essay using Claude API to 300-500 characters."""
    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"""다음 에세이를 300~500자 내외로 한국어로 요약해주세요. 핵심 메시지와 주요 내용만 간결하게 담아주세요.

제목: {title}

내용:
{content[:4000]}

요약:"""
                }
            ]
        )

        summary = message.content[0].text.strip()
        return summary

    except Exception as e:
        print(f"  ✗ Error summarizing: {str(e)}")
        return None

def process_essays():
    """Process all essays and create summaries."""
    # Initialize Anthropic client
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        return

    client = anthropic.Anthropic(api_key=api_key)

    original_dir = Path('essays/original')
    summary_dir = Path('essays/original/summary')
    summary_dir.mkdir(parents=True, exist_ok=True)

    essay_files = sorted(original_dir.glob('*.md'))
    total = len(essay_files)

    print(f"Summarizing {total} essays...")

    successful = 0
    failed = 0

    for i, filepath in enumerate(essay_files, 1):
        try:
            # Check if summary already exists
            summary_path = summary_dir / filepath.name
            if summary_path.exists():
                print(f"[{i}/{total}] Skipped (already exists): {filepath.name}")
                successful += 1
                continue

            # Read original essay
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title
            lines = content.strip().split('\n')
            title = lines[0] if lines else filepath.stem

            print(f"[{i}/{total}] Summarizing: {filepath.name}")

            # Summarize
            summary = summarize_essay(client, title, content)

            if summary:
                # Save summary
                with open(summary_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n\n{summary}\n")

                print(f"  ✓ Saved: {summary_path.name}")
                successful += 1
            else:
                failed += 1

            # Rate limiting - wait a bit between requests
            if i < total:
                time.sleep(0.5)

        except Exception as e:
            print(f"  ✗ Error processing {filepath.name}: {str(e)}")
            failed += 1

    print(f"\n=== Summary ===")
    print(f"Total essays: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    process_essays()
