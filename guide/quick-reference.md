# 빠른 참조 가이드 (Quick Reference)

## 🎨 핵심 색상

```css
/* 배경 */
--bg-primary: #F5F1E8;
--bg-white: #FFFFFF;

/* 텍스트 */
--text-dark: #1A1A1A;
--text-gray: #4A4A4A;

/* 액센트 */
--accent: #E85D04;
```

## 📏 간격

```css
--space-sm: 0.5rem;   /* 8px */
--space-md: 1rem;     /* 16px */
--space-lg: 2rem;     /* 32px */
--space-xl: 4rem;     /* 64px */
```

## 📝 타이포그래피

```css
/* 제목 */
font-family: 'Playfair Display', serif;
font-size: 4rem;

/* 본문 */
font-family: 'Pretendard', sans-serif;
font-size: 1rem;
```

## 📐 그리드

```css
/* 데스크탑: 3열 */
grid-template-columns: repeat(3, 1fr);
gap: 2rem;

/* 태블릿: 2열 */
@media (max-width: 1024px) {
  grid-template-columns: repeat(2, 1fr);
}

/* 모바일: 1열 */
@media (max-width: 640px) {
  grid-template-columns: 1fr;
}
```

## 🎯 주요 개선사항

1. ✅ **누락된 읽기 시간 추가**
2. ✅ **카테고리 버튼 선택 상태 명확화**
3. ✅ **카드 호버 효과 개선**
4. ⚡ **검색 기능 강화** (실시간 필터링)
5. ⚡ **정렬 옵션 추가**
6. 💡 **북마크/읽음 표시** (선택)
7. 🌙 **다크 모드** (선택)

## 🔍 카테고리 색상

| 카테고리 | 배경색 | 텍스트 색상 |
|---------|--------|-----------|
| 마인드셋 | `#E8E8E8` | `#4A4A4A` |
| 시장진입 | `#FFF5E6` | `#8B4513` |
| 펀드레이징 | `#FFE8E8` | `#C84747` |
| 창업기초 | `#FFF9E6` | `#A67C00` |
| 기술/개발 | `#E6F7F7` | `#2C7A7B` |
| 조직문화 | `#F0E8FF` | `#6B46C1` |
| 성장전략 | `#E6F2FF` | `#2B5797` |

## ♿ 접근성 체크리스트

- [ ] 색상 대비 4.5:1 이상
- [ ] 키보드 네비게이션 지원
- [ ] 포커스 표시기 명확
- [ ] 대체 텍스트 제공
- [ ] ARIA 레이블 추가

## 📱 반응형 브레이크포인트

- Mobile: `640px`
- Tablet: `768px`
- Desktop: `1024px`
- Wide: `1280px`
