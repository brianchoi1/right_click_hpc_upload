import time, paramiko, sys
import subprocess, os
from win10toast import ToastNotifier

toaster = ToastNotifier()
ssh = paramiko.SSHClient()           
default_cmd = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; aspera '                                              
# default_cmd = '. /etc/profile; aspera '                                              
# hpc_path_default = '/nas/users/AC'         #에어솔루션
hpc_path_default = '/nas/users/HA'       #에어솔루션 제외하고                
data = open('hpc_id_pw_check').readlines()  
data = [line.rstrip('\n') for line in data]   
ip1 = 'cwhpc.lge.com'
# id = str(data[0])                                          
# pw = str(data[1])   
id = 'jaeyoung.choi'                                   
pw = '1111'

def aspera_():
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    login_validation = ssh.connect(ip1, 22, id, pw)  
    dd = default_cmd + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas' + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas'
    # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/' + fnl)       # scratch 폴더 미적용
    # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/scratch/' + 'upload_cmd1652690597.574724' + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + 'upload_cmd1652690597.574724')      # scratch 폴더 적용
    # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/scratch/' + 'fort.13' + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + 'fort.13')      # scratch 폴더 적용
    stdin, stdout, stderr = ssh.exec_command(dd)      # scratch 폴더 적용
    # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + fnl)      # 냉장고 송세암선임 폴더 적용
    ddd = stdout.readlines()
    exit_status = stdout.channel.recv_exit_status()
    time.sleep(1)
    ssh.close()

aspera_()