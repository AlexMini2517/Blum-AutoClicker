from pyautogui import *
import pyautogui, time, keyboard, random, win32api, win32con, pyscreeze, pygetwindow as gw

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
def get_window():
    try:
        window = gw.getWindowsWithTitle(window_name)[0]
        return window
    except IndexError:
        return None # if the window is not found

def get_settings(choice):
    if choice == "1": # TelegramDesktop
        return 9, 70, -18, -120, 50, -90
    elif choice == "2": # Unigram
        return 9, 60, -32, -80, 50, -70

# function to get the choice of the user
def get_choice():
    print("Select the window you want to use:")
    print("1: TelegramDesktop")
    print("2: Unigram")
    choice = input("Enter the number of the window you want to use: ")
    return choice

choice = get_choice()
if choice == "1":
    window_name = "TelegramDesktop"
elif choice == "2":
    window_name = "Unigram"

window = get_window()
if window is None:
    input("Window not found. Press ENTER to exit.")
    exit(1)

# pyautogui.displayMousePosition()

window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height
x_edit, y_edit, width_edit, height_edit, restart_button_x, restart_button_y = get_settings(choice)
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
            window = get_window()
            window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height
            x, y, width, height = window_left+x_edit, window_top+y_edit, window_width+width_edit, window_height+height_edit
        time.sleep(0.5)

    if not paused:
        # iml = pyautogui.screenshot(region=(x, y, width, height))
        # iml.save(r"Python\Blum\image.jpg")
        
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
            click(window.left+restart_button_x, window.bottom+restart_button_y)
            mouse_stationary_start = time.time()