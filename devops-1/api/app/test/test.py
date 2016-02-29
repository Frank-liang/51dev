#!/usr/bin/env python
#coding:utf-8

import requests
import json
url = "http://127.0.0.1:5000/api"
headers = {"Content-type": "application/json"}

data = {
    "jsonrpc" : 2.0,
    "method" : "idc.create",
    "id" : 1,
    "auth" : None,
    "params" :{
        "name" : "jxq",
        "idc_name": "酒仙桥",
        "address" : '北京',
        "phone" : 12315011401,
        "email" : 'guishi@163.com',
        "user_interface" : 'frank',
        "user_phone" : 12345678912,
        'rel_cabinet_num' : 12,
        'pack_cabinet_num' : 15,
    }
}
'''
data = {
    "jsonrpc" : 2.0,
    "method" : "idc.get",
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
