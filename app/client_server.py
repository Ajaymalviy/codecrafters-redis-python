import socket

def test_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 6379))
    
    for _ in range(2):  # Send multiple PING commands
        client_socket.send(b'PING\r\n')
        response = client_socket.recv(1024)
        print(response.decode())

    client_socket.close()

if __name__ == "__main__":
    test_client()

