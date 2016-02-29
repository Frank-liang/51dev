#!/usr/bin/env python
#coding:utf-8
from app.models import db, Raid
from app.utils import check_field_exists, process_result, check_order_by, check_limit, check_output_field, check_update_params

def create(**kwargs):
    check_field_exists(Raid, kwargs)
    record = Raid(**kwargs)
    db.session.add(record)
    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])
    return record.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')
    
    check_output_field(Raid, output)
    check_order_by(Raid, order_by)
    check_limit(limit)
    data = db.session.query(Raid).order_by(order_by).limit(limit).all()
    db.session.close()
    ret = process_result(data, output)
    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})
    check_update_params(Raid, data, where)
    ret = db.session.query(Raid).filter_by(**where).update(data)
    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])
    return ret
