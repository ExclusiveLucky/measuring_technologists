from decorators_fb import _analysis, _warning
from config import  STAT, ALL_STAT, DASK_PR, ALL_PR, READY, WORK


class Service():
    def __init__(self):
        self.dask_process :list = self.dask_process 
        self.all_process :list = self.all_process

    def dask_proc(self) -> str:
        return f"{DASK_PR}: {len(self.dask_process)}"
    
    def all_proc(self) -> str:
        return f"{ALL_PR}: {len(self.all_process)}"

    def status(self) -> str:
        return f"{STAT}: {READY if len(self.dask_process) == 0 else WORK}"

    def all_stat(self) -> str:
        return f"{ALL_STAT}: {self.status()} {self.dask_proc()} {self.all_proc()}"
    
    @_analysis
    @_warning
    def info(self, task: dict) -> str:
        info_dict = {DASK_PR:self.dask_proc(),
                    ALL_PR:self.all_proc(),
                    STAT:self.status(),
                    ALL_STAT:self.all_stat()}
        return info_dict[task]

if __name__ == '__main__':
    pass
