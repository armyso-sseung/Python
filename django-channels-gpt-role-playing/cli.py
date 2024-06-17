import os
import openai
import pygame

from io import BytesIO
from tempfile import NamedTemporaryFile

# ENV 로드
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()

# ENV를 통한 API_KEY 등록
openai.api_key = os.getenv("OPENAI_API_KEY")


# 상황극 설정
language = "English"
gpt_name = "Steve"
level_string = f"a beginner in {language}"
level_word = "simple"
situation_en = "make new friends"
my_role_en = "me"
gpt_role_en = "new friend"

# 시스템 프롬프트
SYSTEM_PROMPT = (
    f"You are helpful assistant supporting people learning {language}."
    f"Your name is {gpt_name}. Please assume that the user you are assisting "
    f"is {level_string}. And please write only the sentence without "
    f"the character role."
)

# 사용자 프롬프트
USER_PROMPT = (
    f"Let's have a conversation in {language}. Please answer in {language} only "
    f"without providing a translation. And please don't write down the "
    f"pronunciation either. Let us assume that the situation in '{situation_en}'. "
    f"I am {my_role_en}. The character I want you to act as is {gpt_role_en}. "
    f"Please make sure that "
    f"I'm {level_string}, so please use {level_word} words as much as possible. "
    f"Now, start a conversation with the first sentence!"
)

# 추천요청 프롬프트
RECOMMEND_PROMPT = (
    f"Can you please provide me an {level_word} example "
    f"of how to respond to the last sentence "
    f"in this situation, without providing a translation "
    f"and any introductory phrases or sentences."
)

messages = [
    # 시스템 프롬프트 설정
    {"role": "system", "content": SYSTEM_PROMPT},
]


# 사용자 질문을 GPT에 보낸 후 답변을 받는 함수
def gpt_query(user_query: str, skip_save: bool = False) -> str:
    "유저 메시지에 대한 응답을 반환합니다."

    global messages
    messages.append({
        "role": "user",
        "content": user_query,
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    assistant_message = response["choices"][0]["message"]["content"]
    if skip_save is False:
        messages.append({
            "role": "assistant",
            "content": assistant_message,
        })

    return assistant_message


# 소리를 재생 시켜주는 함수
def play_file(file_path: str) -> None:
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.quit()


# 오디오 파일로 전환 시키는 함수
def say(message: str, lang: str):
    io = BytesIO()

    # 임시 파일로 저장 시키는 부분
    gTTS(message, lang=lang).write_to_fp(io)
    with NamedTemporaryFile() as f:
        f.write(io.getvalue())
        play_file(f.name)


def main():
    # 사용자 프롬프트 설정 후 답변 받기
    assistant_message = gpt_query(USER_PROMPT)
    print(f"[assistant] {assistant_message}")
    say(assistant_message, "en")

    # 질문
    while line := input("[name] ").strip():
        # 추천 표현 요청
        if line == "!recommend":
            recommend_message = gpt_query(RECOMMEND_PROMPT, True)
            print("추천 표현: ", recommend_message)

        # 음성 지원 요청
        elif line == "!say":
            say(messages[-1]["content"], "en")

        # 별도 요청 없을 시
        else:
            response = gpt_query(line)
            print(f"[assistant] {response}")
            say(response, "en")


if __name__ == "__main__":
    main()
