import time, paramiko, sys
import subprocess, os
ip1 = 'hpc.lge.com'
id = 'jaeyoung.choi'
pw = '1111'

fname = str(time.time())
cmd = "psftp.exe"
p = subprocess.run([cmd, ip1, '-l', id, '-pw', pw, '-b', 'upload_cmd'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True,shell=True) 
while p.poll() == None:
    out = p.stdout.readline()
    print(out, end='')