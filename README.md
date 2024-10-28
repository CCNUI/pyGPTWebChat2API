# GPT Web Chat Service

## 项目简介

GPT Web Chat Service 是一个基于 Selenium 自动化浏览器操作的服务，用于与 GPT Web 应用进行交互。它可以通过加载存储的 cookies 登录到目标站点，然后使用自动化脚本向 GPT 发送消息并获取回复。

## 功能特点
- 自动加载登录 cookies，跳过手动登录步骤。
- 通过 Selenium 自动化发送消息并获取回复。
- 支持命令行输入 prompt，用户可以方便地与 GPT 进行交互。
- 支持 Ctrl+C 中断信号，能够优雅地停止服务并关闭浏览器。

## 安装和配置

### 先决条件
1. **Python 3.x**
   - 本项目使用 Python 3 进行开发。
2. **Chrome 浏览器**
   - 请确保你已安装 Google Chrome 浏览器。
3. **ChromeDriver**
   - 请确保 ChromeDriver 版本与 Chrome 浏览器匹配，可以从 [ChromeDriver 官方页面](https://chromedriver.chromium.org/downloads) 下载。

### 安装依赖包

使用 `pip` 安装必要的依赖包：

```sh
pip install selenium
```

### 项目结构
```
project-directory/
|-- chrome-win64/
|   |-- chrome.exe
|-- chromedriver-win64/
|   |-- chromedriver.exe
|-- cookies.pkl
|-- gpt_web_chat_service.py
```

- `chrome-win64/chrome.exe`: Google Chrome 浏览器的可执行文件路径。
- `chromedriver-win64/chromedriver.exe`: ChromeDriver 的可执行文件路径。
- `cookies.pkl`: 存储登录信息的 Cookies 文件。
- `gpt_web_chat_service.py`: 主程序代码。

### 使用指南

1. **设置服务配置参数**

   在 `gpt_web_chat_service.py` 文件中，修改以下路径和 URL，使其适应你的环境：

   ```python
   chrome_path = r".\chrome-win64\chrome.exe"
   driver_path = r".\chromedriver-win64\chromedriver.exe"
   cookies_path = "cookies.pkl"
   url = "https://cc01.plusai.io/?temporary-chat=true&mmodel=gpt-4o-mini"
   ```

2. **运行服务**

   运行 Python 脚本启动聊天服务：

   ```sh
   python gpt_web_chat_service.py
   ```

3. **使用命令行输入交互**
   - 启动服务后，可以在命令行输入 prompt，与 GPT 进行交互。
   - 输入 `exit` 可以优雅地停止服务并退出浏览器。

### 注意事项
- **Cookies 文件**：确保 `cookies.pkl` 文件存在且有效，否则可能会导致登录失败。你可以使用 Selenium 自行登录并保存 cookies，方便下次自动登录。
- **浏览器路径**：修改代码中的 `chrome_path` 和 `driver_path`，使它们指向你本地的 Chrome 浏览器和 ChromeDriver 文件位置。

## 示例用法

以下是一个与 GPT 进行交互的示例：

```sh
输入 prompt（输入'exit'以停止服务): 你好，GPT！
Sending message: 你好，GPT！
Response: 你好！有什么我可以帮助你的吗？
```

## 贡献指南

欢迎大家为本项目贡献代码！如果你有改进建议或发现了 Bug，可以通过以下步骤参与贡献：

1. Fork 本仓库。
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)。
4. 推送到分支 (`git push origin feature/AmazingFeature`)。
5. 打开一个 Pull Request。

## 许可证

本项目采用 MIT 许可证。详情请参阅 LICENSE 文件。

## 常见问题

1. **为什么启动服务后无法加载页面？**
   - 请检查你的 `chrome_path` 和 `driver_path` 是否设置正确，确保它们与本地 Chrome 版本匹配。
2. **如何获取 `cookies.pkl` 文件？**
   - 你可以在首次手动登录后，通过 Selenium 的 `driver.get_cookies()` 方法保存 cookies。

## 联系方式

如果你对本项目有任何疑问或建议，请随时通过 [GitHub Issues](https://github.com/yourusername/your-repo/issues) 与我们联系。

