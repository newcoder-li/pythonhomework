# -*- coding: utf-8 -*-
# @Author  : lidonghui
from pythonshizhan.animal import Animal


class Cat(Animal):
    def __init__(self):
        self.hair = "短毛"
        # 重写父类的__init__方法，继承父类的属性
        super().__init__('猫', '白色', '1', 'male')

    # 添加一个新的方法，会捉老鼠
    def catch(self):
        print(f"{self.name}会捉老鼠")

    # 重写父类的【会叫】的方法
    def speak(self):
        print(f"{cat.name}会喵喵叫")


if __name__ == '__main__':
    # 对象实例化
    cat = Cat()
    print(f"{cat.name}的毛发是{cat.hair}")
    cat.catch()
    cat.speak()
