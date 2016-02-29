#!/usr/bin/env python
#coding:utf-8
"""
没有简化之前的IDC的代码
"""
from app.models import db, Idc

def create(**kwargs):
    for field in kwargs.keys():
        if not hasattr(Idc, field):
            raise Exception('params error')
        if kwargs.get(field, None) is None:
            raise Exception('{} is not null')
    idc = Idc(**kwargs)
    db.session.add(idc)
    db.session.commit()
    return idc.id

def get(**kwargs):
    output = kwargs.get('output', [])
    limit = kwargs.get('limit', 10)
    order_by = kwargs.get('order_by', 'id desc')

    if not isinstance(output, list):
        raise Exception('output must a list')
    
    for field in output:
        if not hasattr(Idc, field):
            raise Exception("{} must is not null".format(field))
    
    data = db.session.query(Idc).order_by(order_by).limit(limit).all()
    db.session.close()
    ret = []
    for obj in data:
        if output:
            tmp = {}
            for f in output:
                tmp[f] = getattr(obj, f)
            ret.append(tmp)
        else:
            tmp = obj.__dict__
            tmp.pop('_sa_instance_state')
            ret.append(tmp)
    return ret

def update(**kwargs):
    data = kwargs.get('data', {})
    where = kwargs.get('where', {})

    if not data:
        raise Exception('data must not null')
    for field in data.keys():
        if not hasattr(Idc, field):
            raise Exception('需要更新的{}这个地段不存在'.format(field))
    
    if not where:
        raise Exception('需要提供where条件')
    if where.get('id', None) is None:
        raise Exception('需要提供id作为条件')
    try:
        id = int(where['id'])
        if id <= 0:
            raise Exception('id must positive')
    except ValueError:
        raise Exception('ID MUST BE INIT')
    ret = db.session.query(Idc).filter_by(**where).update(data)
    db.session.commit()
    return ret
