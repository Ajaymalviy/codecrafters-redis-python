import socket  # noqa: F401

def main():
    print("Logs from your program will appear here!")

    # Create server socket
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    print("Server started, waiting for connections...")

    while True:
        client, addr = server_socket.accept()  # Accept a connection
        print(f"Accepted connection from {addr}")

        # Send response to the client
        client.send(b"+PONG\r\n")
        client.close()  # Close the client connection

if __name__ == "__main__":
    main()

