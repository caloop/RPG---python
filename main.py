- from time import sleep
import os
import mundo_1

def linha():
   print("\033[1;90m===\033[m" * 20)
def espaço():
   print(' ')
def cls():
    os.system("clear")

n_registrado = 0
linha()
registro = input('\033[1mSeja bem vindo a Waterfall Kingdom .....\n\n'
'Ja possui Registro? (s/n)  ')
linha()
espaço()

if registro == 'n':
  while n_registrado == 0 :
    cls()
    print(' ')
    nome = input("Qual seu nome: ")
    user = input(f"Ola {nome} digite seu user: ")
    senha = input("Digite uma senha: ")
    with open('login.txt', "r") as loginfile:
      if (user + "," + senha + "\n") in loginfile.readlines():
        cls()
        print('\033[1;91mEsse usuario ja existe.\033[m')
        sleep(2)
        cls()
      else:
        cls()
        print ("Sua conta foi criada com sucesso.")
        espaço()
        print('Entrando no jogo...')
        file = open('login.txt',"a")
        file.write (user)
        file.write (",")
        file.write (senha)
        file.write("\n")
        file.close()
        file = open(user+'.txt', 'a')
        file.write(f'{0}'+',carnes\n')
        file.write(f'{0}'+',pedra\n')
        file.write(f'{0}'+',ouro\n')
        file.write(f'{0}'+',diamante\n')
        file.write(f'{0}'+',ruby\n')
        file.write(f'{0}'+',chifre\n')
        file.write(f'{0}'+',perola\n')
        file.write(f'{0}'+',olho_de_zumbi\n')
        file.write(f'{0}'+',life_potion\n')
        file.write(f'{0}'+',peixe_p\n')
        file.write(f'{0}'+ ',peixe_m\n')
        file.write(f'{0}' +',peixe_g\n')
        file.write(f'{0}' +',xp\n')
        file.write(f'{0}' +',cofre\n')
        file.write(f'{100}' +',vida1\n')
        file.write(f'{10}' +',dano\n')
        file.write(f'{0}' +',armadura\n')
        file.write(f'{0}' +',picareta\n')
        file.write(f'{1}' +',medicina\n')
        file.write(f'{0}' +',maça_dourada\n')
        file.write(f'{100}' +',vida\n')
        file.write(f'{1000}' +',xpl\n')
        file.write(f'{0}' +',maça\n')
        file.write(f'{1}' +',mundo')
        file.write(f'{0}' +',epic_perola')
        file.write(f'{0}' +',hyper_perola')
        file.write(f'{0}' +',epic_chifre')
        file.write(f'{0}' +',hyper_chifre')
        file.close()
        sleep(2)
        cls()
        n_registrado = 1
        mundo = 1
        import mundo_1
else:
  cls()
  print(' ')
  while n_registrado == 0 : 
    linha()
    user = input("Insira seu user: ")
    senha = input('Digite sua senha: ')
    linha()
    with open('login.txt', "r") as loginfile:
      if (user + "," + senha + "\n") in loginfile.readlines():
        espaço()
        print(f'Seja bem vindo novamente, {user}')
        sleep(0.5)
        cls()
        n_registrado = 1
        import mundo_1
      else: 
        cls()
        print('\033[1;91mUsuario ou senha invalidos.\033[m')
        sleep(2)
        cls()