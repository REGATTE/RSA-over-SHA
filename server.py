"""
 ! SERVER File
 ? Bind to socket and listen for client message.
"""

# Import python socket module
import socket

# Connect and recieve message
def recieve():

    # Initialize socket stream
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify port
    port = 6000

    # Bind to port 
    s.bind((socket.gethostname(), port))

    # Listen every 5 ticks
    s.listen(5)

    # Server init message
    print(f"Server initialised and listening to Port:{port}")

    # Listen for client message
    while True:
 
        # Recieved OS assigned socket and address
        clientsocket, address = s.accept()

        # Print Connection details
        print(f"Connection to {address} established!")

        # Recieve message length 1024
        msg_rec=clientsocket.recv(1024)

        # Decoder format
        msg=msg_rec.decode("utf-8")

        # Print out message
        print("Message recieved: " + msg)  
   
    #End of while loop
    
# EOF


# Run function for connection
recieve()

# End of server.py