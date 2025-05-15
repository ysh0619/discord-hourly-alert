import os
import requests
from datetime import datetime, timedelta

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

if not webhook_url:
    raise ValueError("환경변수 DISCORD_WEBHOOK_URL이 설정되지 않았습니다.")

# 현재 시간 (UTC → 한국 시간)
now = datetime.utcnow() + timedelta(hours=9)
hour = now.hour
minute = now.minute

# 00시 ~ 07시 제외
if hour < 8:
    print(f"⏰ {hour:02}:{minute:02} - 알림 제한 시간입니다. 전송 생략.")
    exit(0)

# 메시지 전송
next_hour = (hour + 1) % 24
message = f"⏰ {next_hour:02}시 결계 5분 전입니다!@everyone"

response = requests.post(webhook_url, json={"content": message})

if response.status_code != 204:
    print(f"전송 실패: {response.status_code} - {response.text}")
else:
    print("✅ 메시지 전송 성공")
