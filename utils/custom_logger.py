from settings.logging_settings import *
from utils.log_type import LogType
import sys

class CustomLogger:
    import logging

    def __init__(self):
        if LOG_TYPE == LogType.SYS:
            self.logging.basicConfig(level=LOG_LEVEL,format=LOG_FORMAT, datefmt=LOG_DATE, handlers=(logging.StreamHandler(sys.stdout),))
        else:
            self.logging.basicConfig(filename=LOG_FILE,level=LOG_LEVEL,format=LOG_FORMAT, datefmt=LOG_DATE)
        self._check_if_clear_log_file()
        pass

    def _check_if_clear_log_file(self):
        f = open(LOG_FILE, "r+")
        if len(f.readlines()) > LOG_FILE_MAX_LINE:
            f.seek(0)
            f.truncate()
        f.close()


    def log(self,msg):
        self.logging.info(msg)
