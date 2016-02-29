#!/usr/bin/env python
#coding:utf-8
import psutil
import platform
import socket
import os

def serverIp():
   _ip_addr = psutil.net_if_addrs()
   ip_all = {}
   for key in _ip_addr:
       ip = _ip_addr[key][0][1]
       ip_all[key] = ip
   ip_all.pop('lo')
   return  ip_all


def serverCpuInfo():
    _cpu_num  = int(psutil.cpu_count())
    return 'cpu number :', _cpu_num
    with open('/proc/cpuinfo') as _f:
        _cpu =  _f.readlines()[4].split(':')[1]
    return  str(_cpu)

def serverMemTotal():
    with open('/proc/meminfo') as _mem:
        a = int(_mem.readline().split()[1])
        return  a / 1024

def serverMemUsagr():
    with open('/proc/meminfo') as _mem:
        total = int(_mem.readline().split()[1])
        free = int(_mem.readline().split()[1])
        buffer = int(_mem.readline().split()[1])
        cache = int(_mem.readline().split()[1])
        return  (total-free-buffer-cache) / 1024
        
def serverMemFree():
    with open('/proc/meminfo') as _mem:
        total = int(_mem.readline().split()[1])
        free = int(_mem.readline().split()[1])
        buffer = int(_mem.readline().split()[1])
        cache = int(_mem.readline().split()[1])
        return  (free+buffer+cache) / 1024

def serverHostName():
    _hostname = socket.gethostname()
    return  _hostname

def serverVersion():
    _version =  platform.release()
    return  _version

def serverDiskInfo():
    disk = {}
    for info in os.popen('fdisk -l').readlines():
        _info = str(info).split(' ')
        if _info[0] == 'Disk' and _info[1].startswith('/dev'):
            disk[_info[1]] = int(_info[4])/ 1024 /1024 / 1024
    return disk           

def serverInfo():
    s_info = {
       "Manufacturer" : 0,
        "Product Name" : 0,
        "Serial Number" : 0,
        "UUID" : 0,
        "Release" : 0,
        }
    for info in os.popen(' dmidecode | grep -A6 "System Information"').readlines():
        _info = info.split('\t')
        for i in _info:
            _i = i.split(':')
            if _i[0] == "Manufacturer":
                s_info['Manufacturer'] = _i[1].rstrip('\n')
            if _i[0] == "Product Name":
                s_info['Product Name'] = _i[1].rstrip('\n')
            if _i[0] == "Serial Number":
                s_info['Serial Number'] = _i[1].rstrip('\n')
            if _i[0] == "UUID":
                s_info['UUID'] = _i[1].rstrip('\n')
    for info in os.popen('dmidecode | grep -i release').readlines():
        _info = info.split(':')
        s_info['Release'] = _info[1].rstrip('\n')
    return s_info        
            
if __name__ == "__main__":
    serverIp()
    serverCpuInfo()
    serverMemUsagr()
    serverMemFree()
    serverMemTotal()
    serverHostName()
    serverVersion()
    serverDiskInfo()
    serverInfo()
    
        
