from winreg import *

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