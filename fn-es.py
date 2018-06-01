from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
import random
import json

if es.indices.exists(index="mono") == False: 
    print ("Index creteing")
    createIndex = es.indices.create(index="mono", ignore=400)
else: 
    print ("Index exist")

with open('fn-log.json','r')  as f: 
    data = json.load(f)


payload = { }

# if 'monolith' in log.keys():
#   payload['monolithaa']= log['monolith']['session_vars']



# if 'queue_process' in data.keys() and type(data['queue_process']['message']['providers_ids']) == dict: 
#   payload['queue_process']['message']['providers_ids'] = data['queue_process']['message']['providers_ids'].values()


for k, v in data.items():
  payload[k] = v
  
if 'queue_process' in data.keys() and type(data['queue_process']['message']['providers_ids']) == dict:
    payload['queue_process']['message']['providers_idss'] = '100000000000000000000000000000000000000000000000'
  # p_ids = []
  # for k, v in data['queue_process']['message']['providers_ids'].items():
  #   makelist = [k, v]
  #   p_ids.append(makelist)
  #   payload['queue_process']['message']['providers_ids'] = p_ids




del data['queue_process']['message']['providers_ids']


for k, v in data.items():
  payload[k] = v


# print(provider)

payload['timestamp'] = datetime.now()

numberGenerate = random.uniform(0, 100)

res = es.index(index="mono", doc_type='keyword', id=numberGenerate, body=payload)

print(payload )






