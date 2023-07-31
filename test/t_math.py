import pytest
from ..test.config import *
from ..config import *
from ..math_fb import *
from ..server_v2 import *


@pytest.fixture
def reader():
    return Reader()


@pytest.fixture
def loader():
    return Loader()


@pytest.fixture
def manager():
    return FileManager()


@pytest.fixture
def data():
    return DATA


@pytest.mark.parametrize("test_data",P_R_DATA)
def test_parq_read(reader,test_data):
    assert all([isinstance(reader.parq_read(data), result) for data, result in test_data])


@pytest.mark.parametrize("files",N_FILE)
def test_input_file(data, loader, files):
    def _data(file):
        data[RE][FILE] = file
        return data
    assert all(loader.input_file(_data(file)) == f"{data[RE][DIR]}{data[RE][BASE]}" for file in files)
    assert all(not isinstance(loader.input_file(_data(file)), Exception) for file in files)


@pytest.mark.parametrize("files",N_FILE)
def test_copy_file(manager, files):
    assert all(not isinstance(manager.copy_file(file), Exception) for file in files)


@pytest.mark.parametrize("bad",B_CFG)
@pytest.mark.parametrize("good",N_CFG)
def test_save_parquet(manager, bad, good, data):                 
    assert all(manager.save_parquet(data, result, ANS_NAME) == ANS_PARQ for result, res_type in good)
    assert all(isinstance(manager.save_parquet(data, result, ANS_NAME), res_type) for result, res_type in good)
    assert all(isinstance(manager.save_parquet(data, result, ANS_NAME), res_type) for result, res_type in bad)


@pytest.mark.parametrize("bad",B_CFG)
@pytest.mark.parametrize("good",N_CFG)
def test_save_txt(manager, bad, good, data):
    assert all(manager.save_txt(data, result, ANS_NAME) == ANS_TXT for result, res_type in good)
    assert all(isinstance(manager.save_txt(data, result, ANS_NAME), res_type) for result, res_type in good)
    assert all(manager.save_txt(data, result, ANS_NAME) == ANS_TXT for result, res_type in bad)
    assert all(isinstance(manager.save_txt(data, result, ANS_NAME), str) for result, res_type in bad)


@pytest.mark.parametrize("bad",B_CFG)
@pytest.mark.parametrize("good",N_CFG)
def test_output_file(data, bad, good, loader):
        assert all(loader.output_file(data, result) == ANS_PARQ for result, res_type in good)
        assert all(isinstance(loader.output_file(data, result), str) for result, res_type in good)
        assert all(loader.output_file(data, result) == ANS_TXT for result, res_type in bad)
        assert all(isinstance(loader.output_file(data, result), str) for result, res_type in bad)


if __name__ == '__main__':
    pass




