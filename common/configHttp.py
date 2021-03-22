import requests,json

class RunMain():
    def send_get(self,url,data,headers=None):
        result=requests.get(url,params=data,headers=headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_post(self,url,data,headers=None):

        result = requests.post(url, json=data,headers=headers).json()
        # res = json.dumps(result, ensure_ascii=False,sort_keys=True, indent=2)
        return result

    def run_main(self,method,url=None,data=None,headers=None):
        result1=None
        if method=='post':
            result1=self.send_post(url,data,headers)
        elif method =='get':
            result1=self.send_get(url,data,headers)
        else:
            print('你输入的method错误')
        return result1




if __name__ == '__main__':
    testData = {'username': '20154084', 'password':'123456'}
    # print(type(testData))
    # testData = 'username=20154084&password=123456'
    # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    print(type(testData))
    # headers = {
    #     "Content-Type": "application/json"
    # }
    # data=json.dumps(testData)

    url='http://192.168.30.23:8082/utalk//doLogin'
    res=RunMain().run_main('post',url,testData)
    print(res)
