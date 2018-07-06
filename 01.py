'''
定义一个学生类 ，用来形容学生
'''
#表示定义一个空的类
class Student():
    ##一个空类,pass代表跳过
    #空类必须要有pass
    pass

#定义一个对象
mingyue = Student()

#再定义一个类，用来描述听python的学生
class PythonStudent():
    #在不知道属性值的情况下必须赋值None
    name = None
    age = 18
    coures = "python"
    #1.方法的层级
    #2.默认的self参数
    def doHomework(self):
        print("在写作业")
        #在函数末尾推荐return返回值
        return None

#实例化一个学生
fangfang = PythonStudent()
print(fangfang.age,fangfang.name)

#注意成员函数调用没有传参数
fangfang.doHomework()
