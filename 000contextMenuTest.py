import sys, time

main_dir = str(sys.argv[0])[:-22]
file_list = []

for v in range(1, len(sys.argv)-1):
    file_list.append(str(sys.argv[v]))

fname = str(time.time())
t = open(main_dir + fname, 'w', encoding='utf-8')
t.write('cd scratch\n')
t.close()
t = open(main_dir + fname, 'a', encoding='utf-8')
for fl in file_list:
    t.write('put ' + fl + '\n')
t.close()
time.sleep(50)