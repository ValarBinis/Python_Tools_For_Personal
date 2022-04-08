# -*- coding: utf-8 -*-
# @Time : 2022/4/9 7:33
# @Author : 倪浩凡
# @Email : connorauditorechina@outlook.com
# @File : TXT换行修正工具.py
# @Project : Python


"""
1.PDF转换TXT后会添加很多的换行符
2.一般换行的长度和段落结尾的长度不一样
程序思路：
将TXT读取为一个列表，遍历内容为列表后再重新组合TXT，当长度大于某一个值时不换行，否则当长度小于某一个值并且结尾是句号就添加自动换行符号
"""



