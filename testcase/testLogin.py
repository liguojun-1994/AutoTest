import json
import readConfig
import getpathInfo
import readCase
from common.configHttp  import RunMain
from pytest import mark,main
import os
import log
log=log.Logger().get_logger()



readconfig=readConfig.ReadConfig()
url=readconfig.get_Http('scheme')+'://'+readconfig.get_Http('url')+':'+readconfig.get_Http('port')+'/utalk//doLogin'
login_xls=readCase.readExcel().get_exceldata('油桃接口测试用例文档.xls','1-登录模块','login')


class TestLogin():
    def setup(self):
        print('测试准备')
        # path=os.path.join(getpathInfo.get_Path(),'testcase','testLogin.py')
        # print('日志：')
        # log.info('path:%s',path)

    @mark.parametrize('reqdata,respdata',login_xls)
    def test_login(self,reqdata,respdata):
        response=RunMain().run_main('post',url,reqdata)
        print('实际结果为：',response)
        print('*'*30)
        print('预期结果为：',respdata)
        assert response['reason']==respdata['reason']
    @mark.smoke
    def test_a(self):
        print('ABCD')
    def teardown(self):
        print('测试结束')
if __name__ == '__main__':
    # path=getpathInfo.get_Path()+'/report/tmg'
    # print(path)
    main(["-s","-v",'--alluredir','../report/tmg','testLogin.py','--clean-alluredir'])
    # os.system('allure serve ../report/tmg')
    '''
    问题原因：

    pacharm里面安装了多个python版本，导致allure安装和pycharm中python版本执行的不一致造成的。
    解决办法：

    pycharm中要执行的py文件右键，选择open in Terminal,然后在Terminal中输入pip install allure-pytest，
    安装allure。完毕后直接运行就可以了


    '''
    # main(["-s", "-v", '--alluredir', '../report/tmg', 'testLogin.py'])
    # main(["--html=../report/report.html", "testLogin.py"])
