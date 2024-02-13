import ctypes
import pygetwindow as gw
import pyautogui
import win32gui

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002

def get_window_opacity(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, GWL_EXSTYLE)
    if ex_style & WS_EX_LAYERED:
        style = ctypes.c_ulong()
        opacity = ctypes.c_byte()
        ctypes.windll.user32.GetLayeredWindowAttributes(hwnd, None, ctypes.byref(opacity), ctypes.byref(style))
        return opacity.value
    else:
        return None

def hidden_client():
    windows = pyautogui.getAllWindows()
    for window in windows:
        try:
            window_name = window.title.split('Tibia -')[1]
            if window_name:
                WINDOW_TITLE = window.title
        except:
            continue

    try:
        target_window = [item for item in gw.getWindowsWithTitle(WINDOW_TITLE) if item.title == WINDOW_TITLE][0]
    except:
        pyautogui.alert(title="Hidden Client Tibia", text='Janela do Tibia não localizada')
        raise ValueError('Janela do Tibia não localizada')

    target_hwnd = target_window._hWnd

    OPACITY = 255
    current_opacity = get_window_opacity(target_hwnd)
    if current_opacity == -1:
        OPACITY = 1
    print('OPACITY', OPACITY)
    ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)
    ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, OPACITY, LWA_ALPHA)
    print("Opacidade da janela modificada.")
    if current_opacity is not None:
        print(f"Opacidade atual da janela: {current_opacity}")
    else:
        print("A janela não é uma janela de camada (layered window).")
    return OPACITY

