import win32gui
import time


def win_activate(window, titlematchmode=None):
    """
    TitleMatchMode: 0 = full title, 1 = part title
    """
    
    if titlematchmode == 0:
        match_full(window)
    elif titlematchmode == 1:
        match_soft(window)



def match_full(window):
    """
    Activate and focus a window based on full title, passed as a string.
    """

    handle = win32gui.FindWindow(0, window)
    win32gui.ShowWindow(handle, True)
    win32gui.SetForegroundWindow(handle)  #put the window in foreground


def match_soft(window):
    """
    Activate and focus a window based on part of the title, passed as a string.
    """

    processes = get_app_list()

    for i in processes:
        if window in str(i[1]):
            window = i[1]
            break

    handle = win32gui.FindWindow(0, window)
    win32gui.ShowWindow(handle, True)
    win32gui.SetForegroundWindow(handle)  #put the window in foreground



def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list():
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, mlst)
    return mlst





def win_wait_active(win_to_wait, exception=None, message=True):
    """
    Waits for the specified window to be active.
    Only works with titlematchmaking set to 0/full title.
    Can stop waiting if an exception is given, in cases where a popup window may appear.
    """

    time.sleep(0.25)
    while win_to_wait != win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        if message:
            print("win_wait_active: Waiting for window to appear. Make sure you're matching the full title.")
    
        time.sleep(0.25)
        if win_to_wait == win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            break
    
        if exception:
                print(f"Excepted error: {exception}")
                break
        
