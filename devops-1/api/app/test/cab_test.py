#!/usr/bin/env python
#coding:utf-8

import requests
import json
url = "http://127.0.0.1:5000/api"
headers = {"Content-type": "application/json"}

data = {
    "jsonrpc" : 2.0,
    "method" : "cabinet.create",
    "id" : 1,
    "auth" : None,
    "params" :{
        'name' : 'A11-26',
        "idc_id" : 'jxq',
        'power': 450,
    }
}
'''
data = {
    "jsonrpc" : 2.0,
    "method" : "cabinet.get",
    "id" : 1,
    "auth" : None,
    "params" :{
    }
}

data = {
    "jsonrpc" : 2.0,
    "method" : "cabinet.update",
    "id" : 1,
    "auth" : None,
    "params" :{
        "data" :{
        "power": 160,
        },
        "where" :{
        "id" : 3
        }

    }

    }    
'''   
r = requests.post(url, headers=headers, json=json.dumps(data))
print r.status_code
print r.content
