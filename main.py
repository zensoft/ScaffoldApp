#!/usr/bin/env python
#* * * * * $HOME/ScaffoldApp/main.py

from core.logic import *
from utils.proccess_helper import *
from settings.settings import *
from utils.custom_logger import *

custom_logger = CustomLogger()

if __name__ == "__main__":
    """
    When app is locked another instance can not start
    """
    get_lock(APP_NAME)
    custom_logger.log("Start logic")
    run_logic()
    custom_logger.log("End logic")
