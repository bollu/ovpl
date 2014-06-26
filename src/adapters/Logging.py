import os
import os.path
import logging
from logging.handlers import TimedRotatingFileHandler
import json


def get_logger(name, file_path):
    directory = os.path.dirname(file_path)
    #if the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)   # make log level a setting
    
    #don't attach the same handler multiple times
    if logger.handlers == []:
        # Add the log message handler to the logger
        timed_rotating_handler = TimedRotatingFileHandler(
                                    file_path, when='midnight', backupCount=5)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s : [%(filename)s:%(lineno)d] : %(message)s',
            datefmt='%Y-%m-%d %I:%M:%S %p')
        timed_rotating_handler.setFormatter(formatter)
        logger.addHandler(timed_rotating_handler)

    return logger


def get_controller_logger():
    global ___GLOBAL_CONTROLLER_LOGGER__
    return ___GLOBAL_CONTROLLER_LOGGER__

def get_vmmanager_looger():
    global ___GLOBAL_VM_MANAGER_LOGGER__;
    return ___GLOBAL_VM_MANAGER_LOGGER__;

#this is fugly as hell, but we need a global :/ and the path of the config file is hardcoded
#*cringe*. However, trying to change this is probably a project of it's own because god only knows
#**where** this is supposed to be initialized. 
current_file_path = os.path.dirname(os.path.abspath(__file__))
config_spec = json.loads(open(current_file_path + "/../config/config.json").read())
controller_log_file_path = config_spec["CONTROLLER_CONFIG"]["LOG_FILENAME"]
___GLOBAL_CONTROLLER_LOGGER__ = get_logger("ovpl", log_file_path)

vmmanager_log_file_path = config_spec["VMMANAGER_CONFIG"]["LOG_FILENAME"]
___GLOBAL_VM_MANAGER_LOGGER__ = get_logger("ovpl", log_file_path)

