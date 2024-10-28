from selenium import webdriver
import pickle
import time

# 初始化浏览器驱动
driver = webdriver.Chrome()

# 打开目标网站
driver.get("https://cc01.plusai.io")

# 加载 cookies 并添加到浏览器
with open("cookies.pkl", "rb") as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
print("已通过 Cookies 登录")
# 刷新页面以应用 cookies
# driver.flash
driver.get("https://cc01.plusai.io/c/671e6239-a070-800d-a205-6f47eab10f4e")


time.sleep(10)  # 观察登录效果
driver.quit()
