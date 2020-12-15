import win32gui
import time

# v1.2.1
def win_activate(window_title, partial_match=False):
    """
    Activate and focus a window based on title, passed as a string.
    """

    if partial_match:
        for proc in get_app_list():
            if window_title in proc[1]:
                window_title = proc[1]
                break
        else:
            raise Exception('Could not find window matching title')

    handle = win32gui.FindWindow(0, window_title)
    win32gui.ShowWindow(handle, True)
    win32gui.SetForegroundWindow(handle)


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
    Can stop waiting if an exception is given, in cases where a popup window may appear.
    """

    time.sleep(0.25)
    while win_to_wait not in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        if message:
            print("win_wait_active: Waiting for window to appear. Make sure you're matching the full title.")
    
        time.sleep(0.25)
        if win_to_wait in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            break
    
        if exception:
                print(f"Excepted error: {exception}")
                break
        
