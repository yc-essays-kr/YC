import os
import re

def remove_thanks_section(content):
    """Remove the 'Thanks to...' section from the essay content."""
    # Pattern to match "Thanks to" paragraph at the end
    # This pattern looks for "Thanks to" followed by any text until the end
    pattern = r'\n\n+Thanks to [^\n]+.*$'

    # Remove the thanks section
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)

    return cleaned_content

def process_essay_files():
    """Process all markdown files in the essays directory."""
    essays_dir = 'essays'
    processed = 0

    for filename in os.listdir(essays_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(essays_dir, filename)

            # Read the file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if it contains "Thanks to"
            if 'Thanks to' in content:
                # Remove the thanks section
                cleaned_content = remove_thanks_section(content)

                # Write back to file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)

                processed += 1
                print(f"✓ Processed: {filename}")
            else:
                print(f"- Skipped (no 'Thanks to' found): {filename}")

    print(f"\n=== Summary ===")
    print(f"Total files processed: {processed}")

if __name__ == "__main__":
    process_essay_files()
