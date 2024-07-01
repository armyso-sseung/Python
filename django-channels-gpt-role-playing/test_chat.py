import os
import openai

# ENV 로드
from dotenv import load_dotenv
load_dotenv()

# OpenAI 클래스 내부에서 OPENAI_API_KEY 환경변수를 참조합니다.
client = openai.OpenAI()  # api_key=os.getenv("OPENAI_API_KEY"))


# GPT 응답 받아오기
# SYSTEM: 역할을 부여 하는 PROMPT
# USER: 사용자가 요청 하는 메시지
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 영어 학습을 도와주는 챗봇입니다."},
        {"role": "user", "content": "대화를 나눠봅시다."}
    ]
)

print(response)
print(response.choices[0].message.content)