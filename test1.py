
# import sys 
# var_len = len(sys.argv)
# if var_len == 1:
#     f = open('ttt.txt', 'a', encoding='utf-8')
#     for v in range(0, len(sys.argv)): 
#         f.write(str(sys.argv[v])+'\n')
#         f.write(str(var_len) +'\n')
#     f.close()
# else:
#     f = open('qqq.txt', 'a', encoding='utf-8')
#     for v in range(0, len(sys.argv)): 
#         f.write(str(sys.argv[v])+'\n')
#         f.write(str(var_len) +'\n')
#     f.close()

# import hpc_login
# hpc_login
# print('ddd')

# ss = [1,2,3]
# hpc_uploading(ss)

# dd = 'D:\workothers\right_click_menu_hpc_upload\dist\hpc_file_upload_v1.exe'
# print(dd[:-22])

import sys, time
file_list = []

for v in range(1, len(sys.argv)-1):
    file_list.append(str(sys.argv[v]))

def uploading_func():
    t = open('upload_cmd', 'w', encoding='utf-8')
    t.write('cd scratch\n')
    t.close()
    time.sleep(1)
    t = open('upload_cmd', 'a', encoding='utf-8')
    for fl in file_list:
        t.write('put ' + fl + '\n')
        time.sleep(1)
    t.close()

uploading_func()