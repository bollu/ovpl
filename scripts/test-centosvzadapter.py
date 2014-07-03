import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import json
def test(logger):
    """tests the CentOSVZAdapter code by creating and deploying a lab"""
    
    adapters_conf = json.loads("../src/adapters/config.json")
    adapters_conf[""] = "CentOSVZAdapter"
    json.dumps(adapters_conf)

    import AdapterServer
    import ControllerServer


    logger.info("starting test")

