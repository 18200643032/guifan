import subprocess
import time
def runcmd(command,environment="export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64"):
    # command = command.split(";")
    # command.insert(0,environment)
    res_p = subprocess.Popen(f"{environment};{command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = res_p.communicate()
    returncode = res_p.returncode
    if returncode == 0:
        if stdout.decode('utf-8').endswith('\n'):
            return True, stdout.decode('utf-8').replace('\n','')
        return True, stdout.decode('utf-8')
    else:
        return False, stderr.decode('utf-8')

def write_res(res):
    with open("/zhengzhong/project_res.txt","a") as f:
        f.write(res)
def write_top(res):
    with open("/zhengzhong/top.txt","a") as f:
        f.write(res)
def time_time():
    t = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    return t

