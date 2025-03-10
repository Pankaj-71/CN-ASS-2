import socket
import time

# Client settings
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
FILE_PATH = r"testfile"
SEND_RATE = 40  # bytes per second
ENABLE_NAGLE = True  # Set True/False based on configuration
ENABLE_QUICKACK = True  # Set True/False based on configuration

# Setup socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Set Nagle’s Algorithm
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, ENABLE_NAGLE)

# Read file and send data
with open(FILE_PATH, 'rb') as file:
    while chunk := file.read(SEND_RATE):
        client_socket.sendall(chunk)

        # Enable/disable Delayed ACK
        if ENABLE_QUICKACK:
            client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1)

        time.sleep(1)  # Maintain 40 bytes/sec rate

client_socket.close()
print("File transmission complete.")

