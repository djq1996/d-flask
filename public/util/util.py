#!/usr/bin/python3
# coding:utf-8

from datetime import *
import time


def get_time():
    timestamp = time.time()
    print(timestamp)
    return timestamp


def get_now():
    now_time = datetime.now()
    print(now_time)
    return now_time
