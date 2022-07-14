path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
del x[-1]
filename = '\\'.join(x)
print(filename)