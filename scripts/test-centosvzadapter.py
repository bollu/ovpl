import sys, os, plumbum, time, requests
from multiprocessing import Process
from threading import Thread

from IPy import IP

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'adapters'))

import json

def start_controller_server(logger):
    with plumbum.local.cwd("../src/"):
        logger.info("starting controller. pwd: {}".format(plumbum.local.cwd))
        plumbum.local["ls"]()
        plumbum.local["python2.7"]["ControllerServer.py"]()


def start_adapter_server(logger):
    with plumbum.local.cwd("../src/adapters"): 
        logger.info("starting adapter. pwd: {}".format(plumbum.local.cwd))
        plumbum.local["python2.7"]["AdapterServer.py"]()


def test(logger):
    """tests the CentOSVZAdapter code by creating and deploying a lab"""
    
    adapters_conf = json.load(open("../src/adapters/config.json"))
    adapters_conf["ADAPTER_NAME"] = "CentOSVZAdapter"
    json.dump(adapters_conf, open("../src/adapters/config.json", "w"))
    
    controller_server = Thread(target=start_controller_server, args=(logger, ))
    adapter_server = Thread(target=start_adapter_server, args=(logger, ))
   
    
    logger.info("starting controller and adapter servers") 
    controller_server.start()
    adapter_server.start()
   
    #sleep for a second
    logger.info("sleeping so that server can startup IOLoop") 
    time.sleep(5)
    
    payload = {"lab_id": "cse02", "lab_src_url": "https://bitbucket.org/virtuallabs/cse02-programming.git"}
    response = requests.post("http://localhost:8080/", data=payload)
 

    logger.info("response: {}".format(response))
    logger.info("response text: {}".format(response.text))
    
    logger.info("ending test")
    
    controller_server.join(3)
    adapter_server.join(3)
    #try to construct IP from return value - TODO: change conrollerserver to return 200 on success and 400 on failure so we can check
    #error codes.
    try:
        ip = IP(response.text)
        return True
    except Exception, e:
        return False

