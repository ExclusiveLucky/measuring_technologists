from config import logging, socket
from decorators_fb import _analysis, _critical
from config import RES, HEAD, STAT, DISC, BAD, NOHEAD
from config import errore_ansver

from manager_fb import Manager
from tcp_fb import TCP

class Handler(Manager,TCP):
    def __init__(self):
        self.dask_process :list = self.dask_process 
        self.all_process :list = self.all_process
        self.host :str = self.host
        self.port :int  = self.port

    def append_process(self, ip: str) -> None:
        self.all_process.append(ip)

    def clear_process(self, ip: str) -> None:
        for ip_list in [self.all_process,self.dask_process]:
            if ip in ip_list: 
                ip_list.remove(ip)

    @_analysis
    @_critical
    def handle_client(self, client_socket: socket, ip: str) -> None:
        self.append_process(ip)
        logging.info(f"[*] Connect from : {ip}")

        if isinstance((data := self.socket_request(client_socket)), Exception):
            data = errore_ansver(data)
        elif isinstance((response := self.task_manager(data, ip)), Exception):
            data[RES] = str(response)
        else:
            data[RES] = response

        self.socket_response(client_socket, data)
        client_socket.close()

        logging.info(f"[*] Connect close : {ip}")
        self.clear_process(ip)

if __name__ == '__main__':
    pass