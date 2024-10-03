import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    print(server_socket)
    server_socket.accept() # wait for client
    # client, addr = server_socket.accept()
    print(server_socket.accept)
    
    client.send(b"+PONG\r\n")
    # for conn, address in next_client(socket_server):
    #     for message in next_message(conn, address):
    #         handle_message(message, conn, address)  # type: ignore
    #         raise CloseServer("Done")

if __name__ == "__main__":
    main()
