import win32gui


def winActivate(window, titlematchmode=None):
    """
    TitleMatchMode: 0 = full title, 1 = part title
    """
    window = window

    if titlematchmode == 0:
        matchFull(window=window)
    elif titlematchmode == 1:
        matchSoft(windowM=window)



def matchFull(window):
    """
    Activate and focus a window based on full title, passed as a string.
    """
    win = window
    handle = win32gui.FindWindow(0, win)
    win32gui.ShowWindow(handle, True)
    win32gui.SetForegroundWindow(handle)  #put the window in foreground


def matchSoft(windowM):
    """
    Activate and focus a window based on part of the title, passed as a string.
    """
    win = windowM
    processes = get_app_list()

    for i in processes:
        if win in str(i[1]):
            win = i[1]
            break


    handle = win32gui.FindWindow(0, win)
    win32gui.ShowWindow(handle, True)
    win32gui.SetForegroundWindow(handle)  #put the window in foreground



def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst