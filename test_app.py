#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys

# 라이브러리 확인
libs = ['streamlit', 'pandas', 'plotly', 'requests']
for lib in libs:
    try:
        __import__(lib)
        print(f"OK: {lib}")
    except ImportError:
        print(f"FAIL: {lib}")

# Supabase 연결 테스트
print("\n--- Supabase Test ---")
supabase_url = "https://tocyczehcbcqfksyvggr.supabase.co"
supabase_key = "sb_publishable_9gOkip9t8XZKJpiZvsyFBw_hn4QcRKD"

headers = {
    "apikey": supabase_key,
    "Authorization": f"Bearer {supabase_key}",
}

url = f"{supabase_url}/rest/v1/sales?select=date,category,sales&limit=3"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"SUCCESS: Connected - {len(data)} records loaded")
else:
    print(f"FAILED: {response.status_code}")
