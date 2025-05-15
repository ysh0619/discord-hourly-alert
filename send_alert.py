import os
import requests
from datetime import datetime, timedelta

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

if not webhook_url:
    raise ValueError("환경변수 DISCORD_WEBHOOK_URL이 설정되지 않았습니다.")

# 한국 시간 기준 (UTC+9)
now = datetime.utcnow() + timedelta(hours=9)
minute = now.minute
hour = now.hour

if minute == 55:
    target_hour = (hour + 1) % 24
    message = f"⏰ {target_hour:02}시 정각 5분 전입니다! 준비하세요."
elif minute == 0:
    message = f"🕛 {hour:02}시가 되었습니다! 지금 시작하세요."
else:
    message = "✅ 예기치 않은 실행입니다. 확인 필요."

response = requests.post(webhook_url, json={"content": message})

if response.status_code != 204:
    print(f"전송 실패: {response.status_code} - {response.text}")
else:
    print("✅ 메시지 전송 성공")
