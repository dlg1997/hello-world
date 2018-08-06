class student():
    def __init__(self,name="NoName",age=18):
        self.name = name
        self.age = age
    def say(self):
        print("My name is {0}".format(self.name))
def sayHello():
    print("hi 欢迎来到深圳")
    ###判断文件是不是以主线程在执行
if __name__ == '__main__':
    print("这是p01模块")


