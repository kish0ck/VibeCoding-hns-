# 🏪 홈앤쇼핑 실시간 매출 모니터링 대시보드

홈앤쇼핑 판매 데이터를 실시간으로 모니터링하고 시각화하는 Streamlit 기반 대시보드 애플리케이션입니다.

---

## 📋 프로젝트 개요

이 프로젝트는 다음을 목표로 합니다:
- **실시간 매출 현황 모니터링** - Supabase에서 데이터를 조회하여 최신 정보 제공
- **한국어 지원 대시보드** - 완전한 한국어 인터페이스
- **인터랙티브 시각화** - Plotly를 이용한 다양한 차트 제공
- **빠른 로딩** - Streamlit 캐싱으로 성능 최적화

---

## 🛠️ 기술 스택

| 항목 | 기술 |
|------|------|
| **프로젝트 타입** | Python 웹 애플리케이션 |
| **웹 프레임워크** | Streamlit ≥1.28.0 |
| **데이터 분석** | Pandas ≥2.0.0 |
| **데이터 시각화** | Plotly ≥5.17.0 |
| **API 통신** | Requests ≥2.31.0 |
| **백엔드 데이터베이스** | Supabase (PostgreSQL) |
| **Python 버전** | 3.8 이상 |

---

## 📦 필수 요구사항

- **Python 3.8 이상** 설치 필요
- **pip** (Python 패키지 관리자)
- **Supabase 계정** (데이터베이스 연동용)
  - Supabase URL
  - Supabase API Key

---

## 🚀 설치 및 실행 가이드

### 1️⃣ 저장소 클론

```bash
git clone https://github.com/kish0ck/VibeCoding-hns-.git
cd VibeCoding-hns-
```

### 2️⃣ Python 가상환경 설정 (권장)

**Windows의 경우:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux의 경우:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 4️⃣ Supabase 설정

#### 4-1. secrets.toml 파일 생성

`.streamlit/secrets.toml` 파일을 생성하고 다음 내용을 추가합니다:

```toml
supabase_url = "https://your-project.supabase.co"
supabase_key = "your-anon-key"
```

#### 4-2. Supabase 정보 찾기

1. [Supabase 대시보드](https://supabase.com/dashboard)에 로그인
2. 프로젝트 선택 → **Settings** → **API**
3. **Project URL** 복사 → `supabase_url`에 붙여넣기
4. **anon public** 키 복사 → `supabase_key`에 붙여넣기

#### 4-3. Supabase 데이터베이스 설정

Supabase에서 다음과 같은 구조의 `sales` 테이블을 생성합니다:

```sql
CREATE TABLE sales (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  product_name VARCHAR(255),
  sales_amount DECIMAL(10, 2),
  quantity INTEGER,
  sale_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5️⃣ 애플리케이션 실행

```bash
streamlit run app.py
```

브라우저가 자동으로 열리며, 대시보드에 접속할 수 있습니다:
- **로컬 주소**: http://localhost:8501

---

## 📁 프로젝트 구조

```
VibeCoding-hns-/
├── app.py                      # 메인 대시보드 애플리케이션
├── requirements.txt            # Python 의존성 패키지 목록
├── test_app.py                 # 애플리케이션 테스트
├── capture_screenshot.py       # 대시보드 스크린샷 캡처 유틸리티
├── README.md                   # 이 파일
├── .streamlit/
│   └── secrets.toml           # Supabase 자격증명 (git에 포함 금지)
├── .devcontainer/
│   └── devcontainer.json      # Docker Dev Container 설정
├── data/
│   └── sales.csv              # 샘플 판매 데이터
└── .git/                       # Git 버전 관리

```

---

## 🎯 주요 기능

### 대시보드 메인 화면
- 📊 실시간 매출 현황 표시
- 📈 시계열 차트로 매출 추이 분석
- 📍 제품별 판매량 분석
- 🔄 자동 새로고침 기능

### 성능 최적화
- Streamlit의 `@st.cache_data` 데코레이터로 API 호출 캐싱
- 불필요한 재계산 방지

---

## 🔧 개발 가이드

### 로컬 개발 환경 설정

**Dev Container 사용 (VS Code):**
```bash
# VS Code에서 Remote - Containers 확장 프로그램 설치 후
# 프로젝트 폴더 열기 → "Reopen in Container" 클릭
```

### 새로운 패키지 추가

```bash
# 패키지 설치
pip install <package-name>

# requirements.txt 업데이트
pip freeze > requirements.txt
```

### 테스트 실행

```bash
python -m pytest test_app.py -v
```

또는

```bash
python test_app.py
```

### 스크린샷 캡처

```bash
python capture_screenshot.py
```

---

## 📚 Streamlit 주요 API

### 페이지 설정
```python
st.set_page_config(page_title="", layout="wide")
```

### 데이터 캐싱
```python
@st.cache_data
def fetch_data():
    # 비용이 큰 작업 (API 호출 등)
    return data
```

### UI 컴포넌트
```python
st.title()          # 제목
st.metric()         # 지표 표시
st.dataframe()      # 데이터 표 표시
st.plotly_chart()   # Plotly 차트 표시
st.sidebar.selectbox()  # 사이드바 선택 상자
```

---

## 🐛 문제 해결

### 문제: "Supabase 설정이 필요합니다" 에러

**원인**: `.streamlit/secrets.toml` 파일이 없음

**해결책**:
```bash
# .streamlit 폴더가 없다면 생성
mkdir .streamlit

# secrets.toml 파일 생성 (위의 '4️⃣ Supabase 설정' 참고)
```

### 문제: "ModuleNotFoundError: No module named 'streamlit'"

**원인**: 필수 패키지가 설치되지 않음

**해결책**:
```bash
# 가상환경이 활성화되었는지 확인
pip install -r requirements.txt
```

### 문제: Supabase 연결 실패 (상태 코드 401, 403)

**원인**: API Key가 잘못되었거나 권한이 없음

**해결책**:
1. Supabase 대시보드에서 API Key 재확인
2. `.streamlit/secrets.toml`에 올바르게 입력되었는지 확인
3. 앱 재시작 (Ctrl+C 후 `streamlit run app.py`)

### 문제: 포트 8501이 이미 사용 중

**원인**: Streamlit이 이미 실행 중

**해결책**:
```bash
# 다른 포트에서 실행
streamlit run app.py --server.port 8502
```

---

## 📝 커밋 히스토리

프로젝트 작업 내역:

| 커밋 | 설명 |
|------|------|
| `ac00ce6` | Initial commit: Add Streamlit dashboard for 홈앤쇼핑 sales monitoring |
| `a628fcb` | Added Dev Container Folder |
| `d584c92` | Update dashboard: Add real-time monitoring and improved features |
| `5af3b14` | Merge branch 'main' of GitHub repository |

---

## 🚢 배포 가이드

### Streamlit Cloud에 배포

1. **GitHub 저장소 준비**
   - 모든 코드가 GitHub에 푸시되어 있어야 함

2. **Streamlit Cloud 배포**
   ```bash
   # https://share.streamlit.io 방문
   # GitHub 계정으로 로그인
   # New app → VibeCoding-hns- 저장소 선택
   ```

3. **Secrets 설정**
   - Streamlit Cloud 대시보드 → Settings → Secrets
   - `.streamlit/secrets.toml`의 내용 복사하여 붙여넣기

### Docker를 이용한 배포

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 📧 문의 및 피드백

프로젝트 관련 문제나 개선 사항이 있다면:
- **이메일**: 3kistone@gmail.com
- **GitHub Issues**: [프로젝트 이슈](https://github.com/kish0ck/VibeCoding-hns-/issues)

---

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 제공됩니다.

---

**마지막 업데이트**: 2026년 6월 4일
