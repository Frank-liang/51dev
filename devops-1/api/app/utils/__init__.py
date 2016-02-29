#coding: utf-8

def check_field_exists(obj, data, field_none=[]):
    """
    验证字段是否合法
    验证参数不能为空
    """
    for field in data.keys():
        if not hasattr(obj, field):
            raise Exception("params error")
        
        if not data.get(field, None):
            if data[field] not in field_none:
                raise Exception("{} is not null".format(data[field]))

def process_result(data, output):
    black = ['_sa_instance_state']
    ret = []
    for obj in data:
        if output:
            tmp = {}
            for f in output:
                tmp[f] = getattr(obj, f)
            ret.append(tmp)
        else:
            tmp = obj.__dict__
            for p in black:
                try:
                    tmp.pop(p)
                except:
                    pass
            ret.append(tmp)
    return ret        

def check_order_by(obj, order_by=''):
    '''
    :param obj
    :param order_by
    :return
    '''
    order_by = order_by.split()
    if len(order_by) != 2:
        raise Exception('order by params is not right')
    
    field, order = order_by

    order_list = ['asc', 'desc']
    if order.lower() not in order_list:
        raise Exception('排序参数不正确，值可以为：{}'.format(order_list))
    
    if not hasattr(obj, field.lower()):
        raise Exception("排序字段不在该表中")

def check_limit(limit):
    if not str(limit).isdigit():
        return Exception('limit must is digit')

def check_output_field(obj, output=[]):
    if not isinstance(output, list):
        raise Exception('output must a list')
    
    for field in output:
        if not hasattr(obj, field):
            raise Exception("{} must is not null".format(field))

def check_update_params(obj, data, where):
    if not data:
        raise Exception('data must not null')
    print data
    print where
    for field in data.keys():
        if not hasattr(obj, field):
            raise Exception('need update {} params id not exist'.format(field))
    
    if not where:
        raise Exception('need where condition')

    if where.get('id', None) is None:
        if where.get('uuid', None) is None:
            raise Exception('need update conditon')
    try:
        id = int(where['id'])
        if id <= 0:
            raise Exception('id must positive')
    except ValueError:
        raise Exception('ID MUST BE INIT')

def check_value_exists(obj, name, value):
    from app.models import db
    where = {name : value}
    ret = db.session.query(obj).filter_by(**where).first()
    if not ret:
        raise Exception('{} is not exist'.format(value))

