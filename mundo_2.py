from random import randint
from time import sleep
import time
import os
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

def cls() :
    os.system("clear")

def linha():
   print("\033[1;90m===\033[m" * 20)
def espaço():
   print(' ')
def div():
  print(' '*6+'─'*40)
def jogada_invalida():
  jogada_invalida

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
  
linha()
print('\033[1mSeja bem vindo a Area 2, mais conhecida como Montanhas de gelo.....\n\n' 
'Aqui os animais e monstros são mais fortes, tome cuidado...\n\n\033[1;90mPara ver os comandos disponiveis nessa area digite [help]\033[0;0m')
linha()
espaço()

from main_carregar import xp , cofre, vida, vida1, dano, armadura,carnes,life_potion ,diamante ,ouro ,pedra,perola ,chifre ,peixe_p,peixe_m,peixe_g,picareta,maça_dourada,medicina,olho_de_zumbi, ruby,xpl,maça,epic_perola,hyper_perola,epic_chifre,hyper_chifre 

mundo = 2

#ITENS_2
quest = 0

first_time_h = 0
first_time_m = 0
first_time_p = 0
first_time_q = 0

if vida <= 0:
    print('Você Morreu')

#INICIO DO PROGRAMA
jogador = input('Qual sua escolha : ')
cls() 

while mundo == 2 :
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
    caça_dano = (20, 30, 40)
    moedas = (3, 5, 7,11,15)
    caça_xp = (13,16,19,24,30)

#DADOS    
    dado_carnes = randint(0, 2)
    dado_dano_caça = randint(0, 2)
    dado_moedas = randint (0,4)
    dado_drops = randint (0,100)
    dado_drop_item = randint(0,2)
    dado_xp = randint (0,4)
    dado_boss = randint (0,200)
    dado_minerar = randint(0, 100)
    dado_ruby = randint (0,100)

    drop = ('Perola','Chifre','Olho de Zumbi')
    mineracao = ('Pedra comum', 'Ouro', 'Diamante')

#FUNÇOES
    def quantidade_(x) :
          return x < quantidade         
    def loja_(x) :
          return quantidade * x
    def venda(x):
          x - quantidade

#EVENTOS
  #1 - BOSS
  #2 - 69
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

#EVENTOS
  #1 - BOSS
  #2 - 69
    if jogador ==  'd' :

       espaço()
       linha()
       b = 'vivo'
       boss = 1000
       div()
       print('             \033[1;35m✠ VOCÊ INICIOU A DUNGEON!✠\033[m')
       espaço()
       print('A entrada esta logo a frente, algo pode estar te esperando nessa dungeon')
       espaço()
       sleep(4)
       print(f'... uma sombra enorme surge...')
       espaço()
       sleep(2)
       print('É UM DRAGÃO!!') 
       espaço()
       sleep(2)
       print('Para passar dessa area você devera matar o dragão que guarda a passagem')
       while b == 'vivo' :

            dado_boss2 = randint (0,10)
            dado_boss3 = (0,25, 40, 75 ,100)
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
                boss = 1000
                linha()
                break

            if jogada_boss == 'a':
              cls()
              save()
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
              save()
              if dado_fuga < 8 :
                espaço()
                print ('....Você correu para bem longe do ogro, boa sorte da proxima vez.... ') 
                boss = 1000
                break
                espaço()
                jogador = input('Qual sua escolha : ')
                cls()
                save()
              else : 
                espaço()
                print('...Você foi correr desesperado e acabou tropeçando e deixando todos seus itens para traz....')
                espaço()
                boss = 1000
                carnes = 0 
                cofre = 0 
                pedra = 0 
                ouro = 0 
                diamante = 0
                b = ' '
                jogador = input('Qual sua escolha : ')
                cls()
                save()
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
                  save()
                  mundo = 3
                  import mundo_3
       else :
          jogador = input('Qual sua escolha : ')
          cls()
          save()
    if jogador == '69':
      mundo = 3
      import mundo_3
      break
#JOGADAS

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
                ruby = 0
                chifre = 0
                peixe_p = 0
                peixe_m = 0
                peixe_g = 0
                linha()
                espaço()
                jogador = input('Deseja continuar? (s/n) : ')
                if jogador == 's':
                  cls()
                  save()
                  break
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
            save()
          else :
            first_time_h = int(time.time()) 
            linha()
            dano_tomado = caça_dano[dado_dano_caça]- armadura
            if caça_dano[dado_dano_caça]- armadura < 0:
              dano_tomado = 0
            carnes = (carnes + caça_carnes[dado_carnes])
            cofre = (cofre + moedas[dado_moedas])
            xp = (xp + caça_xp[dado_xp])
            print('Você coletou {} carne(s) \n\033[1;93m+{}\033[m moedas''\n\033[1;34m+{}\033[m xp ''\n\033[1;31m-{}\033[m' ' de vida'.format(caça_carnes[dado_carnes], moedas[dado_moedas], caça_xp[dado_xp] ,dano_tomado))
            if maça_dourada > 0 :
              print('\033[1;33m**Imortal**\033[m')
              maça_dourada -= 1
            else:
              vida = (vida - (dano_tomado))
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
              elif drop[dado_drop_item] == 'Olho de Zumbi':
                olho_de_zumbi += 1
                print ('Você matou um Zumbi e coletou um {}'.format(drop[dado_drop_item]))
            if vida > 0 :
              espaço()
              print('    Vida')
              life()
              linha()
              jogador = input('Qual sua escolha : ')
              cls()
              save()
              
            else:
              espaço()
              print ('Sua vida esta em 0')
              life()
            espaço()
        
    elif jogador == 'm':
        linha()
        second_time_m = int(time.time())
        if second_time_m - first_time_m < 20 :
            print('Você ainda não pode minerar novamente')
            print(f'Ainda restam { ((second_time_m -first_time_m) - 20)*-1}s')
        else :
          first_time_m = int(time.time())
          print ('Minerando...⸕')
          linha()
          espaço()
          if dado_minerar < 70:
              print('Você coletou {}x \033[1;37mPedra comum\033[m'.format(2+picareta))
              pedra += 2 + picareta
          elif dado_ruby == 1 :
              print('Você encontrou um \033[1;31mRuby \033[mno meio das pedras')
              ruby += 1 
          elif 69 < dado_minerar < 95 :
              print('Você coletou {}x \033[1;33mOuro\033[m'.format(1+picareta))
              ouro += 1 + picareta
          else :
              print ('Você achou {}x \033[1;36mDIAMANTE\033[m'.format(1+picareta))
              diamante += 1 + picareta
        linha()
        espaço()
        jogador = input('Qual sua escolha : ')
        cls()
        save()
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
              carnes -= quantidade_cura
              linha()
              print('Você restaurou \033[1;32m {} \033[m de vida'.format(5* (quantidade_cura*medicina)))     
              vida += 5* (quantidade_cura*medicina)
          elif cura == '2' :
            if life_potion < 1 :
              linha()
              print ('\033[1;31m Material insuficiente \033[m')
              linha()
            else :
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
              save()
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
              save()
              peixe_m -= quantidade_cura
              linha()
              print('Você restaurou \033[1;32m {} \033[m de vida'.format(15* quantidade_cura))     
              vida += 15* quantidade_cura
          elif cura == '5' :
            quantidade_cura = int(input (' Quantidade : '))
            if peixe_g < quantidade_cura :
              linha()
              print ('\033[1;31m Material insuficiente \033[m')
              linha()
            else :
              cls()
              save()
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
        cls()
        save()
        espaço()

    elif jogador == 'i' :
      def inventario(x,item):
        if x > 0 :
          print('╏ {}× {}'.format(x,item))
      linha()
      div()
      print (' '*22+' \033[;1mPERFIL\033[m')
      print ('╏ ''Vida : {} de {}'.format(vida,vida1),' '*15, 'XP : {}'.format(xp))  
      life()      
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
      inventario(olho_de_zumbi,'Olho de zumbi')
      inventario(life_potion,'Potions')
      inventario(peixe_p,'Peixe pequeno')
      inventario(peixe_m,'Peixe epico')
      inventario(peixe_g,'TAINHA')
      inventario(maça,'Maça Especial')
      print(' '*24+'...')
      espaço()
      linha()
      jogador = input('Qual sua escolha : ')
      cls()
      save()
      espaço()


    elif jogador == 'l' :
      
    
        linha()
        print ( 'Seja bem vindo a loja \nAqui podemos comprar seus itens\n')
        linha()
        print('VENDER \n(1) Pedra comum [5 moedas]\n(2) Ouro [15 moedas] \n(3) Diamante [50 moedas] \n(4) Chifre [100 moedas]'
        '\n(5) Perola [100 moedas] \nCOMPRAR \n(6) Life Potion [30 moedas] \n(7) Maça especial [500 moedas] \n(8) Elmo de guerreiro [1200 moedas]')
        linha()
        loja = input('Qual seu pedido?:  ')
        if loja == '0':
          espaço()
          linha()
          jogador = input('Qual sua escolha : ')
          cls()
          save()
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
          elif loja == '7' :
            if cofre > 500 :
              cofre -= quantidade * 500
              maça += quantidade
              print('Você recebeu {} maças'.format(quantidade))
            else: 
              print('\033[1;31m Moedas insuficientes \033[m')
          elif loja == '8' :
            if cofre > 1200 :
              cofre -= quantidade * 1200
              armadura += 2
              dano += 2
              print(f'+{2*quantidade} Dano\n+{2*quantidade} Armadura ')
            else: 
              print('\033[1;31m Moedas insuficientes \033[m')
          else :
            jogada_invalida()
          linha()
          jogador = input('Qual sua escolha : ')
          cls()
          save() 

    elif jogador == 'f' :
        linha()
        print ( 'Seja bem vindo a forja \n Aqui podemos fazer seus itens\n')
        linha()
        print ('(1) Armadura Comum \n(2) Espada de diamante\n(3) Armadura encantada  \n(4) Espada encantada\n(5) Totem\n(6) Maça Dourada\n(7) Armadura do Gladiador\n(8) Espada do Gladiador')
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
            armadura = 5
            ouro -= 5
            linha()
        elif forjar == '2' :
          linha()
          if perola < 1 or ouro < 5 :
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else :
            print ('+15 Armadura')
            armadura = 15
            ouro -=5 
            perola -=1
            linha()
        elif forjar == '3' :
          linha()
          if diamante < 1 or  chifre < 1 :
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else:
            diamante -= 2
            chifre -= 1
            dano += 40
            print('\033[1mEspada forjada com sucesso\033[m')
            linha()
        elif forjar == '4' :
          linha()
          if ruby < 1 or  ouro < 3 or perola < 1 :
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else:
            ruby -= 1
            ouro -= 3
            olho_de_zumbi -= 1
            dano += 20
            armadura += 10
            print('\033[1mTotem forjado\033[m\n+20 Dano\n+10 Armadura')
            linha()
        elif forjar == '5' :
          linha()
          if maça < 1 or  ouro < 10 :
            print ('\033[1;31m Material insuficiente \033[m')
            linha()
          else:
            maça -= 1
            ouro -= 10
            maça_dourada += 15
            print('\033[1mMaça Dourada forjada\033[m\nImortal por 15 caças')
            linha()
        espaço()
        jogador = input('Qual sua escolha : ')
        cls()
        save()

    elif jogador == 't' :
        linha()
        print('\033[1;95mTREINAMENTO\033[m')
        linha()
        espaço()
        print('- Aqui você pode treinar suas habilidades..')
        sleep(2)
        espaço()
        print('[1] Treinar mineração : + Eficiencia\n[2] Treinar medicina : + Cura ')
        linha()
        espaço()
        habilidade = input('Qual gostaria de treinar?  ')
        espaço()
        if habilidade == '1' :
          if pedra < 100 :
            linha()
            print ('Você não é bom o suficiente \ncolete 100 pedras antes de voltar aqui novamente...')
          else :
            linha()
            print ('\033[;1m+ Eficiencia ao minerar\033[m')
            pedra -= 100
            picareta += 1

        if habilidade == '2':
          if olho_de_zumbi < 2 :
            print ('Você não é bom o suficiente \nColete 2 olhos de zumbi e traga 5 Life potions antes de voltar aqui...')
          elif life_potion < 5 :
            print ('Você não é bom o suficiente \nColete 2 olhos de zumbi e traga 5 Life potions antes de voltar aqui...')
          else: 
            linha()
            print ('\033[;1m+ Aprendeu : Medicina\033[m')
            life_potion -= 5
            olho_de_zumbi -= 1
            medicina = 3
        linha()
        espaço()
        jogador = input('Qual sua escolha : ')
        cls()
        save() 

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
          else:
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

        elif cassino == '0':
          espaço()
          linha()
          print('Obrigado volte sempre!')
          linha()
          espaço()
          jogador = input('Qual sua escolha : ')
          cls()
          save()
      espaço()
      linha()
      print('Obrigado volte sempre!')
      linha()
      espaço()
      jogador = input('Qual sua escolha : ')
      cls()
      save()


    elif jogador == 'q' :
      linha()
      print (' '*25,'\033[1;93mQUEST\033[m')
      dado_quests = randint (0,1)
      if quest == 0 :
        second_time_q = int(time.time())
        if second_time_q - first_time_q <= 20 :
            linha()
            print('Você ainda não pode realizar uma quest novamente')
            print(f'Ainda restam { ((second_time_q -first_time_q) - 60)*-1}s')
            linha()
            espaço()
        elif dado_quests == 0 :
          linha()
          print('Sua missão sera coletar um Cifre de um javali selvagem.')
          sleep(1)
          espaço()
          aceitar_quest = input('Aceita a missão?(s/n) ')
          if aceitar_quest == 's':
            quest = 1
            first_time_q = int(time.time())
            espaço()
            print('\033[1;37mMissão em andamento...\033[m')
          else :
            quest = 0
        elif dado_quests == 1 :
          linha()
          print('Sua missão sera coletar uma Perola de uma fada.')
          sleep(1)
          espaço()
          aceitar_quest = input('Aceita a missão?(s/n) ')
          if aceitar_quest == 's':
            quest = 2
            first_time_q = int(time.time())
            espaço()
            print('\033[1;37mMissão em andamento...\033[m')
          else :
            quest = 0
        elif dado_quests == 2 :
          linha()
          print('Sua missão sera coletar um Diamante enquanto minera.')
          sleep(1)
          espaço()
          aceitar_quest = input('Aceita a missão?(s/n) ')
          if aceitar_quest == 's':
            quest = 3
            first_time_q = int(time.time())
            espaço()
            print('\033[1;37mMissão em andamento...\033[m')
          else :
            quest = 0
      elif quest == 1 :
          if chifre >= 1 : 
            linha()
            print('\033[;1mVocê completou a quest!\n+\033[1;93m100\033[m moedas\n+\033[1;94m60\033[m xp\033[m')
            quest = 0
          else:
            linha()
            print('Você ainda não completou sua missão.')
      elif quest == 2 :
          if perola >= 1 : 
            linha()
            print('\033[;1mVocê completou a quest!\n+\033[1;93m100\033[m moedas\n+\033[1;94m60\033[m xp\033[m')
            quest = 0
          else:
            linha()
            print('Você ainda não completou sua missão.')
      elif quest == 3 :
          if diamante >= 1 : 
            linha()
            print('\033[;1mVocê completou a quest!\n+\033[1;93m100\033[m moedas\n+\033[1;94m60\033[m xp\033[m')
            quest = 0
          else:
            linha()
            print('Você ainda não completou sua missão.')
      linha()
      espaço()
      jogador = input('Qual sua escolha : ')
      cls()
      save()        

    elif jogador == 'p' :
      second_time_p = int(time.time())
      if second_time_p - first_time_p < 20 :
            linha()
            print('Você ainda não pode pescar novamente')
            print(f'Ainda restam { ((second_time_p -first_time_p) - 20)*-1}s')
            linha()
            espaço()
            jogador = input('Qual sua escolha :\033[;1m ')
            cls()
            save()
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
          cls()
          save()
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
      print('\033[1m[t] TREINAR\033[m : Aprenda habilidades que ajudarão no desempenho das atividades.')
      espaço()
      print('\033[1m[p] PESCAR\033[m : Pesque para obter comida ou  encontrar algum \nitem boiando.')
      espaço()
      print('\033[1m[q] QUEST\033[m : Você aceita uma missão? Receba recompensas ao \nfinalizar suas missões com perfeição.')
      espaço()
      print('\033[1m[receitas] RECEITAS\033[m : Aqui você pode checar as receitas dos itens que podem ser forjados\ncom os materiais do seu inventario.')
      espaço()
      print('\033[1m[fundir] FUNDIÇÃO\033[m : Fundir itens para forma-los em itens mais raros.')
      espaço()
      print('\033[1m[lootbox] LOOTBOX\033[m : Uma caixa com itens e quantidades randomicas.\nUma caixinha de surpresas')
      linha()
      espaço()
      jogador = input('Qual sua escolha : ')
      cls()
      save()

    else:
      linha()
      print ('\033[1;31m Jogada Invalida \033[m')
      linha()
      espaço()
      jogador = input('Qual sua escolha : ')
      cls()
      save()
if mundo == 3 :
  vida = vida1
  mundo = 3
else :
  vida = vida1
  mundo = 1
  








