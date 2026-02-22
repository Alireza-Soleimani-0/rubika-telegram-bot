# 🤖 Rubika Login Telegram Bot

A simple yet powerful Telegram bot that allows users to log into their Rubika account directly through Telegram.

The bot collects the user's phone number, sends the Rubika verification code, and completes the login process once the user submits the code.
Sessions are stored for future use, making the authentication process seamless and efficient.

---

## ✨ Features

✔️ Phone number authentication via Telegram
✔️ Automatic verification code request
✔️ Secure session storage
✔️ Asynchronous architecture for better performance
✔️ Lightweight and easy to deploy

---

## 🛠 Tech Stack

* **Python**
* **python-telegram-bot**
* **rubpy**
* **AsyncIO**

---

## 🚀 Getting Started

### 1️⃣ Install dependencies

```bash
pip install python-telegram-bot rubpy
```

### 2️⃣ Add your Telegram bot token

Open the file and replace:

```python
TOKEN = "YOUR_TOKEN"
```

### 3️⃣ Run the bot

```bash
python bot.py
```

---

## 🌐 Deployment Note

To run this bot on a remote server, the hosting environment must allow network access to Rubika data centers.
If the server cannot reach Rubika services, the login process will fail.

---

## 📌 Use Cases

* Automating Rubika authentication workflows
* Building Telegram-based service panels
* Educational purposes for async bot development

---

## 👨‍💻 Author

**Alireza Soleimani**

---

⭐ If you find this project useful, consider giving it a star on GitHub!
