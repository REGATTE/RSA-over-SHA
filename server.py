import socket, random, sympy, hashlib, pickle
def recieve():
    PRIME_LIMIT = int(input("Enter PRIME the upper bound (1000,1000000000) - (Higher is better): "))
    e,d,n = generate(sympy.randprime(1,PRIME_LIMIT),sympy.randprime(1,PRIME_LIMIT))
    print(f"Encryption Key: {e} \n Mod Key: {n} \n Secret Key: {d}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket stream initialised as TCP/IP")
    port = 6000
    s.bind((socket.gethostname(), port))
    s.listen(1)
    print(f"Server initialised and listening to Port:{port}")
    while True:
        clientsocket, address = s.accept()
        print(f"Connection to {address} established!")

        clientsocket.send(bytes(str(e),"utf-8"))
        clientsocket.send(bytes(str(n),"utf-8"))
        data_string = clientsocket.recv(4096)
        hex_encoded = clientsocket.recv(1024)
        public_hex_value = hex_encoded.decode("utf-8")
        signed_msg = pickle.loads(data_string)

        print(f"Authentication Status: True \n Recieved: {signed_msg}")
        hex_value = decrypt(signed_msg, d, n)
        print(f"Decrypted Hash Value: {hex_value}")
        if hex_value == public_hex_value: 
            print("Integrity Status : True")
            break
    clientsocket.close()
    s.close()


def decrypt(ctext,d,n):

    try:
        text = [chr(pow(int(char),d,n)) for char in ctext]
        return "".join(text)
    except TypeError as e: print(e)


def generate(p_num1,p_num2,key_size = 128):
    
    n = p_num1 * p_num2
    tot = (p_num1 - 1) * (p_num2 - 1)
    
    e = generatePublicKey(tot,key_size)
    d = generatePrivateKey(e,tot)

    return e,d,n


def generatePublicKey(tot,key_size):
   
    e = random.randint(2**(key_size-1),2**key_size - 1)
    g = gcd(e,tot)
    
    while g != 1:

        e = random.randint(2**(key_size-1),2**key_size - 1)
        g = gcd(e,tot)

    return e


def generatePrivateKey(e,tot):
    
    d = egcd(e,tot)[1]
    d = d % tot
    
    if d < 0 : d += tot
    
    return d


def egcd(a,b):
    
    if a == 0: return (b, 0, 1)
    else: g, y, x = egcd(b % a, a)
    
    return (g, x - (b // a) * y, y)


def gcd(e,tot):
     
    temp = 0
    
    while True:
        
        temp = e % tot
        
        if temp == 0: return tot
        
        e = tot
        tot = temp


def isPrime(num):
     
    if num < 2 : return False
    if num == 2 : return True
    if num & 0x01 == 0 : return False
    
    n = int(num ** 0.5 )
    
    for i in range(3,n,2):
        if num % i == 0: return False

    return True

recieve()
