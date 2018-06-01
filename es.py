from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
import random



if es.indices.exists(index="raju") == False: 
    print ("Index creteing")
    createIndex = es.indices.create(index="raju", ignore=400)
else: 
    print ("Index exist")

jfile = {
  "mappings": {
    "_doc": {
      "properties": {
        "tags": {
          "type":  "keyword"
        }
      }
    }
  }
}

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
    "service": {
    "repo": "fieldnation",
    "revision": "7f48deedd28fb87237d15a86bf0b584c91d4abed",
    "correlation_id": 'null'
  },
  "user_context": {

    "id": 5,

    "company": {

      "id": 10

    },

    "group": {

      "id": 20

    }

  }
}

numberGenerate = random.uniform(0, 100)

res = es.index(index="raju", doc_type='keyword', id=numberGenerate, body=doc)
# print(res['created'])

#deleteindex = es.indices.delete(index="raju", ignore=400)






