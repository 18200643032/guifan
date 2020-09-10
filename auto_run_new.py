# @Time : 2020/9/8 16:08 
# @modele : auto_run_new.py
# @Author : zhengzhong
# @Software: PyCharm
import os
import time
import json
import unittest
from top_config import  write_res,time_time,write_top
from config import Terminal,Config_file
from utls.subprocess_test import runcmd
class Auto_run(unittest.TestCase):
    def setUp(self):
        pass
    @staticmethod
    def file_config_setting(conten):
        with open("algo_config.json","r") as f:
            json_str = json.load(f)
        for key, vaule in conten.items():
            json_str[key]=vaule
        with open("algo_config.json", "w") as f2:
            json.dump(json_str, f2)
    def test00001_not_function(self):
        """验证未授权返回-999"""
        code,connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_not_function}")
        write_res(connet+'\n')
    def test00002_yes_function(self):
        """授权"""
        code, connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_yes_function}")
        write_res(connet + '\n')
    def test00003_ev_license(self):
        """ev_license版本是否一致"""
        code,connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_ev_license}")
        write_res(connet + '\n')
    def test00004_project_path(self):
        """验证工程路径与规范一致"""
        code,connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_project_path}")
        write_res(connet + '\n')
    def test00005_make_file(self):
        """验证test.cpp和makefile"""
        code, connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_make_file}")
        write_res(connet + '\n')
    def test00006_catalogue(self):
        """test-ji-api和license.txt移动到任意目录，都需要能够正常运行目录"""
        code,connet = runcmd(f"bash /zhengzhong/zz.sh {Terminal.main_catalogue}")
        write_res(connet + '\n')
    def test00007_libji_connect(self):
        """libjo.so链接所有库"""
        code，connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_libji_connect}")
        write_res(connet + '\n')
    def test00008_verification_pem(self):
        """# 公私钥位置，名称验证"""
        code,connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_verification_pem}")
        write_res(connet + '\n')
    def test00009_libji_connect(self):
        """libjo.so链接所有库"""
        code,connet = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_libji_connect}")
        write_res(connet + '\n')
    def test000091_algo_config(self):
        """生成不同的结果图片"""
        config = Config_file.config
        for con in config:
            file_name = ''
            for a, b in con.items():
                file_name += a + "_" + str(b)
            self.file_config_setting(config[con])
            code,conten = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_run_sdk} {file_name}")
            write_res(conten + '\n')
    def test000092_dynamiv_config(self):
        """动态传参生成不同的结果图片"""
        config = Config_file.config
        for con in config:
            file_name = ''
            for a, b in con.items():
                file_name += a + "_" + str(b)
            code,conten = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_run_sdk_dynamiv} {file_name} {config[con]}")
            write_res(conten + '\n')
    def test000093_function(self):
        """实现的接口测试"""
        for i in range(1,5):
            code,conten=runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_function} {i}")
            write_res(conten + '\n')
    def test000093_top_free(self):
        """测试接口1和接口5是否存在内存显存泄露"""
        code,pid = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_free_num1}")
        write_top("接口1资源占用情况"+ '\n')
        for i in range(10):
            time.sleep(120)
            cmd_cpu = "top -n 1 -p %s |grep test-ji-api  |awk '{print $10}'"%pid
            cmd_mem = "top -n 1 -p %s |grep test-ji-api  |awk '{print $11}'"%pid
            cmd_nvidia = "nvidia-smi |grep Default |awk '{print $9}'|awk 'NR==1'"
            code,nvidia= runcmd(cmd_nvidia)
            code,cpu = runcmd(cmd_cpu)  #cpu占用
            code,mem = runcmd(cmd_mem)  #内存占用
            t = time_time()               #当前时间
            write_top("当前时间:%s \n cpu占用:%s \n 内存占用:%s \n 显存占用:%s"%(t,cpu,mem,nvidia))
        os.system("kill -9 %s"%pid)
        time.sleep(2)
        code, pid = runcmd(f"bash /zhengzhong/sh/zz.sh {Terminal.main_free_num5}")
        write_top("接口5资源占用情况" + '\n')
        for i in range(10):
            time.sleep(120)
            cmd_cpu = "top -n 1 -p %s |grep test-ji-api  |awk '{print $10}'"%pid
            cmd_mem = "top -n 1 -p %s |grep test-ji-api  |awk '{print $11}'"%pid
            cmd_nvidia = "nvidia-smi |grep Default |awk '{print $9}'|awk 'NR==1'"
            code,nvidia= runcmd(cmd_nvidia)
            code,cpu = runcmd(cmd_cpu)  #cpu占用
            code,mem = runcmd(cmd_mem)  #内存占用
            t = time_time()               #当前时间
            write_top("当前时间:%s \n cpu占用:%s \n 内存占用:%s \n 显存占用:%s"%(t,cpu,mem,nvidia))



if __name__ == "__main__":
    unittest.main()
