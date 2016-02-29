#!/usr/bin/env python
#coding:utf-8
import os
import imp

class AutoLoad():
    def __init__(self, module_name):
        DIR = os.path.abspath(os.path.dirname(__file__))
        self.moduleDir = os.path.join(os.path.dirname(DIR),'modules')
        self.module_name = module_name
        self.method =None
    
    def isValidModule(self):
        return self._load_module()
    
    def isValidMethod(self,func=None):
        self.method = func
        return hasattr(self.module, self.method)
   
    def getCallMethod(self):
        if hasattr(self.module, self.method):
            return getattr(self.module, self.method)
        else:
            return None
    
    def _load_module(self):
        ret = False
        for filename in os.listdir(self.moduleDir):
            if filename.endswith('.py'):
                module_name = filename.rstrip('.py')
                if self.module_name == module_name:
                    fp, pathname, desc = imp.find_module(module_name,[self.moduleDir])
                    if not fp:
                        continue
                    try:
                        self.module = imp.load_module(module_name, fp, pathname, desc)
                        ret = True
                    finally:
                        fp.close()
                    break
                else:
                    print 'fail'
        return ret        
        

class Response():
    self.errorCode = 0
    self.errorMessage = None
    sel.data = None


class JsonRpc():
    def __init__(self, jsonData):
        self.VERSION = '2.0'
        self._error = True
        self.jsonData = jsonData
        self._response = {}

    def execute(self):
        if not self.jsonData.get('id', None):
            self.jsonData['id'] = None
        if self.validate():
            params = self.jsonData.get('params', None)
            auth = self.jsonData.get('auth', None)
            module, func = self.jsonData.get('method','').split('.')
            ret = self.callMethod(module, func, params, auth)
            self.processResult(ret)
        return self._response

    def processResult(self, response):
        if response.errorCode != 0:
            self.jsonError(self.jsonData.get('id'), response.errorCode, response.errorMessage)
        else:
            self._response = {
                "jsonrpc" : self.VERSION,
                "result" : response.data,
                'id' : self.jsonData.get(id)
                }
    
    def callMethod(self, module, func, params, auth):
        module_name = module.lower()
        func = func.lower()
        response = Response()
        autoload = AutoLoad(module_name)
        if not autoload.isValidModule():
            response.errorCode = 106
            response.errorMessage = 'module does not exist'
            return response
        if not autoload.isValidMethod(func):
            response.errorCode = 107
            response.errorMessage = 'No method like..'.format(module_name, func)
            return response
        flag = self.requireAuthentication(module_name, func)
        if flag:
            if auth is None:
                response.errorCode = 108
                response.errorMessage = 'token'
                return response
            else:
                pass
        try:
            called = autoload.getCallMethod()
            if callable(called):
                response.data = called(**params)
            else:   
                response.errorCode = 109
                response.errorMessage = 'Method can not work'.format(module_name, func)
        except Exception,e:
            response.errorCode = -1
            response.errorMessage = e.message
            return response
        return response

    def requireAuthentication(self, module, func):
        if module == 'user' and func == 'login':
            return False
        if module == 'test':
            return False
        return True

    def validate(self):
        if not self.jsonData.get('jsonrpc', None):
            self.jsonError(self.jsonData.get('id', 0), 101, 'jsonrpc need parameter')
            return False
        if str(self.jsonData.get('jsonrpc')) != self.VERSION:
            self.jsonError(self.jsonData.get('id', 0), 101, 'jsonrpc version wrong')
            return False
        if not self.jsonData.get('method', None):
            self.jsonError(self.jsonData.get('id', 0), 102, 'jsonrpc method need parameter')
            return False
        if self.jsonData.get('params', None) is None:        
            self.jsonError(self.jsonData.get('id', 0), 103, 'params method need parameter')
            return False
        if '.' not in  self.jsonData.get('method'):    
            self.jsonError(self.jsonData.get('id', 0), 104, 'need .')
            return False
        if not isinstance(self.jsonData.get('params'), dict):            
            self.jsonError(self.jsonData.get('id', 0), 105, 'params mast dict')
            return False
        return True

    def jsonError(self, id, errno, errmsg):
        self._error = True
        format_err = {
            'jsonrpc' :self.VERSION,
            'error' : errmsg,
            'errno' : errno,
            'id' : id
            }
        self._response = format_err    
#if  __name__ == "__main__":
#    at = AutoLoad('test')
#    at.isValidModule()
#    print at.isValidMethod('get')
#    func = at.getCallMethod()
#    func()
    data= { 
        'jsonrpc':2.0,
        'method':'test.get',
        'params':{},
        }
    at = JsonRpc(data)
    ret = at.execute()
    print ret
