import yaml

class YmalHandler:
    def read_ymal(self,file,encoding='utf-8'):
        with open(file,encoding=encoding,mode='r') as f:
            # readdata=f.read()
            # return readdata
            return yaml.load(f.read(), Loader=yaml.FullLoader)
    def write_ymal(self,file,data,encoding='utf-8'):
        with open(file,encoding=encoding,mode='w') as f:
            # writedata=f.write(data)
            return yaml.dump(data, stream=f, allow_unicode=True)
if __name__ == '__main__':

    data = {
        "user": {
            "username": "vivi",
            "password": "123456"
        }
    }
    YmalHandler().write_ymal('../config/config.yaml',data)
    res = YmalHandler().read_ymal('../config/config.yaml')
    print(res)

