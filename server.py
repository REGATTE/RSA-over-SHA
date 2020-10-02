import socket

def recieve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 5996))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f"Connectt from {address} established!")

        msg_rec=clientsocket.recv(1024)
        msg=msg_rec.decode("utf-8")
        print("Message recieved: " + msg)

recieve()