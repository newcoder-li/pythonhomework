# -*- coding: utf-8 -*-
import saved


# 定义发工资方法
def send_money():
    salary = 1000
    saved.saved_money += salary
    return salary
