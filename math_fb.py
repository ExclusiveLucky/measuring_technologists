import tasks.work as work
from config import shutil, os, pandas, dask, importlib, numpy, time
from decorators_fb import _analysis, _error, _warning, _critical
from config import  RE, DIR, FILE, BASE



class FileManager():
    def __init__(self):
        pass

    @staticmethod
    def file_name(data: dict) -> str:
        return data[RE][FILE].split(".py")[0]

    @staticmethod
    @_analysis
    @_error
    def copy_file(file: str) -> None:
        current_dir = f"{os.getcwd()}\\tasks"
        shutil.copyfile(file, f'{current_dir}\\work.py')
        shutil.copyfile(file, f'{current_dir}\\test_{time.strftime("%d_%m_%Y__%H_%M_%S")}.py')

    @staticmethod
    @_warning
    def save_parquet(data, result: any, handler: str) -> str:
        fourier_df = pandas.DataFrame(result)
        name = handler + ".parquet"
        fourier_df.to_parquet(f'{data[RE][DIR]}{name}')
        return name

    @staticmethod
    @_error
    def save_txt(data: dict, result: any, handler: str) -> str:
        name = handler + ".txt"
        with open(f'{data[RE][DIR]}{name}', "w") as file:
            file.write(str(result))
        return name


class Loader(FileManager):
    def __init__(self):
        pass

    @_analysis
    @_error
    def input_file(self, data: dict) -> None:
        file = data[RE][DIR] + data[RE][FILE]
        self.copy_file(file)
        return data[RE][DIR] + data[RE][BASE]
    
    @_analysis
    def output_file(self, data: dict, result: any) -> any:
        handler = self.file_name(data) + "_ansver"
        if isinstance((file:=self.save_parquet(data, result, handler)), Exception):
            return self.save_txt(data, result, handler)
        return file

    
class Reader():
    def __init__(self):
        pass

    @staticmethod
    @_analysis
    @_critical
    def parq_read(file: str) -> any:
        return dask.dataframe.read_parquet(file)


class MyDask():
    def __init__(self):
        pass
    
    @staticmethod
    @_analysis
    @_critical
    def dask_work(parquet_data: any) -> any:
        importlib.reload(work)
        ansver = work.main(parquet_data)
        return ansver
    

class Math(Loader,Reader,MyDask):
    def __init__(self):
        pass
    
    @_analysis
    @_error
    def math_work(self, data: dict) -> any: 
        if not isinstance((result := self.input_file(data)), Exception):
            if not isinstance((result := self.parq_read(result)), Exception):
                if not isinstance((result := self.dask_work(result)), Exception):
                    return self.output_file(data, result)
        return result


if __name__ == '__main__':
    pass
