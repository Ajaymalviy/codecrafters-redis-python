import socket
import logging
from contextlib import contextmanager
from dataclasses import dataclass
from app.server import (
    Address,
    CloseServer,
    CloseClient,
    make_server,
    next_client,
    next_message,
)
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
def handle_message(message: bytes, conn: socket.socket, address: tuple[str, int]):
    msg = message.decode("utf-8")
    if msg.lower() == "*1\r\n$4\r\nping\r\n":
        conn.send(b"+PONG\r\n")
    else:
        log.error(f"Unknown message from {address}: {msg}")
def main():
    server_addr = Address("localhost", 6379)
    with make_server(server_addr) as socket_server:
        for conn, address in next_client(socket_server):
            for message in next_message(conn, address):
                handle_message(message, conn, address)  # type: ignore
                raise CloseServer("Done")
