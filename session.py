import requests

# 登录接口
url = 'http://127.0.0.1:8000/user/login'
payload = {
    "mobilephone":"1530272****",
    "pwd":"123456"
}
# 创建session会话管理
session = requests.session()
login_res = session.post(url,data=payload)
print(login_res.json())

# 充值接口
url = 'http://127.0.0.1:8000/recharge'
payload = {
    "mobilephone":"1530272****",
    "amount":100
}
recharge_res = session.post(url,data=payload)
print(recharge_res.json())