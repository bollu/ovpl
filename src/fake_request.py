#!/usr/bin/env python
import requests


 
adapter_url = "http://10.2.59.57:8000/api/1.0/vm/create"

payload = {'lab_spec': '{"lab_id": "cse02", "revision_tag": null, "template": "1.0", "lab": {"build_requirements": {"platform": {"os": "ubuntu", "service_pack": "", "build_steps": {"status": [], "pre_build": [], "post_build": [], "build": ["make -C ../src"], "configure": []}, "installer": [], "osVersion": "12", "arch": "i386"}}, "runtime_requirements": {"platform": {"servicepack": "", "arch": "i386", "lab_actions": {"restore": [], "pause": [], "stats": [], "shutdown": ["service apache2 stop"], "resume": [], "stop": [], "publish": [], "start": ["service apache2 start"], "init": ["mv /var/www/index.html index.html.default", "cp -r ../build/* /var/www/"], "clean": [], "backup": []}, "storage": {"min_required": "10gb"}, "hosting": "dedicated", "memory": {"min_required": "256mb", "max_required": "2gb"}, "installer": ["sudo apt-get update", "sudo apt-get install -y php5 apache2"], "osVersion": "12", "os": "ubuntu"}, "hosting": "dedicated"}, "description": {"discipline": ["Computer Science & Engineering"], "status": "Released", "name": "Computer Programming", "type": "", "server-side": true, "integration_level": 5, "id": "cse02", "developer": [{"web": "", "name": "Jawahar C.V", "title": "", "institute": "IIIT Hyderabad", "contact": {"alternate_email": "", "email": "jawahar@iiit.ac.in", "office_number": "", "mobile_number": ""}, "role": "Lab Developer", "department": "", "organization": ""}, {"web": "", "name": "Phani Phani", "title": "", "institute": "IIIT Hyderabad", "contact": {"alternate_email": "", "email": "phani@iiit.ac.in", "office_number": "", "mobile_number": ""}, "role": "Lab RA", "department": "", "organization": ""}, {"web": "", "name": "Kumar Srijan", "title": "", "institute": "IIIT Hyderabad", "contact": {"alternate_email": "", "email": "kumarsrijan@students.iiit.ac.in", "office_number": "", "mobile_number": ""}, "role": "Lab RA", "department": "", "organization": ""}, {"web": "", "name": "Jay Panda", "title": "", "institute": "IIIT Hyderabad", "contact": {"alternate_email": "", "email": "jayaguru.pandaug08@students.iiit.ac.in", "office_number": "", "mobile_number": ""}, "role": "Lab RA", "department": "", "organization": ""}, {"web": "", "name": "Shashank Sharma", "title": "", "institute": "IIIT Hyderabad", "contact": {"alternate_email": "", "email": "shashank.sharmaug08@students.iiit.ac.in", "office_number": "", "mobile_number": ""}, "role": "Lab RA", "department": "", "organization": ""}]}}, "lab_src_url": "git@bitbucket.org:virtuallabs/cse02-programming.git"}'}

print requests.get(adapter_url)
print requests.post(adapter_url, data=payload)
