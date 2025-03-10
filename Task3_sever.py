import socket
import time

# Server settings
HOST = '0.0.0.0'
PORT = 12345
BUFFER_SIZE = 1024  # Adjust for max packet size
ENABLE_NAGLE = True  # Set True/False based on configuration
ENABLE_QUICKACK = True  # Set True/False based on configuration

# Setup socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server is listening...")
conn, addr = server_socket.accept()
print(f"Connection from {addr}")

# Set Nagle’s Algorithm
conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, ENABLE_NAGLE)

# Receive file
start_time = time.time()
total_bytes_received = 0

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    total_bytes_received += len(data)

    # Enable/disable Delayed ACK
    if ENABLE_QUICKACK:
        conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1) 


end_time = time.time()
conn.close()
server_socket.close()

# Calculate performance metrics
duration = end_time - start_time
throughput = total_bytes_received / duration
goodput = total_bytes_received / duration  # (assuming no retransmissions)
packet_loss_rate = 0  # (can be measured using packet capture tools)
max_packet_size = BUFFER_SIZE

# Print results
print(f"Throughput: {throughput} bytes/sec")
print(f"Goodput: {goodput} bytes/sec")
print(f"Packet Loss Rate: {packet_loss_rate}")
print(f"Max Packet Size Achieved: {max_packet_size} bytes")
