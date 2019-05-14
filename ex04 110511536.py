# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:27:06 2019

@author: User
"""

month = int(input("請輸入月份："))
if month >= 3 and month <= 5:
    print("輸入的{}月份是春天".format(month))
elif month >= 6 and month <= 8:
    print("輸入的{}月份是夏天".format(month))
elif month >= 9 and month <= 11:
    print("輸入的{}月份是秋天".format(month))
elif month ==12 or month == 1 or month == 2 :
    print("輸入的{}月份是冬天".format(month))
else:
    print("別亂打超過12好嗎")