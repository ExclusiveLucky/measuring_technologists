from config import logging, time

def _base(func: any, *args, **kwargs) -> dict:
    try:
        logging.debug(f"Function {func.__name__} start.")
        result = func(*args, **kwargs)
        logging.debug(f"Function {func.__name__} complete.")
        return result
    except Exception as e:
        return e

def _warning(func: any, *args, **kwargs) -> any:
    def wrapper(*args, **kwargs) -> any:
        if isinstance((result := _base(func, *args, **kwargs)), Exception):
            logging.warning(f"Warning in function {func.__name__}: {result}")
        return result
    return wrapper

def _error(func: any, *args, **kwargs) -> any:
    def wrapper(*args, **kwargs) -> any:
        if isinstance((result := _base(func, *args, **kwargs)), Exception):
            logging.error(f"Error in function {func.__name__}: {result}", exc_info=True)
        return result
    return wrapper

def _critical(func: any, *args, **kwargs) -> any:
    def wrapper(*args, **kwargs) -> any:
        if isinstance((result := _base(func, *args, **kwargs)), Exception):
            logging.critical(f"Critical exception in function {func.__name__}: {result}", exc_info=True)
        return result
    return wrapper

def _analysis(func: any, *args, **kwargs) -> any:
    def wrapper(*args, **kwargs) -> any:
        start_time = time.time()
        result = func(*args, **kwargs)
        func_work_time = time.time() - start_time
        logging.debug(f"Function complete at {func_work_time} sec")
        return result
    return wrapper