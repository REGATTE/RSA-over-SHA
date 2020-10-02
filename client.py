"""
 ! CLIENT File
 ? Connect to socket and send message to server.
"""

# Import Python Socket Module
import socket
# Import Hash Library
import hashlib

# Recieve message from user
print("Enter message to send: \n")
# Assign to @param msg
msg = input()

# Connect to server port and send message
def connect(msg):

    # Initialize socket stream
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify port
    port = 6000
    # Connect to port 
    s.connect((socket.gethostname(), port))

    # Encrypt message
    enc_msg = encrypt(msg)

    # Send message via byte stream 
    s.send(bytes(str(enc_msg),"utf-8"))

# EOF

# Returns encrypted message
def encrypt(msg):

    # Hash message using SHA-1
    hash_obj = hashlib.sha1(bytes(msg, encoding='utf-8'))

    # Convert Hash object to hex
    hex_value = hash_obj.hexdigest()
    
    # Convert to Unsigned int
    unsigned_int_msg = int(hex_value, 16)
    
    # Confirm hashing completed
    print(f"Hashed message to {unsigned_int_msg}")

    # Return encrypted message
    return unsigned_int_msg

# EOF

# Run function for connection
connect(msg)

# End of client.py