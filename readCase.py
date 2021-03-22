import os,getpathInfo,xlrd,json,pprint
path=getpathInfo.get_Path()

class readExcel():
    def get_exceldata(self,excelname,sheetname,cassname):
        listdata=[]
        # 测试用例的路径
        casedir = os.path.join(path,'data',excelname)
        # print(casedir)
        # 打开测试用例
        file=xlrd.open_workbook(casedir,formatting_info=True)
        # 打开测试用例的sheet
        sheet=file.sheet_by_name(sheetname)
        #根据sheet的行数做循环
        nrows=sheet.nrows
        # print(nrows)
        for i in range(nrows):
            if cassname in sheet.row_values(i)[0]:
                reqdata=sheet.row_values(i)[6]
                respdata=sheet.row_values(i)[8]
                # url=sheet.row_values(i)[3]
                # print(reqdata)
                # print(respdata)
                # print(type(reqdata,respdata))
                
                # listdata.append((json.loads(reqdata),json.loads(respdata),url))
                listdata.append((json.loads(reqdata),json.loads(respdata)))

        return listdata
# res=readExcel().get_exceldata('油桃接口测试用例文档.xls','1-登录模块','login')
# pprint.pprint(res)

