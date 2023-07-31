from config import socket, threading, logging
from handler_fb import Handler

logging.basicConfig(level=logging.DEBUG, filename="server_log.log",filemode="w",encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(filename)s %(lineno)d %(message)s")

class Server(Handler):
    def __init__(self, host: str, port: int):
        self.server :socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.all_process :list = [(host,port)]
        self.dask_process :list = []
        self.host :str = host
        self.port :int = port

    
    def start(self) -> None:
        if not isinstance(self.socket_listen(), Exception):
            while True:
                threading.Thread(target = self.handle_client, args=(*self.server.accept(),)).start()


if __name__ == '__main__':
    Server("0.0.0.0",27700).start()