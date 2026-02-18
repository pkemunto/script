
# Email Automation Script

This project lets you **send an email with an attachment automatically** using Python.
Even if you’ve never coded before, you just need to enter your email details inside the script and run it.

---

## 📂 Repository Structure

```
your-repo/
│
├── script/
│   ├── sendemail.py        # The main script to send emails
│   └── TEY.pdf             # File that will be attached
│
└── README.md
```

---

## 🛠️ How It Works

1. Open the `sendemail.py` file in a text editor.
2. Enter your email credentials and SMTP settings at the top of the file:

```python
EMAIL = "your-email@gmail.com"
PASSWORD = "your-password"  # Use an app password for Gmail
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
```

3. The script connects securely to your email provider using SMTP.
4. It builds the email, attaches `TEY.pdf`, and sends it to the recipient.

> ⚠️ The email will be sent from the account you enter in the script.

---

## ⚙️ Setup & Running the Script

1. Make sure [Python](https://www.python.org/downloads/) is installed.
   Check in a terminal:

```bash
python --version
```

2. Navigate to the `script` folder in your terminal or command prompt.
3. Run the script:

```bash
python sendemail.py
```

Your email with the attachment will be sent automatically.

---

## 📌 Notes for Non-Coders

* Keep `TEY.pdf` in the same folder as `sendemail.py`.
* If using Gmail, create an **App Password** instead of your main password.
* **Never share your email and password** publicly.

---

## ✅ Optional: Run Without Terminal (Windows)

Create a `run_email.bat` file inside the `script` folder:

```bat
@echo off
python sendemail.py
pause
```

Double-click it to run the script without opening the terminal.

---

This version makes it **super simple** for someone to use — they just edit the credentials inside the file and run it.

If you want, I can **also rewrite the `sendemail.py` top section** to clearly mark where to put credentials, so even a beginner won’t get confused. Do you want me to do that?
