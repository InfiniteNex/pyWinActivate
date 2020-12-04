# pyWinActivate

## Just like WinActivate in AutoHotkey, this module lets you easily activate and focus an opened window.


### Examples
```py
from winActivate import winActivate as winAct


# Activate window with partial winTitle string.
winAct(window="Book1", titlematchmode=1)


# Activate window with exact winTitle string.
winAct(window="Book1.xlsx - Excel", titlematchmode=0)

```


###Todo:
* error handling
* winWait function
