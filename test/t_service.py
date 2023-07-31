import pytest
from ..config import *
from ..server_v2 import *
from ..test.config import *


@pytest.fixture
def service():
    return Server("0.0.0.0",27700)


@pytest.mark.parametrize("process",PROCESS)
@pytest.mark.parametrize("comands",RESULTS)
def test_info(service,process,comands):
    for all_point in process:
        service.all_process = all_point

        for dask_point in process:
            service.dask_process = dask_point

            assert all(isinstance(service.info(comand), Exception) for comand in comands)
            assert service.info(STAT) == f"{STAT}: {READY if len(service.dask_process) == 0 else WORK}"
            assert service.info(DASK_PR) == f"{DASK_PR}: {len(service.dask_process)}"
            assert service.info(ALL_PR) == f"{ALL_PR}: {len(service.all_process)}"
            assert service.info(ALL_STAT) == f"{ALL_STAT}: {STAT}: {READY if len(service.dask_process) == 0 else WORK} {DASK_PR}: {len(service.dask_process)} {ALL_PR}: {len(service.all_process)}"


if __name__ == '__main__':
    pass