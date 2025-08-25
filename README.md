# Python Keylogger with Email Reporting

A Python-based keylogger that captures keyboard input and automatically sends logs via email. This project demonstrates cybersecurity concepts and network programming for educational purposes only.

Repository: https://github.com/Prajjwal2051/Key-Logger.git

## ⚠️ IMPORTANT ETHICAL DISCLAIMER

**This tool is for educational and research purposes only.** Users are solely responsible for compliance with applicable laws and regulations.

### ✅ Ethical Uses:
- Learning cybersecurity concepts
- Testing your own systems
- Authorized penetration testing
- Parental monitoring (with disclosure)
- Employee monitoring (with proper consent and legal compliance)
- Digital forensics on systems you own

### ❌ Prohibited Uses:
- Unauthorized monitoring of others
- Installing on computers without permission
- Stealing credentials or personal information
- Any illegal surveillance activities
- Violating privacy laws or terms of service

## 🚀 Features

- **Real-time Keystroke Capture**: Records all keyboard input including special keys
- **Automatic Email Reporting**: Sends keylog files via SMTP when stopped
- **Multi-Provider Support**: Works with Gmail, Outlook, Yahoo, and other email providers
- **User-Friendly Setup**: Interactive configuration for email credentials
- **Secure Authentication**: Uses App Passwords for enhanced security
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Clean Logging**: Timestamps and organized log format

## 📋 Prerequisites

### System Requirements
- Python 3.6 or higher
- Internet connection for email functionality
- Administrator/root privileges (may be required for keyboard monitoring)

### Python Dependencies
Install pynput using: pip install pynput

Note: smtplib, logging, email, os, re, and getpass are built-in Python modules.

## 📥 Download & Installation

### Method 1: Git Clone (Recommended)
Clone the repository using: git clone https://github.com/Prajjwal2051/Key-Logger.git
Navigate to project directory using: cd Key-Logger

### Method 2: Direct Download
1. Go to https://github.com/Prajjwal2051/Key-Logger.git
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file to your desired location
4. Open terminal/command prompt in the extracted folder

### Setup Virtual Environment (Recommended)
Create virtual environment using: python3 -m venv keylogger_env
Activate virtual environment - On Linux/macOS: source keylogger_env/bin/activate - On Windows: keylogger_env\Scripts\activate
Install dependencies using: pip install pynput

## 📧 Email Setup Guide

### Gmail Setup (Recommended)

#### Step 1: Enable 2-Step Verification
1. Go to Google Account Settings (https://myaccount.google.com)
2. Navigate to Security → 2-Step Verification
3. Follow the setup process to enable 2FA

#### Step 2: Generate App Password
1. In Security settings, find App passwords
2. Select Mail as the app type
3. Generate a 16-character password
4. Save this password - you'll use it in the program

#### Step 3: Enable IMAP
1. Open Gmail → Settings (gear icon)
2. Go to Forwarding and POP/IMAP tab
3. Enable IMAP access
4. Save changes

### Outlook/Hotmail Setup

#### Step 1: Enable 2-Step Verification
1. Go to Microsoft Security Settings (https://account.microsoft.com/security)
2. Enable Two-step verification

#### Step 2: Generate App Password
1. In Security settings, find App passwords
2. Click Create a new app password
3. Choose Mail as the app type
4. Save the generated password

### Yahoo Mail Setup

#### Step 1: Generate App Password
1. Go to Yahoo Account Security (https://login.yahoo.com/account/security)
2. Find App passwords section
3. Click Generate app password
4. Choose Mail as app type
5. Save the generated password

## 🖥️ Usage

### 1. Run the Program
Execute the keylogger using: python keylogger.py

### 2. Configure Email Settings
The program will prompt you to enter:
- Sender Email: Your email address
- Sender Password: Your App Password (not regular password)
- Recipient Email: Where to send the keylog

### 3. Start Keylogging
- The program will begin capturing keystrokes
- All input is logged to keylog.txt
- Real-time feedback is displayed in the console

### 4. Stop and Send Report
- Press Escape to stop the keylogger
- The program automatically emails the log file
- Check the recipient's email for the keylog report

## 📁 File Structure

Key-Logger/
├── keylogger.py (Main keylogger script)
├── keylog.txt (Generated log file)
├── README.md (This file)
└── requirements.txt (Python dependencies)

## 🔍 How It Works

### 1. Keystroke Capture
- Uses pynput.keyboard.Listener to monitor keyboard events
- Captures both regular characters (a, b, 1, 2) and special keys (Ctrl, Alt, Space)
- Logs all events with timestamps

### 2. Data Storage
- Saves keystrokes to keylog.txt using Python's logging module
- Includes timestamps for each keystroke
- Handles file creation and management automatically

### 3. Email Reporting
- Automatically detects email provider and uses appropriate SMTP server
- Creates MIME multipart message with log file attachment
- Uses secure TLS encryption for email transmission
- Supports Gmail, Outlook, Yahoo, and other major providers

### 4. Security Features
- Uses App Passwords instead of regular passwords
- Hides password input using getpass module
- Validates email address format
- Provides clear error messages for troubleshooting

## 🛠️ Configuration

### Email Provider Settings
The program automatically detects SMTP settings based on your email domain:

Gmail: smtp.gmail.com:587 (TLS)
Outlook/Hotmail: smtp-mail.outlook.com:587 (TLS)
Yahoo: smtp.mail.yahoo.com:587 (TLS)

### Custom SMTP Configuration
To use a different email provider, modify the get_smtp_server() function in the code.

## 🐛 Troubleshooting

### Common Issues

#### Authentication Failed Error
- Solution: Use App Password, not regular password
- Gmail: Generate App Password in Google Account Security
- Outlook: Generate App Password in Microsoft Account Security

#### No Module Named 'pynput' Error
Solution: Install pynput using: pip install pynput

#### Permission Denied Error
- Linux/macOS: Run with sudo if needed
- Windows: Run as Administrator
- Solution: Some systems require elevated permissions for keyboard monitoring

#### Email Not Received
- Check spam folder
- Verify recipient email address
- Ensure sender email has proper App Password
- Check internet connection

### Getting Help
1. Check error messages in console
2. Verify email setup following this guide
3. Test with a simple email first
4. Ensure all dependencies are installed

## 🔒 Security Considerations

### Data Protection
- Log files contain sensitive information - handle carefully
- Consider encrypting log files for additional security
- Delete log files after use if not needed
- Use secure channels when sharing logs

### Access Control
- Store App Passwords securely
- Don't hardcode credentials in the source code
- Use environment variables for production deployments
- Regularly rotate App Passwords

### Legal Compliance
- Obtain proper authorization before deployment
- Follow local privacy and surveillance laws
- Provide appropriate disclosure when monitoring
- Maintain audit trails for authorized use

## 🚀 Future Enhancements & Roadmap

### Version 2.0 Features (Planned)
- Screenshot Capture: Automatically take screenshots at intervals
- Audio Recording: Record microphone input alongside keystrokes
- Stealth Mode: Complete background operation with no console output
- Remote Access: Access logs remotely via web interface
- Real-time Monitoring: Live dashboard for real-time keystroke viewing

### Version 2.1 Features (Planned)
- Machine Learning: Detect suspicious typing patterns
- Multi-language Support: Support for different keyboard layouts
- Cloud Storage: Direct upload to cloud storage services (Google Drive, Dropbox)
- Mobile App: Companion mobile app for remote monitoring
- Advanced Encryption: End-to-end encryption for all communications

### Version 3.0 Features (Future Vision)
- Cross-platform GUI: Native desktop application for all platforms
- Network Monitoring: Monitor network traffic alongside keystrokes
- Behavioral Analysis: AI-powered user behavior analysis
- Compliance Tools: Built-in tools for legal compliance and audit trails
- Plugin Architecture: Extensible plugin system for custom features

## 📚 Educational Resources

### Learning Objectives
This project demonstrates:
- Network Programming: SMTP protocol implementation
- File I/O Operations: Logging and file management
- Input Handling: Keyboard event processing
- Email Protocols: MIME message construction
- Security Practices: App Password authentication
- Error Handling: Robust exception management

### Further Reading
- Python SMTP Documentation: https://docs.python.org/3/library/smtplib.html
- Pynput Documentation: https://pynput.readthedocs.io/
- Email Security Best Practices: https://owasp.org/www-community/controls/Email_Security
- Cybersecurity Ethics Guidelines: https://www.acm.org/code-of-ethics

## 🤝 Contributing

### Development Guidelines
1. Follow ethical use principles
2. Test thoroughly before submitting changes
3. Document new features clearly
4. Maintain compatibility with major email providers

### How to Contribute
1. Fork the repository
2. Create a feature branch using: git checkout -b feature/AmazingFeature
3. Commit your changes using: git commit -m 'Add some AmazingFeature'
4. Push to the branch using: git push origin feature/AmazingFeature
5. Open a Pull Request

### Reporting Issues
- Provide detailed error messages
- Include system information (OS, Python version)
- Describe steps to reproduce the issue
- Check existing issues before creating new ones

## 📄 License

This project is for educational purposes only. Users are responsible for compliance with applicable laws and regulations.

### Disclaimer
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. USE AT YOUR OWN RISK.

## 📞 Support

For educational questions or technical issues:
1. Check the troubleshooting section
2. Review the setup guide carefully
3. Ensure proper email configuration
4. Create an issue on GitHub with detailed information

Remember: Use this tool responsibly and ethically! 🛡️

## 🏷️ Version History

- v1.0: Initial release with basic keylogging and email functionality
- v1.1: Added multi-provider email support and improved error handling
- v1.2: Enhanced security with App Password support and input validation
- v1.3: Added download instructions and future roadmap
- v2.0: (Coming Soon) Screenshot capture and stealth mode

## 📋 Quick Start Checklist

Before running the keylogger, make sure you have:

- [ ] Python 3.6+ installed
- [ ] Downloaded/cloned the repository
- [ ] Installed pynput using: pip install pynput
- [ ] Set up 2-Step Verification on your email account
- [ ] Generated App Password for your email provider
- [ ] Enabled IMAP (for Gmail users)
- [ ] Read and understood the ethical guidelines
- [ ] Obtained proper authorization for monitoring

### Quick Commands
Clone repository using: git clone https://github.com/Prajjwal2051/Key-Logger.git
Install dependencies using: pip install pynput
Run the program using: python keylogger.py
Stop logging and send email by pressing Escape key while program is running

## 🔗 Useful Links

- Repository: https://github.com/Prajjwal2051/Key-Logger.git
- Issues: https://github.com/Prajjwal2051/Key-Logger/issues
- Releases: https://github.com/Prajjwal2051/Key-Logger/releases
- Wiki: https://github.com/Prajjwal2051/Key-Logger/wiki

*This README provides comprehensive guidance for educational use of this keylogger project. Always prioritize ethical considerations and legal compliance.*'''

print(readme_content)
