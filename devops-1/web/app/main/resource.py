#!/usr/bin/env python
# coding:utf-8
from __future__ import unicode_literals
from flask import render_template, request
from app.common import api_action
from . import main
import requests
import json
import time

@main.route('/resource/index',methods=['GET'])
def resource_index():
    return render_template('resource/index.html')

@main.route('/resource/idc', methods=['GET','POST'])
def resource_idc():
    return render_template("resource/server_add_idc.html")

@main.route("/resource/server_list", methods=['GET'])
def resource_server_list():
    servers = api_action("server.get")
    return render_template("resource/server_list.html",
                                   servers=servers)

@main.route('/resource/server_add', methods=['GET'])
def resource_server_add():
    idc_info = api_action('idc.get', {'output': ['name', 'id']})
    status = api_action('status.get', {'output': ['id', 'name']})
    manufacturers = api_action('manufacturers.get', {'output': ['id', 'name']})
    return render_template("resource/server_add.html", 
                                                        idc_info=idc_info,
                                                        status = status,
                                                        manufacturers = manufacturers,
                                                        )




'''
添加IDC页面
'''
@main.route("/resource/server_idc_add", methods=['GET'])
def resource_server_idc_add():
    return render_template("resource/server_add_idc.html")
'''
执行IDC添加
'''
@main.route("/resource/server_idc_doadd", methods=['POST'])
def resource_server_idc_doadd():
    ret = api_action("idc.create", dict(request.form))
    print dict(request.form)
    print ret
    if str(ret).isdigit():
        return "操作成功"
    else:
        return "操作失败"    
'''
添加服务器状态
'''
@main.route('/resource/server_status_add', methods=['GET'])
def resource_server_status_add():
    return render_template("resource/server_add_status.html")
'''
执行服务器状态添加
'''
@main.route('/resource/server_status_doadd', methods=['POST'])
def resource_server_status_doadd():
    ret = api_action('status.create', dict(request.form))
    if str(ret).isdigit():
        return '操作成功'
    else:   
        return '操作失败'

'''
添加制造商信息
'''
@main.route('/resource/server_manufacturers_add', methods=['GET'])
def resource_manufacturers_add():
    return render_template("resource/server_add_manufacturers.html")
'''
执行制造商状态添加
'''
@main.route('/resource/server_manufacturers_doadd', methods=['POST'])
def resource_manufacturers_doadd():
    ret = api_action('manufacturers.create', dict(request.form))
    if str(ret).isdigit():
        return '操作成功'
    else:   
        return '操作失败'


'''
添加服务器型号信息
'''
@main.route('/resource/server_servertype_add', methods=['GET'])
def resource_servertype_add():
    manufacturers = api_action('manufacturers.get', {'output': ['id', 'name']})
    return render_template("resource/server_add_servertype.html", manufacturers=manufacturers)
'''
执行服务器型号状态添加
'''
@main.route('/resource/server_servertype_doadd', methods=['POST'])
def resource_servertype_doadd():
    ret = api_action('servertype.create', dict(request.form))
    print dict(request.form)
    print ret
    if str(ret).isdigit():
        return '操作成功'
    else:   
        return '操作失败'



'''
主机数据采集并入库
'''
@main.route('/resource/server/auto/collection', methods=['POST'])
def resource_server_collection():
    # 接受传递过来的主机信息
    if request.method == 'POST':
        data = dict(request.form)
        data['check_update_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #更新数据
        ret = api_action('server.update', {'data': data, 'where':{'uuid': data['uuid']}})
        if not ret.isdigit():
            ret = api_action('server.create', data)
    return '200'    
    
