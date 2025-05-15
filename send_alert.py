import os
import requests
from datetime import datetime, timedelta

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")

if not webhook_url:
    raise ValueError("환경변수 DISCORD_WEBHOOK_URL이 설정되지 않았습니다.")

# 현재 시간 (KST 기준)
now = datetime.utcnow() + timedelta(hours=9)
hour = now.hour
minute = now.minute

print(f"⏰ 현재 시간 (KST): {hour:02}:{minute:02} - 메시지 전송 중...")

message = f"🎯 현재 시간 {hour:02}:{minute:02}! 에픽다이스 열쇠를 획득해보세요! @everyone"

response = requests.post(webhook_url, json={"content": message})

if response.status_code != 204:
    print(f"전송 실패: {response.status_code} - {response.text}")
else:
    print("✅ 메시지 전송 성공")
