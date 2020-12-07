# pyWinActivate

## Just like WinActivate in AutoHotkey, this module lets you easily activate and focus an opened window.


### Examples
```py
from pyWinActivate import win_activate, win_wait_active


# Activate window with partial winTitle string.
win_activate(window="Book1", titlematchmode=1)


# Activate window with exact winTitle string.
win_activate(window="Book1.xlsx - Excel", titlematchmode=0)




# Wait for the specified window to be active.
# You can pass an exception for a popup window's title. If not needed leave as None or skip entirely.
# Note: works only with a full title
win_wait_active(win_to_wait=Book1.xlsx - Excel, exception="potential popup window", message=False)

```


## Changes
### 1.1.1
#### Changed function names to follow PEP8 guidelines
#### Changed get_app_list() to not use mutable deafults
#### Added argument to win_wait_active() to turn off the message while waiting. Its True by default.
#### Changed some function argument names to be more desriptive.
