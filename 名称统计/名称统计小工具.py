# -*- coding: utf-8 -*-
# @Time : 2022/5/8 11:03
# @Author : 倪浩凡
# @Email : connorauditorechina@outlook.com
# @File : 名称统计小工具.py
# @Project : Python

"""
新建一个名为name.txt的文档，名字一行一个，将name.txt和程序放在一起
"""


file_path = "./name.txt"
not_include_names = []

searching_text = input("请输入查找的字符串：")


def read_name_list():
    name_list = ''
    with open(file_path.encode("utf-8"), 'r') as n:
        name_list = n.readlines()

    searching_names(name_list)


def searching_names(name_list):
    for n in name_list:
        n = n.split('\n')[0]
        if n not in searching_text:
            not_include_names.append(n)
    output_not_include_name()


def output_not_include_name():
    print(not_include_names)


if __name__ == '__main__':
    read_name_list()
    exit_input = input("输入任意字符退出：")
