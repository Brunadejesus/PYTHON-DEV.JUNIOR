import os
import time


with open('host.txt') as file: 
    dump = file.read()
    dump=dump.splitlines()

    for ip in dump:
        print("*" * 60)
        print('Verificando o IP: ' , ip)
        print("*" * 60)
        os.system(' ping -n 2 {}' .format (ip))
    
print("*" * 60)
time.sleep(5)
