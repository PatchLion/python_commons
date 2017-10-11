﻿from flask import request

from Practices.MyContractServer import app


@app.route('/')
@app.route('/index')
def index():
    return "<p>欢迎光临API服务器(Contract Server API)!</p><p><a href='https://www.showdoc.cc/1669185'>API文档</a>      By 打补丁的狮子 / SimpleLove</p>"

# 注册用户
@app.route('/api/user/register', methods=["POST"])
def regist():
    return doRegister(request, None)


# 删除用户
@app.route('/api/user/remove', methods=["POST"])
def remove_user():
    return removeUser(request, None)

# 登录
@app.route('/api/user/login', methods=["POST"])
def login():
    return doUserLogin(request, None)

# 修改用户信息
@app.route('/api/user/modify', methods=["POST"])
def user_modify():
    return doUserModify(request, None)

# 获取用户列表
@app.route('/api/user/list', methods=["POST"])
def user_list():
    return getUserList(request, None)

# 添加角色
@app.route('/api/role/create', methods=["POST"])
def role_create():
    return doCreateRole(request, None)

# 修改角色权限
@app.route('/api/role/modify', methods=["POST"])
def role_modify():
    return doRoleModify(request, None)


# 删除角色
@app.route('/api/role/remove', methods=["POST"])
def role_remove():
    return doRoleRemove(request, None)


# 获取角色列表
@app.route('/api/role/list', methods=["POST"])
def role_list():
    return getRoleList(request, None)


# 获取项目列表
@app.route('/api/project/list', methods=["POST"])
def project_list():
    return getProjectList(request, None)

# 创建项目
@app.route('/api/project/create', methods=["POST"])
def project_create():
    return doProjectCreate(request, None)

# 创建合同
@app.route('/api/contract/create', methods=["POST"])
def contract_create():
    return doContractCreate(request, None)

# 获取合同
@app.route('/api/contract/list', methods=["POST"])
def contract_list():
    return getContractList(request, None)

# 修改合同信息
@app.route('/api/contract/modify', methods=["POST"])
def contract_modify():
    return doContractModify(request, None)

'''
# 增加合同执行记录
@app.route('/api/contract/history/create', methods=["POST"])
def create_contracts_history():
    return doContractHistory(request, None)
'''

# 获取公司列表
@app.route('/api/companies/list', methods=["POST"])
def get_companies():
    return getCompanies(request, None)

# 创建公司
@app.route('/api/companies/create', methods=["POST"])
def create_company():
    return doCompanyCreate(request, None)
'''
# 创建公司
@app.route('/api/contract/bill/create', methods=["POST"])
def create_bill():
    return doBillCreate(request, None)
'''
'''
# 上传文件
@app.route('/api/contract/upload', methods=["POST"])
def upload():
    return doUpload(request, None)
'''

# 获取行业列表
@app.route('/api/trade/list', methods=["POST"])
def trade_list():
    return getTradeList(request, None)

# 获取建筑性质列表
@app.route('/api/buildtype/list', methods=["POST"])
def buildtype_list():
    return getBuildTypeList(request, None)

# 获取资金来源类型列表
@app.route('/api/moneytype/list', methods=["POST"])
def moneytype_list():
    return getMoneyTypeList(request, None)

# 上传合同票据信息
@app.route('/api/bill/upload', methods=["POST"])
def bill_upload():
    return uploadBill(request, None)

#获取合同票据列表
@app.route('/api/bill/list', methods=["POST"])
def bill_list():
    return getBillList(request, None)



        # 增加项目审批请求
#@app.route('/api/project/ask_approve/create', methods=["POST"])
#def ask_approve_create():
    #return doAskApproveCreate(request, None)

# 获取项目审批请求
#@app.route('/api/project/ask_approve/get', methods=["POST"])
#def get_ask_approve():
    #return getAskApprove(request, None)

# 项目通过审批
#@app.route('/api/project/ask_approve/set', methods=["POST"])
#def set_approve_state():
    #return setApproveState(request, None)