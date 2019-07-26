"""Used to get key presses in the range {W, A, S, D, J, K}.
win32api: gets currently pressed keys.
"""
import win32api as wapi

KEYLIST = ["\b"]
for char in "WASDJK":
    KEYLIST.append(char)


def key_check():
    """Gets currently pressed keys.

    Returns:
        Array of currently pressed keys (String[])
    """
    keys = []
    for key in KEYLIST:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

if __name__ == "__main__":
    while True:
        print(key_check())
