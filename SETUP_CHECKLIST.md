# ✅ 환경 세팅 체크리스트

이 문서는 처음 이 프로젝트를 설정할 때 필요한 모든 단계를 체크리스트 형태로 정리한 것입니다.

---

## 사전 준비 (Prerequisites)

- [ ] **Python 3.8 이상 설치**
  - 확인: `python --version` 명령어로 버전 확인
  - 설치: https://www.python.org/downloads/
  
- [ ] **Git 설치** (소스코드 버전 관리용)
  - 확인: `git --version` 명령어로 확인
  - 설치: https://git-scm.com/

- [ ] **GitHub 계정** (코드 저장소 접근)
  - GitHub 회원가입: https://github.com/signup

- [ ] **Supabase 계정** (데이터베이스 연동)
  - Supabase 회원가입: https://supabase.com
  - 프로젝트 생성 완료

---

## 프로젝트 로컬 설정

### 1. 저장소 클론

- [ ] GitHub에서 저장소 클론
  ```bash
  git clone https://github.com/kish0ck/VibeCoding-hns-.git
  cd VibeCoding-hns-
  ```

- [ ] 프로젝트 폴더가 제대로 열렸는지 확인
  ```bash
  ls -la  # Mac/Linux
  dir     # Windows
  ```

### 2. Python 가상환경 설정

- [ ] **Windows 사용자**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- [ ] **Mac/Linux 사용자**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- [ ] 가상환경 활성화 확인
  ```bash
  python --version  # Python 경로가 프로젝트 내 venv를 가리킴
  ```

### 3. 패키지 설치

- [ ] 요구되는 Python 패키지 설치
  ```bash
  pip install -r requirements.txt
  ```

- [ ] 설치 확인
  ```bash
  pip list
  # 다음 패키지들이 설치되었는지 확인:
  # - streamlit
  # - pandas
  # - plotly
  # - requests
  ```

---

## Supabase 설정

### 1. Supabase 프로젝트 생성

- [ ] Supabase 대시보드 접속: https://supabase.com/dashboard
- [ ] "New Project" 클릭
- [ ] 프로젝트 이름 입력 (예: "hns-dashboard")
- [ ] 데이터베이스 비밀번호 설정
- [ ] 지역 선택 (권장: Asia (Seoul))
- [ ] 프로젝트 생성 완료 대기 (약 2-3분)

### 2. 데이터베이스 테이블 생성

- [ ] Supabase 대시보드 → "SQL Editor" 접속
- [ ] "New query" → 다음 SQL 실행:
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

- [ ] 테이블 생성 확인
  - "Table editor" → "sales" 테이블이 보이는지 확인

### 3. API 자격증명 복사

- [ ] Supabase 대시보드 → Settings → API
- [ ] **Project URL** 복사
  ```
  https://[your-project].supabase.co
  ```

- [ ] **anon public** 키 복사
  ```
  eyJhbGc... (매우 긴 문자열)
  ```

---

## 로컬 애플리케이션 설정

### 1. Secrets 파일 생성

- [ ] `.streamlit` 폴더 생성 (없는 경우)
  ```bash
  mkdir .streamlit  # Mac/Linux
  md .streamlit     # Windows
  ```

- [ ] `.streamlit/secrets.toml` 파일 생성
  ```bash
  # Mac/Linux
  touch .streamlit/secrets.toml
  
  # Windows (VS Code, Notepad++ 등으로 직접 생성)
  ```

### 2. Secrets 파일 작성

- [ ] 다음 내용을 `.streamlit/secrets.toml`에 입력:
  ```toml
  supabase_url = "https://[your-project].supabase.co"
  supabase_key = "eyJhbGc..."  # 위에서 복사한 anon key
  ```

- [ ] 파일 저장 확인
  - 파일이 존재하고 올바른 경로: `.streamlit/secrets.toml`

### 3. Git 보안 설정

- [ ] `.gitignore` 확인
  ```bash
  cat .gitignore  # Mac/Linux
  type .gitignore # Windows
  ```

- [ ] `.streamlit/secrets.toml`이 `.gitignore`에 포함되어 있는지 확인
  ```
  .streamlit/secrets.toml
  ```

---

## 애플리케이션 테스트

### 1. 기본 실행 테스트

- [ ] Streamlit 앱 시작
  ```bash
  streamlit run app.py
  ```

- [ ] 브라우저 접속
  - URL: http://localhost:8501
  - 대시보드가 정상으로 로드되는지 확인

### 2. Supabase 연결 테스트

- [ ] 대시보드에서 데이터가 표시되는지 확인
  - 에러 메시지가 없는지 확인
  - "❌ Supabase 연결 실패" 메시지가 없는지 확인

- [ ] 샘플 데이터 추가 (선택사항)
  ```bash
  # Supabase 대시보드 → Table editor → sales
  # "+" 버튼으로 샘플 데이터 추가
  ```

### 3. 테스트 실행

- [ ] 테스트 코드 실행
  ```bash
  python test_app.py
  ```

- [ ] 모든 테스트가 통과하는지 확인

---

## IDE/에디터 설정 (선택사항)

### VS Code 설정

- [ ] VS Code 설치 (https://code.visualstudio.com/)

- [ ] 필수 확장 프로그램 설치:
  - [ ] "Python" (Microsoft)
  - [ ] "Pylance" (Microsoft)
  - [ ] "Streamlit" (Streamlit)

- [ ] Python Interpreter 설정
  - Ctrl+Shift+P → "Python: Select Interpreter"
  - `./venv/Scripts/python` 선택 (Windows)
  - `./venv/bin/python` 선택 (Mac/Linux)

### Dev Container 설정 (선택사항, Docker 필수)

- [ ] Docker 설치 (https://www.docker.com/)

- [ ] VS Code 확장 설치: "Remote - Containers"

- [ ] VS Code에서 프로젝트 폴더 열기

- [ ] "Reopen in Container" 클릭
  - Docker 이미지 빌드 대기 (약 5-10분)

---

## 버전 관리 설정

### Git 설정

- [ ] Git 사용자 이름 설정 (로컬)
  ```bash
  git config user.name "Your Name"
  git config user.email "your-email@example.com"
  ```

- [ ] 또는 전역 설정 (모든 프로젝트)
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your-email@example.com"
  ```

### GitHub 연결

- [ ] SSH 키 설정 (선택사항, 권장)
  - GitHub 공식 문서: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

- [ ] 또는 HTTPS 사용
  - GitHub 토큰 생성: https://github.com/settings/tokens

---

## 최종 확인

- [ ] 모든 체크리스트 항목 완료

- [ ] 다음 명령어들이 정상 작동:
  ```bash
  git status              # Git 상태 확인
  python --version       # Python 버전 확인
  streamlit run app.py   # 앱 실행
  ```

- [ ] GitHub에 코드 푸시 (초기 설정 후)
  ```bash
  git add .
  git commit -m "Initial setup complete"
  git push origin main
  ```

---

## 문제 해결

| 문제 | 해결 방법 |
|------|---------|
| Python을 찾을 수 없음 | Python을 설치하고 PATH에 추가 |
| 가상환경 활성화 실패 | `python -m venv venv` 재실행 |
| 패키지 설치 실패 | `pip install --upgrade pip` 후 재시도 |
| Supabase 연결 실패 | secrets.toml 파일 확인, app 재시작 |
| 포트 8501이 이미 사용 중 | `streamlit run app.py --server.port 8502` |
| Git 명령어 실패 | `git config --global user.email` 설정 |

---

## 설정 완료 후

✅ 축하합니다! 이제 개발할 준비가 되었습니다.

### 다음 단계:
1. [README.md](README.md)를 읽어 프로젝트 구조 이해
2. [QUICKSTART.md](QUICKSTART.md)를 참고하여 빠르게 시작
3. `app.py` 코드를 분석하여 기능 이해
4. 새로운 기능 추가 또는 버그 수정 시작

### 유용한 리소스:
- Streamlit 공식 문서: https://docs.streamlit.io/
- Supabase 공식 문서: https://supabase.com/docs
- Plotly 공식 문서: https://plotly.com/python/

---

**마지막 업데이트**: 2026년 6월 4일
