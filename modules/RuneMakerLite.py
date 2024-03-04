import time
import keyboard

def start():
    while True:
        keyboard.press_and_release('F2')
        time.sleep(1)
        keyboard.press_and_release('F4')
        time.sleep(5)
        keyboard.press_and_release('F3')
        time.sleep(5)
        keyboard.press_and_release('F1')
        time.sleep(5)
        keyboard.press_and_release('F2')

keyboard.wait('h')
start()