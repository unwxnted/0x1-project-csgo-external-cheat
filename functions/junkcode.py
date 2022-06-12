import random

def junkcode():
    with open('main.py', 'a') as f:
        for i in range(1, 20):
            f.writelines('\n')
            f.writelines('vac' + str(random.randrange(1,1337)) +'='+ str(random.random()))
            f.writelines('\n')
            