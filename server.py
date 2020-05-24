# BSD Socket
from socket import socket, AF_INET, SOCK_STREAM
import logging


class ChatServer:
    def __init__(self, host, port):
        self.logger = self._setup_logger()
        self.sock = self._setup_socket(host, port)

    def run(self):
        self.logger.info("Chat Server is now running...")

        while True:
            # This accept() can block & wait for any incoming connections
            # Retuns a Tuple containing a new socket object with the
            # Connection and address of the Client on the other end
            conn, addr = self.sock.accept()
            self.logger.debug(f"New Connection: {addr}")

    @staticmethod
    def _setup_socket(host, port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()
        return sock

    @staticmethod
    def _setup_logger(self):
        logger = logging.getLogger('chat_server')
        logger.addHandler(logging.StreamHandler())
        logger.SetLevel(logging.DEBUG)
        return logger
