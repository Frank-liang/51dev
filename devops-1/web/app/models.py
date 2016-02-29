#!/usr/bin/env python
# coding:utf-8
from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    deparment_id = db.Column(db.Integer, index=True)
    is_leader = db.Column(db.Integer, index=True,default=0)
    phone = db.Column(db.Integer)


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50),nullable=False)
    superior = db.Column(db.Integer, default=0)
    path = db.Column(db.String(200))


class Idc(db.Model):
    __tablename__ = 'idc'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False,index=True,unique=True)
    idc_name = db.Column(db.String(30),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    phone = db.Column(db.String(15),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    user_interface = db.Column(db.String(50),nullable=False)
    user_phone = db.Column(db.String(20),nullable=False)
    rel_cabinet_num = db.Column(db.Integer, nullable=False)
    pack_cabinet_num = db.Column(db.Integer, nullable=False)


class Cabinet(db.Model):
    __tablename__ = 'cabinet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False, unique=True)
    idc_id = db.Column(db.String(10), index=True, nullable=False)
    power = db.Column(db.Integer)


class Manufacturers(db.Model):
    __tablename__ = 'manufacture'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Servertype(db.Model):
    __tablename__ = 'servertype'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    manufactures_id = db.Column(db.Integer, nullable=False, index=True)


class Raid(db.Model):
    __tablename__ = 'raid'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)



class Raidtype(db.Model):
    __tablename__ = 'raidtype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(20), nullable=False)
    pid = db.Column(db.Integer, nullable=False, index=True)
    module_letter = db.Column(db.String(10), nullable=False)
    dev_interface  = db.Column(db.String(100))
    op_interface  = db.Column(db.String(100))


class Power(db.Model):
    __tablename__ = 'power'
    id = db.Column(db.Integer, primary_key=True)
    server_power = db.Column(db.String(20), nullable=False)



class Ip_info(db.Model):
    __tablename__ = 'ip_info'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20), nullable=False)
    mac = db.Column(db.String(20), nullable=False)
    device = db.Column(db.String(20), nullable=False)
    serve_id = db.Column(db.Integer, nullable=False, index=True)
    swich_id = db.Column(db.Integer, nullable=False, index=True)
    swich_port = db.Column(db.Integer)



class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.Integer, index=True)
    manufactures = db.Column(db.String(50), nullable=False, index=True)
    manufacture_date = db.Column(db.Date)
    server_type = db.Column(db.String(20))
    st = db.Column(db.String(60), index=True)
    assets_no = db.Column(db.String(60))
    idc_id = db.Column(db.Integer, index=True)
    cabinet_id = db.Column(db.Integer)
    cabinet_pos = db.Column(db.String(10))
    expire = db.Column(db.Date)
    ups = db.Column(db.Integer)
    parter = db.Column(db.String(50))
    parter_type = db.Column(db.String(50))
    server_up_time = db.Column(db.Date)
    os_type = db.Column(db.String(20))
    os_version = db.Column(db.String(10))
    hostname = db.Column(db.String(32), nullable=False, index=True)
    inner_ip = db.Column(db.String(32), nullable=False, index=True)
    mac_address = db.Column(db.String(32))
    ip_info = db.Column(db.String(300))
    server_cpu = db.Column(db.String(250))
    server_disk = db.Column(db.String(250))
    server_mem = db.Column(db.String(250))
    raid = db.Column(db.String(10))
    raid_card_type = db.Column(db.String(50))
    remote_card = db.Column(db.String(32))
    remote_cardip = db.Column(db.String(32))
    status = db.Column(db.Integer, index=True)
    remark = db.Column(db.Text)
    last_op_time = db.Column(db.Time)
    last_op_people = db.Column(db.Integer)
    monitor_mail_group = db.Column(db.String(32))
    service_id = db.Column(db.Integer, index=True)
    server_purpose = db.Column(db.Integer, index=True)
    trouble_resolve = db.Column(db.Integer)
    op_interface_other = db.Column(db.Integer)
    dev_interface = db.Column(db.Integer)
    check_update_time = db.Column(db.Time)
    vm_status = db.Column(db.Integer, index=True, nullable=False)
    power = db.Column(db.Integer)
    host = db.Column(db.Integer, index=True)



class Switch(db.Model):
    __tablename__ = 'switch'
    id = db.Column(db.Integer, primary_key=True)
    switch_name = db.Column(db.String(50), nullable=False)
    switch_type = db.Column(db.String(50), nullable=False)
    manager_ip = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    idc_id = db.Column(db.Integer, index=True)
    cabinet_id = db.Column(db.Integer, index=True)
    status = db.Column(db.Integer, index=True)
    expire = db.Column(db.Date)
    remark = db.Column(db.Text)
    manufacturers = db.Column(db.Integer)
    last_op_time = db.Column(db.Time)
    last_op_people = db.Column(db.Integer)
    switch_port_nums = db.Column(db.Integer)




