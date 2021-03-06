#!/usr/bin/env python
# -*- coding: utf-8 -*-
#解析并校验参数
class ArgsChecker(object):
    def __init__(self, args):
        self._args = args
        self._results = []
        self._output_params = {}

    def clear(self):
        self._results.clear()
        self._output_params.clear()

    # 注意: 只存储字符串和数字型的参数
    def outputParams(self):
        print("ArgsChecker output_params = ", self._output_params)
        return self._output_params

    #检测结果
    def checkResult(self):
        k,v = len(self._results) == 0, self._results
        print("args =", self._args, "\nCheck result =", k, v)
        return k,{"errors": v}

    #添加bool类型检测
    def addBooleanChecker(self, name, is_req = False):
        exist_message = self.checkExist(key=name)
        if exist_message is not None:
            if is_req:
                self._results.append(ArgsChecker.buildErrorMessage(name, exist_message))
            return None
        else:
            if not isinstance(self._args[name], bool):
                self._results.append(ArgsChecker.buildErrorMessage(name, "参数不是Bool格式"))
                return None
            else:
                self._output_params[name] = self._args[name]
                return self._args[name]

    # 添加字符串类型检测
    def addStringChecker(self, name, is_req = False):
        exist_message = self.checkExist(key=name)
        if exist_message is not None:
            if is_req:
                self._results.append(ArgsChecker.buildErrorMessage(name, exist_message))
            return None
        else:
            check_message = self.CheckString(arg=self._args[name], is_req=is_req)
            if check_message is not None:
                self._results.append(ArgsChecker.buildErrorMessage(name, check_message))
                return None
            else:
                self._output_params[name] = self._args[name]
                return self._args[name]

    # 添加bytes类型检测
    def addBytesChecker(self, name, is_req = False):
        exist_message = self.checkExist(key=name)
        if exist_message is not None:
            if is_req:
                self._results.append(ArgsChecker.buildErrorMessage(name, exist_message))
            return None
        else:
            check_message = self.CheckBytes(arg=self._args[name], is_req=is_req)
            if check_message is not None:
                self._results.append(ArgsChecker.buildErrorMessage(name, check_message))
                return None
            else:
                self._output_params[name] = self._args[name]
                return self._args[name]

    # 添加数值类型检测
    def addNumerChecker(self, name, is_req = False, range = (None, None)):
        exist_message = self.checkExist(key=name)
        if exist_message is not None:
            if is_req:
                self._results.append(ArgsChecker.buildErrorMessage(name, exist_message))
            return None
        else:
            check_message = self.CheckNumber(arg=self._args[name], range=range, is_req=is_req)
            if check_message is not None:
                self._results.append(ArgsChecker.buildErrorMessage(name, check_message))
                return None
            else:
                self._output_params[name] = self._args[name]
                return self._args[name]

    # 添加字典类型检测
    def addDictChecker(self, name, is_req=False, keys = None):
        exist_message = self.checkExist(key=name)
        if exist_message is not None:
            if is_req:
                self._results.append(ArgsChecker.buildErrorMessage(name, exist_message))
            return None
        else:
            check_message = self.CheckDict(arg=self._args[name], keys=keys, is_req=is_req)
            if check_message is not None:
                self._results.append(ArgsChecker.buildErrorMessage(name, check_message))
                return None
            else:
                #print("1111", name, self.args[name])
                return self._args[name]

    # 添加数组类型检测
    def addArrayChecker(self, name, is_req=False, value_range = None):
        exist_message = self.checkExist(key=name)
        if exist_message is not None:
            if is_req:
                self._results.append(ArgsChecker.buildErrorMessage(name, exist_message))
            return None
        else:
            check_message = self.CheckArray(arg=self._args[name], value_range=value_range, is_req=is_req)
            if check_message is not None:
                self._results.append(ArgsChecker.buildErrorMessage(name, check_message))
                return None
            else:
                return self._args[name]

    # 构建错误消息
    @classmethod
    def buildErrorMessage(cls, arg_name, messsage):
        return {"param": arg_name, "message": messsage}

    def checkExist(self, key):
        if not isinstance( self._args, dict):
            return "_args不为dict类型"

        if key not in self._args.keys():
            return "没有找到参数"
        else:
            return None

    # 检测二进制数据
    @classmethod
    def CheckBytes(cls, arg, is_req):
        if not isinstance(arg, bytes):
            return "参数类型不为字节数组"

        if is_req and ((arg is None) or len(arg) == 0):
            return "参数为空"
        else:
            return None

    # 检测字符串
    @classmethod
    def CheckString(cls, arg, is_req):
        if not isinstance(arg, str):
            return "参数类型不为字符串"

        if is_req and ((arg is None) or len(arg) == 0):
            return "参数为空"
        else:
            return None

    # 检测数值
    @classmethod
    def CheckNumber(cls,  arg, range, is_req):
        if not isinstance(arg, int) and not isinstance(arg, float):
            return "参数类型不为数值"

        if range is None:
            return None
        else:
            start = range[0]
            end = range[1]

            if start is not None:
                if arg < start:
                    return "超出最小值:" + str(start)
            if end is not None:
                if arg > end:
                    return "超出最大值:" + str(end)
        return None

    # 检测字典
    @classmethod
    def CheckDict(cls, arg, keys, is_req):
        if not isinstance(arg, dict):
            return "参数类型不为字典"

        if keys is None or (len(arg.keys()) == 0):
            return None

        not_exist_keys = []
        for key in keys:
            if key not in arg.keys():
                not_exist_keys.append(key)
        if len(not_exist_keys) == 0:
            return None
        else:
            return "字典里不包含必须的Key: " + ", ".join(["\"" +  str(key) + "\"" for key in not_exist_keys])

    # 检测数组
    @classmethod
    def CheckArray(cls, arg, value_range, is_req):
        if not isinstance(arg, list):
            return "参数类型不为数组"

        if is_req and len(arg) == 0:
            return "数据为空"

        if value_range is None:
            return None

        print(arg, value_range)
        check = [False for c in arg if c not in value_range]
        if len(check) == 0:
            return None
        else:
            return "数组" + str(arg) + "超出限制范围: " +  str(value_range)

