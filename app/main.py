import socket
import logging
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Generator, Tuple

# Set up logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# Define Address data class
@dataclass
class Address:
    host: str
    port: int

# Custom exceptions for server control
class CloseServer(Exception):
    pass

class CloseClient(Exception):
    pass

# Function to create a server
@contextmanager
def make_server(address: Address) -> Generator[socket.socket, None, None]:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address.host, address.port))
    server_socket.listen()
    log.info(f"Server started on {address.host}:{address.port}")
    try:
        yield server_socket
    finally:
        server_socket.close()
        log.info("Server closed.")

# Function to accept the next client connection
def next_client(server_socket: socket.socket) -> Generator[Tuple[socket.socket, Tuple[str, int]], None]:
    while True:
        conn, addr = server_socket.accept()
        log.info(f"Client connected: {addr}")
        yield conn, addr

# Function to read the next message from the client
def next_message(conn: socket.socket, address: Tuple[str, int]) -> Generator[bytes, None, None]:
    while True:
        data = conn.recv(1024)
        if not data:
            log.info(f"Client disconnected: {address}")
            raise CloseClient("Client disconnected")
        yield data

# Handle incoming messages
def handle_message(message: bytes, conn: socket.socket, address: Tuple[str, int]):
    msg = message.decode("utf-8").strip()  # Trim whitespace/newlines
    log.debug(f"Received message from {address}: {msg}")
    
    if msg.lower() == "*1\r\n$4\r\nping\r\n":
        conn.send(b"+PONG\r\n")
    else:
        log.error(f"Unknown message from {address}: {msg}")

# Main server loop
def main():
    server_addr = Address("localhost", 6379)
    with make_server(server_addr) as socket_server:
        for conn, address in next_client(socket_server):
            try:
                while True:  # Continue to listen for messages
                    for message in next_message(conn, address):
                        handle_message(message, conn, address)
            except CloseClient:
                log.info(f"Connection closed for {address}")
            except CloseServer:
                log.info("Server closing.")
                break

if __name__ == "__main__":
    main()
