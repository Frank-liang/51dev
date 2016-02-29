#!/usr/bin/env python
#coding:utf-8

import requests
import json
url = "http://127.0.0.1:5000/api"
headers = {"Content-type": "application/json"}

data = {
    "jsonrpc" : 2.0,
    "method" : "servertype.create",
    "id" : 1,
    "auth" : None,
    "params" :{
        "type" : 'dell720',
        'manufactures_id' : 1,
    }
}
'''
data = {
    "jsonrpc" : 2.0,
    "method" : "power.get",
    "id" : 1,
    "auth" : None,
    "params" :{
    }
}

data = {
    "jsonrpc" : 2.0,
    "method" : "idc.update",
    "id" : 1,
    "auth" : None,
    "params" :{
        "data" :{
        "user_interface": 'xiaohong',
        },
        "where" :{
        "id" : 1
        }

    }

    }    
'''   
r = requests.post(url, headers=headers, json=json.dumps(data))
print r.status_code
print r.content
