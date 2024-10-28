"""
GPTWebChat.py - 这是 GPT Web Chat Service 的实现模块。

此模块定义了 GPTWebChatService 类，提供启动、停止服务以及通过 Selenium 与 GPT 进行交互的功能。
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import threading


class GPTWebChatService:
    def __init__(self, chrome_path, driver_path, cookies_path, url):
        # 设置 Chrome 浏览器选项
        chrome_options = Options()
        chrome_options.binary_location = chrome_path
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.cookies_path = cookies_path
        self.url = url
        self.conversation_counter = 3  # 初始值为 3
        self.is_running = False

    def start(self):
        try:
            # 启动服务，加载 Cookies 并登录
            self.load_cookies_and_login()
            self.is_running = True
            print("GPT Web Chat Service has started.")
        except Exception as e:
            print(f"Error starting service: {e}")
            self.stop()

    def load_cookies_and_login(self):
        # 打开目标网站
        print("Opening the target URL...")
        self.driver.get(self.url)

        # 加载 cookies 并添加到浏览器
        print("Loading cookies...")
        with open(self.cookies_path, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        print("Cookies loaded. Refreshing page to apply cookies...")

        # 刷新页面以应用 cookies
        self.driver.get(self.url)

    def send_message(self, message):
        # 检查服务是否在运行
        if not self.is_running:
            raise Exception("Service is not running. Please start the service first.")

        # 发送消息
        print(f"Sending message: {message}")
        try:
            textarea = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "prompt-textarea"))
            )
            textarea.click()
            textarea.send_keys(message)
            send_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]'))
            )
            send_button.click()

            # 等待 stop-button 出现并消失
            stop_button = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="stop-button"]'))
            )
            print("Stop button is visible, waiting for it to disappear...")

            WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="stop-button"]'))
            )
            print("Stop button has disappeared.")
        except Exception as e:
            print(f"Error during message sending: {e}")
            return None

        return self.get_response()

    def get_response(self):
        # 构造 conversation turn 的动态选择器
        conversation_xpath = f'//*[@data-testid="conversation-turn-{self.conversation_counter}"]'
        print(f"Attempting to retrieve response at {conversation_xpath}...")
        try:
            conversation_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, conversation_xpath))
            )
            markdown_element = conversation_element.find_element(By.CSS_SELECTOR,
                                                                 ".markdown.prose.w-full.break-words.dark\\:prose-invert.dark")
            p_elements = markdown_element.find_elements(By.TAG_NAME, 'p')
            response = "\n".join([p.text for p in p_elements])

            self.conversation_counter += 2
            print(f"Response received: {response}")
            return response
        except Exception as e:
            print(f"Error retrieving response: {e}")
            return None

    def stop(self):
        self.is_running = False
        print("正在退出浏览器...")
        self.driver.quit()
        print("GPT Web Chat Service has been stopped.")

    def command_listener(self):
        while self.is_running:
            command = input("输入prompt（输入'exit'以停止服务): ")
            if command.lower() == 'exit':
                self.stop()
            else:
                try:
                    response = self.send_message(command)
                    print(f"Response: {response}")
                except Exception as e:
                    print(f"Error executing command: {e}")

def signal_handler(signum, frame):
    print("收到中断信号，正在停止服务...")
    chat_service.stop()
    sys.exit(0)

# Example usage to simulate a service
if __name__ == "__main__":
    # 服务配置参数
    chrome_path = r".\chrome-win64\chrome.exe"
    driver_path = r".\chromedriver-win64\chromedriver.exe"
    cookies_path = "cookies.pkl"
    url = "https://cc01.plusai.io/?temporary-chat=true&model=gpt-4o-mini"

    # 启动服务
    chat_service = GPTWebChatService(chrome_path, driver_path, cookies_path, url)
    chat_service.start()

    # 启动命令输入线程
    input_thread = threading.Thread(target=chat_service.command_listener, daemon=True)
    input_thread.start()

    # 等待服务结束
    input_thread.join()

    # 停止服务
    # chat_service.stop()
