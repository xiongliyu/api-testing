from src.common import Common

# 实例化Common
host_url = r'http://127.0.0.1:12356'
comm = Common(host_url)

# 访问首页
uri_index = '/'
res_index = comm.get(uri_index)
print('访问首页' + res_index.text)

# 存储战场的登录
uri = r'/login'
username = 'criss'
password = 'criss'

payload = 'username=' + username + '&password=' + password
res_login = comm.post(uri, payload)
print(res_login.text)

# 存储战场的武器选择
uri_selectEq = r'/selectEq'
equipmentid = '10003'
payload_selectEq = 'equipmentid=' + equipmentid
res_selectEq = comm.post(uri_selectEq, payload_selectEq)
print(u'存储战场的武器选择' + res_selectEq.text)

# 存储战场另一个武器选择
enmyid = '20001'
uri_kill = '/kill'
payload_enmyid = 'enmyid=' + enmyid + '&equipmentid=' + equipmentid
res_enmyid = comm.post(uri_kill, payload_enmyid)
print(u'存储战场的武器选择' + res_enmyid.text)
print(111)

