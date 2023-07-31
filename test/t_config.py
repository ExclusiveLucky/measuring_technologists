import pytest
from ..config import *
from ..test.config import *


@pytest.mark.parametrize("data",RES_TYPE)
def test_ansver(data):
    assert all([isinstance(ansver(status,discription), dict) for status, discription in data])
    assert all([ansver(status,discription) == {STAT:status,DISC:discription} for status, discription in data])


@pytest.mark.parametrize("result",RESULTS)
def test_errore_ansver(result):
    assert all([isinstance(errore_ansver(data), dict) for data in result])
    assert all([errore_ansver(data) == {HEAD:NOHEAD, RES:{STAT:BAD, DISC:str(data)}}  for data in result])


if __name__ == '__main__':
    pass