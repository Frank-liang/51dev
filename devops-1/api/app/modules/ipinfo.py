#!/usr/bin/env python
#coding:utf-8
from app.models import db, Ip_info, Server, Switch
from app.utils import *

def create(**kwargs):
    check_field_exists(Ip_info, kwargs)
    
    check_value_exists(Server, 'id', kwargs.get('server_id', None))
    check_value_exists(Switch, 'id', kwargs.get('switch_id', None))


    cabinet = Ip_info(**kwargs)
    db.session.add(cabinet)
    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])
    return cabinet.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')
    
    check_output_field(Ip_info, output)
    check_order_by(Ip_info, order_by)
    check_limit(limit)
    data = db.session.query(Ip_info).order_by(order_by).limit(limit).all()
    db.session.close()
    ret = process_result(data, output)
    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})
    check_update_params(Ip_info, data, where)
    if data.get('server_id', None): 
        check_value_exists(Server, 'id', kwargs.get('server_id', None))
    if data.get('switch_id', None): 
        check_value_exists(Switch, 'id', kwargs.get('switch_id', None))

    ret = db.session.query(Ip_info).filter_by(**where).update(data)
    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])
    return ret
