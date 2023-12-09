import os

width = 10
title = "-" * width + "欢迎进入植物信息管理系统" + "-" * width


def show_options(kwg):
    for i in range(0, len(kwg)):
        print(" " * (int)(len(title) / 2) + (str)(i + 1) + "." + kwg[i])


# 负责输出页面
# list 要输出的参数
# success 是否输出失败信息
def show_page(list, success=True):
    os.system('cls')
    print(title)
    show_options(list)
    if not success:
        print("输入命令不正确，请重新输入")
    success, num = get_number()
    if success:
        print(num)
    else:
        show_page(list, False)


def get_number():
    num = input("请输入操作:")
    if num.isdigit():
        return True, int(num)
    else:
        return False, 0


list = ['登录', '注册', '退出']
show_page(list)
