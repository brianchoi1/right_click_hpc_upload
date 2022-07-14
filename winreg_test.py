from winreg import *
import os

cdir = os.getcwd()
main_name = 'hpc_file_upload_v4'
try:
    path1 = 'SOFTWARE\SimonTatham\PuTTY'
    CreateKey(HKEY_CURRENT_USER, path1)
    path2 = path1 + '\SshHostKeys'
    CreateKey(HKEY_CURRENT_USER, path2)
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path2, 0, KEY_WRITE)
    data = '0x2d41b704856d1b4225f154d3a9554110d33ccd850c604f905990a4051715757c,0x1303ccc4236f7a4ce4d8d05c26b5ec394bcee2241432c577523d40b818fe9280'
    try:
        SetValueEx(key, 'ssh-ed25519@22:cwhpc.lge.com' , 0, REG_SZ, data)
    except EnvironmentError:
        print('error occur')
    CloseKey(key)
    CloseKey(reg_handle)

    path1 = '*\shell\HPC파일전송 >> 창원'
    CreateKey(HKEY_CLASSES_ROOT, path1)
    path2 = path1 + '\command'
    CreateKey(HKEY_CLASSES_ROOT, path2)
    reg_handle = ConnectRegistry(None, HKEY_CLASSES_ROOT)
    key = OpenKey(reg_handle, path2, 0, KEY_WRITE)
    data = cdir + '\\' + main_name + ' "%1" "CW"'
    try:
        SetValueEx(key, None , 0, REG_SZ, data)
    except EnvironmentError:
        print('error occur')
    CloseKey(key)
    CloseKey(reg_handle)

    path1 = '*\shell\HPC파일전송 >> 평택'
    CreateKey(HKEY_CLASSES_ROOT, path1)
    path2 = path1 + '\command'
    CreateKey(HKEY_CLASSES_ROOT, path2)
    reg_handle = ConnectRegistry(None, HKEY_CLASSES_ROOT)
    key = OpenKey(reg_handle, path2, 0, KEY_WRITE)
    data = cdir + '\\' + main_name + ' "%1" "PT"'
    try:
        SetValueEx(key, None , 0, REG_SZ, data)
    except EnvironmentError:
        print('error occur')
    CloseKey(key)
    CloseKey(reg_handle)

    path1 = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer'
    reg_handle = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg_handle, path1, 0, KEY_WRITE)
    data = 100
    try:
        SetValueEx(key, 'MultipleInvokePromptMinimum' , 0, REG_DWORD, data)
    except EnvironmentError:
        print('error occur')
    CloseKey(key)
    CloseKey(reg_handle)

    f = open('regi_check', 'w', encoding='utf-8')
    f.write('1')
    f.close()
except:
    f = open('regi_check', 'w', encoding='utf-8')
    f.write('0')
    f.close()
    exit()