import socket, pickle, hashlib

print("Enter message to send: ")

msg = input()
def connect(msg):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    port = 6000

    s.connect((socket.gethostname(), port))
    e = s.recv(1024)
    e = e.decode("utf-8")

    print(f"Key recieved {e}")


    n = s.recv(1024)
    n = n.decode("utf-8")
    enc_msg, hex_value = encrypt(msg, e, n)
    data_string = pickle.dumps(enc_msg)
    s.send(data_string)

    s.send(bytes(str(hex_value), "utf-8"))

    s.close()

def encrypt(msg, e, n):

    hash_obj = hashlib.sha1(bytes(msg, encoding='utf-8'))
    hex_value = hash_obj.hexdigest()
    print(f"Hashed message to {hex_value}")

    signed_msg = rsa(str(hex_value), int(e), int(n))
    print(f"Signed message to {signed_msg}")

    return signed_msg, hex_value

def rsa(text, e, n):
    ctext = [pow(ord(char),e,n) for char in text]
    return ctext

  connect(msg)
