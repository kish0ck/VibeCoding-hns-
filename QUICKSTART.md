# ⚡ 빠른 시작 가이드 (Quick Start)

## 5분 안에 시작하기

### Step 1: 저장소 클론 (1분)

```bash
git clone https://github.com/kish0ck/VibeCoding-hns-.git
cd VibeCoding-hns-
```

### Step 2: 가상환경 설정 (1분)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: 패키지 설치 (2분)

```bash
pip install -r requirements.txt
```

### Step 4: Supabase 설정 (1분)

`.streamlit/secrets.toml` 파일을 생성하고 다음을 붙여넣기:

```toml
supabase_url = "https://your-project.supabase.co"
supabase_key = "your-anon-key"
```

> **Supabase URL과 API Key는 어디서?**
> 1. https://supabase.com/dashboard에 로그인
> 2. 프로젝트 선택 → Settings → API
> 3. Project URL과 anon public key 복사

### Step 5: 실행하기 (즉시!)

```bash
streamlit run app.py
```

**끝!** 🎉 브라우저에서 http://localhost:8501 접속

---

## 자주 묻는 질문

**Q: Python이 없다고 나옵니다**
- A: https://www.python.org/downloads/ 에서 Python 3.8 이상 설치

**Q: "ModuleNotFoundError" 에러가 나옵니다**
- A: 가상환경이 활성화되었는지 확인 후 `pip install -r requirements.txt` 재실행

**Q: Supabase 에러가 나옵니다**
- A: `.streamlit/secrets.toml` 파일이 존재하고 올바른 내용이 있는지 확인

**Q: 포트 8501이 이미 사용 중이라고 나옵니다**
- A: `streamlit run app.py --server.port 8502` 로 다른 포트 사용

---

더 자세한 내용은 [README.md](README.md)를 참고하세요.
