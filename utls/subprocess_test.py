import subprocess
def runcmd(command,environment="export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64"):
    # command = command.split(";")
    # command.insert(0,environment)
    res_p = subprocess.Popen(f"{environment};{command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = res_p.communicate()
    returncode = res_p.returncode
    if returncode == 0:
        if stdout.decode('utf-8').endswith('\n'):
            return True, stdout.replace('\n', '')
        return True, stdout
    else:
        return False, stderr
