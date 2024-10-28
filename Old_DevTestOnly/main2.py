# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = r".\chrome.exe"

service = Service(r".\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 获取浏览器驱动对象
# driver = webdriver.Chrome()
# 浏览器最大化
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)

# 打开url
url = 'https://www.baidu.com/'
driver.get(url)
# 设置cookie
driver.add_cookie({"name": "BDUSS",
                   "value": "R5flpkUlBWbXJCNnFSQlZxeVJoY0FVQlljWERZSzFKamE1MUFlbDUyRmEtNlJlSVFBQUFBJCQAAAAAAAAAAAEAAADWOD6WeW9wdjEyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFpufV5abn1eV3"})

sleep(2)
# 刷新
driver.refresh()
"""
    目标： cookie操作
    案例：
        使用cookie绕过百度登录
    步骤：
        1.手动登录百度网站
        2.手动获得登陆后的cookies 'BDUSS'
        3.使用selenium内的add_cookie(name='BDSS',value='xxx')
"""

# 暂停3秒
sleep(5)
# 刷新
driver.quit()