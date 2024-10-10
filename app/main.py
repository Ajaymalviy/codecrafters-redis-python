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

        try:
            while True:
                data = client.recv(1024)  # Receive data from the client
                if not data:
                    print(f"Connection closed by {addr}")
                    break  # No data means the client has closed the connection

                # Split the received data into commands
                commands = data.split(b'\r\n')
                for command in commands:
                    if command == b'*1':
                        continue  # Skip the command count

                    if command.startswith(b'$'):
                        command_length = int(command[1:].decode())
                        if command_length > 0:
                            # Read the actual command
                            command_data = client.recv(command_length + 2)  # +2 for \r\n
                            if command_data == b'PING\r\n':
                                client.send(b"+PONG\r\n")  # Send the response
                            else:
                                client.send(b"-ERR Unknown command\r\n")
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client.close()  # Close the client connection after finishing

if __name__ == "__main__":
    main()
