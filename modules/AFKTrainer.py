import ctypes
import time

hdwn = ctypes.windll.user32.FindWindowW(0, 'Tibia - Brunao Qqmuda') #nome da janela do tibia
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

F1=0x70
F2=0x71
F3=0x72
F4=0x73
F5=0x74
F6=0x75
F7=0x76
F8=0x77
F9=0x78
F10=0x79
F11=0x7A
F12=0x7B

def send_messege_keyboard(hdwd, key_code):
   ctypes.windll.user32.SendMessageW(hdwn, WM_KEYDOWN, key_code, 0)
   time.sleep(0.2)
   ctypes.windll.user32.SendMessageW(hdwn, WM_KEYUP, key_code, 0)


while True:
   send_messege_keyboard(hdwn, F12)
   time.sleep(2)
   send_messege_keyboard(hdwn, F11)
   time.sleep(2)
   send_messege_keyboard(hdwn, F10)
   time.sleep(2)
   send_messege_keyboard(hdwn, F9)