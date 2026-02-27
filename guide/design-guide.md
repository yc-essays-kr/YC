# Paul Graham Essays in Korean - 디자인 가이드

## 📋 목차

1. [브랜드 아이덴티티](#브랜드-아이덴티티)
2. [색상 시스템](#색상-시스템)
3. [타이포그래피](#타이포그래피)
4. [레이아웃 & 그리드](#레이아웃--그리드)
5. [컴포넌트 가이드](#컴포넌트-가이드)
6. [반응형 디자인](#반응형-디자인)
7. [접근성](#접근성)
8. [개선 사항](#개선-사항)

---

## 🎨 브랜드 아이덴티티

### 디자인 철학
- **미니멀리즘**: 불필요한 요소를 제거하고 콘텐츠에 집중
- **가독성 우선**: 긴 에세이를 편안하게 읽을 수 있는 환경 제공
- **전문성**: 스타트업 생태계의 신뢰할 수 있는 지식 플랫폼

### 톤 앤 매너
- **진지하면서도 접근하기 쉬운** (Serious yet Approachable)
- **지적이면서도 친근한** (Intellectual yet Friendly)
- **깔끔하고 정돈된** (Clean and Organized)

---

## 🎨 색상 시스템

### 기본 색상 (Base Colors)

```css
/* 배경색 */
--color-background-primary: #F5F1E8;      /* 아이보리/베이지 */
--color-background-secondary: #FFFFFF;     /* 화이트 */
--color-background-tertiary: #F9F7F2;      /* 라이트 베이지 */

/* 텍스트 */
--color-text-primary: #1A1A1A;             /* 다크 그레이 */
--color-text-secondary: #4A4A4A;           /* 미디엄 그레이 */
--color-text-tertiary: #757575;            /* 라이트 그레이 */

/* 액센트 */
--color-accent-primary: #E85D04;           /* 오렌지 (CTA) */
--color-accent-hover: #DC5203;             /* 다크 오렌지 */
```

### 카테고리 색상 (Category Colors)

```css
/* 마인드셋 */
--color-category-mindset: #E8E8E8;         /* 라이트 그레이 */
--color-category-mindset-text: #4A4A4A;

/* 시장진입 */
--color-category-market: #FFF5E6;          /* 라이트 피치 */
--color-category-market-text: #8B4513;

/* 펀드레이징 */
--color-category-funding: #FFE8E8;         /* 라이트 코랄 */
--color-category-funding-text: #C84747;

/* 창업기초 */
--color-category-basics: #FFF9E6;          /* 라이트 옐로우 */
--color-category-basics-text: #A67C00;

/* 기술/개발 */
--color-category-tech: #E6F7F7;            /* 라이트 터콰이즈 */
--color-category-tech-text: #2C7A7B;

/* 조직문화 */
--color-category-culture: #F0E8FF;         /* 라이트 퍼플 */
--color-category-culture-text: #6B46C1;

/* 성장전략 */
--color-category-growth: #E6F2FF;          /* 라이트 블루 */
--color-category-growth-text: #2B5797;
```

### 상태 색상 (State Colors)

```css
/* 성공 */
--color-success: #48BB78;
--color-success-light: #C6F6D5;

/* 경고 */
--color-warning: #F6AD55;
--color-warning-light: #FEEBC8;

/* 오류 */
--color-error: #F56565;
--color-error-light: #FED7D7;

/* 정보 */
--color-info: #4299E1;
--color-info-light: #BEE3F8;
```

---

## 📝 타이포그래피

### 폰트 패밀리

```css
/* 영문 헤딩 */
--font-heading-en: 'Playfair Display', 'Georgia', serif;

/* 한글 헤딩 */
--font-heading-ko: 'Noto Serif KR', 'Apple SD Gothic Neo', serif;

/* 본문 */
--font-body-ko: 'Pretendard', 'Apple SD Gothic Neo', -apple-system, sans-serif;
--font-body-en: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

/* 코드/고정폭 */
--font-mono: 'JetBrains Mono', 'SF Mono', 'Consolas', monospace;
```

### 폰트 크기 (Font Sizes)

```css
/* 헤딩 */
--text-6xl: 4rem;      /* 64px - 메인 타이틀 */
--text-5xl: 3rem;      /* 48px - 서브 타이틀 */
--text-4xl: 2.25rem;   /* 36px - 섹션 헤딩 */
--text-3xl: 1.875rem;  /* 30px - 카드 타이틀 */
--text-2xl: 1.5rem;    /* 24px - 서브 헤딩 */
--text-xl: 1.25rem;    /* 20px - 카드 서브타이틀 */

/* 본문 */
--text-lg: 1.125rem;   /* 18px - 큰 본문 */
--text-base: 1rem;     /* 16px - 기본 본문 */
--text-sm: 0.875rem;   /* 14px - 작은 텍스트 */
--text-xs: 0.75rem;    /* 12px - 메타 정보 */
```

### 행간 (Line Height)

```css
--leading-tight: 1.25;      /* 타이트한 헤딩 */
--leading-snug: 1.375;      /* 헤딩 */
--leading-normal: 1.5;      /* 일반 본문 */
--leading-relaxed: 1.625;   /* 여유있는 본문 */
--leading-loose: 2;         /* 느슨한 텍스트 */
```

### 폰트 굵기 (Font Weight)

```css
--font-light: 300;
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
--font-black: 900;
```

### 타이포그래피 사용 예시

```css
/* 메인 헤딩 */
.main-heading {
  font-family: var(--font-heading-en);
  font-size: var(--text-6xl);
  font-weight: var(--font-black);
  line-height: var(--leading-tight);
  color: var(--color-text-primary);
}

/* 한글 서브 헤딩 */
.subheading-ko {
  font-family: var(--font-heading-ko);
  font-size: var(--text-2xl);
  font-weight: var(--font-medium);
  line-height: var(--leading-snug);
  color: var(--color-text-secondary);
}

/* 본문 텍스트 */
.body-text {
  font-family: var(--font-body-ko);
  font-size: var(--text-base);
  font-weight: var(--font-normal);
  line-height: var(--leading-relaxed);
  color: var(--color-text-primary);
}
```

---

## 📐 레이아웃 & 그리드

### 컨테이너 너비

```css
--container-sm: 640px;    /* 모바일 */
--container-md: 768px;    /* 태블릿 */
--container-lg: 1024px;   /* 데스크탑 */
--container-xl: 1280px;   /* 와이드 스크린 */
--container-2xl: 1536px;  /* 초대형 스크린 */
```

### 그리드 시스템

```css
/* 3-컬럼 그리드 (에세이 카드) */
.essay-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;           /* 32px */
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* 태블릿: 2-컬럼 */
@media (max-width: 1024px) {
  .essay-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;       /* 24px */
  }
}

/* 모바일: 1-컬럼 */
@media (max-width: 640px) {
  .essay-grid {
    grid-template-columns: 1fr;
    gap: 1rem;         /* 16px */
    padding: 0 1rem;
  }
}
```

### 여백 (Spacing)

```css
--space-0: 0;
--space-1: 0.25rem;    /* 4px */
--space-2: 0.5rem;     /* 8px */
--space-3: 0.75rem;    /* 12px */
--space-4: 1rem;       /* 16px */
--space-5: 1.25rem;    /* 20px */
--space-6: 1.5rem;     /* 24px */
--space-8: 2rem;       /* 32px */
--space-10: 2.5rem;    /* 40px */
--space-12: 3rem;      /* 48px */
--space-16: 4rem;      /* 64px */
--space-20: 5rem;      /* 80px */
--space-24: 6rem;      /* 96px */
```

---

## 🧩 컴포넌트 가이드

### 1. 헤더 (Header)

```css
.header {
  background: var(--color-background-primary);
  padding: var(--space-16) var(--space-8);
  text-align: center;
}

.header-title {
  font-family: var(--font-heading-en);
  font-size: var(--text-6xl);
  font-weight: var(--font-black);
  color: var(--color-text-primary);
  margin-bottom: var(--space-4);
  line-height: var(--leading-tight);
}

.header-subtitle {
  font-family: var(--font-body-ko);
  font-size: var(--text-xl);
  font-weight: var(--font-normal);
  color: var(--color-text-secondary);
}
```

### 2. 검색창 (Search Bar)

```css
.search-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: var(--space-8) var(--space-8);
  display: flex;
  gap: var(--space-4);
  align-items: center;
}

.search-input {
  flex: 1;
  padding: var(--space-4) var(--space-6);
  font-size: var(--text-base);
  border: 2px solid #E0E0E0;
  border-radius: 8px;
  background: var(--color-background-secondary);
  transition: border-color 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: var(--color-accent-primary);
  box-shadow: 0 0 0 3px rgba(232, 93, 4, 0.1);
}

.search-icon {
  position: absolute;
  left: var(--space-4);
  color: var(--color-text-tertiary);
}
```

### 3. 카테고리 필터 (Category Filter)

```css
.category-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: var(--space-6) var(--space-8);
}

.category-label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-4);
}

.category-buttons {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
}

.category-button {
  padding: var(--space-3) var(--space-5);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  border: 2px solid transparent;
  border-radius: 24px;
  background: var(--color-background-secondary);
  color: var(--color-text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
}

.category-button:hover {
  background: var(--color-background-tertiary);
  border-color: var(--color-text-tertiary);
}

.category-button.active {
  background: var(--color-accent-primary);
  color: white;
  border-color: var(--color-accent-primary);
}
```

### 4. 에세이 카드 (Essay Card)

```css
.essay-card {
  background: var(--color-background-secondary);
  border-radius: 12px;
  padding: var(--space-6);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  cursor: pointer;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.essay-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}

.essay-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-4);
}

.essay-reading-time {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--color-text-tertiary);
}

.essay-category-tag {
  padding: var(--space-2) var(--space-4);
  border-radius: 16px;
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
}

.essay-title-ko {
  font-family: var(--font-heading-ko);
  font-size: var(--text-2xl);
  font-weight: var(--font-bold);
  color: var(--color-text-primary);
  margin-bottom: var(--space-2);
  line-height: var(--leading-snug);
}

.essay-title-en {
  font-family: var(--font-body-en);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: var(--space-4);
}

.essay-description {
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-6);
  flex-grow: 1;
}

.essay-cta {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  color: var(--color-accent-primary);
  font-weight: var(--font-semibold);
  font-size: var(--text-sm);
  transition: gap 0.2s ease;
}

.essay-card:hover .essay-cta {
  gap: var(--space-3);
}
```

### 5. CTA 버튼 (Call to Action Button)

```css
.btn-primary {
  padding: var(--space-4) var(--space-8);
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: white;
  background: var(--color-accent-primary);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
}

.btn-primary:hover {
  background: var(--color-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(232, 93, 4, 0.3);
}

.btn-primary:active {
  transform: translateY(0);
}

.btn-secondary {
  padding: var(--space-4) var(--space-8);
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
  background: transparent;
  border: 2px solid var(--color-text-primary);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: var(--color-text-primary);
  color: white;
}
```

### 6. 푸터 (Footer)

```css
.footer {
  background: var(--color-background-primary);
  padding: var(--space-12) var(--space-8);
  margin-top: var(--space-20);
  border-top: 1px solid #E0E0E0;
}

.footer-content {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-copyright {
  font-size: var(--text-sm);
  color: var(--color-text-tertiary);
}

.footer-links {
  display: flex;
  gap: var(--space-6);
}

.footer-link {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: var(--color-accent-primary);
}
```

---

## 📱 반응형 디자인

### 브레이크포인트

```css
/* 모바일 우선 접근법 */

/* 스몰 모바일 */
@media (min-width: 375px) { }

/* 모바일 */
@media (min-width: 640px) { }

/* 태블릿 */
@media (min-width: 768px) { }

/* 데스크탑 */
@media (min-width: 1024px) { }

/* 대형 데스크탑 */
@media (min-width: 1280px) { }

/* 초대형 스크린 */
@media (min-width: 1536px) { }
```

### 반응형 타이포그래피

```css
/* 메인 헤딩 */
.main-heading {
  font-size: 2.5rem;  /* 모바일: 40px */
}

@media (min-width: 640px) {
  .main-heading {
    font-size: 3rem;  /* 태블릿: 48px */
  }
}

@media (min-width: 1024px) {
  .main-heading {
    font-size: 4rem;  /* 데스크탑: 64px */
  }
}
```

### 반응형 그리드

```css
/* 에세이 그리드 */
.essay-grid {
  /* 모바일: 1열 */
  grid-template-columns: 1fr;
  gap: 1rem;
  padding: 0 1rem;
}

@media (min-width: 768px) {
  .essay-grid {
    /* 태블릿: 2열 */
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    padding: 0 2rem;
  }
}

@media (min-width: 1024px) {
  .essay-grid {
    /* 데스크탑: 3열 */
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }
}
```

---

## ♿ 접근성

### 색상 대비 (Color Contrast)

모든 텍스트는 WCAG 2.1 AA 기준을 충족해야 합니다:

- **일반 텍스트**: 최소 4.5:1 대비
- **대형 텍스트** (18px 이상): 최소 3:1 대비

```css
/* 좋은 예 */
.text-on-light {
  color: #1A1A1A;              /* 검정 텍스트 */
  background: #F5F1E8;         /* 베이지 배경 */
  /* 대비율: 12.5:1 ✓ */
}

/* 나쁜 예 */
.text-on-light-bad {
  color: #C0C0C0;              /* 라이트 그레이 텍스트 */
  background: #F5F1E8;         /* 베이지 배경 */
  /* 대비율: 2.1:1 ✗ */
}
```

### 키보드 네비게이션

모든 인터랙티브 요소는 키보드로 접근 가능해야 합니다:

```css
/* 포커스 스타일 */
*:focus {
  outline: 2px solid var(--color-accent-primary);
  outline-offset: 2px;
}

/* 포커스 표시기 - 더 명확하게 */
.btn-primary:focus,
.search-input:focus,
.category-button:focus {
  outline: 3px solid var(--color-accent-primary);
  outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(232, 93, 4, 0.2);
}

/* 마우스 클릭 시 포커스 링 제거 (선택적) */
.btn-primary:focus:not(:focus-visible) {
  outline: none;
  box-shadow: none;
}
```

### 스크린 리더 지원

```html
<!-- 시맨틱 HTML 사용 -->
<header role="banner">
  <h1>Paul Graham Essays in Korean</h1>
</header>

<nav role="navigation" aria-label="카테고리 필터">
  <button aria-label="전체 에세이 보기">전체 에세이</button>
</nav>

<main role="main">
  <section aria-label="에세이 목록">
    <!-- 에세이 카드들 -->
  </section>
</main>

<!-- 대체 텍스트 -->
<img src="icon.svg" alt="읽기 시간 아이콘" />

<!-- ARIA 레이블 -->
<input
  type="search"
  aria-label="에세이 검색"
  placeholder="에세이 검색..."
/>
```

---

## 🔧 개선 사항

### 우선순위 높음 (High Priority)

#### 1. 누락된 읽기 시간 데이터 수정

**문제점**: 일부 최신 에세이들의 읽기 시간이 누락됨

**해결 방법**:
```javascript
// 에세이 데이터에 읽기 시간 추가
const essays = [
  {
    id: 37,
    title: "창업자 모드",
    titleEn: "Founder Mode",
    readingTime: 8,  // ← 추가 필요
    category: "mindset",
    // ...
  }
];
```

#### 2. 카테고리 버튼 선택 상태 명확화

**개선 방법**:
```css
.category-button {
  /* 기본 상태 */
  background: white;
  border: 2px solid #E0E0E0;
  color: var(--color-text-secondary);
}

.category-button.active {
  /* 선택 상태 - 더 명확하게 */
  background: var(--color-accent-primary);
  border-color: var(--color-accent-primary);
  color: white;
  font-weight: var(--font-semibold);
  box-shadow: 0 2px 8px rgba(232, 93, 4, 0.3);
}

.category-button:hover:not(.active) {
  background: var(--color-background-tertiary);
  border-color: var(--color-text-tertiary);
}
```

#### 3. 카드 호버 효과 개선

```css
.essay-card {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.essay-card:hover {
  transform: translateY(-8px);
  box-shadow:
    0 12px 24px rgba(0, 0, 0, 0.08),
    0 4px 8px rgba(0, 0, 0, 0.04);
}

/* 카드 내부 CTA 애니메이션 */
.essay-card:hover .essay-cta {
  gap: var(--space-3);
  color: var(--color-accent-hover);
}

.essay-card:hover .essay-cta-arrow {
  transform: translateX(4px);
}
```

### 우선순위 중간 (Medium Priority)

#### 4. 검색 기능 강화

```javascript
// 실시간 검색 필터링
const searchInput = document.querySelector('.search-input');
let debounceTimer;

searchInput.addEventListener('input', (e) => {
  clearTimeout(debounceTimer);

  debounceTimer = setTimeout(() => {
    const searchTerm = e.target.value.toLowerCase();
    filterEssays(searchTerm);
  }, 300);
});

// 검색 하이라이트 표시
function highlightSearchTerm(text, searchTerm) {
  if (!searchTerm) return text;

  const regex = new RegExp(`(${searchTerm})`, 'gi');
  return text.replace(regex, '<mark>$1</mark>');
}
```

#### 5. 로딩 상태 개선

```css
/* 스켈레톤 로더 */
.skeleton {
  background: linear-gradient(
    90deg,
    #F5F1E8 25%,
    #E8E4DB 50%,
    #F5F1E8 75%
  );
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}

.skeleton-card {
  height: 320px;
  border-radius: 12px;
}
```

#### 6. 정렬 옵션 추가

```html
<div class="sort-container">
  <label for="sort-select">정렬:</label>
  <select id="sort-select" class="sort-select">
    <option value="latest">최신순</option>
    <option value="oldest">오래된순</option>
    <option value="reading-time-asc">읽기 시간 (짧은순)</option>
    <option value="reading-time-desc">읽기 시간 (긴순)</option>
    <option value="title">제목순</option>
  </select>
</div>
```

```css
.sort-select {
  padding: var(--space-3) var(--space-6);
  border: 2px solid #E0E0E0;
  border-radius: 8px;
  font-size: var(--text-sm);
  background: white;
  cursor: pointer;
}
```

### 우선순위 낮음 (Low Priority)

#### 7. 추가 기능

**북마크/즐겨찾기**:
```javascript
// LocalStorage 활용
function toggleBookmark(essayId) {
  const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');

  if (bookmarks.includes(essayId)) {
    // 북마크 제거
    const index = bookmarks.indexOf(essayId);
    bookmarks.splice(index, 1);
  } else {
    // 북마크 추가
    bookmarks.push(essayId);
  }

  localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
}
```

**읽음 표시**:
```javascript
// 읽음 상태 저장
function markAsRead(essayId) {
  const readEssays = JSON.parse(localStorage.getItem('readEssays') || '[]');
  if (!readEssays.includes(essayId)) {
    readEssays.push(essayId);
    localStorage.setItem('readEssays', JSON.stringify(readEssays));
  }
}
```

**다크 모드**:
```css
/* 다크 모드 색상 변수 */
[data-theme="dark"] {
  --color-background-primary: #1A1A1A;
  --color-background-secondary: #2D2D2D;
  --color-background-tertiary: #242424;
  --color-text-primary: #F5F1E8;
  --color-text-secondary: #C0C0C0;
  --color-text-tertiary: #909090;
}

/* 다크 모드 토글 버튼 */
.theme-toggle {
  padding: var(--space-3);
  border: none;
  background: transparent;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.theme-toggle:hover {
  transform: rotate(180deg);
}
```

---

## 🎯 성능 최적화

### 이미지 최적화

```html
<!-- WebP 포맷 사용 + 폴백 -->
<picture>
  <source srcset="icon.webp" type="image/webp">
  <img src="icon.png" alt="아이콘" loading="lazy">
</picture>

<!-- 반응형 이미지 -->
<img
  srcset="
    icon-small.webp 320w,
    icon-medium.webp 768w,
    icon-large.webp 1024w
  "
  sizes="(max-width: 640px) 320px, (max-width: 1024px) 768px, 1024px"
  src="icon-medium.webp"
  alt="아이콘"
  loading="lazy"
>
```

### 폰트 최적화

```html
<!-- 폰트 프리로드 -->
<link
  rel="preload"
  href="/fonts/pretendard-variable.woff2"
  as="font"
  type="font/woff2"
  crossorigin
>

<!-- font-display: swap 사용 -->
<style>
  @font-face {
    font-family: 'Pretendard';
    src: url('/fonts/pretendard-variable.woff2') format('woff2-variations');
    font-weight: 100 900;
    font-display: swap;
  }
</style>
```

### CSS 최적화

```css
/* 하드웨어 가속 활용 */
.essay-card {
  will-change: transform;
  transform: translateZ(0);
}

/* 애니메이션 최적화 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 📐 디자인 원칙

### 1. 일관성 (Consistency)
- 모든 페이지에서 동일한 컴포넌트 스타일 사용
- 색상, 타이포그래피, 간격을 변수로 관리
- 패턴을 재사용하여 예측 가능한 UI 제공

### 2. 명확성 (Clarity)
- 시각적 계층 구조를 명확하게 표현
- 중요한 정보를 눈에 띄게 배치
- 불필요한 장식 요소 제거

### 3. 효율성 (Efficiency)
- 사용자가 원하는 에세이를 빠르게 찾을 수 있도록
- 검색, 필터, 정렬 기능 제공
- 로딩 시간 최소화

### 4. 반응성 (Responsiveness)
- 모든 기기에서 최적화된 경험 제공
- 터치 친화적인 인터페이스
- 적절한 타겟 사이즈 (최소 44x44px)

### 5. 접근성 (Accessibility)
- 모든 사용자가 콘텐츠에 접근할 수 있도록
- 키보드 네비게이션 지원
- 스크린 리더 호환성

---

## 📋 체크리스트

### 디자인 구현 전

- [ ] 디자인 시스템 색상 변수 설정
- [ ] 타이포그래피 설정 (폰트, 크기, 굵기)
- [ ] 간격 시스템 정의
- [ ] 반응형 브레이크포인트 설정

### 컴포넌트 개발

- [ ] 헤더 컴포넌트
- [ ] 검색 바 컴포넌트
- [ ] 카테고리 필터 컴포넌트
- [ ] 에세이 카드 컴포넌트
- [ ] CTA 버튼 컴포넌트
- [ ] 푸터 컴포넌트

### 기능 구현

- [ ] 검색 기능
- [ ] 카테고리 필터링
- [ ] 정렬 기능
- [ ] 북마크 기능 (선택)
- [ ] 읽음 표시 (선택)
- [ ] 다크 모드 (선택)

### 최적화

- [ ] 이미지 최적화 (WebP, lazy loading)
- [ ] 폰트 최적화 (preload, font-display)
- [ ] CSS 최적화 (번들 크기 최소화)
- [ ] JavaScript 최적화 (코드 스플리팅)

### 접근성 & 테스트

- [ ] 키보드 네비게이션 테스트
- [ ] 스크린 리더 테스트
- [ ] 색상 대비 확인
- [ ] 반응형 디자인 테스트 (모바일, 태블릿, 데스크탑)
- [ ] 크로스 브라우저 테스트

---

## 🎨 디자인 토큰

```javascript
// design-tokens.js
export const tokens = {
  colors: {
    background: {
      primary: '#F5F1E8',
      secondary: '#FFFFFF',
      tertiary: '#F9F7F2',
    },
    text: {
      primary: '#1A1A1A',
      secondary: '#4A4A4A',
      tertiary: '#757575',
    },
    accent: {
      primary: '#E85D04',
      hover: '#DC5203',
    },
    category: {
      mindset: { bg: '#E8E8E8', text: '#4A4A4A' },
      market: { bg: '#FFF5E6', text: '#8B4513' },
      funding: { bg: '#FFE8E8', text: '#C84747' },
      basics: { bg: '#FFF9E6', text: '#A67C00' },
      tech: { bg: '#E6F7F7', text: '#2C7A7B' },
      culture: { bg: '#F0E8FF', text: '#6B46C1' },
      growth: { bg: '#E6F2FF', text: '#2B5797' },
    },
  },
  typography: {
    fontFamily: {
      headingEn: '"Playfair Display", Georgia, serif',
      headingKo: '"Noto Serif KR", "Apple SD Gothic Neo", serif',
      bodyKo: '"Pretendard", "Apple SD Gothic Neo", sans-serif',
      bodyEn: '"Inter", -apple-system, BlinkMacSystemFont, sans-serif',
      mono: '"JetBrains Mono", "SF Mono", Consolas, monospace',
    },
    fontSize: {
      xs: '0.75rem',
      sm: '0.875rem',
      base: '1rem',
      lg: '1.125rem',
      xl: '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
      '6xl': '4rem',
    },
    fontWeight: {
      light: 300,
      normal: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
      black: 900,
    },
    lineHeight: {
      tight: 1.25,
      snug: 1.375,
      normal: 1.5,
      relaxed: 1.625,
      loose: 2,
    },
  },
  spacing: {
    0: '0',
    1: '0.25rem',
    2: '0.5rem',
    3: '0.75rem',
    4: '1rem',
    5: '1.25rem',
    6: '1.5rem',
    8: '2rem',
    10: '2.5rem',
    12: '3rem',
    16: '4rem',
    20: '5rem',
    24: '6rem',
  },
  borderRadius: {
    sm: '4px',
    md: '8px',
    lg: '12px',
    xl: '16px',
    full: '9999px',
  },
  shadows: {
    sm: '0 2px 4px rgba(0, 0, 0, 0.05)',
    md: '0 4px 8px rgba(0, 0, 0, 0.08)',
    lg: '0 8px 16px rgba(0, 0, 0, 0.12)',
    xl: '0 12px 24px rgba(0, 0, 0, 0.15)',
  },
};
```

---

## 📚 참고 자료

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Material Design Color System](https://material.io/design/color)
- [Tailwind CSS Design System](https://tailwindcss.com/docs)
- [Ant Design Components](https://ant.design/components/overview)

---

**마지막 업데이트**: 2026년 2월 1일
**버전**: 1.0.0
