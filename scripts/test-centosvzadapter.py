import sys, os, plumbum
from multiprocessing import Process


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'adapters'))

import json

def start_controller_server():
    plumbum.local["python"]["ControllerServer.py"]()


def start_adapter_server():
    plumbum.local["python"]["AdapterServer.py"]()


def test(logger):
    """tests the CentOSVZAdapter code by creating and deploying a lab"""
    
    adapters_conf = json.load(open("../src/adapters/config.json"))
    adapters_conf["ADAPTER_NAME"] = "CentOSVZAdapter"
    json.dump(adapters_conf, open("../src/adapters/config.json", "w"))
    
    with plumbum.local.cwd("../src"):
        p = Process(target=start_controller_server)
        p.start()
    
    with plumbum.local.cwd("../src/adapters"):
        p = Process(target=start_adapter_server)
        p.start()
   
    #sleep for a second
    sleep(1)
    logger.info("starting test")
    return True

