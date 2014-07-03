import sys, os, plumbum, time
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
    
    controller_server = None
    with plumbum.local.cwd("../src"):
        controller_server = Process(target=start_controller_server)
        controller_server.start()
    
    adapter_server = None
    with plumbum.local.cwd("../src/adapters"):
        adapter_server = Process(target=start_adapter_server)
        adapter_server.start()
   
    #sleep for a second
    time.sleep(1)
    logger.info("starting test")
    
    logger.info("ending test")
    controller_server.join()
    adapter_server.join()

    return True

