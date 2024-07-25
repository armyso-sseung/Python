# 모듈 가져오기
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager # 크롬버전을 확인해서 자동으로 다운로드 후 사용해줌
import time

# 명시적 대기를 위해
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


def setVideoSpeed(browser):
    # 영상 속도 변경
    browser.execute_script('''
        setInterval(() => {
            document.getElementsByTagName("video")[0].playbackRate = 3.8;
        }, 5000);
    ''')

def getVideoTag(browser, iframe):
    try:
        # iframe 전환
        browser.switch_to.frame(iframe)
        videos = browser.find_elements(By.CSS_SELECTOR, 'video')
        if (len(videos) > 0):
            # 영상 음소거
            browser.execute_script("return arguments[0].muted = true;", videos[0])
        
            paused = browser.execute_script("return arguments[0].paused;", videos[0])
            if (paused):
                # 영상 재생버튼 클릭
                buttos = browser.find_elements(By.CSS_SELECTOR, "button[title='영상 재생']")
                if (len(buttos) > 0):
                    browser.execute_script("arguments[0].click();", buttos[0])
                    time.sleep(2)

                setVideoSpeed(browser)
            else:
                setVideoSpeed(browser)
                return
            
    except Exception as e:
        print(e)

    finally:
        # iframe 종료
        browser.switch_to.default_content()

def main():
    # URL
    FASTCAMPUS = 'https://skillflo.io/course-detail/14731/11468?tab=status'
    
    # 회원정보
    USER_ID = '아이디'
    USER_PWD = '패스워드'

    # 브라우저 꺼짐 방지 옵션
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # 불필요한 에러 메시지 삭제
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 브라우저 init
    service = Service(executable_path=ChromeDriverManager().install())
    browser = wd.Chrome(service=service, options=chrome_options)



    """
        -- 코드시작 --
        CREATE: 24.07.19
        MODIFY: 
        By. SeungHyeon Jung
    """

    # 브라우저 실행
    browser.get(FASTCAMPUS)
    time.sleep(2)

    # 로그인
    id_input = browser.find_element(By.CSS_SELECTOR, "input[data-e2e='email']")
    id_input.send_keys(USER_ID)

    pwd_input = browser.find_element(By.CSS_SELECTOR, "input[data-e2e='password']")
    pwd_input.send_keys(USER_PWD)
    pwd_input.send_keys(Keys.RETURN)
    time.sleep(3)
    
    # 로그인 후 브라우저 이동
    browser.get(FASTCAMPUS)
    time.sleep(2)

    # 강의보기
    browser.find_element(By.CSS_SELECTOR, "button.fc-button").click()
    time.sleep(3)


    while (True) :
        # 이어보기 알림
        confirm_buttons = browser.find_elements(By.CSS_SELECTOR, "button[data-e2e='modal-confirm']")
        if (len(confirm_buttons) > 0):
            confirm_buttons[0].click()
            time.sleep(3)
        
        # 영상부분
        iframes = browser.find_elements(By.CSS_SELECTOR, "iframe")
        for iframe in iframes:
            getVideoTag(browser, iframe)

        time.sleep(30)




    # 브라우저 종료 
    # time.sleep(2)
    # browser.quit()



if __name__ == '__main__':
    main()