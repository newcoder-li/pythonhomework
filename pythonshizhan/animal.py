# -*- coding: utf-8 -*-
# @Author  : lidonghui

class Animal:
    # Animal类的构造方法
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 定义类方法run
    def run(self):
        print(f"{self.name}会跑")

    # 定义类方法speak
    def speak(self):
        print(f"{self.name}会叫")
