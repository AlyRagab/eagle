import os
import json
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
jsonfiles=os.path.abspath(os.path.join(os.path.dirname(__file__),"../output/"))

def Elastic():
	for filename in os.listdir(jsonfiles):
		filename=os.path.join(jsonfiles, filename)
		with open(filename) as f:
    			logs = f.read()
			return es.index(index='eagle-es', doc_type='log' ,body=json.loads(logs))
		
