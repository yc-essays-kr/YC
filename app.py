import streamlit as st
import os
import re
from pathlib import Path

# ===== Page Config =====
st.set_page_config(
    page_title="Paul Graham Essays in Korean",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ===== Constants =====
BASE_DIR = Path(__file__).parent
TRANSLATED_DIR = BASE_DIR / "essays" / "translated"
SUMMARY_DIR = BASE_DIR / "essays" / "original" / "summary"
PAGE_SIZE = 18

CATEGORIES = {
    "mindset": [
        "mindset", "think", "work hard", "passion", "determination", "persistence",
        "stubborn", "wisdom", "taste", "good", "heresy", "ideas", "smart", "nerds",
        "noob", "learning", "procrastination", "disagree", "love", "write", "essay",
        "philosophy", "alien",
    ],
    "market": [
        "market", "users", "product", "launch", "scale", "growth", "traction", "pmf",
        "competition", "customer", "domain", "industry", "bubble", "web", "google",
        "apple", "microsoft", "yahoo", "twitter", "airbnb",
    ],
    "funding": [
        "funding", "fundraising", "investor", "vc", "venture", "money", "angel",
        "valuation", "equity", "investment", "capital", "raise", "pitch", "convince",
        "herd", "squeeze", "super angel", "rich",
    ],
    "basics": [
        "startup", "founder", "company", "start", "yc", "y combinator", "idea",
        "mvp", "launch", "die", "mistake", "lesson", "begin", "early", "before",
        "version 1", "first", "hub", "silicon valley",
    ],
    "tech": [
        "programming", "code", "hacker", "software", "language", "lisp", "python",
        "java", "technology", "developer", "computer", "algorithm", "patent",
        "design", "architecture", "web app", "spam", "filter", "mac",
    ],
    "culture": [
        "team", "culture", "people", "hiring", "employee", "boss", "management",
        "organization", "mean", "nice", "schlep", "relentless", "nerd", "marginal",
        "jessica", "cofounder", "ambitious",
    ],
    "growth": [
        "scale", "growth", "strategy", "business", "model", "expansion", "market",
        "revenue", "profit", "metrics", "default alive", "ramen profitable",
        "organic", "returns", "wealth", "inequality",
    ],
}

CATEGORY_META = {
    "mindset": {"bg": "#E8E8E8", "text": "#4A4A4A", "label": "마인드셋"},
    "market": {"bg": "#FFF5E6", "text": "#8B4513", "label": "시장진입"},
    "funding": {"bg": "#FFE8E8", "text": "#C84747", "label": "펀드레이징"},
    "basics": {"bg": "#FFF9E6", "text": "#A67C00", "label": "창업기초"},
    "tech": {"bg": "#E6F7F7", "text": "#2C7A7B", "label": "기술/개발"},
    "culture": {"bg": "#F0E8FF", "text": "#6B46C1", "label": "조직문화"},
    "growth": {"bg": "#E6F2FF", "text": "#2B5797", "label": "성장전략"},
}


# ===== Data Processing =====
def categorize(filename: str, content: str) -> str:
    text = (filename.replace("_", " ") + " " + content[:2000]).lower()
    scores = {}
    for cat, keywords in CATEGORIES.items():
        scores[cat] = sum(1 for kw in keywords if kw.lower() in text)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "mindset"


def estimate_reading_time(content: str) -> int:
    chars = len(content.replace(" ", "").replace("\n", ""))
    return max(1, round(chars / 500))


def extract_date(content: str) -> str:
    lines = content.split("\n")[:15]
    for line in lines:
        m = re.search(r"(\d{4})년\s*(\d{1,2})월", line)
        if m:
            return f"{m.group(1)}년 {m.group(2)}월"
        m = re.search(
            r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})",
            line,
        )
        if m:
            months_map = {
                "January": "1월", "February": "2월", "March": "3월",
                "April": "4월", "May": "5월", "June": "6월",
                "July": "7월", "August": "8월", "September": "9월",
                "October": "10월", "November": "11월", "December": "12월",
            }
            return f"{m.group(2)}년 {months_map[m.group(1)]}"
    return ""


def extract_year(date_str: str) -> int:
    m = re.search(r"(\d{4})", date_str)
    return int(m.group(1)) if m else 0


def extract_title(content: str) -> str:
    lines = content.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


@st.cache_data
def load_essays():
    essays = []
    files = sorted([f for f in os.listdir(TRANSLATED_DIR) if f.endswith(".md")])

    for i, filename in enumerate(files):
        filepath = TRANSLATED_DIR / filename
        content = filepath.read_text(encoding="utf-8")

        title_ko = extract_title(content)
        title_en = filename.replace(".md", "").replace("_", " ")
        date = extract_date(content)
        category = categorize(filename, content)
        reading_time = estimate_reading_time(content)

        # Summary
        summary_path = SUMMARY_DIR / filename
        summary = ""
        description = ""
        if summary_path.exists():
            sc = summary_path.read_text(encoding="utf-8")
            summary = sc
            paras = [p.strip() for p in sc.split("\n\n") if p.strip() and not p.strip().startswith("#")]
            for p in paras:
                p = p.strip()
                if p.startswith("**") and p.endswith("**"):
                    continue
                p = re.sub(r"\*\*[^*]+\*\*\s*", "", p)
                if len(p) > 20:
                    description = p[:150]
                    if len(p) > 150:
                        description += "..."
                    break

        if not description:
            lines = content.strip().split("\n")
            for line in lines[3:]:
                line = line.strip()
                if line and not line.startswith("#") and not line.startswith("**") and not line.startswith("---") and len(line) > 30:
                    description = line[:150]
                    if len(line) > 150:
                        description += "..."
                    break

        essays.append({
            "id": i + 1,
            "titleKo": title_ko,
            "titleEn": title_en,
            "category": category,
            "readingTime": reading_time,
            "description": description,
            "date": date,
            "filename": filename,
            "year": extract_year(date),
            "content": content,
            "summary": summary,
        })

    essays.sort(key=lambda x: x["year"], reverse=True)
    for i, e in enumerate(essays):
        e["id"] = i + 1

    return essays


# ===== Custom CSS =====
def inject_css():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Noto+Serif+KR:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
    <style>
        /* Hide Streamlit defaults */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 1280px;
        }

        /* Font families */
        html, body, [class*="st-"] {
            font-family: 'Pretendard', 'Apple SD Gothic Neo', -apple-system, sans-serif;
        }

        /* Header */
        .site-header {
            text-align: center;
            padding: 3rem 1rem 1.5rem;
        }
        .site-header h1 {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 4rem;
            font-weight: 900;
            color: #1A1A1A;
            margin-bottom: 0.5rem;
            line-height: 1.25;
        }
        .site-header .subtitle {
            font-size: 1.25rem;
            color: #4A4A4A;
            margin-bottom: 0.25rem;
        }
        .site-header .stats {
            font-size: 0.875rem;
            color: #757575;
        }
        .site-header .stats span {
            font-weight: 600;
            color: #E85D04;
        }

        /* Category buttons */
        .category-pills {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            margin-bottom: 0.5rem;
        }
        .category-pill {
            padding: 0.5rem 1.25rem;
            font-size: 0.875rem;
            font-weight: 500;
            border: 2px solid #E0E0E0;
            border-radius: 24px;
            background: #FFFFFF;
            color: #4A4A4A;
            cursor: pointer;
            transition: all 0.2s ease;
            text-decoration: none;
            display: inline-block;
        }
        .category-pill:hover {
            background: #F9F7F2;
            border-color: #757575;
        }
        .category-pill.active {
            background: #E85D04;
            color: white;
            border-color: #E85D04;
            font-weight: 600;
            box-shadow: 0 2px 8px rgba(232, 93, 4, 0.3);
        }
        .cat-count {
            font-size: 0.75rem;
            opacity: 0.7;
            margin-left: 0.25rem;
        }

        /* Essay cards */
        .essay-card {
            background: #FFFFFF;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            height: 100%;
            display: flex;
            flex-direction: column;
            text-decoration: none;
            color: inherit;
            border: 1px solid transparent;
        }
        .essay-card:hover {
            box-shadow: 0 12px 24px rgba(0,0,0,0.08), 0 4px 8px rgba(0,0,0,0.04);
            transform: translateY(-8px);
            border-color: #E0E0E0;
        }
        .essay-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        .essay-category-tag {
            padding: 0.25rem 0.75rem;
            border-radius: 16px;
            font-size: 0.75rem;
            font-weight: 500;
            white-space: nowrap;
        }
        .essay-meta-info {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 0.75rem;
            color: #757575;
        }
        .essay-title-ko {
            font-family: 'Noto Serif KR', serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: #1A1A1A;
            margin-bottom: 0.5rem;
            line-height: 1.375;
        }
        .essay-title-en {
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            font-weight: 500;
            color: #757575;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.75rem;
        }
        .essay-desc {
            font-size: 0.875rem;
            line-height: 1.625;
            color: #4A4A4A;
            margin-bottom: 1.5rem;
            flex-grow: 1;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        .essay-cta {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #E85D04;
            font-weight: 600;
            font-size: 0.875rem;
        }
        .essay-card:hover .essay-cta {
            gap: 0.75rem;
        }

        /* Detail view */
        .detail-back {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: #E85D04;
            font-weight: 600;
            font-size: 0.875rem;
            cursor: pointer;
            padding: 0.75rem 0;
            margin-bottom: 1.5rem;
            text-decoration: none;
        }
        .detail-back:hover {
            gap: 0.75rem;
        }
        .detail-header {
            margin-bottom: 2rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid #E0E0E0;
        }
        .detail-title {
            font-family: 'Noto Serif KR', serif;
            font-size: 2.25rem;
            font-weight: 700;
            color: #1A1A1A;
            line-height: 1.3;
            margin-bottom: 0.75rem;
        }
        .detail-title-en {
            font-family: 'Inter', sans-serif;
            font-size: 0.875rem;
            font-weight: 500;
            color: #757575;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }
        .detail-meta {
            display: flex;
            align-items: center;
            gap: 1rem;
            font-size: 0.875rem;
            color: #757575;
        }

        /* Summary section */
        .summary-section {
            background: #F9F7F2;
            border: 1px solid #E0E0E0;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2.5rem;
        }
        .summary-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #E0E0E0;
        }
        .summary-title {
            font-family: 'Noto Serif KR', serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: #1A1A1A;
        }
        .ai-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.25rem 0.75rem;
            border-radius: 16px;
            font-size: 0.75rem;
            font-weight: 600;
            background: linear-gradient(135deg, #E6F2FF, #F0E8FF);
            color: #5B4FC4;
            border: 1px solid rgba(91, 79, 196, 0.2);
        }
        .summary-body {
            font-size: 1rem;
            line-height: 1.8;
            color: #4A4A4A;
        }
        .summary-body p {
            margin-bottom: 1rem;
        }

        /* Translation section */
        .translation-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 2px solid #E85D04;
        }
        .translation-title {
            font-family: 'Noto Serif KR', serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: #1A1A1A;
        }
        .essay-body {
            font-size: 1.125rem;
            line-height: 1.8;
            color: #1A1A1A;
        }
        .essay-body p {
            margin-bottom: 1.5rem;
        }
        .essay-body h2 {
            font-family: 'Noto Serif KR', serif;
            font-size: 1.5rem;
            font-weight: 700;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
        }
        .essay-body h3 {
            font-family: 'Noto Serif KR', serif;
            font-size: 1.25rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 0.75rem;
        }
        .essay-body blockquote {
            border-left: 3px solid #E85D04;
            padding-left: 1.5rem;
            margin: 1.5rem 0;
            color: #4A4A4A;
            font-style: italic;
        }
        .essay-body ul, .essay-body ol {
            margin-bottom: 1.5rem;
            padding-left: 2rem;
        }
        .essay-body li {
            margin-bottom: 0.5rem;
        }
        .essay-body a {
            color: #E85D04;
            text-decoration: underline;
        }

        /* Footer */
        .site-footer {
            text-align: center;
            padding: 3rem 1rem;
            margin-top: 4rem;
            border-top: 1px solid #E0E0E0;
            font-size: 0.875rem;
            color: #757575;
        }
        .site-footer a {
            color: #4A4A4A;
            text-decoration: none;
        }
        .site-footer a:hover {
            color: #E85D04;
        }

        /* Results info */
        .results-info {
            font-size: 0.875rem;
            color: #757575;
            margin-bottom: 1rem;
        }

        /* No results */
        .no-results {
            text-align: center;
            padding: 4rem;
            color: #757575;
            font-size: 1.125rem;
        }

        /* Card row spacing - match horizontal gap */
        div[data-testid="stHorizontalBlock"] {
            margin-bottom: 1.5rem;
        }

        /* Category button height fix */
        div[data-testid="stHorizontalBlock"] button[data-testid="stBaseButton-secondary"],
        div[data-testid="stHorizontalBlock"] button[data-testid="stBaseButton-primary"] {
            height: 2.5rem;
            font-size: 0.8rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            padding: 0 0.5rem;
        }

        /* Streamlit overrides */
        .stTextInput > div > div > input {
            border: 2px solid #E0E0E0;
            border-radius: 8px;
            font-size: 1rem;
            padding: 0.75rem 1rem;
        }
        .stTextInput > div > div > input:focus {
            border-color: #E85D04;
            box-shadow: 0 0 0 3px rgba(232, 93, 4, 0.1);
        }
        .stSelectbox > div > div {
            border: 2px solid #E0E0E0;
            border-radius: 8px;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .site-header h1 { font-size: 2.5rem; }
            .essay-title-ko { font-size: 1.25rem; }
            .detail-title { font-size: 1.875rem; }
        }
    </style>
    """, unsafe_allow_html=True)


# ===== Markdown to HTML =====
def markdown_to_html(md: str) -> str:
    # Remove front matter
    if md.strip().startswith("---"):
        md = re.sub(r"^---\n[\s\S]*?\n---\n*", "", md.strip())

    # Remove title line
    md = re.sub(r"^#\s+.+\n*", "", md, count=1, flags=re.MULTILINE)

    # Remove date/meta near the top
    top = md[:300]
    rest = md[300:]
    top = re.sub(r"^\*\*[^*]+\*\*.*$", "", top, flags=re.MULTILINE)
    top = re.sub(r"^---\s*$", "", top, flags=re.MULTILINE)
    top = re.sub(r"^\d{4}년\s*\d{1,2}월\s*$", "", top, flags=re.MULTILINE)
    md = top + rest

    html = md
    # Headers
    html = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^##\s+(.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    # Bold and italic
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)
    # Links
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', html)
    # Blockquotes
    html = re.sub(r"^>\s*(.+)$", r"<blockquote>\1</blockquote>", html, flags=re.MULTILINE)
    # Lists
    html = re.sub(r"^[-*]\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    html = re.sub(r"(<li>.*?</li>\n?)+", lambda m: "<ul>" + m.group(0) + "</ul>", html)
    html = re.sub(r"^\d+\.\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)

    # Paragraphs
    blocks = re.split(r"\n\n+", html)
    result = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block.startswith(("<h", "<ul", "<ol", "<blockquote")):
            result.append(block)
        else:
            result.append("<p>" + block.replace("\n", "<br>") + "</p>")
    html = "\n".join(result)
    html = re.sub(r"<p>\s*</p>", "", html)
    return html


# ===== Session State =====
if "category" not in st.session_state:
    st.session_state.category = "all"
if "display_count" not in st.session_state:
    st.session_state.display_count = PAGE_SIZE


def set_category(cat):
    st.session_state.category = cat
    st.session_state.display_count = PAGE_SIZE


def load_more():
    st.session_state.display_count += PAGE_SIZE


# ===== Main =====
inject_css()
essays = load_essays()

# Use query params for navigation (enables browser back/forward)
query_params = st.query_params
essay_id_param = query_params.get("essay", None)

if essay_id_param is not None:
    # ===== Detail View =====
    try:
        eid = int(essay_id_param)
    except (ValueError, TypeError):
        eid = None
    essay = next((e for e in essays if e["id"] == eid), None) if eid else None
    if essay is None:
        st.query_params.clear()
        st.rerun()

    col_detail = st.columns([1, 8, 1])[1]
    with col_detail:
        # Back button
        st.markdown('<a href="/" class="detail-back">← 목록으로 돌아가기</a>', unsafe_allow_html=True)

        # Header
        cat_info = CATEGORY_META[essay["category"]]
        st.markdown(f"""
        <div class="detail-header">
            <div class="detail-title">{essay['titleKo']}</div>
            <div class="detail-title-en">{essay['titleEn']}</div>
            <div class="detail-meta">
                <span class="essay-category-tag" style="background-color:{cat_info['bg']};color:{cat_info['text']};">{cat_info['label']}</span>
                {'<span>' + essay['date'] + '</span>' if essay['date'] else ''}
                <span>{essay['readingTime']}분 읽기</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Summary section
        if essay["summary"]:
            summary_html = markdown_to_html(essay["summary"])
            st.markdown(f"""
            <div class="summary-section">
                <div class="summary-header">
                    <div class="summary-title">📄 요약</div>
                    <span class="ai-badge">✨ AI 생성 요약</span>
                </div>
                <div class="summary-body">{summary_html}</div>
            </div>
            """, unsafe_allow_html=True)

        # Translation section
        content_html = markdown_to_html(essay["content"])
        st.markdown(f"""
        <div class="translation-header">
            <div class="translation-title">📖 번역본</div>
        </div>
        <div class="essay-body">{content_html}</div>
        """, unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div class="site-footer">
            <p>&copy; 2026 Paul Graham Essays in Korean. All rights reserved.</p>
            <a href="http://www.paulgraham.com" target="_blank">원문 보기 (paulgraham.com)</a>
        </div>
        """, unsafe_allow_html=True)

else:
    # ===== List View =====

    # Header
    st.markdown(f"""
    <div class="site-header">
        <h1>Paul Graham Essays</h1>
        <div class="subtitle">폴 그레이엄의 에세이를 한국어로 읽어보세요</div>
        <div class="stats"><span>{len(essays)}</span>편의 에세이 | 스타트업 · 기술 · 투자 · 인생</div>
    </div>
    """, unsafe_allow_html=True)

    # Search and sort
    col_search, col_sort = st.columns([4, 1])
    with col_search:
        search_term = st.text_input(
            "검색", placeholder="에세이 제목이나 내용으로 검색...",
            label_visibility="collapsed", key="search_input",
        )
    with col_sort:
        sort_option = st.selectbox(
            "정렬", ["최신순", "오래된순", "읽기 시간 (짧은순)", "읽기 시간 (긴순)", "제목순 (가나다)"],
            label_visibility="collapsed", key="sort_select",
        )

    # Category filter
    cat_counts = {"all": len(essays)}
    for cat in CATEGORY_META:
        cat_counts[cat] = sum(1 for e in essays if e["category"] == cat)

    current_cat = st.session_state.category
    cats = [("all", "전체")] + [(k, v["label"]) for k, v in CATEGORY_META.items()]

    # Category filter pills (functional)
    cat_cols = st.columns(len(cats))
    for i, (cat_key, cat_label) in enumerate(cats):
        with cat_cols[i]:
            count = cat_counts.get(cat_key, 0)
            if st.button(
                f"{cat_label} ({count})",
                key=f"cat_{cat_key}",
                use_container_width=True,
                type="primary" if cat_key == current_cat else "secondary",
            ):
                set_category(cat_key)
                st.rerun()

    # Filter essays
    filtered = list(essays)
    if current_cat != "all":
        filtered = [e for e in filtered if e["category"] == current_cat]

    if search_term:
        term = search_term.lower()
        filtered = [
            e for e in filtered
            if term in e["titleKo"].lower()
            or term in e["titleEn"].lower()
            or term in e["description"].lower()
        ]

    # Sort
    if sort_option == "최신순":
        filtered.sort(key=lambda x: x["year"], reverse=True)
    elif sort_option == "오래된순":
        filtered.sort(key=lambda x: x["year"])
    elif sort_option == "읽기 시간 (짧은순)":
        filtered.sort(key=lambda x: x["readingTime"])
    elif sort_option == "읽기 시간 (긴순)":
        filtered.sort(key=lambda x: x["readingTime"], reverse=True)
    elif sort_option == "제목순 (가나다)":
        filtered.sort(key=lambda x: x["titleKo"])

    # Results info
    if search_term or current_cat != "all":
        st.markdown(f'<div class="results-info">{len(filtered)}개의 에세이</div>', unsafe_allow_html=True)

    # Essay grid
    if not filtered:
        st.markdown('<div class="no-results">검색 결과가 없습니다. 다른 키워드로 검색해보세요.</div>', unsafe_allow_html=True)
    else:
        display_count = st.session_state.display_count
        to_show = filtered[:display_count]

        for row_start in range(0, len(to_show), 3):
            row_essays = to_show[row_start:row_start + 3]
            cols = st.columns(3)
            for col_idx, essay in enumerate(row_essays):
                with cols[col_idx]:
                    cat_info = CATEGORY_META[essay["category"]]
                    card_html = f"""
                    <a href="/?essay={essay['id']}" class="essay-card" id="card-{essay['id']}">
                        <div class="essay-card-header">
                            <span class="essay-category-tag" style="background-color:{cat_info['bg']};color:{cat_info['text']};">{cat_info['label']}</span>
                            <div class="essay-meta-info">
                                {'<span>' + essay['date'] + '</span>' if essay['date'] else ''}
                                <span>⏱ {essay['readingTime']}분</span>
                            </div>
                        </div>
                        <div class="essay-title-ko">{essay['titleKo']}</div>
                        <div class="essay-title-en">{essay['titleEn']}</div>
                        <div class="essay-desc">{essay['description']}</div>
                        <div class="essay-cta">읽어보기 →</div>
                    </a>
                    """
                    st.markdown(card_html, unsafe_allow_html=True)

        # Load more
        if display_count < len(filtered):
            col_more = st.columns([1, 2, 1])[1]
            with col_more:
                if st.button(f"더 보기 ({display_count}/{len(filtered)})", key="load_more", use_container_width=True):
                    load_more()
                    st.rerun()

    # Footer
    st.markdown("""
    <div class="site-footer">
        <p>&copy; 2026 Paul Graham Essays in Korean. All rights reserved.</p>
        <a href="http://www.paulgraham.com" target="_blank">원문 보기 (paulgraham.com)</a>
    </div>
    """, unsafe_allow_html=True)
