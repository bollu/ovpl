import os
import os.path
import logging
from logging.handlers import TimedRotatingFileHandler, HTTPHandler
import json


def create_logger(name, file_path, logging_hostname, logging_port, logging_endpoint):
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


        #HACK: DEBUG CODE. DO DELETE BEFORE CHECKIN
        print logging_hostname + ":" + logging_port + " api: " + logging_endpoint
        #create an HTTP handler to connect to our logging endpoint.
        #http_handler = HTTPHandler(host=(logging_hostname + ":" + logging_port), url=logging_endpoint, method="POST")
        http_handler = HTTPHandler(host="127.0.0.1:8239", url="/log/", method="POST")
        logger.addHandler(http_handler)



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


def __load_logging_hostname(config_spec):
    return config_spec["LOGGING_CONFIGURATION"]["SERVER_HOSTNAME"]

def __load_logging_port(config_spec):
    return config_spec["LOGGING_CONFIGURATION"]["SERVER_PORT"]


def __load_logging_endpoint(config_spec):
    return config_spec["API_ENDPOINTS"]["LOGGING_URI_ENDPOINT"]




def setup_controller_log(config_spec):
    log_path = config_spec["CONTROLLER_CONFIG"]["LOG_FILE_PATH"]


    log_hostname = __load_logging_hostname(config_spec)
    log_port = __load_logging_port(config_spec)
    log_endpoint = __load_logging_endpoint(config_spec)
    create_logger("controller", log_path, log_hostname, log_port, log_endpoint)

def setup_vmmanager_log(config_spec):
    log_path = config_spec["VMMANAGER_CONFIG"]["LOG_FILE_PATH"]

    log_hostname = __load_logging_hostname(config_spec)
    log_port = __load_logging_port(config_spec)
    log_endpoint = __load_logging_endpoint(config_spec)

    create_logger("vmmanager", log_path, log_hostname, log_port, log_endpoint)

def setup_adapter_log(config_spec):
    log_path = config_spec["LOG_FILE_PATH"]

    log_hostname = __load_logging_hostname(config_spec)
    log_port = __load_logging_port(config_spec)
    log_endpoint = __load_logging_endpoint(config_spec)
    create_logger("adapter", log_path, log_hostname, log_port, log_endpoint)
