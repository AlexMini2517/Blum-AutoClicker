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
    print(f"[ERROR]: {e}. Press ENTER to exit...")
    input()
    exit(1)

# function to click a certain x, y position on the screen
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def double_click(x, y):
    click(x, y)
    time.sleep(0.1)
    click(x, y)

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

sleep_time = 1
print(colored("[INFO]", "white", attrs=['bold']), end="")
print(colored(f" - The program will start in {sleep_time} seconds. Press 'q' to activate/pause.", "white"))
time.sleep(sleep_time)

paused = False
flag = 0
offset = 0
index = 0
while True:
    if offset != 40*3:
        click(25, 50) # user menu
        time.sleep(1)
        click(135, 185+offset) # user 1
        time.sleep(1)
        click(305, 50) # search bar
        time.sleep(1)
        pyautogui.write("https://t.me/BlumCryptoBot")
        time.sleep(2)
        click(305, 100) # blum bot
        time.sleep(1)
        click(810, 925) # start bot
        time.sleep(5)

        window_name = "TelegramDesktop"
        window = get_window(window_name)
        is_window_none(window)

        window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height
        x_edit, y_edit, width_edit, height_edit, restart_button_x, restart_button_y = 9, 150, -18, -200, int(window_width / 2), -85
        x, y, width, height = window_left + x_edit, window_top + y_edit, window_width + width_edit, window_height + height_edit
        click(window.left + restart_button_x, window.bottom + restart_button_y)
        time.sleep(1)

        click(960, 715) # farming button
        time.sleep(1)
        click(960, 715) # farming button
        time.sleep(1)

        click(1050, 490) # click and then scroll to show the play button
        time.sleep(1)
        pyautogui.scroll(-300)
        time.sleep(1)

        click(1080, 620) # click the play button inside the blum app
        time.sleep(1)
        offset += 40

        # start the autoclicker
        prev_mouse_pos = pyautogui.position()
        last_move_time = time.time()
        while flag==0:
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
                window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height
                x, y, width, height = window_left+x_edit, window_top+y_edit, window_width+width_edit, window_height+height_edit

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
                    
                    current_mouse_position = pyautogui.position()
                    if current_mouse_position != prev_mouse_pos:
                        prev_mouse_pos = current_mouse_position
                        last_move_time = time.time()
                    if time.time() - last_move_time > 3:
                        flag = 1
                except:
                    is_window_none(window)
        
        flag = 0
        click(1120, 195) # close the blum window
        time.sleep(1)
    else:
        if index == 0:
            index += 3
            offset = 0
            click(1919, 1079) # go to desktop
            time.sleep(1)
            double_click(875, 735) # open the second telegram
            time.sleep(5)
        else:
            exit(1)