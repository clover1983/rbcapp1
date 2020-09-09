#!/usr/bin/env python3

import subprocess
import json
import socket
import time

timenow=time.time()
local_time=time.localtime(timenow)
now = time.strftime('%Y-%m-%d-%H-%M-%S',local_time)
host = socket.gethostname()

services = ['httpd', 'rabbitmq-server', 'postgresql']

for service in services:
    ret = subprocess.call("systemctl status %s" % service, shell=True)
    if ret != 0:
        status = {
            "service_name":"%s" % service, 
            "service_status":"DOWN", 
            "host_name":"%s" % host
        }
        with open("%s-status-%s.json" % (service, now),  'w') as outfile:
            json.dump(status, outfile, indent=4)
    else:
        status = {
            "service_name":"%s" % service, 
            "service_status":"DOWN", 
            "host_name":"%s" % host
        }
        with open("%s-status-%s.json" % (service, now),  'w') as outfile:
            json.dump(status, outfile, indent=4)
