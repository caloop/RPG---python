from random import randint
from time import sleep
import os
import time
from main import user
from random import sample

def life():
  vd = vida1 - 100
  if vida == 100 + vd :
    print('⟦\033[1;92m∎∎∎∎∎∎∎∎∎∎\033[m⟧')
  elif 90 <=  vida < 100 + vd :
    print('⟦\033[1;92m∎∎∎∎∎∎∎∎∎ \033[m⟧')
  elif 80 <= vida < 90 + vd :
    print('⟦\033[1;92m∎∎∎∎∎∎∎∎   \033[m⟧')
  elif 70 <= vida < 80 + vd :
    print('⟦\033[1;93m∎∎∎∎∎∎∎    \033[m⟧')
  elif 60 <= vida < 70 +vd :
    print('⟦\033[1;93m∎∎∎∎∎∎     \033[m⟧')
  elif 50 <= vida < 60 +vd:
    print('⟦\033[1;93m∎∎∎∎∎      \033[m⟧')
  elif 40 <= vida < 50 +vd:
    print('⟦\033[1;93m∎∎∎∎       \033[m⟧')
  elif 30 <= vida < 40 +vd:
    print('⟦\033[1;91m∎∎∎        \033[m⟧')
  elif 20 <= vida < 30 +vd:
    print('⟦\033[1;91m∎∎         \033[m⟧')
  elif 10 <= vida < 20 +vd:
    print('⟦\033[1;91m∎          \033[m⟧')
  elif 0 <= vida < 10 +vd:
    print('⟦\033[1;92m           \033[m⟧')

def save():
  file = open(user+'.txt','w+') 
  file.write(f'{carnes}'+',carnes\n')
  file.write(f'{pedra}'+',pedra\n')
  file.write(f'{ouro}'+',ouro\n')
  file.write(f'{diamante}'+',diamante\n')
  file.write(f'{ruby}'+',ruby\n')
  file.write(f'{chifre}'+',chifre\n')
  file.write(f'{perola}'+',perola\n')
  file.write(f'{olho_de_zumbi}'+',olho_de_zumbi\n')
  file.write(f'{life_potion}'+',life_potion\n')
  file.write(f'{peixe_p}'+',peixe_p\n')
  file.write(f'{peixe_m}'+ ',peixe_m\n')
  file.write(f'{peixe_g}' +',peixe_g\n')
  file.write(f'{xp}' +',xp\n')
  file.write(f'{cofre}' +',cofre\n')
  file.write(f'{vida1}' +',vida1\n')
  file.write(f'{dano}' +',dano\n')
  file.write(f'{armadura}' +',armadura\n')
  file.write(f'{picareta}' +',picareta\n')
  file.write(f'{medicina}' +',medicina\n')
  file.write(f'{maça_dourada}' +',maça_dourada\n')
  file.write(f'{vida}' +',vida\n')
  file.write(f'{xpl}' +',xpl\n')
  file.write(f'{maça}' +',maça\n')
  file.write(f'{mundo}' +',mundo\n')
  file.write(f'{epic_perola}' +',epic_perola\n')
  file.write(f'{hyper_perola}' +',hyper_perola\n')
  file.write(f'{epic_chifre}' +',epic_chifre\n')
  file.write(f'{hyper_chifre}' +',hyper_chifre')
  file.close()

def cls():

    os.system("clear")

def linha():
   print("\033[1;90m===\033[m" * 20)
def espaço():
   print(' ')
def div():
  print(' '*6+'─'*40)
def jogada_invalida():
  linha()
  print ('\033[1;31m Jogada Invalida \033[m')
  linha()
  espaço()
  jogador = input('Qual sua escolha : ')
  save()
  cls()



#JOGADOR
xp = 0
xpl = 1000
cofre = 0
vida1 = 100
vida = vida1
dano = 10
armadura = 0
if vida <= 0:
    print('Você Morreu')

#LIFE
carnes = 0  
life_potion = 0

#COLETAVEIS
diamante = 0
ouro = 0
pedra = 0
madeira = 0
ruby = 0
peixe_p = 0
peixe_m = 0
peixe_g = 0

#DROPS
perola = 0
epic_perola = 0
hyper_perola = 0
chifre = 0
epic_chifre = 0
hyper_chifre = 0
maça = 0
olho_de_zumbi = 0

#HABILIDADES
picareta = 0
medicina = 0
maça_dourada = 0


first_time_h = 0
second_time_h = 0
first_time_m = 0
first_time_p = 0

from main_carregar import xp , cofre, vida, vida1, dano, armadura,carnes,life_potion ,diamante ,ouro ,pedra,perola ,chifre ,peixe_p,peixe_m,peixe_g,picareta,maça_dourada,medicina,olho_de_zumbi, ruby,xpl,maça,epic_perola,hyper_perola,epic_chifre,hyper_chifre, mundo

if mundo == 2 :
  import mundo_2
mundo = 1

linha()
print(f'\033[1mOla {user}, seja bem-vindo a Waterfall Kingdom .....\n\n' 
'Você se encontra em um mundo medieval, perdido em uma pequena vila\nsobreviva e evolua juntando itens e matandos chefes de cada area.\n\n\033[1;90mPara ver os comandos disponiveis digite [help]\033[0;0m')
linha()
espaço()

#INICIO DO PROGRAMA
jogador = input('Qual sua escolha :\033[;1m ')
cls()



while mundo == 1 :
    save()

    if xp >= xpl :
        vida1 += 20
        espaço()
        linha()
        print ('\033[1;95mVocê subiu de nivel!!! \n\n+20 vida total \n+2 dano \n+1 armadura')
        dano += 2
        armadura += 1
        linha()
        espaço()
        xpl = xpl*2 - 800
        xp = 0
#POSSIBILIDADES    
    caça_carnes = (1, 3, 5)
    caça_dano = (15, 20, 30)
    moedas = (1, 5, 7,9,11)
    caça_xp = (10,12,15,18,21)

#DADOS    
    dado_carnes = randint(0, 2)
    dado_dano_caça = randint(0, 2)
    dado_moedas = randint (0,4)
    dado_drops = randint (0,100)
    dado_drop_item = randint(0, 2)
    dado_xp = randint (0,4)
    dado_boss = randint (0,200)
    dado_minerar = randint(0, 100)

    drop = ('Perola','Chifre','Olho de zumbi')
    mineracao = ('Pedra comum', 'Ouro', 'Diamante')
    monstros = ('Javali', 'Fada pequena','Troll')
#FUNÇOES
    def luta_boss(x):
      if (dano_boss) < 1 :
        print ('Você deu \033[1;94m{}\033[m de dano'.format(dano*x))
        print('\033[1;37mdesviou!\033[m')
      else: 
        print ('Você deu \033[1;94m{}\033[m de dano'.format(dano*x))
        print ('\033[1;31m-{}\033[m de vida'.format((dano_boss)))
        if vida > 0 :   
          print('Vida')
          life()
          
        else :
          print('Sua vida esta em \033[;1m0\033[m')


    def quantidade_(x) :
          return x < quantidade         
    def loja_(x) :
          return quantidade * x
    def venda(x):
          x - quantidade

#EVENTOS
  #1 - BOSS
  #2 - 69
    if jogador ==  'd' :

       espaço()
       linha()
       b = 'vivo'
       boss = 400
       div()
       print('             \033[1;35m✠ VOCÊ INICIOU A DUNGEON!✠\033[m')
       espaço()
       print('A entrada esta logo a frente, algo pode estar te esperando nessa dungeon')
       espaço()
       sleep(4)
       print(f'... uma sombra enorme surge...')
       espaço()
       sleep(2)
       print('É UM OGRO!!') 
       espaço()
       sleep(2)
       print('Para passar dessa area você devera matar o ogro que guarda a passagem')
       while b == 'vivo' :

            dado_boss2 = randint (0,10)
            dado_boss3 = (0,10, 20, 30 ,40)
            dado_boss_dano = randint (0,4)
            dado_fuga = randint (0,10)
            dano_boss = dado_boss3[dado_boss_dano] - armadura

            if dano_boss < 0 :
              dano_boss = dano_boss *-1
            linha()
            espaço()
            jogada_boss = input('Atacar ou fugir? (a)/(f): ')
            if vida <= 0:
                linha()
                print('Não foi desta vez, você perdeu a batalha..\n(sua vida esta em 1)')
                vida = 1
                boss = 400
                linha()
                break

            if jogada_boss == 'a':
              cls()
              espaço()
              linha()
              if dado_boss2 < 5 :
                boss -= dano*1
                vida -= (dano_boss)
                luta_boss(1)
                
              elif 5 <= dado_boss2 <= 8 :
                boss -= dano*2
                vida -= (dano_boss)
                luta_boss(2)
                
              elif  dado_boss2 == 9  :
                boss -= dano*3
                vida -= (dano_boss)
                print('\033[1;95mBelo Golpe\033[m')
                luta_boss(3)
                
              elif  dado_boss2 == 10 :
                boss -= dano*4
                vida -= (dano_boss)
                print('\033[1;33m GOLPE CRITICO\033[m')
                luta_boss(4)
            elif jogada_boss == 'f':
              cls()
              if dado_fuga < 8 :
                espaço()
                print ('....Você correu para bem longe do ogro, boa sorte da proxima vez.... ') 
                boss = 400
                break
                espaço()
                jogador = input('Qual sua escolha : ')
                save()
                cls()
              else : 
                espaço()
                print('...Você foi correr desesperado e acabou tropeçando e deixando todos seus itens para traz....')
                espaço()
                boss = 400
                carnes = 0 
                cofre = 0 
                pedra = 0 
                ouro = 0 
                diamante = 0
                b = ' '
                jogador = input('Qual sua escolha : ')
                save()
                cls()
            else :
                linha()
                print ('\033[1;31m Jogada Invalida \033[m')
            if boss < 1 :
                  espaço()
                  linha()
                  b = ' '
                  print('VOCÊ DERROTOU O OGRO')
                  espaço()
                  sleep(2)
                  print('Você conseguiu liberar a passagem para a segunda area \nboa sorte na sua jornada aventureiro!')
                  espaço()
                  sleep (3)
                  print('Aqui estão suas recompensas')
                  cofre += 250      
                  carnes += 15
                  chifre += 3
                  perola += 3
                  diamante += 1 
                  print ('+250 moedas \n+15 carnes \n+3 chifres \n+3 perolas \n+1 diamante')
                  sleep(3)
                  cls()
                  mundo = 2
                  import mundo_2
      
       else :
          jogador = input('Qual sua escolha : ')
          save()
          cls()
    if jogador == '69':
      mundo = 2
      import mundo_2
      break

    elif jogador == 'h':
          if vida < 1:
                linha()
                print('Você Morreu amigo')
                xp = 0
                cofre = 0
                vida = vida1
                carnes = 0 
                life_potion = 0
                diamante = 0
                ouro = 0
                pedra = 0
                perola = 0
                chifre = 0
                peixe_p = 0
                peixe_m = 0
                peixe_g = 0
                linha()
                espaço()
                jogador = input('Deseja continuar? (s/n) : ')
                if jogador == 's':
                  cls()
                  vida = vida1
                  linha()
                  print('\033[1mSeja bem vindo a Waterfall Kingdom .....\n\n' 
                  'Você se encontra em um mundo medieval, perdido em uma pequena vila\nsobreviva e evolua juntando itens e matandos chefes de cada area.\n\n\033[1;90mPara ver os comandos disponiveis digite [help]\033[0;0m')
                  linha()
                  espaço()
                  
                else :
                  quit() 
          second_time_h = int(time.time())
          if second_time_h - first_time_h <= 20 :
            linha()
            print('Você ainda não pode caçar novamente')
            print(f'Ainda restam { ((second_time_h -first_time_h) - 20)*-1}s')
            linha()
            espaço()
            jogador = input('Qual sua escolha :\033[;1m ')
            cls()
          else :
            first_time_h = int(time.time())   
            linha()
            dano_tomado = caça_dano[dado_dano_caça]- armadura
            if caça_dano[dado_dano_caça]- armadura < 0:
              dano_tomado = 0
            vida = (vida - (dano_tomado))
            carnes = (carnes + caça_carnes[dado_carnes])
            cofre = (cofre + moedas[dado_moedas])
            xp = (xp + caça_xp[dado_xp])
            print('Você coletou {} carne(s) \n\033[1;93m+{}\033[m moedas''\n\033[1;34m+{}\033[m xp ''\n\033[1;31m-{}\033[m' ' de vida'.format(caça_carnes[dado_carnes], moedas[dado_moedas], caça_xp[dado_xp] ,dano_tomado))

            if dado_drops > 95 :
              if drop[dado_drop_item] == 'Perola':
                dado_drops_perola = randint(0,1)
                if dado_drops_perola == 0:
                  print ('Você matou uma Fada Obscura e coletou uma {}'.format(drop[dado_drop_item]))
                  perola += 1
                else: 
                  print ('Você matou uma Fada Obscura e coletou uma Epic Perola')
                  epic_perola += 1
              elif drop[dado_drop_item] == 'Chifre':
                dado_drops_chifre = randint(0,1)
                if dado_drops_chifre == 0:
                    print ('Você matou um Javali selvagem e coletou um {}'.format(drop[dado_drop_item]))
                    chifre += 1
                else:
                    print ('Você matou um Javali selvagem e coletou um Epic Chifre')
                    epic_chifre += 1
            if vida > 0 :
              espaço()
              print('    Vida')
              life()
              linha()
              jogador = input('Qual sua escolha : ')
              save()
              cls()
              save()
            else:
              espaço()
              print ('Sua vida esta em \033[;1m0\033[m')
            espaço()
        
    elif jogador == 'm':
        linha()
        second_time_m = int(time.time())
        if second_time_m - first_time_m <= 20 :
            print('Você ainda não pode minerar novamente')
            print(f'Ainda restam { ((second_time_m -first_time_m) - 20)*-1}s')
            linha()
            espaço()
        else :
          first_time_m = int(time.time())
          print ('Minerando...⸕')
          linha()
          espaço()
          if dado_minerar < 70:
              print('Você coletou uma {}x \033[1;37mPedra comum\033[m'.format(1+picareta))
              pedra += 1 + picareta
          elif 69 < dado_minerar < 95 :
              print('Você coletou {}x \033[1;33mOuro\033[m'.format(1+picareta))
              ouro += 1 + picareta
          else :
              print ('Você achou {}x \033[1;36mDIAMANTE\033[m'.format(1+picareta))
              diamante += 1 
          linha()
        jogador = input('Qual sua escolha : ')
        save()
        cls()
        espaço()
    
    elif jogador == 'c':
        linha()
        if vida >= vida1:
          vida = vida1
          espaço()
          linha()
        else : 
          cura = input('(1) Carne [\033[1;32m+5\033[m] \n(2) Life potion [\033[1;32m+FULL\033[m] \n(3) Peixe Pequeno [\033[1;32m+5\033[m] \n(4) Peixe Epico [\033[1;32m+15\033[m] \n(5) TAINHA[\033[1;32m+100\033[m] \n'
        '\n\n Sua escolha: ')
          if cura == '1' :
            quantidade_cura = int(input (' Quantidade : '))
            if carnes < quantidade_cura :
              linha()
              print ('\033[1;31m Material insuficiente \033[m')
              linha()
            else :
              cls()
              carnes -= quantidade_cura
              linha()
              print('Você restaurou \033[1;32m {} \033[m de vida'.format(5* quantidade_cura))     
              vida += 5* quantidade_cura
          elif cura == '2' :
            if life_potion < 1 :
              linha()
              print ('\033[1;31m Material insuficiente \033[m')
              linha()
            else :
              cls()
              life_potion -= 1
              linha()
              print('Você restaurou sua vida')
              vida = vida1
          elif cura == '3' :
            quantidade_cura = int(input (' Quantidade : '))
            if peixe_p < quantidade_cura :
              linha()
              print ('\033[1;31m Material insuficiente \033[m')
              linha()
            else :
              cls()
              peixe_p -= quantidade_cura
              linha()
              print('Você restaurou \033[1;32m {} \033[m de vida'.format(5* quantidade_cura))     
              vida += 5* quantidade_cura
          elif cura == '4' :
            quantidade_cura = int(input (' Quantidade : '))
            if peixe_m < quantidade_cura :
              linha()
              print ('\033[1;31m Material insuficiente \033[m')
              linha()
            else :
              cls()
              peixe_m -= quantidade_cura
              linha()
              print('Você restaurou \033[1;32m {} \033[m de vida'.format(15* quantidade_cura))     
              vida += 15* quantidade_cura
          if cura == '5' :
            quantidade_cura = int(input (' Quantidade : '))
            if peixe_g < quantidade_cura :
              linha()
              print ('\033[1;31m Material insuficiente \033[m')
              linha()
            else :
              cls()
              peixe_g -= quantidade_cura
              linha()
              print('Você restaurou \033[1;32m {} \033[m de vida'.format(100* quantidade_cura))     
              vida += 100* quantidade_cura
          else : 
              linha()
              jogada_invalida
              linha()
        if vida < vida1 :
          print('    Vida')
          life()
        else :
          vida = vida1
          print('    Vida')
          life()
        linha()
        jogador = input('Qual sua escolha : ')
        save()
        cls()
        espaço()

    elif jogador == 'i' :
      def inventario(x,item):
        if x > 0 :
          print('╏ {}× {}'.format(x,item))
      linha()
      div()
      print (' '*22+' \033[;1mPERFIL\033[m')
      print ('╏ ''Vida : {} de {}'.format(vida,vida1),' '*15, 'XP : {}'.format(xp))    
      print('╏ '+life())      
      print('╏ ''Armadura : {}'.format(armadura),' '*18,'Cofre : {} moedas'.format(cofre) )
      print('╏ ''Dano : {}'.format(dano))
      espaço()
      div()
      print (' '*20+' \033[;1mINVENTARIO\033[m')
      inventario(carnes,'carnes')
      inventario(pedra,'Pedra')
      inventario(ouro,'Ouro')
      inventario(diamante,'Diamante')
      inventario(ruby,'Ruby')
      inventario(chifre,'Chifre')
      inventario(perola,'Perola')
      inventario(epic_chifre,'Epic Chifre')
      inventario(epic_perola,'Epic Perola')
      inventario(olho_de_zumbi,'Olho de zumbi')
      inventario(life_potion,'Potions')
      inventario(peixe_p,'Peixe pequeno')
      inventario(peixe_m,'Peixe epico')
      inventario(peixe_g,'TAINHA')
      print(' '*24+'...')
      espaço()
      linha()
      jogador = input('Qual sua escolha : ')
      save()
      cls()
      espaço()

    elif jogador == 'l' :
        linha()
        print ( 'Seja bem vindo a loja \nAqui podemos comprar seus itens\n')
        linha()
        print('VENDER \n(1) Pedra comum [5 moedas]\n(2) Ouro [15 moedas] \n(3) Diamante [50 moedas] \n(4) Chifre [100 moedas]'
        '\n(5) Perola [100 moedas] \nCOMPRAR \n(6) Life Potion')
        linha()
        loja = input('Qual seu pedido?:  ')
        if loja == '0':
          espaço()
          linha()
          jogador = input('Qual sua escolha : ')
          save()
          cls()
        else: 
          quantidade = int(input('Quantidade:  '))
          linha()
          if loja == '1' :
            if quantidade_(pedra) :
              print('\033[1;31m Material insuficiente \033[m')
            else :
              cofre +=  loja_(5)
              pedra -= quantidade
              print ('Você recebeu \033[1;93m{}\033[m moedas'.format(loja_(5))) 
          elif loja == '2' :
            if quantidade_(ouro) :
              print('\033[1;31m Material insuficiente \033[m')
            else :
              cofre += loja_(15)
              ouro -= quantidade
              print('Você recebeu \033[1;93m{}\033[m moedas'.format(loja_(15)))
          elif loja == '3' :
            if quantidade_(diamante) :
              print('\033[1;31m Material insuficiente \033[m')
            else :
              cofre += loja_(50)
              diamante -= quantidade
              print('Você recebeu \033[1;93m{}\033[m moedas'.format(loja_(50)))
          elif loja == '4' :
            if chifre < quantidade :
              print('\033[1;31m Material insuficiente \033[m')
            else :
              cofre += loja_(100)
              chifre -= quantidade
              print('Você recebeu \033[1;93m{}\033[m moedas'.format(loja_(100)))
          elif loja == '5' :
            if perola < quantidade :
              print('\033[1;31m Material insuficiente \033[m')
            else :
              cofre += loja_(100)
              perola -= quantidade
              print('Você recebeu \033[1;93m{}\033[m moedas'.format(loja_(100)))
          elif loja == '6' :
            if cofre > 29 :
              cofre -= quantidade * 30
              life_potion += quantidade
              print('Você recebeu {} potions'.format(quantidade))
            else: 
              print('\033[1;31m Moedas insuficientes \033[m')
          else :
            jogada_invalida
          linha()
          jogador = input('Qual sua escolha : ')
          save()
          cls() 

    elif jogador == 'f' :
        linha()
        print ( 'Seja bem vindo a forja \n Aqui podemos fazer seus itens\n')
        linha()
        print ('(1) Armadura Comum \n(2) Espada de diamante\n(3) Armadura encantada  \n(4) Espada encantada\n(5) ??? [Bloqueado]\n(6) ??? [Bloqueado] \n(7) ??? [Bloqueado]')
        print ('')
        forjar = input('Qual gostaria de forjar?  ')
        espaço()
        if forjar == '1' :
          if ouro < 1 :
            linha()
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else :
            linha()
            print ('+5 Armadura')
            armadura += 5
            ouro -= 5
            linha()
        elif forjar == '3' :
          linha()
          if epic_perola < 1 or ouro < 5 :
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else :
            print ('+15 Armadura')
            armadura += 15
            ouro -=5 
            epic_perola -=1
            linha()
        elif forjar == '2' :
          linha()
          if diamante < 1 or  chifre < 1 :
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else:
            diamante -= 2
            chifre -= 1
            dano = 20
            print('\033[1mEspada forjada com sucesso\033[m')
            linha()
        elif forjar == '4' :
          linha()
          if diamante < 2 or  epic_chifre < 1 :
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else:
            diamante -= 2
            epic_chifre -= 1
            dano = 40
            print('\033[1mEspada forjada com sucesso\033[m')
            linha()
        espaço()
        jogador = input('Qual sua escolha : ')
        save()
        cls()

    elif jogador == 'cassino':
      novamente = 's'
      while novamente == 's':
        linha()
        print('\033[1;34mBEM VINDO AO CASSINO\033[m')
        linha()
        espaço()
        print('(1) Dados da sorte\n(2) Cara ou coroa\n(0) SAIR')
        espaço()
        cassino = input('Qual sua escolha : ')
        espaço()
        cls()
        if cassino == '1' :
          linha()
          print('Nesse jogo temos um dado de 6 lados.\nVocê deverá escolher um numero de 1 a 6.\nSuas chances são de 1 em 6 então os valores ganhos e descontados são equivalentes não se preocupe.\nBoa sorte! ')
          linha()
          espaço()
          aposta = input('Qual valor da sua aposta : ')
          chute = input('Qual seu chute? ')
          cls()
          if cofre < int(aposta):
            linha()
            espaço()
            print('\033[1;31mVocê não tem dinheiro suficiente para apostar.')
            espaço()
            linha()
            print('Obrigado volte sempre!')
            linha()
            espaço()
            jogador = input('Qual sua escolha : ')
            save()
            cls()
          dado_cassino = randint(1,6)
          espaço()
          print('Dado lancado...')
          espaço()
          sleep(1)
          print('\033[;1mO numero do dado é {}\033[m'.format(dado_cassino))
          print(f'Seu chute foi {chute}\nO valor apostado é \033[;1m{aposta}\033[m')
          espaço()
          if dado_cassino == int(chute):
            espaço()
            print(f'Você acertou o numero!!\n+{int(int(aposta)*5)} moedas')
            cofre += int(int(aposta)*5)
          else :
            print(f'Você errou.\n\033[1;91m-{int(int(aposta)/5)}\033[m moedas')
            cofre -= int(int(aposta)/5)
          espaço()
          novamente = input('Quer jogar novamente?(s/n) ')
          cls()
        elif cassino == '2':
          linha()
          print('Nesse jogo você tem 50% de chance de ganhar e perder\n\nEscolha cara ou coroa e faça sua aposta\n\nSe errar, perde tudo, se acertar seu dinheiro volta em dobro.\n\nBoa sorte não esqueça que você pode ficar negativo..')
          linha()
          espaço()
          aposta = int(input('Qual valor da sua aposta : '))
          espaço()
          cara_coroa = input('Vamos la..\n\nCara ou Coroa? ')
          espaço()
          dado_couc = randint (0,1)
          espaço()
          linha()
          if dado_couc == 0:
            if cara_coroa == 'cara':
              espaço()
              print('CARA\nVocê GANHOU!!\n+{} moedas'.format(aposta))
              cofre += aposta
            elif cara_coroa == 'coroa':
              espaço()
              print('CARA\nVocê perdeu\n-{} moedas'.format(aposta))
              cofre -= aposta
            else: 
              print('Não existe essa opção.. ')
              espaço()
          elif dado_couc == 1:
            if cara_coroa == 'cara':
              espaço()
              print('COROA\nVocê perdeu\n-{} moedas'.format(aposta))
              cofre -= aposta
            elif cara_coroa == 'coroa':
              espaço()
              print('COROA\nVocê GANHOU!!\n+{} moedas'.format(aposta))
              cofre+= aposta
            else: 
              espaço()
              print('Não existe essa opção.. ')
              espaço()
          espaço()
          novamente = input('Quer jogar novamente?(sim/não) ')
          cls()

    elif jogador == 'p' :
      second_time_p = int(time.time())
      if second_time_p - first_time_p <= 20 :
            linha()
            print('Você ainda não pode pescar novamente')
            print(f'Ainda restam { ((second_time_p -first_time_p) - 20)*-1}s')
            linha()
            espaço()
            jogador = input('Qual sua escolha :\033[;1m ')
            cls()
      else :
          first_time_p = int(time.time())
          linha()
          print('Pescando...')
          linha()
          dado_pesca = randint (0,100)
          dado_drop_pesca = randint(0,2)
          espaço()
          linha()
          if dado_pesca < 71 :
            print('Pescou 1x \033[;1mPeixe pequeno')
            peixe_p += 1
          elif 71 <= dado_pesca < 95 :
            print('Pescou 1x \033[1;95mPeixe epico')
            peixe_m += 1
          elif 95 <= dado_pesca < 99 :
            print('Pescou 1x \033[1;33mBIG TAINHA') 
            peixe_g += 1   
          elif dado_pesca >= 99 :
            if dado_drop_pesca == 0 :
              print('Você encontrou uma \033[;1mArmadura antiga\033[m boiando no lago \n+5 Armadura')
              armadura += 5

            elif dado_drop_pesca == 1 :
              print('Você encontrou um \033[;1msaco de moedas\033[m boiando no lago \n\033[1;93m+175\033[m moedas')
              cofre += 175

            elif dado_drop_pesca == 2 :
              print('Você pescou o \033[1;34mPEIXE SAFIRA')
          linha()
          espaço()
          jogador = input('Qual sua escolha : ')
          save()
          cls()

    elif jogador == 'receitas':
      linha()
      print (' '*25,'\033[1;93mReceitas\033[m')
      linha()
      espaço()
      print('Armadura Comum [5x Ouros]\nEspada de diamante [1x Diamante e 1x Chifre] \n\nArmadura encantada [5x Ouros e 1x Epic Perola]\nEspada Encantada [2x Diamantes e 1x Epic Chifre] \n\nArmadura do Gladiador [8x Diamantes, 5x Ouros e 2x Epic Perola] \nEspada do Gladiador [3x Rubys e 3x Epic Chifre]\n\nTotem [1x Ruby , 3x Ouros e 1x Olho de zumbi]\n\nMaça Dourada [1x Maça especial e 10x Ouros]')
      espaço()

      jogador = input('Qual sua escolha : ')
      save()
      cls()
    
    elif jogador == 'fundir':
      def materiais(x):
          if x < 10*int(quantidade) :
            linha()
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
      def materiais1(x):
          if x < 5*int(quantidade) :
            linha()
            print ('\033[1;31m Material insuficiente \033[m')
            linha()

      linha()
      print (' '*25,'\033[1;93mFUNDIÇÃO\033[m')
      linha()
      espaço()
      print('10x Pedra    ➜ 1x Ouro\n10x Ouro     ➜ 1x Diamante\n10x Diamante ➜ 1x Ruby\n\n5x chifres     ➜ 1x \033[1;95mEpic Chifre\033[m\n5x \033[1;95mEpic Chifre\033[m ➜ 1x \033[1;33mHyper Chifre\033[m\n\n5x Perola      ➜ 1x \033[1;95mEpic Perola\033[m\n5x \033[1;95mEpic Perola\033[m ➜ 1x \033[1;33mHyper Perola\033[m\n')
      fundir = input('\033[;1mColoque o item que deseja fazer: \033[m')
      quantidade = input('Quantidade: ')
      if fundir.lower() == 'ouro':
        materiais(pedra)
        if pedra >= 10*int(quantidade) :
          pedra -= 10
          ouro += 1
          espaço()
          print (f'Você fez {quantidade}x \033[1;93mOuro\033[1m')
          linha()
          espaço()
      elif fundir.lower() == 'diamante':
        materiais(ouro)
        if ouro >= 10*int(quantidade) :
          ouro -= 10
          diamante += 1
          espaço()
          print (f'Você fez {quantidade}x \033[1;96mDiamante\033[1m')
          linha()
          espaço()
      elif fundir.lower() == 'ruby':
        materiais(diamante)
        if diamante >= 10*int(quantidade) :
          diamante -= 10
          ruby += 1
          espaço()
          print (f'Você fez {quantidade}x \033[1;91mruby\033[1m')
          linha()
          espaço()
      elif fundir.lower() == 'epic perola':
        materiais1(perola)
        if perola >= 5*int(quantidade) :
          perola -= 5
          epic_perola += 1
          espaço()
          print (f'Você fez {quantidade}x \033[1;94mEpic Perola\033[1m')
          linha()
          espaço()
      elif fundir.lower() == 'hyper perola':
        materiais1(epic_perola)
        if epic_perola >= 5*int(quantidade) :
          epic_perola -= 5
          hyper_perola += 1
          espaço()
          print (f'Você fez {quantidade}x \033[1;94mHyper Perola\033[1m')
          linha()
          espaço()
      elif fundir.lower() == 'epic chifre':
        materiais1(chifre)
        if chifre >= 5*int(quantidade) :
          chifre -= 5
          epic_chifre += 1
          espaço()
          print (f'Você fez {quantidade}x \033[1;94mEpic Chifre\033[1m')
          linha()
          espaço()
      elif fundir.lower() == 'hyper chifre':
        materiais1(epic_chifre)
        if epic_chifre >= 5*int(quantidade) :
          epic_chifre -= 5
          hyper_chifre += 1
          espaço()
          print (f'Você fez {quantidade}x \033[1;94mHyper Chifre\033[1m')
          linha()
          espaço()
      
          
      jogador = input('Qual sua escolha : ')
      save()
      cls()
      
    elif jogador == 'lootbox':
      def inventario(x,item):
        if x > 0 :
          print('\033[;1m╏ {}× {}'.format(x,item))

      linha()
      print (' '*25,'\033[1;93mLOOTBOX\033[m')
      linha()
      espaço()

      print('\033[;1m Caixas disponiveis:\033[m\n\n(1) Lootbox \033[1;94mcomum\033[m [2000 moedas]\n(2) Lootbox \033[1;95mEpic\033[m [5000 moedas]\n(3) Lootbox \033[1;37mminerios\033[m [3500 moedas]')
      espaço()
      x = input('Qual deseja comprar?: ')
      cls()

      
      if x == '1':
        if cofre < 2000 :
          linha()
          print ('\033[1;31m Material insuficiente \033[m')
          linha()
        else:
          linha()
          print (' '*25,'\033[1;94mLOOTBOX ABERTA\033[m')
          linha()
          espaço()

          lista = []
          lista_drops = []

          lista = sample(range(5,15),2)
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

      elif x == '2':
        if cofre< 5000:
          linha()
          print ('\033[1;31m Material insuficiente \033[m')
          linha()
        else:
          linha()
          print (' '*25,'\033[1;95mLOOTBOX ABERTA\033[m')
          linha()
          espaço()

          lista = []
          lista_drops = []
          lista = sample(range(10,20),2)
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
      elif x == '3':
        if cofre< 3500:
          linha()
          print ('\033[1;31m Material insuficiente \033[m')
          linha()
        else:
          linha()
          print (' '*25,'\033[1;95mLOOTBOX ABERTA\033[m')
          linha()
          espaço()

          lista = []
          lista_drops = []
          lista = sample(range(15,30),2)
          lista2= sample(range(7,15),1)
          lista3 = sample(range(0,5),1)

          pedra += lista[0]
          ouro += lista[1]
          diamante += lista2[0]
          ruby += lista3[0]


          inventario(lista[0],'Pedra')
          inventario(lista[1],'Ouro')
          inventario(lista2[0],'Diamante')
          inventario(lista3[0],'Ruby')

      espaço()
      jogador = input('Qual sua escolha : ')
      save()
      cls()


    elif jogador == 'help' :
      espaço()
      linha()
      print('\033[1m[h] CAÇAR\033[m : Caçando você conegue XP, moedas, carnes e drops de itens,\nmas em troca perde um pouco de sua vida. ')
      espaço()
      print('\033[1m[m] MINERAR\033[m : Minere pedras para vender ou forjar equipamentos na Forja. ')
      espaço()
      print('\033[1m[p] PESCAR\033[m : Pesque para obter comida ou  encontrar algum \nitem boiando.')
      espaço()
      print('\033[1m[c] CURAR\033[m : Recupere sua vida perdida com carnes coletadas ou poções \ncompradas na loja. ')
      espaço()
      print('\033[1m[i] INVENTARIO\033[m : Veja suas estatisticas e os itens presentes no seu \ninventario.')
      espaço()
      print('\033[1m[l] LOJA\033[m : Compra e venda de itens para facilitar seu jogo. ')
      espaço()
      print('\033[1m[f] FORJA\033[m : Forje itens com seus materiais coletados para ganhar \nmais armadura ou dar mais dano.')
      espaço()
      print('\033[1m[d] DUNGEON\033[m : Lute com o boss que protege a passagem para \navançar para outra area.')
      espaço()
      print('\033[1m[receitas] RECEITAS\033[m : Aqui você pode checar as receitas dos itens que podem ser forjados\ncom os materiais do seu inventario.')
      espaço()
      print('\033[1m[fundir] FUNDIÇÃO\033[m : Fundir itens para forma-los em itens mais raros.')
      espaço()
      print('\033[1m[lootbox] LOOTBOX\033[m : Uma caixa com itens e quantidades randomicas.\nUma caixinha de surpresas')
      linha()
      espaço()
      jogador = input('Qual sua escolha : ')
      save()
      cls()

    else:
      linha()
      print ('\033[1;31m Jogada Invalida \033[m')
      linha()
      espaço()
      jogador = input('Qual sua escolha : ')
      save()
      cls()