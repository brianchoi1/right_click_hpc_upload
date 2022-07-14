import time, paramiko, sys
import subprocess, os
from win10toast import ToastNotifier

if len(sys.argv) == 1:
    import winreg_test
    # import hpc_login
    winreg_test
    # hpc_login

else:
    main_dir = str(sys.argv[0])[:-22]
    server_ = str(sys.argv[-1])

    xx = sys.argv[1].split('\\')
    del xx[-1]
    ex_filepath = '\\'.join(xx)
    ex_filepath = ex_filepath + '\\__temp'

    fname_list = []
    file_list = []

    # for v in range(1, len(sys.argv)-1):
    #     file_list.append(str(sys.argv[v]))

    # for fitem in file_list:
    #     fname_list.append(fitem.split('\\')[-1])

    toaster = ToastNotifier()
    ssh = paramiko.SSHClient()           
    default_cmd = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; aspera '                                              
    # hpc_path_default = '/nas/users/AC'         #에어솔루션
    hpc_path_default = '/nas/users/HA'       #에어솔루션 제외하고                
    data = open(main_dir + 'hpc_id_pw_check').readlines()  
    data = [line.rstrip('\n') for line in data]   
    ip1 = 'cwhpc.lge.com'
    id = str(data[0])                                          
    pw = str(data[1])                                          

    def uploading_func():
        fname = str(time.time())
        t = open(main_dir + 'upload_cmd' + fname, 'w', encoding='utf-8')
        t.write('lcd ' + ex_filepath + '\n')
        # t.write('cd scratch\n')  # scratch 폴더 적용
        t.close()
        t = open(main_dir + 'upload_cmd' + fname, 'a', encoding='utf-8')
        # for fl in file_list:
        #     t.write('put ' + fl + '\n')
        t.close()
        cmd = resource_path("psftp.exe")
        subprocess.run([cmd, ip1, '-l', id, '-pw', pw, '-b', main_dir + 'upload_cmd' + fname],  shell=True) 

    def resource_path(relative):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative)
        else:
            return os.path.join(os.path.abspath("."), relative)

    def aspera_():
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        login_validation = ssh.connect(ip1, 22, id, pw)  
        # for fnl in fname_list:
        #     # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/' + fnl)       # scratch 폴더 미적용
        #     # stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/scratch/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + fnl)      # scratch 폴더 적용
        #     stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + fnl)      # 냉장고 송세암선임 폴더 적용
        #     exit_status = stdout.channel.recv_exit_status()
        #     time.sleep(1)
        ssh.close()
    
    def job_alarm():
        icon = resource_path("OUTGOING.ICO")
        # for fnl in fname_list:
        #     toaster.show_toast('HPC file upload alarm', fnl + ' is uploaded on HPC (/Home/)', icon_path = icon, duration = 1, threaded = True)       # scratch 폴더 미적용
        #     # toaster.show_toast('HPC file upload alarm', fnl + ' is uploaded on HPC (/Scratch/)', icon_path = icon, duration = 5, threaded = True)       # scratch 폴더 적용
        #     toaster.notification_active()
            
    
    # def createFolder(directory):
        # try:
        #     if not os.path.exists(directory):
        #         os.makedirs(directory)
        # except OSError:
        #     return
            
    if server_ == 'CW':
        # createFolder(ex_filepath)
        uploading_func()
        job_alarm()
    else:
        # createFolder(ex_filepath)
        uploading_func()
        aspera_()
        job_alarm()