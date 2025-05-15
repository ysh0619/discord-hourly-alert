import os
import requests
from datetime import datetime, timedelta

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

if not webhook_url:
    raise ValueError("환경변수 DISCORD_WEBHOOK_URL이 설정되지 않았습니다.")

# 현재 시간 (UTC+9 → 한국 시간)
now = datetime.utcnow() + timedelta(hours=9)
hour = now.hour
minute = now.minute

# 알림 제한 시간: 00:00 ~ 07:59
if 0 <= hour < 8:
    print(f"⏰ 현재 시간 {hour:02}:{minute:02} - 알림 제한 시간입니다. 전송 생략.")
    exit(0)

# 알림 허용된 분인지 확인
if minute not in [15, 20, 55]:
    print(f"⏰ 현재 시간 {hour:02}:{minute:02} - 대상 분이 아니므로 전송 생략.")
    exit(0)

# 알림 메시지 전송
next_hour = (hour + 1) % 24
message = f"⏰ 결계 5분 전입니다! @everyone"

response = requests.post(webhook_url, json={"content": message})

if response.status_code != 204:
    print(f"전송 실패: {response.status_code} - {response.text}")
else:
    print("✅ 메시지 전송 성공")
