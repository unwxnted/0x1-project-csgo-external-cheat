import random

def junkcode():
    with open('main.py', 'a') as f:
        for i in range(1, 20):
            v = str(random.randrange(1,1337))
            f.writelines('\n')
            f.writelines('    j' + v +'='+ str(random.random()))
            f.writelines('\n')
            f.writelines('    print(j'+v+')')
            f.writelines('\n')
        
