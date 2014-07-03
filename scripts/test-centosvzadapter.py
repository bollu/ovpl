import sys, os, plumbum, time, requests
from multiprocessing import Process


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
    
    controller_server = Process(target=start_controller_server, args=(logger, ))
    adapter_server = Process(target=start_adapter_server, args=(logger, ))
   
    
    logger.info("starting test") 
    controller_server.start()
    adapter_server.start()
   
    #sleep for a second
    logger.info("sleeping") 
    time.sleep(60)
    
    logger.info("CURLing")
    logger.info("curl: {}".format(plumbum.local["curl"]["127.0.0.1:8000"]()))

    payload = {"lab_id": "cse02", "lab_url": "https://bitbucket.org/virtuallabs/cse02-programming.git"}
    response = requests.post("http://localhost:8000/", data=payload)
 

    logger.info("response: {}".format(response))
    logger.info("response text: {}".format(response.text))

    logger.info("ending test")
    
    controller_server.join(3)
    adapter_server.join(3)

    return True

