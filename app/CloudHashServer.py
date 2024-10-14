import socket

class CloudHashServer:
    def __init__(self, port):
        self.storage = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', port))
        self.server_socket.listen(5)
        print(f"Listening on port {port}")

    def start(self):
        while True:
            conn, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            self.handle(conn)

    def handle(self, connection):
        request = connection.recv(1024).decode()
        response = self.process(request)
        connection.sendall(response.encode())
        connection.close()

    def process(self, request):
        parts = request.split()
        command = parts[0].upper()
        if command == 'GET':
            key = parts[1]
            return self.storage.get(key, "Key not found")
        elif command == 'SET':
            key = parts[1]
            value = parts[2]
            self.storage[key] = value
            return f"Set {key} = {value}"

# Start the server
server = CloudHashServer(4481)
server.start()

