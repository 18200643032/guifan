import os
import json
import time
# 运行的接口
# 传入参数是接口对应的数字
def write_res(res):
    with open("/zhengzhong/project_res.txt","a") as f:
        f.write(res)
def write_top(res):
    with open("/zhengzhong/top.txt","a") as f:
        f.write(res)
def time_time():
    t = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    return t
