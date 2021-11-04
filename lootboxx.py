from random import sample 
from save import save
from main_carregar import xp , cofre, vida, vida1, dano, armadura,carnes,life_potion ,diamante ,ouro ,pedra,perola ,chifre ,peixe_p,peixe_m,peixe_g,picareta,maça_dourada,medicina,olho_de_zumbi, ruby,xpl,maça,epic_perola,hyper_perola,epic_chifre,hyper_chifre 

def inventario(x,item):
        if x > 0 :
          print('╏ {}× {}'.format(x,item))


def lootbox(x):

  if x == 1:
    lista = []
    lista_drops = []

    lista = sample(range(0,15),2)
    lista2= sample(range(0,6),5)
    pedra += lista[0]
    ouro += lista[1]
    diamante += lista2[0]
    ruby += lista2[1]
    chifre += lista2 [2]
    perola += lista2[3]
    olho_de_zumbi += lista2[4]

    inventario(lista[0],'Pedra')
    inventario(lista[1],'Ouro')
    inventario(lista2[0],'Diamante')
    inventario(lista2[1],'Ruby')
    inventario(lista2[2],'Chifre')
    inventario(lista2[3],'Perola')
    inventario(lista2[4],'Olho de Zumbi')

  else:
    lista = []
    lista_drops = []

    lista = sample(range(0,20),2)
    lista2= sample(range(0,6),5)
    lista3 = sample(range(0,3),2)
    lista4 = sample(range(0,2),2)
    pedra += lista[0]
    ouro += lista[1]
    diamante += lista2[0]
    ruby += lista2[1]
    chifre += lista2 [2]
    perola += lista2[3]
    olho_de_zumbi += lista2[4]
    epic_chifre += lista3[0]
    epic_perola += lista3[1]
    hyper_chifre += lista4[0]
    hyper_perola += lista4[1]

    inventario(lista[0],'Pedra')
    inventario(lista[1],'Ouro')
    inventario(lista2[0],'Diamante')
    inventario(lista2[1],'Ruby')
    inventario(lista2[2],'Chifre')
    inventario(lista2[3],'Perola')
    inventario(lista2[4],'Olho de Zumbi')
    inventario(lista3[0],'Epic Chifre')
    inventario(lista3[1],'Epic Perola')
    inventario(lista4[0],'Hyper Chifre')
    inventario(lista4[1],'Hyper Perola')
  save()
