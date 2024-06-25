import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import json
import os
from conf import Constants

def create_folder(hunt):
    if not os.path.isdir(f'imgs/flags/{hunt}'):
        os.mkdir(f'imgs/flags/{hunt}')

class Rec:
    def __init__(self):
        self.count = 0
        self.coordinates = []

    def photo(self):
        global hunt
        x, y = pg.position()
        photo = pg.screenshot(region=(x - 3,y - 3, 6, 6))
        path = f'imgs/flags/{hunt}/flag_{self.count}.png'
        photo.save(path)
        self.count = self.count + 1
        infos = {
            "path": path,
            "down_hole": 0,
            "up_hole": 0,
            "wait": 10,
        }
        self.coordinates.append(infos)

    def down_hole(self):
        last_coordinates = self.coordinates[-1]
        last_coordinates['down_hole'] = 1

    def up_hole(self):
        last_coordinates = self.coordinates[-1]
        last_coordinates['up_hole'] = 1

    def key_code(self,key):
        global hunt
        if key == keyboard.Key.esc:
            with open(f'scripts/{hunt}.json', 'w') as file:
                file.write(json.dumps(self.coordinates))
            return False
        if key == keyboard.Key.insert:
            self.photo()
        if key == keyboard.Key.page_down:
            self.down_hole()
        if key == keyboard.Key.page_up:
            self.up_hole()

    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()

global hunt
hunt = (input('Digite o nome da hunt: '))
create_folder(hunt)
record = Rec()
record.start()
