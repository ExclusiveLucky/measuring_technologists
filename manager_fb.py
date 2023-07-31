from config import logging, ansver, file
from decorators_fb import _analysis, _error
from config import RE, BAD, GOOD, HEAD, DASK, INFO, UNKNOWN

from service_fb import Service
from math_fb import Math

class Manager(Service,Math):
    def __init__(self):
        self.dask_process :list = self.dask_process 
        self.all_process :list = self.all_process
  
    @_analysis
    @_error
    def task_manager(self, data: dict, ip: list) -> dict:
        result = UNKNOWN
        if data[HEAD] == INFO :
            if not isinstance((result := self.info(data[RE])), Exception):
                return ansver(GOOD,result)

        elif data[HEAD] == DASK:
            self.dask_process.append(ip)
            if not isinstance((result := self.math_work(data)), Exception):
                return ansver(GOOD,file(data, result))

        else:
            logging.warning(f"[*] {UNKNOWN}: {data}")

        return ansver(BAD,str(result))


if __name__ == '__main__':
    pass