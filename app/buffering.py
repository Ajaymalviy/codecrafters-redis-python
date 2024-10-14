import socket

# Server Code
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

conn, addr = server_socket.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)  # Receiving data (with buffering)
        if not data:
            break
        print("Received:", data.decode())
        conn.sendall(b'ACK: Data received')  # Sending acknowledgment

# Client Code
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Sending data in chunks
client_socket.sendall(b'Hello, World!')  # This data goes into a buffer first
ack = client_socket.recv(1024)  # Waiting for acknowledgment
print(ack.decode())

client_socket.close()

