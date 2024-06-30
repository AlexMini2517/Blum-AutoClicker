try:
    import keyboard
    # import os
    import pyautogui
    import pygetwindow as gw
    import pyscreeze
    import random
    import time
    import win32api
    import win32con
except ImportError as e:
    print(f"[ERROR]: {e}")
    input("Press ENTER to exit...")
    exit(1)

# function to click a certain x, y position on the screen
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# function to check if the mouse has moved
def has_mouse_moved(prev_pos):
    current_pos = pyautogui.position()
    return current_pos != prev_pos

# function to get the window of the application
def get_window(window_name):
    try:
        window = gw.getWindowsWithTitle(window_name)[0]
        return window
    except IndexError:
        return None # if the window is not found

def is_window_none(window):
    if window is None:
        input("Window not found. Press ENTER to exit...")
        exit(1)

# function to get the choice of the user
def show_menu():
    print("1: TelegramDesktop")

# pyautogui.displayMousePosition()

show_menu()
choice = input("Select the window you want to use: ")
print()
if choice == "1":
    window_name = "TelegramDesktop"
else:
    input("Invalid choice. Press ENTER to exit...")
    exit(1)

window = get_window(window_name)
is_window_none(window)

window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height
x_edit, y_edit, width_edit, height_edit, restart_button_x, restart_button_y = 9, 70, -18, -120, int(window_width/2), -85
x, y, width, height = window_left+x_edit, window_top+y_edit, window_width+width_edit, window_height+height_edit

sleep_time = 1
print(f"[STARTING] - The program will start in {sleep_time} seconds. Press 'q' to pause/resume.")
time.sleep(sleep_time)

prev_mouse_pos = pyautogui.position() # get the initial position of the mouse
mouse_stationary_start = time.time()
paused = False
while True:
    if keyboard.is_pressed('q'):
        paused = not paused # one time it pauses, the other time it resumes
        if paused:
            print("  [PAUSED] - Program paused. Press 'q' to resume.")
        else:
            print(" [RESUMED] - Program resumed. Press 'q' to pause.")
            # get the window again in case it was moved
            window = get_window(window_name)
            is_window_none(window)
            window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height
            x, y, width, height = window_left+x_edit, window_top+y_edit, window_width+width_edit, window_height+height_edit
        time.sleep(0.5)

    if not paused:
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # iml = pyautogui.screenshot(region=(x, y, width, height))
        # iml.save(r"{current_dir}\screenshot.png")

        window = get_window(window_name)
        is_window_none(window)
        
        pic = pyautogui.screenshot(region=(x, y, width, height))
        width, height = pic.size
        for i in range(0, width, 2): # for loops for clicking the green objects
            for j in range(0, height, 2):
                r, g, b = pic.getpixel((i, j))
                if r == 205 and g == 220:
                    click(i + x, j + y)
                    time.sleep(0.001) # sleep to prevent too much CPU usage
                    break
        
        if has_mouse_moved(prev_mouse_pos): # check if the mouse has moved
            prev_mouse_pos = pyautogui.position()
            mouse_stationary_start = time.time()
        elif time.time() - mouse_stationary_start > 2: # if the mouse has not moved for 2 seconds, click the restart button
            restart_button_color = pyautogui.pixel(window.left+restart_button_x, window.bottom+restart_button_y)
            if restart_button_color == (255, 255, 255):
                click(window.left+restart_button_x, window.bottom+restart_button_y)
            mouse_stationary_start = time.time()