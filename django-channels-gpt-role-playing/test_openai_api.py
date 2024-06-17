import os
import openai

# ENV 로드
from dotenv import load_dotenv
load_dotenv()

# ENV를 통한 API_KEY 등록
openai.api_key = os.getenv("OPENAI_API_KEY")


# GPT 응답 받아오기
# Completion : 일반적인 새로운 텍스트를 형성하는 방식
response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="""
    Fix grammar errors:
    - I is a boy
    - You is a girl""".strip()
)

print(response)
print(response.choices[0].text.strip())


# ChatCompletion : 이전의 대화를 인지하고 이어서 하는 방식
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 지식이 풍부한 도우미입니다."},
        {"role": "user", "content": "세계에서 가장 큰 도시는 어디인가요?"}
    ]
)

print(response)
print(response["choices"][0]["message"]["content"])
