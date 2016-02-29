#coding:utf-8
import os
import imp
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('base.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


class AutoLoad():
    def __init__(self, module_name):
        DIR  = os.path.abspath(os.path.dirname(__file__))
        self.moduleDir = os.path.join(os.path.dirname(DIR),"modules")
        self.module_name = module_name
        self.method = None

    def isValidModule(self):   
        return self._load_module()
    
    def isValidMethod(self, func=None):
        self.method = func
        return hasattr(self.module, self.method)
     
    def getCallMethod(self):
        if hasattr(self.module, self.method):
           return getattr(self.module, self.method)
        return None    

    def _load_module(self):
        ret = False
        for filename in  os.listdir(self.moduleDir):
            if filename.endswith('.py'):
                module_name = filename.rstrip(".py")
                if self.module_name == module_name:
                    fp, pathname, desc = imp.find_module(module_name, [self.moduleDir])
                    logger.debug('fp pathname desc %s %s %s' %(fp, pathname, desc))
                    if not fp:
                        continue
                    try:
                        self.module = imp.load_module(module_name, fp, pathname, desc)
                        ret = True
                    finally:
                        fp.close()
                    break    
                else:
                    print "没有找到"
        return ret

#class Response():
#    def __init__(self):
#        self.data = None
#        self.errorCode = 0
#        self.errorMessage = None
class Response():
    def __init__(self):
            self.errorCode = 0 
            self.errorMessage = None
            self.data = None

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
            module, func = self.jsonData.get('method', "").split(".")
            logger.debug('module func %s %s' %(module,func))
            ret = self.callMethod(module, func, params, auth)
            logger.debug('execute %s' %ret)
            self.processResult(ret)
        return self._response

    def processResult(self, response):
        if response.errorCode != 0:
            self.jsonError(self.jsonData.get('id'), response.errorCode, response.errorMessage)
        else:
            self._response = {
            "jsonrpc": self.VERSION,
            "result": response.data,
            "id": self.jsonData.get("id"),
            }
    
    def callMethod(self, module, func, params, auth):
        module_name = module.lower()
        func = func.lower()
        logger.debug('callMethod_func %s' %func)
        response = Response
        logger.debug('callMethod_response %s' %response)
        autoload = AutoLoad(module_name)
        logger.debug('callMethod_autoload %s' %autoload)
        if not autoload.isValidModule():
            response.errorCode = 106
            response.errorMessage = "module is not exit"
            return response
        
        if not autoload.isValidMethod(func):
            response.errorCode = 107
            response.errorMessage ="{}下没有{}该方法".format(module_name, func)
            return response
        
        flag = self.requireAuthentication(module_name, func)
        if flag:
            if auth is None:
                response.errorCode = 108
                response.errorMessage = "该操作需要提供token"
                return response
            else:
                pass
            
        try:
            called = autoload.getCallMethod()
            if callable(called):
                response.data = called(**params)
            else:
                response.errorCode = 109
                response.errorMessage = "{}.{} 不能被调用".format(module_name, func)
        except Exception, e:
            response.errorCode = -1
            response.errorMessage = e.message
            return response

    def requireAuthentication(self, module, func):
        if module == "user" and func == "login":
            return False
        if module == "test":
            return False
        return True    
    
    def validate(self):
        if not self.jsonData.get('jsonrpc', None):
            self.jsonError(self.jsonData.get('id', 0), 101, "jsonrpc 参数没有传" )
            return False
        if str(self.jsonData.get("jsonrpc")) != self.VERSION:
            self.jsonError(self.jsonData.get('id', 0), 101, "参数jsonrpc的版本不正确，应该为：{}".format(self.VERSION))
            return False
        if not self.jsonData.get("method", None):
            self.jsonError(self.jsonData.get('id', 0), 102, "jsonrpc 参数没有传" )
            return False
        if "." not in self.jsonData.get("method"):
            self.jsonError(self.jsonData.get('id', 0), 104, "参数method格式格式不正确")
            return False
        if  self.jsonData.get("params", None) is None:
            self.jsonError(self.jsonData.get('id', 0), 103, "params没有传")
            return False
        if not isinstance(self.jsonData.get("params"), dict):    
            self.jsonError(self.jsonData.get('id', 0), 105, "params应该为dict")
            return False
        return True
    
    def jsonError(self, id, errno, errmsg):
        self._error = True
        format_err = {
            "jsonrpc": self.VERSION,
            "error": errmsg,
            "errno": errno,
            "id": id,
        }
        self._response = format_err
'''
    101 jsonrpc 版本， 或没有这个参数
    102 "参数method没有传"
    103 "params没有传"
    104 参数method 格式不不正确
    105 params 应该为dict
    106 指定的module不存在
    107 {}下没有{}的方法
    108 该操作需要提供token
    109 不能调用
    -1 api里有except
'''
if  __name__ == "__main__":
    #at = AutoLoad('test')
    #at.isValidModule()
    #print at.isValidMethod('get')
    #func = at.getCallMethod()
    #func()
    data = {
    "jsonrpc": 2.0,
    "method": 'test.get',
    "params": {},
    }
    jrpc = JsonRpc(data)
    logger.debug('result %s' %jrpc)
    ret = jrpc.execute()
    logger.debug('result %s' %ret)
    print ret
