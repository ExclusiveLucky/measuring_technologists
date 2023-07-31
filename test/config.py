import dask.dataframe.core
import os
from ..config import HEAD, DASK, RE, DIR, FILE, BASE, BAD, GOOD

TEST_DIR = os.getcwd()
TEST_NAME = "test"
TEST_PY = TEST_NAME + ".py"
TEST_PARQ = TEST_NAME + ".parquet"
TEST_TXT = TEST_NAME + ".txt"


ANS_NAME = "test_ansver"
ANS_PARQ = ANS_NAME + ".parquet"
ANS_TXT = ANS_NAME + ".txt"

DATA = {HEAD:DASK,
            RE: {DIR: TEST_DIR,
                FILE: TEST_PY,
                BASE: TEST_PARQ}}

PROCESS =  [[],
            ["1", "2", "3"], 
            ["1", "2", "3", "4", "5"]]


RES_TYPE = [[(BAD,"Bad discription")],
            [(GOOD,"Good discription")]]

RESULTS =  [["abrakadabra"],
            [123], 
            [123.123], 
            [[1,2,3]], 
            [1,2,3], 
            ["q","W"], 
            [{"Q":1}], 
            [(1,2,3,4,)], 
            [Exception], 
            [False], 
            [None], 
            []]

P_R_DATA = [[(TEST_PARQ,dask.dataframe.core.DataFrame)],
            [(TEST_TXT,Exception)],
            [(TEST_PY,Exception)],
            [("abrakadabra",Exception)],
            [(123,Exception)],
            [(123.123,Exception)],
            [([1,2,3],Exception)],
            [({"Q":1},Exception)],
            [(False,Exception)],
            [(None,Exception)],
            [(Exception,Exception)]]

B_CFG = [[("abrakadabra", Exception)],
         [(1, Exception)],
         [([1,2,3], Exception)]]

N_CFG = [[({'a':[1,2,3,4,5]}, str)],
         [({'a':[1,2,3,4,5],'b':[1,2,3,4,5]}, str)],
         [({'a':[1,2,3,4,5],'b':[1,2,3,4,5],'c':[1,2,3,4,5],'d':[1,2,3,4,5]}, str)]]

N_FILE = [[(TEST_PY)],
          [(TEST_PARQ)],
          [(TEST_TXT)],
          [("abrakadabra")]]