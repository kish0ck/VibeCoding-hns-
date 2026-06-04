# 🏗️ 프로젝트 아키텍처

이 문서는 프로젝트의 구조, 주요 컴포넌트, 데이터 흐름을 설명합니다.

---

## 📐 전체 시스템 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                     사용자 (브라우저)                          │
│                   http://localhost:8501                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  Streamlit 웹 서버                            │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           app.py (메인 애플리케이션)                    │  │
│  │                                                      │  │
│  │  • 페이지 레이아웃 설정                               │  │
│  │  • UI 컴포넌트 구성                                  │  │
│  │  • 데이터 조회 로직                                  │  │
│  │  • 시각화 생성                                       │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   Supabase REST API                          │
│              https://[project].supabase.co/rest/v1           │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        PostgreSQL 데이터베이스 (Supabase)              │  │
│  │                                                      │  │
│  │  • sales 테이블 (판매 데이터)                         │  │
│  │  • 자동 타임스탬프                                    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 프로젝트 디렉토리 구조

```
VibeCoding-hns-/
│
├── 🐍 Python 애플리케이션
│   ├── app.py                    # ⭐ 메인 Streamlit 애플리케이션
│   ├── test_app.py               # 단위 테스트
│   ├── capture_screenshot.py     # 스크린샷 캡처 유틸리티
│   └── requirements.txt           # Python 패키지 의존성
│
├── 📋 문서
│   ├── README.md                  # 프로젝트 개요 및 사용 설명서
│   ├── QUICKSTART.md              # 빠른 시작 가이드
│   ├── SETUP_CHECKLIST.md         # 환경 세팅 체크리스트
│   ├── ARCHITECTURE.md            # 이 파일 (시스템 구조)
│   └── DEPLOYMENT.md              # 배포 가이드 (선택사항)
│
├── 🔧 설정 파일
│   ├── .streamlit/
│   │   └── secrets.toml           # Supabase 자격증명 (⚠️ git 제외)
│   ├── .devcontainer/
│   │   └── devcontainer.json      # Docker Dev Container 설정
│   ├── .mcp.json                  # MCP 설정
│   ├── .gitignore                 # Git 제외 파일 목록
│   └── .claude/
│       └── settings.local.json    # Claude Code 설정
│
├── 📊 데이터 파일
│   └── data/
│       └── sales.csv              # 샘플 판매 데이터 (CSV)
│
├── 📸 스크린샷 및 리소스
│   ├── dashboard_app.png
│   ├── dashboard_final.png
│   ├── streamlit_dashboard.png
│   └── dashboard_screenshot.png
│
└── 🗂️ 버전 관리
    └── .git/                      # Git 저장소
```

---

## 📄 주요 파일 설명

### 1. `app.py` - 메인 애플리케이션 ⭐

**역할**: Streamlit 웹 애플리케이션의 핵심 파일

**주요 구성**:

```python
# 1. 페이지 설정
st.set_page_config(page_title="...", layout="wide")

# 2. 스타일 설정 (한글 폰트)
st.markdown("""<style>...</style>""", unsafe_allow_html=True)

# 3. 페이지 제목
st.title("📊 홈앤쇼핑 일일 매출 현황")

# 4. 데이터 조회 함수 (캐싱)
@st.cache_data
def fetch_sales_data():
    # Supabase REST API에서 데이터 조회
    
# 5. UI 컴포넌트
st.dataframe()      # 데이터 테이블
st.plotly_chart()   # 상호작용형 차트
st.metric()         # 지표 표시

# 6. 사이드바 (필터링)
st.sidebar.selectbox()
st.sidebar.date_input()
```

**주요 함수**:
- `fetch_sales_data()` - Supabase에서 판매 데이터 조회
- 데이터 처리 및 시각화 로직

---

### 2. `requirements.txt` - 패키지 의존성

```
streamlit>=1.28.0     # 웹 프레임워크
pandas>=2.0.0         # 데이터 분석
plotly>=5.17.0        # 상호작용형 차트
requests>=2.31.0      # HTTP 요청
```

**업데이트 방법**:
```bash
# 새 패키지 설치 후
pip install <package-name>

# requirements.txt 업데이트
pip freeze > requirements.txt
```

---

### 3. `.streamlit/secrets.toml` - 보안 자격증명

```toml
supabase_url = "https://[project].supabase.co"
supabase_key = "eyJhbGc..."
```

⚠️ **중요**: 이 파일은 `.gitignore`에 포함되어 있어 GitHub에 올라가지 않습니다.

**접근 방법** (app.py):
```python
supabase_url = st.secrets["supabase_url"]
supabase_key = st.secrets["supabase_key"]
```

---

### 4. `test_app.py` - 단위 테스트

애플리케이션의 핵심 함수들을 테스트합니다.

**실행**:
```bash
python test_app.py
```

---

### 5. `capture_screenshot.py` - 스크린샷 캡처

대시보드의 스크린샷을 자동으로 캡처합니다.

**실행**:
```bash
python capture_screenshot.py
```

---

## 🔄 데이터 흐름

### 1️⃣ 사용자 요청

```
사용자가 http://localhost:8501 접속
           ↓
Streamlit이 app.py 실행
```

### 2️⃣ 데이터 조회

```python
@st.cache_data
def fetch_sales_data():
    # URL 구성
    url = f"{supabase_url}/rest/v1/sales?select=*"
    
    # 헤더 설정 (인증)
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json"
    }
    
    # HTTP GET 요청
    response = requests.get(url, headers=headers)
    
    # JSON 응답을 DataFrame으로 변환
    df = pd.DataFrame(response.json())
    return df
```

### 3️⃣ 데이터 처리

```python
# Pandas를 사용한 데이터 분석
df['sale_date'] = pd.to_datetime(df['sale_date'])
daily_sales = df.groupby('sale_date')['sales_amount'].sum()
product_sales = df.groupby('product_name')['sales_amount'].sum()
```

### 4️⃣ 시각화

```python
# Plotly를 사용한 상호작용형 차트
fig = px.line(daily_sales, title="일일 매출 추이")
st.plotly_chart(fig, use_container_width=True)
```

### 5️⃣ 페이지 렌더링

```
UI 컴포넌트 → Streamlit 서버 → 브라우저 렌더링
```

---

## 🗄️ 데이터베이스 스키마

### Sales 테이블

```sql
CREATE TABLE sales (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  product_name VARCHAR(255),        -- 상품명
  sales_amount DECIMAL(10, 2),      -- 판매액
  quantity INTEGER,                 -- 수량
  sale_date DATE,                   -- 판매 날짜
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 생성 시간
);
```

**예시 데이터**:

| id | product_name | sales_amount | quantity | sale_date | created_at |
|----|---|---|---|---|---|
| 1 | 스킨케어 세트 | 150000 | 10 | 2026-06-01 | 2026-06-01 10:00:00 |
| 2 | 청소 용품 | 45000 | 5 | 2026-06-01 | 2026-06-01 10:05:00 |
| 3 | 침대 시트 | 89000 | 3 | 2026-06-02 | 2026-06-02 09:30:00 |

---

## 🔐 보안 고려사항

### 1. API 키 보호

```python
# ✅ 올바른 방법
supabase_key = st.secrets["supabase_key"]

# ❌ 잘못된 방법 (코드에 직접 작성)
supabase_key = "eyJhbGc..."  # 절대 금지!
```

### 2. HTTPS 통신

```python
# Supabase는 기본적으로 HTTPS 사용
url = f"{supabase_url}/rest/v1/..."  # https://...
```

### 3. 권한 제한

```python
# 기본 RLS (Row Level Security) 설정으로 데이터 접근 제한
# Supabase 대시보드에서 설정 가능
```

---

## 🚀 성능 최적화

### 1. Streamlit 캐싱

```python
@st.cache_data  # 함수 결과 캐싱
def fetch_sales_data():
    # API 호출 (초기 1회만 실행)
    # 이후 캐시된 데이터 반환
```

**이점**:
- API 호출 최소화
- 페이지 로드 속도 향상
- 서버 부하 감소

### 2. 데이터 필터링

```python
# 필요한 컬럼만 조회
url = f"{supabase_url}/rest/v1/sales?select=id,product_name,sales_amount"

# 날짜 범위로 필터링
url += f"&sale_date=gte.{start_date}&sale_date=lte.{end_date}"
```

### 3. 페이지 레이아웃

```python
st.set_page_config(layout="wide")  # 더 넓은 화면 활용
```

---

## 🔄 배포 파이프라인

```
로컬 개발
   ↓
Git Commit
   ↓
GitHub Push
   ↓
Streamlit Cloud 배포 (자동)
```

**배포 설정**:
1. GitHub에 코드 푸시
2. Streamlit Cloud 계정 생성
3. "New app" → GitHub 저장소 선택
4. Secrets 설정 (`.streamlit/secrets.toml` 내용)

---

## 📚 기술 스택 상세

| 레이어 | 기술 | 용도 |
|------|------|------|
| **프론트엔드** | Streamlit | 웹 UI/UX |
| **시각화** | Plotly | 인터랙티브 차트 |
| **데이터 처리** | Pandas | 데이터 분석 및 변환 |
| **백엔드** | Supabase (PostgreSQL) | 데이터베이스 |
| **API** | Supabase REST API | 클라이언트-서버 통신 |
| **배포** | Streamlit Cloud | 웹 호스팅 |

---

## 🔗 컴포넌트 상호작용도

```
Streamlit 페이지
│
├─ 헤더 (제목, 설명)
│
├─ 메트릭 (KPI)
│  ├─ 총 매출
│  ├─ 총 판매량
│  └─ 평균 판매액
│
├─ 필터 (사이드바)
│  ├─ 날짜 범위
│  ├─ 상품 선택
│  └─ 정렬 옵션
│
├─ 주요 차트
│  ├─ 일일 매출 추이 (라인 차트)
│  ├─ 상품별 판매액 (막대 그래프)
│  └─ 판매량 분포 (원형 차트)
│
└─ 상세 데이터
   └─ 판매 기록 테이블 (DataFrame)
```

---

## 💡 확장 가능성

### 새로운 기능 추가

1. **새로운 데이터 조회**
   ```python
   def fetch_customers():
       # customers 테이블에서 데이터 조회
   ```

2. **새로운 차트**
   ```python
   fig = px.scatter(df, x='date', y='sales_amount', title='...')
   st.plotly_chart(fig)
   ```

3. **새로운 페이지**
   ```
   pages/
   ├── analytics.py     # 분석 페이지
   ├── reports.py       # 보고서 페이지
   └── settings.py      # 설정 페이지
   ```

---

## 📞 문제 진단

### 로그 확인

```bash
# Streamlit 상세 로그
streamlit run app.py --logger.level=debug
```

### API 응답 확인

```python
# 응답 상태 및 내용 확인
response = requests.get(url, headers=headers)
print(f"Status: {response.status_code}")
print(f"Body: {response.text}")
```

---

**마지막 업데이트**: 2026년 6월 4일
