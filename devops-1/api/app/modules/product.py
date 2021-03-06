#!/usr/bin/env python
#coding:utf-8
from app.models import db, Product
from app.utils import * 

def create(**kwargs):
    check_field_exists(Product, kwargs)
    if kwargs.get('pid', 0) != 0:
        check_value_exists(Product, 'id', kwargs.get('pid', None))
    record = Product(**kwargs)
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
    
    check_output_field(Product, output)
    check_order_by(Product, order_by)
    check_limit(limit)
    data = db.session.query(Product).order_by(order_by).limit(limit).all()
    db.session.close()
    ret = process_result(data, output)
    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})
    check_update_params(Product, data, where)

    if data['pid'] != 0 and data.get('pid', None) is not None:
        check_value_exists(Product, 'id', kwargs.get('pid', None))

    ret = db.session.query(Product).filter_by(**where).update(data)
    try:
        db.session.commit()
    except Exception,e:
        raise Exception(e.message.split(") ")[1])
    return ret
