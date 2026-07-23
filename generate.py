import os, requests, json
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
today = datetime.now(KST)
weekday = ["월","화","수","목","금","토","일"][today.weekday()]

prompt = f"""오늘은 {today.month}월 {today.day}일 {weekday}요일이다.
전자공학 학부연구생으로 SAR 레이더 연구실에서 일하며,
대학원 진학과 논문 공부를 준비하는 사람에게
아침에 침대에서 일어나게 만드는 음성 메시지를 써라.

조건:
- 3~4문장, 말로 읽었을 때 자연스러운 구어체
- 뻔한 자기계발 문구 금지
- 오늘 하루의 구체적 행동 하나를 짚어줄 것
- 존댓말, 담백하게"""

r = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
    json={
        "model": "claude-sonnet-4-6",
        "max_tokens": 500,
        "messages": [{"role": "user", "content": prompt}],
    },
)

text = r.json()["content"][0]["text"].strip()

with open("message.txt", "w", encoding="utf-8") as f:
    f.write(text)

print(text)
