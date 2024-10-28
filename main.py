"""
main.py - 这是 GPT Web Chat Service 的主入口，用于启动聊天服务。

此程序的作用是初始化 GPTWebChatService，并启动命令行输入线程。

目前不能从main.py启动，还是得从GPTWebChat.py启动
"""

from GPTWebChat import GPTWebChatService
import threading
import signal
import sys

# 默认服务配置参数，需在GPTWebChat.py中修改
chrome_path = r".\chrome-win64\chrome.exe"
driver_path = r".\chromedriver-win64\chromedriver.exe"
cookies_path = "cookies.pkl"
url = "https://cc01.plusai.io/?temporary-chat=true&mmodel=gpt-4o-mini"


# 启动服务
def signal_handler(signum, frame):
    print("收到中断信号，正在停止服务...")
    chat_service.stop()
    sys.exit(0)


def start_service():
    global chat_service
    chat_service = GPTWebChatService(
        chrome_path=chrome_path,
        driver_path=driver_path,
        cookies_path=cookies_path,
        url=url
    )
    chat_service.start()


if __name__ == "__main__":
    # 注册信号处理器
    signal.signal(signal.SIGINT, signal_handler)

    # 启动聊天服务线程
    service_thread = threading.Thread(target=start_service)
    service_thread.daemon = True  # 设置为守护线程，以便程序退出时能够自动关闭
    service_thread.start()

    # 保持主线程运行，以便捕获信号
    print("聊天服务已启动，按 Ctrl+C 退出")
    while True:
        try:
            # 主线程等待
            service_thread.join(1)
        except KeyboardInterrupt:
            signal_handler(signal.SIGINT, None)