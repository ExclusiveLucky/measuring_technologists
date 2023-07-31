from config import logging, socket, json
from decorators_fb import _analysis, _error, _warning, _critical


class TCP():
    def __init__(self):
        self.host :str = self.host
        self.port :int  = self.port
        self.server :socket = self.server 

    @staticmethod
    @_analysis
    @_warning
    def socket_request(client_socket: socket) -> dict:
        request = client_socket.recv(4096).decode()
        logging.info(f"New request: {request}")
        return json.loads(request)

    @staticmethod
    @_analysis       
    @_error
    def socket_response(client_socket: socket, data :dict) -> None:
        ansver = json.dumps(data,ensure_ascii=False)
        client_socket.send(bytes(f"{ansver}", "utf-8"))
        logging.info(f"[*] Ansver : {ansver}")

    @_analysis
    @_critical
    def socket_listen(self) -> None:
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        logging.info(f"[*] Сервер запущен  Слушаем сокет {self.host}:{self.port}")
        
if __name__ == '__main__':
    pass

