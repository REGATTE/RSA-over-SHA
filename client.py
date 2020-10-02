import socket

def connect(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 5996))
    s.send(bytes(str(msg),"utf-8"))

connect("Hello World")