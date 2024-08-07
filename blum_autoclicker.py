try:
    import keyboard
    # import os
    import pyautogui
    import pygetwindow as gw
    import random
    import time
    import win32api
    import win32con
    from termcolor import colored
except ImportError as e:
    print(f"[ERROR]: {e}")
    input("Press ENTER to exit...")
    exit(1)

# function to click a certain x, y position on the screen
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# function to get the window of the application
def get_window(window_name):
    try:
        window = gw.getWindowsWithTitle(window_name)[0]
        return window
    except IndexError:
        return None # if the window is not found

def is_window_none(window):
    if window is None:
        print(colored("[ERROR]", "red", attrs=['bold']), end="")
        print(colored(f" - Window '{window_name}' not found. Press ENTER to exit...", "red"), end="")
        input()
        exit(1)

# pyautogui.displayMousePosition()
window_name = "TelegramDesktop"
window = get_window(window_name)
is_window_none(window)

x_edit, y_edit, width_edit, height_edit, restart_button_x, restart_button_y = 9, 150, -18, -200, int(window.width / 2), -85
x, y, width, height = window.left + x_edit, window.top + y_edit, window.width + width_edit, window.height + height_edit

sleep_time = 1
print(colored("[INFO]", "white", attrs=['bold']), end="")
print(colored(f" - The program will start in {sleep_time} seconds. Press 'q' to activate/pause.", "white"))
time.sleep(sleep_time)

paused = False
while True:
    if keyboard.is_pressed('q'):
        paused = not paused # one time it pauses, the other time it resumes
        if paused:
            print(colored("[PAUSED]", "yellow", attrs=['bold']), end="")
            print(colored(" - Program paused. Press 'q' to activate.", "yellow"))
        else:
            print(colored("[ACTIVE]", "green", attrs=['bold']), end="")
            print(colored(" - Program active. Press 'q' to pause.", "green"))
        time.sleep(0.25)

    if paused:
        time.sleep(0.1)
    else:
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # iml = pyautogui.screenshot(region=(x, y, width, height))
        # iml.save(f"{current_dir}\screenshot.png")
        # time.sleep(1)

        # refresh the window status and coordinates
        window = get_window(window_name)
        is_window_none(window)
        x, y, width, height = window.left+x_edit, window.top+y_edit, window.width+width_edit, window.height+height_edit

        try:
            restart_button_color = pyautogui.pixel(window.left + restart_button_x, window.bottom + restart_button_y)
            if restart_button_color == (255, 255, 255):
                time.sleep(0.5) # sleep to not click the restart button too fast
                click(window.left + restart_button_x, window.bottom + restart_button_y)

            pic = pyautogui.screenshot(region=(x, y, width, height))
            width, height = pic.size
            for i in range(0, width, 2): # for loops for clicking the green objects
                for j in range(0, height, 2):
                    r, g, b = pic.getpixel((i, j))
                    if r == 205 and g == 220:
                        click(i + x, j + y)
                        time.sleep(0.001) # sleep to prevent too much CPU usage
                        j = height
        except:
            is_window_none(window)