import threading
import importlib
import logging
import socket
import pandas
import shutil
import numpy
import json
import dask
import time
import os

RE = "Request"
RES = "Response"
DIR = "Directory"
BAD = "error"
FILE = "File"
BASE = "Base"
STAT = "Status"
GOOD = "complete"
DISC = "Discription"
HEAD = "Header"
DASK = "dask"
INFO = "info"
READY = "Ready"
WORK = "Work"
DASK_PR = "Dask process"
ALL_PR = "All process"
ALL_STAT = "All statistic"
NOHEAD = "noheader"
UNKNOWN = "Unknown header."


def errore_ansver(data: any):
    return {HEAD:NOHEAD, RES:{STAT:BAD, DISC:str(data)}}

def ansver(status: str, discription: any) -> dict:
    return {STAT:status,DISC:discription}

def file(data: dict, file: any) -> dict:
    return {DIR:data[RE][DIR],FILE:file}
    
################   FOR   TEST

# {"Header":"dask","Request":{"Directory":"C:/python/DASK_WORK/server/","Base":"time_series.parquet","File":"work.py"}}
# {"Header":"info","Request":"All statistic"}



if __name__ == '__main__':
    pass