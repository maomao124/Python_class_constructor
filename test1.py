"""
 * Project name(项目名称)：Python类的构造方法
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 20:08
 * Version(版本): 1.0
 * Description(描述)：
 在创建类时，我们可以手动添加一个 __init__() 方法，该方法是一个特殊的类实例方法，称为构造方法（或构造函数）。
构造方法用于创建对象时使用，每当创建一个类的实例对象时，Python 解释器都会自动调用它
def __init__(self,...):
    代码块
 """


class C1:
    def __init__(self):
        print("调用构造方法")


class C2:
    def __init__(self, a, b):
        print("调用有参构造方法")
        print(a, "---", b)


if __name__ == '__main__':
    c1 = C1()
    c2 = C2(3, 7)
