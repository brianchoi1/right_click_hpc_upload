import time, paramiko, sys

if len(sys.argv) == 1:
    import winreg_test
    import hpc_login
    winreg_test
    hpc_login

    ff = open('ttt.txt', 'a', encoding='utf-8')
    for v in range(0, len(sys.argv)): 
        ff.write(str(sys.argv[v])+'\n')
        ff.write(str(len(sys.argv)) +'\n')
    ff.close()

else:
    ff = open('ttt.txt', 'a', encoding='utf-8')
    for v in range(0, len(sys.argv)): 
        ff.write(str(sys.argv[v])+'\n')
        ff.write(str(len(sys.argv)) +'\n')
    ff.close()

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
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        login_validation = ssh.connect(ip1, 22, id, pw)  
        for fl, fnl in zip(file_list[:], fname_list[:]):
            sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
            time.sleep(1)
            sftp.put(fl, hpc_path_default + '/' + id + '/scratch/' + fnl)
        ssh.close()

    def aspera_():
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        login_validation = ssh.connect(ip1, 22, id, pw)  
        for fl, fnl in zip(file_list[:], fname_list[:]):
            stdin, stdout, stderr = ssh.exec_command(default_cmd + hpc_path_default + '/' + id + '/scratch/' + fnl + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + fnl)
            exit_status = stdout.channel.recv_exit_status()
            time.sleep(1)
        ssh.close()

    if server_ == 'CW':
        uploading_func()
    else:
        uploading_func()
        aspera_()