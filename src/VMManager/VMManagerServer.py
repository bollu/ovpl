#!/bin/python

# Services exposed by the VM Manager
# The REST url : 
# http://host-name/api/1.0/disk-usage
# http://host-name/api/1.0/running-time 
# http://host-name/api/1.0/mem-usage
# http://host-name/api/1.0/running-processes
# http://host-name/api/1.0/cpu-load
# http://host-name/api/1.0/execute/<command>

import urlparse

# bunch of tornado imports
import tornado.httpserver 
import tornado.ioloop 
import tornado.options 
import tornado.web
from tornado.options import define, options

import VMManager
import Logging

#Logger is setup in main()
Logger = None 


define("port", default=8089, help="run on the given port", type=int)


class DiskUsageHandler(tornado.web.RequestHandler):
    def get(self):
        #response = VMManager.disk_usage()
        self.write(VMManager.disk_usage())


class CPULoadHandler(tornado.web.RequestHandler):
    def get(self):    
        self.write(VMManager.cpu_load())


class RunningTimeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(VMManager.running_time())


class RunningProcHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(VMManager.running_processes())


class MemUsageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(VMManager.mem_usage())  


class ExecuteHandler(tornado.web.RequestHandler):
    def get(self, command):
        self.write(VMManager.execute(command))


class TestLabHandler(tornado.web.RequestHandler):
    def post(self):
        post_data = dict(urlparse.parse_qsl(self.request.body))
        Logger.info("VMManagerServer: TestLabHandler: post(): post_data = %s" % str(post_data))
        self.write(VMManager.test_lab(post_data['lab_src_url'], post_data.get('version', None)))

    def get(self):
        Logger.info("VMManagerServer: TestLabHandler: get()")
        self.write("Hello World")


if __name__ == "__main__":
    import os
    import json
    #load config file
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    #TODO: fix the config file (split it out that is)
    config_spec = json.loads(open(current_file_path + "/../../config/config.json").read())
 
    
    #setup logger
    Logging.setup_vmmanager_log(config_spec)
    global Logger
    Logger = Logging.get_vmmanager_logger()

    
    
    Logger.info("VMManagerServer: __main()")
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/api/1.0/disk-usage", DiskUsageHandler),
            (r"/api/1.0/mem-usage", MemUsageHandler),
            (r"/api/1.0/running-time", RunningTimeHandler),
            (r"/api/1.0/running-processes", RunningProcHandler),
            (r"/api/1.0/cpu-load", CPULoadHandler),
            (r"/api/1.0/execute/([\w*\d*\%\-]+)", ExecuteHandler),
            (r"/api/1.0/test-lab", TestLabHandler)
        ],
        debug = False)
    
   
    http_server = tornado.httpserver.HTTPServer(app) 
    http_server.listen(options.port) 
    tornado.ioloop.IOLoop.instance().start()
