from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

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
driver.get("https://cc01.plusai.io/?temporary-chat=true&mmodel=gpt-4o-mini")

# 发送第一条测试消息
textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
textarea.click()
textarea.send_keys("这是一个测试消息")
send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]')))
send_button.click()

# 等待响应出现并打印第一次回复
# 等待 stop-button 出现并消失
try:
    # 等待 stop-button 出现
    stop_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="stop-button"]'))
    )
    print("Stop button is visible, waiting for it to disappear...")

    # 等待 stop-button 消失
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="stop-button"]'))
    )
    print("Stop button has disappeared.")
except Exception as e:
    print(f"Error waiting for stop button: {e}")

try:
    conversation_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@data-testid="conversation-turn-3"]'))
    )
    markdown_element = conversation_element.find_element(By.CSS_SELECTOR, ".markdown.prose.w-full.break-words.dark\\:prose-invert.dark")
    p_elements = markdown_element.find_elements(By.TAG_NAME, 'p')
    for p in p_elements:
        print(p.text)
except Exception as e:
    print(f"Error retrieving first response: {e}")

# 发送第二条测试消息
textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
textarea.click()
textarea.send_keys("再试一下")
send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]')))
send_button.click()

# 等待响应出现并打印第二次回复
# 等待 stop-button 出现并消失
try:
    # 等待 stop-button 出现
    stop_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="stop-button"]'))
    )
    print("Stop button is visible, waiting for it to disappear...")

    # 等待 stop-button 消失
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="stop-button"]'))
    )
    print("Stop button has disappeared.")
except Exception as e:
    print(f"Error waiting for stop button: {e}")
try:
    conversation_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@data-testid="conversation-turn-5"]'))
    )
    markdown_element = conversation_element.find_element(By.CSS_SELECTOR, ".markdown.prose.w-full.break-words.dark\\:prose-invert.dark")
    p_elements = markdown_element.find_elements(By.TAG_NAME, 'p')
    for p in p_elements:
        print(p.text)
except Exception as e:
    print(f"Error retrieving second response: {e}")

# 保持浏览器打开一段时间以观察结果
WebDriverWait(driver, 30).until(lambda d: d.execute_script("return document.readyState") == "complete")

# 关闭浏览器
driver.quit()
