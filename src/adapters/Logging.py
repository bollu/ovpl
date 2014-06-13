import os
import logging
from logging.handlers import TimedRotatingFileHandler


def get_logger(log_filename):
    LOGGER = logging.getLogger('AdapterServer')
    LOGGER.setLevel(logging.DEBUG)   # make log level a setting
   
    current_dir = current_file_path = os.path.dirname(os.path.abspath(__file__))
    log_folder = current_dir + "/log/"
    log_path = log_folder  + log_filename      
   
    
    #create the log folder if it doesn't exist	
    if not os.path.isdir(log_folder):
    	os.mkdir(log_folder)

    #setup the rotating file handler    
    myhandler = TimedRotatingFileHandler(
                                log_path, when='midnight', backupCount=5)
 

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s : [%(filename)s:%(lineno)d] : %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %p')
    myhandler.setFormatter(formatter)
    LOGGER.addHandler(myhandler)

    return LOGGER
