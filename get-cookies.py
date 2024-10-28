from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time

# 初始化浏览器驱动
driver = webdriver.Chrome()

# 打开目标网站
driver.get("https://cc01.plusai.io")

# 等待手动登录（或者在这里自动登录）
time.sleep(30)  # 让用户有时间手动登录网站

# 获取登录后的 cookies 并保存到文件
cookies = driver.get_cookies()
with open("cookies.pkl", "wb") as file:
    pickle.dump(cookies, file)

print("Cookies 已保存")
driver.quit()
