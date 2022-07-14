import time, paramiko, sys
import subprocess, os

if len(sys.argv) == 1:
    import winreg_test
    import hpc_login
    winreg_test
    hpc_login

else:
    main_dir = str(sys.argv[0])[:-22]
    server_ = str(sys.argv[-1])
    fname_list = []
    file_list = []

    for v in range(1, len(sys.argv)-1):
        file_list.append(str(sys.argv[v]))

    for fitem in file_list:
        fname_list.append(fitem.split('\\')[-1])

    ssh = paramiko.SSHClient()           
    default_cmd = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; aspera '                                              
    hpc_path_default = '/nas/users/HA'                         
    data = open(main_dir + 'hpc_id_pw_check').readlines()  
    data = [line.rstrip('\n') for line in data]   
    ip1 = 'cwhpc.lge.com'
    id = str(data[0])                                          
    pw = str(data[1])                                          

    def uploading_func():
        fname = str(time.time())
        t = open(main_dir + 'upload_cmd' + fname, 'w', encoding='utf-8')
        t.write('cd scratch\n')
        t.close()
        t = open(main_dir + 'upload_cmd' + fname, 'a', encoding='utf-8')
        for fl in file_list:
            t.write('put ' + fl + '\n')
        t.close()
        cmd = resource_path("D:\\workothers\\right_click_menu_hpc_upload\\psftp.exe")
        subprocess.run([cmd, ip1, '-l', id, '-pw', pw, '-b', main_dir + 'upload_cmd' +fname],  shell=True) 

    def resource_path(relative):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative)
        else:
            return os.path.join(os.path.abspath("."), relative)

    def aspera_():
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        login_validation = ssh.connect(ip1, 22, id, pw)  
        for fnl in fname_list:
            stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/scratch/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + fnl)
            exit_status = stdout.channel.recv_exit_status()
            time.sleep(1)
        ssh.close()
    
    def job_alarm():
        for fl in file_list:
            t = open('upload_finished_' + fl, 'w')
            t.close()

    if server_ == 'CW':
        uploading_func()
        job_alarm()
    else:
        uploading_func()
        aspera_()
        job_alarm()