import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'adapter'))

import json
def test(logger):
    """tests the CentOSVZAdapter code by creating and deploying a lab"""
    
    adapters_conf = json.load(open("../src/adapters/config.json"))
    adapters_conf["ADAPTER_NAME"] = "CentOSVZAdapter"
    json.dump(adapters_conf, open("../src/adapters/config.json", "w"))

    import AdapterServer
    import ControllerServer

    logger.info("starting test")
    return True

