import pyautogui as pg

def locateImage(image: str, grayscale: bool = False, confidence: float = 0.85, center: bool = False):
    screenshot = pg.screenshot()
    if not center:
       return pg.locate(image, screenshot, grayscale=grayscale, confidence=confidence)
    else:
        return pg.center(pg.locate(image, screenshot, grayscale=grayscale, confidence=confidence))
