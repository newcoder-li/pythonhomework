# -*- coding: utf-8 -*-
import saved
from send import send_money
from select import select_money

# 启动发工资和展示存款
if __name__ == '__main__':
    print(f"初始工资为{saved.saved_money}")
    print(f"发工资{send_money()}")
    select_money()
