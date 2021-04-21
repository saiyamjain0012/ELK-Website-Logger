import requests
import json
from elasticsearch import Elasticsearch
from datetime import datetime


def login(lid,pasw):
    global gid, gpasw, initime
    gid=lid
    gpasw=pasw
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    dateTimeObj = datetime.now()
    initime=dateTimeObj
    dateTimeObj=dateTimeObj.isoformat()
    data={'@timestamp': dateTimeObj,
          'login_id': lid,
          'login_pass': pasw,
          'category':'login'
          }
    es.index(index='website_logs', doc_type='log', body=json.dumps(data))

def product(prodname):

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    dateTimeObj = datetime.now()
    dateTimeObj=dateTimeObj.isoformat()
    data={'@timestamp': dateTimeObj,
          'product':prodname,
          'login_id': gid,
          'login_pass': gpasw,
          'category':'click'
          }
    es.index(index='website_logs', doc_type='log', body=json.dumps(data))


def review(prod,qual,price):

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    dateTimeObj = datetime.now()
    diff=dateTimeObj-initime
   
    diff=diff.total_seconds()
    diff=int(diff)
    dateTimeObj=dateTimeObj.isoformat()

    data={'@timestamp': dateTimeObj,
          'login_id': gid,
          'login_pass': gpasw,
          'product':prod,
          'quality':qual,
          'price':price,
          'duration':diff,
          'category':'review'
          }
    es.index(index='website_logs', doc_type='log', body=json.dumps(data))
