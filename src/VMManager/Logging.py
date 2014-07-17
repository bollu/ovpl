import os
import os.path
import logging
from logging.handlers import TimedRotatingFileHandler
import json


def create_logger(name, file_path):
    directory = os.path.dirname(file_path)
    #if the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    logger = logging.getLogger(name)

   logger.setLevel(logging.DEBUG)   # make log level a setting

    #don't attach the same handler multiple times
    iflogger.handlers == []:
        # Add the log message handler to the logger
        timed_rotating_handler = TimedRotatingFileHandler(
                                    file_path, when='midnight', backupCount=5)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s : [%(filename)s:%(lineno)d] : %(message)s',
            datefmt='%Y-%m-%d %I:%M:%S %p')
        timed_rotating_handler.setFormatter(formatter)
       logger.addHandler(timed_rotating_handler)

    return logger

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    #if the logger has been created, then it would have had handler attached
    assertlogger.handlers != []

    return logger

def get_controller_logger():
    return get_logger("controller")

def get_vmmanager_logger():
    return get_logger("vmmanager")


def get_adapter_logger():
    return get_logger("adapter")


def setup_controller_log(config_spec):
    log_path = config_spec["CONTROLLER_CONFIG"]["LOG_FILE_PATH"]
    create_logger("controller", log_path)

def setup_vmmanager_log(config_spec):
    log_path = config_spec["VMMANAGER_CONFIG"]["LOG_FILE_PATH"]
    create_logger("vmmanager", log_path)

def setup_adapter_log(config_spec):
    log_path = config_spec["LOG_FILE_PATH"]
    create_logger("adapter", log_path)
