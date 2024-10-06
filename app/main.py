import socket

def main():
    print("Logs from your program will appear here!")

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 6379))
    server_socket.listen()

    print("Server started, waiting for connections...")

    while True:
        client, addr = server_socket.accept()  # Accept a connection
        print(f"Accepted connection from {addr}")

        while True:
            data = client.recv(1024)  # Receive data from the client
            if not data:
                break  # No data means the client has closed the connection

            # Check if the received command is PING
            if data.strip() == b'PING':
                client.send(b"+PONG\r\n")  # Send the response

        client.close()  # Close the client connection after finishing

if __name__ == "__main__":
    main()
