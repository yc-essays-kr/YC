import os
import re
from pathlib import Path

# 카테고리 정의 (디자인 가이드 기준)
CATEGORIES = {
    '마인드셋': ['mindset', 'think', 'work hard', 'passion', 'determination', 'persistence', 'stubborn',
                 'wisdom', 'taste', 'good', 'heresy', 'ideas', 'smart', 'nerds', 'noob', 'learning',
                 'procrastination', 'disagree', 'love', 'write', 'essay', 'philosophy', 'alien'],
    '시장진입': ['market', 'users', 'product', 'launch', 'scale', 'growth', 'traction', 'pmf',
                 'competition', 'customer', 'domain', 'industry', 'bubble', 'web', 'google',
                 'apple', 'microsoft', 'yahoo', 'twitter', 'airbnb'],
    '펀드레이징': ['funding', 'fundraising', 'investor', 'vc', 'venture', 'money', 'angel',
                  'valuation', 'equity', 'investment', 'capital', 'raise', 'pitch', 'convince',
                  'herd', 'squeeze', 'super angel', 'rich'],
    '창업기초': ['startup', 'founder', 'company', 'start', 'yc', 'y combinator', 'idea',
                'mvp', 'launch', 'die', 'mistake', 'lesson', 'begin', 'early', 'before',
                'version 1', 'first', 'hub', 'silicon valley'],
    '기술/개발': ['programming', 'code', 'hacker', 'software', 'language', 'lisp', 'python',
                 'java', 'technology', 'developer', 'computer', 'algorithm', 'patent',
                 'design', 'architecture', 'web app', 'spam', 'filter', 'mac'],
    '조직문화': ['team', 'culture', 'people', 'hiring', 'employee', 'boss', 'management',
                'organization', 'mean', 'nice', 'schlep', 'relentless', 'nerd', 'marginal',
                'Jessica', 'cofounder', 'ambitious'],
    '성장전략': ['scale', 'growth', 'strategy', 'business', 'model', 'expansion', 'market',
                 'revenue', 'profit', 'metrics', 'default alive', 'ramen profitable',
                 'organic', 'returns', 'wealth', 'inequality']
}

def extract_title_and_date(content):
    """Extract title and date from essay content."""
    lines = content.strip().split('\n')
    title = lines[0] if lines else 'Untitled'

    # Look for date in first few lines
    date = ''
    for line in lines[:10]:
        date_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}', line)
        if date_match:
            date = date_match.group(0)
            break

    return title, date

def categorize_essay(title, content):
    """Categorize essay based on title and content keywords."""
    text = (title + ' ' + content).lower()

    category_scores = {}
    for category, keywords in CATEGORIES.items():
        score = sum(1 for keyword in keywords if keyword.lower() in text)
        category_scores[category] = score

    # Get category with highest score
    best_category = max(category_scores, key=category_scores.get)

    # If no clear match, default to 마인드셋
    if category_scores[best_category] == 0:
        best_category = '마인드셋'

    return best_category

def process_essays():
    """Process all essays and categorize them."""
    original_dir = Path('essays/original')
    output_dir = Path('essays')

    essay_files = sorted(original_dir.glob('*.md'))
    total = len(essay_files)

    print(f"Processing {total} essays...")

    category_stats = {cat: 0 for cat in CATEGORIES.keys()}

    for i, filepath in enumerate(essay_files, 1):
        try:
            # Read original essay
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title and date
            title, date = extract_title_and_date(content)

            # Categorize
            category = categorize_essay(title, content)
            category_stats[category] += 1

            # Create output with YAML front matter
            output_content = f"""---
title: {title}
date: {date}
category: {category}
original_file: {filepath.name}
---

{content}
"""

            # Save to essays folder
            output_path = output_dir / filepath.name
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output_content)

            print(f"[{i}/{total}] {filepath.name} → {category}")

        except Exception as e:
            print(f"✗ Error processing {filepath.name}: {str(e)}")

    # Print statistics
    print("\n=== Category Statistics ===")
    for category, count in sorted(category_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{category}: {count} essays")
    print(f"\nTotal: {sum(category_stats.values())} essays")

if __name__ == "__main__":
    process_essays()
