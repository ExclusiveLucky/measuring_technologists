import pandas as pd
import dask.dataframe as dd
import numpy as np
from dask.array.fft import fft

def main(ddf):
    # Инициализаруем вычисление функции Фурье на значениях временного ряда
    fft_values = fft(ddf['values'].to_dask_array(lengths=True))

    # Производим вычисления
    result = fft_values.compute()

    return result


if __name__ == '__main__':
    main()


