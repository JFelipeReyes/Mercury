from pynput import keyboard
import socket
import time

HOST = '192.168.0.17'  # The server's hostname or IP address
PORT = 8080        # The port used by the serverfrom pynput import keyboard

def on_press(key):
    global msg
    if format(key.char) == 'w':
        s.sendall(b'go')
    elif format(key.char) == 's':
        s.sendall(b'back')
    elif format(key.char) == 'a':
        s.sendall(b'left')
    elif format(key.char) == 'd':
        s.sendall(b'right')
    elif format(key.char) == 'q':
        s.sendall(b'stop')
    elif format(key.char) == 'k':
        s.sendall(b'kill')
    elif format(key.char) == 'y':
        s.sendall(b'go_boost')
    elif format(key.char) == 'h':
        s.sendall(b'back_boost')
    else:
        msg=""
    time.sleep(0.5)

if __name__ == "__main__":
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
