from main import user
file = open(user+'.txt','r+')
import os
def cls():
    os.system("clear")
cls()
for linha in file:
  valores = linha.split(',')
  vars()[valores[1].replace('\n','')]= int(valores[0])


file.close()


