import requests

# 登录接口
url = 'http://192.168.30.23:8082/utalk//doLogin'
payload = {
    "username":"011604",
    "password":"88888888"
}
# 创建session会话管理
# session = requests.session()
# login_res = session.post(url,data=payload)
# print(login_res.json())

# 充值接口
# url = 'http://127.0.0.1:8000/recharge'
# payload = {
#     "mobilephone":"1530272****",
#     "amount":100
# }
# recharge_res = session.post(url,data=payload)
# print(recharge_res.json())
# res=requests.post(url,json=payload)
#
#
# print(res.reason)
session=requests.session()
res=session.post(url,json=payload)
print(res.json())