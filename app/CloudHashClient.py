import socket

class CloudHashClient:
    host = 'localhost'
    port = 4481

    @staticmethod
    def get(key):
        return CloudHashClient.request(f"GET {key}")

    @staticmethod
    def set(key, value):
        return CloudHashClient.request(f"SET {key} {value}")

    @staticmethod
    def request(command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((CloudHashClient.host, CloudHashClient.port))
            client_socket.sendall(command.encode())
            response = client_socket.recv(1024).decode()
        return response

# Example usage
print(CloudHashClient.set('prez', 'obama'))
print(CloudHashClient.get('prez'))
print(CloudHashClient.get('vp'))

