from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import pyautogui
import time

# 设置 Chrome 浏览器选项
chrome_options = Options()
chrome_options.binary_location = r".\chrome-win64\chrome.exe"
service = Service(r".\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开目标网站
driver.get("https://cc01.plusai.io")

# 加载 cookies 并添加到浏览器
with open("cookies.pkl", "rb") as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
print("已通过 Cookies 登录")

# 刷新页面以应用 cookies
driver.get("https://cc01.plusai.io/c/671e6239-a070-800d-a205-6f47eab10f4e")

# 等待页面加载
time.sleep(5)

# 定位输入框并输入消息
textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
textarea.click()
textarea.send_keys("这是一个测试消息")
# 等待发送按钮可点击并发送消息
send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]')))
#send_button.click()

# 等待一段时间以便页面加载
time.sleep(1)

# 尝试点击模型切换按钮
try:
    model_switch_button = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-testid, 'model-switcher-dropdown-button')]"))
    )
    model_switch_button.click()
except Exception as e:
    print(f"点击 model-switcher 失败: {e}")

# 使用 pyautogui 查找按钮图像并点击
def click_button_by_image(image_path):
    try:
        button_location = pyautogui.locateOnScreen(image_path)
        if button_location:
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center)
            print("成功点击按钮")
        else:
            print("未找到按钮")
    except Exception as e:
        print(f"图像识别出错: {e}")

# 尝试点击按钮
click_button_by_image("model_button2.png")

# 切换到另一个模型
model_switch_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-testid, 'temporary-chat-toggle')]"))
)
model_switch_button.click()

# 等待并再次点击按钮图像
time.sleep(5)
click_button_by_image("model_button2.png")

# 切换到 GPT-4o mini 模型
model_switch_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@data-testid, 'model-switcher-gpt-4o-mini')]"))
)
model_switch_button.click()

# 发送第一条测试消息
textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
textarea.click()
textarea.send_keys("这是一个测试消息")
send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]')))
send_button.click()

# 接收第一次回复
textarea.send_keys("-")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]')))
# 查找具有 data-testid="conversation-turn-3" 的元素
conversation_element = driver.find_element(By.XPATH, '//*[@data-testid="conversation-turn-3"]')
# 查找类为 .markdown.prose.w-full.break-words.dark:prose-invert.dark 的元素
markdown_element = conversation_element.find_element(By.CSS_SELECTOR, ".markdown.prose.w-full.break-words.dark\\:prose-invert.dark")
# 查找 <p> 标签并打印文本内容
p_elements = markdown_element.find_elements(By.TAG_NAME, 'p')
for p in p_elements:
    print(p.text)

# 发送第二条测试消息
textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
textarea.click()
textarea.send_keys("再试一下")
send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]')))
send_button.click()

time.sleep(2)
# 接收第二次回复
textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
textarea.click()
textarea.send_keys("-")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]')))
# 查找具有 data-testid="conversation-turn-3" 的元素
conversation_element = driver.find_element(By.XPATH, '//*[@data-testid="conversation-turn-5"]')
# 查找类为 .markdown.prose.w-full.break-words.dark:prose-invert.dark 的元素
markdown_element = conversation_element.find_element(By.CSS_SELECTOR, ".markdown.prose.w-full.break-words.dark\\:prose-invert.dark")
# 查找 <p> 标签并打印文本内容
p_elements = markdown_element.find_elements(By.TAG_NAME, 'p')
for p in p_elements:
    print(p.text)

# 保持浏览器打开一段时间以观察结果
time.sleep(5)

# 关闭浏览器
driver.quit()
