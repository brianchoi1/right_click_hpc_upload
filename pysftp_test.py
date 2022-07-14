import subprocess, os, sys

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)

cmd = resource_path("psftp.exe")
# subprocess.run([cmd, 'hpc.lge.com', '-l', 'jaeyoung.choi', '-pw', '1111', '-b', 'test2.txt'],  shell=True) 
# stdin, stdout, stderr = subprocess.run(['echo', 'put', 'test11', '|', cmd, 'hpc.lge.com', '-l', 'jaeyoung.choi', '-pw', '1111'],  shell=True) 

# proc = subprocess.run(['echo', 'lpwd', '|', cmd, 'hpc.lge.com', '-l', 'jaeyoung.choi', '-pw', '1111'],  shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) 
# proc = subprocess.Popen([cmd, 'hpc.lge.com', '-l', 'jaeyoung.choi', '-pw', '1111'],  shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) 
proc = subprocess.Popen(['echo', 'lpwd', '|', cmd, 'hpc.lge.com', '-l', 'jaeyoung.choi', '-pw', '1111'], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf8') 



out = proc.stdout.readlines()
data = [line.rstrip('\n') for line in out]  
print(out, end='')

stdout, stderr = proc.communicate()
print(stdout)

# print(stdout)
print(proc.stdout.read())
print(proc.stdout.read().decode().splitlines(True))
proc.stdin.write('put OUTGOING.ICO\n')

print('dd')
# subprocess.run(['put', 'test1.spec'],  shell=True) 