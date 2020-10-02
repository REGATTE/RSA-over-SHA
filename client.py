"""
 ! CLIENT File
 ? Connect to socket and send message to server.
"""

# Import Python Socket Module
import socket

# Connect to server port and send message
def connect(msg):

    # Initialize socket stream
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify port
    port = 5996
    # Connect to port 
    s.connect((socket.gethostname(), port))

    # Send message via byte stream 
    s.send(bytes(str(msg),"utf-8"))
# EOF

# Run function for connection
connect("Hello World")

# End of client.py