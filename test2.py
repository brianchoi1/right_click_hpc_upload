from winreg import *
import os

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
