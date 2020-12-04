# pyWinActivate

## Just like WinActivate in AutoHotkey, this module lets you easily activate and focus an opened window.


### Examples
```py
from winActivate import winActivate


# Activate window with partial winTitle string.
winActivate(window="Book1", titlematchmode=1)


# Activate window with exact winTitle string.
winActivate(window="Book1.xlsx - Excel", titlematchmode=0)




# Wait for the specified window to be active.
# You can pass an exception for a popup window. If not needed leave as None or skip entirely.
winWait(windowW=Book1.xlsx - Excel, exception="potential popup window")

```
