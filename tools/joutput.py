import os
import socket
import json 
import resources as res
import datetime

output_path=os.path.abspath(os.path.join(os.path.dirname(__file__),"../output"))
timestamp = datetime.datetime.now().isoformat()
rs=res.Resources()

meminfo=rs.MemoryUsage()
hostname=rs.hostname()

def Update_dict(name):
	name.update({'hostname':hostname})
	name.update({'@timestamp':timestamp})

def json_output(file, dict, dictname ):
	Update_dict(dict)
	file_path=os.path.join(output_path, file)
	name={dictname: dict}
	with open(file_path,"w") as f:
  		return json.dump(name, f)
		

#json_output('meminfo.json', meminfo, 'memory')


