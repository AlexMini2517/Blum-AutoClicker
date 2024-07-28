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

def initialize():
    sleep_time = 1
    print(colored("[INFO]", "white", attrs=['bold']), end="")
    print(colored(f" - The program will start in {sleep_time} seconds. Press 'q' to activate/pause.", "white"))
    time.sleep(sleep_time)

def setup_blum_bot(offset):
    click(25, 50) # user menu
    time.sleep(1)
    click(135, 185+offset) # user 1, then the next users
    time.sleep(1)
    click(305, 50) # search bar
    time.sleep(1)
    pyautogui.write("https://t.me/BlumCryptoBot")
    time.sleep(2)
    click(305, 100) # blum bot
    time.sleep(1)
    click(810, 925) # start bot
    time.sleep(5)

def start_game():
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

def check_restart_button():
    restart_button_color = pyautogui.pixel(window.left + restart_button_x, window.bottom + restart_button_y)
    if restart_button_color == (255, 255, 255):
        time.sleep(0.5) # sleep to not click the restart button too fast
        click(window.left + restart_button_x, window.bottom + restart_button_y)

def click_green_objects(x, y, width, height):
    pic = pyautogui.screenshot(region=(x, y, width, height))
    for i in range(0, width, 2): # for loops for clicking the green objects
        for j in range(0, height, 2):
            r, g, b = pic.getpixel((i, j))
            if r == 205 and g == 220:
                click(i + x, j + y)
                time.sleep(0.001) # sleep to prevent too much CPU usage
                j = height

def close_blum_window():
    click(1120, 195) # close the blum window
    time.sleep(1)

def main():
    # pyautogui.displayMousePosition()
    paused = False
    flag = 0
    offset = 0
    index = 0
    while True:
        if offset != 40*3:
            setup_blum_bot(offset)

            window_name = "TelegramDesktop"
            window = get_window(window_name)
            is_window_none(window)

            x_offset, y_offset, width_offset, height_offset, restart_button_x, restart_button_y = 9, 150, -18, -200, int(window.width / 2), -85
            x, y, width, height = window.left + x_offset, window.top + y_offset, window.width + width_offset, window.height + height_offset
            click(window.left + restart_button_x, window.bottom + restart_button_y)
            time.sleep(1)

            start_game()

            # start the autoclicker
            offset += 40
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
                    x, y, width, height = window.left+x_offset, window.top+y_offset, window.width+width_offset, window.height+height_offset

                    try:
                        check_restart_button()

                        click_green_objects(x, y, width, height)
                        
                        current_mouse_position = pyautogui.position()
                        if current_mouse_position != prev_mouse_pos:
                            prev_mouse_pos = current_mouse_position
                            last_move_time = time.time()
                        if time.time() - last_move_time > 3: # if the mouse is not moving for 3 seconds
                            flag = 1 # exit the inner while loop to change the user
                    except:
                        is_window_none(window)
            
            flag = 0
            close_blum_window()
        else:
            if index == 0:
                index += 3
                offset = 0
                click(1919, 1079) # go to desktop
                time.sleep(1)
                double_click(875, 735) # open the second telegram
                time.sleep(5)
            else:
                print(colored("[INFO]", "white", attrs=['bold']), end="")
                print(colored(" - All users have been farmed. Press ENTER to exit...", "white"))
                input()
                exit(1)

if __name__ == "__main__":
    initialize()
    main()