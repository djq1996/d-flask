#!/usr/bin/python3
# coding:utf-8
import os
from public.util.util import *


get_time()
get_now()

print('__file__ :', __file__)
print('__name__ :', __name__)

APP_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(APP_DIR)
DIST_DIR = os.path.join(ROOT_DIR, 'dist')
print(APP_DIR, ROOT_DIR, DIST_DIR)

# djq()


# 乘法口诀
# for a in range(1, 10):
#     for b in range(1, 10):
#         if b <= a:
#             print("%s*%s=%s" % (b, a, a * b), end='  ')
#             # print("%d" % (a))
#     print('\n')


# print("我叫 %s 今年 %d 岁!" % ('董建强', 24))
