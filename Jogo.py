

import random
import time



def menu():
	
	print('{}'.format('=' * 41))
	print('{} Bem Vindo a Jogo de Adivinhação {}'.format('=' * 4, '=' * 4))
	print('{}'.format('=' * 41))
	
	dificuldadefuc()
	
def dificuldadefuc():
	
	global numerodetentativas
	
	print('{} Escolha uma dificuldade {}'.format('=' * 8, '=' * 8))
	
	print('{} 1 - Fácil 2 - Medio 3 - Difícil {}'.format('=' * 4, '=' * 4))
	
	dificuldade = int(input('Selecione uma Dificuldade - '))
	
	
	if dificuldade == 1:
		numerodetentativas = 20
		jogar()
		
	elif dificuldade == 2:
		numerodetentativas = 10
		jogar()
		
	elif dificuldade == 3:
		numerodetentativas = 5
		jogar()
		
	else:
		time.sleep(0.5)
		print('\n {} Escolha uma opção valida {} \n'.format('#' * 7, '#' * 7))
		
		time.sleep(0.7)
		dificuldadefuc()
	
def jogar():
	

	numero_oculto = random.randrange(1, 101)
	
	for rodada in range(1, numerodetentativas+1):
		
		print('{} Números de tentativas {} {} \n{} Número de tentativas restantes {} {}'.format('=' * 8, rodada, '=' * 8, '=' * 3, numerodetentativas - rodada, '=' * 4))
		
		print('{} Fala um número de 1 a 100 {}'.format('=' * 7, '=' * 7))
		
		#debug cheat
		#print(numero_oculto)
		
		tentativa = int(input('Digite o número - '))
		
		if tentativa < 1 or tentativa > 100:
			print('Número invalido')
		else:
			if tentativa < numero_oculto:
				print('O número oculto é maior que esse')
			elif tentativa > numero_oculto:
				print('O número oculto é menor que esse')
			elif tentativa == numero_oculto:
				print('Parabéns você acertou o número')
				jogarnovamente()
				break
		if rodada == numerodetentativas:
			jogarnovamente()
	
def jogarnovamente():
		 
	print('{} Deseja Jogar novamente {} \n{} 1- Sim 2- Não {}'.format('=' * 7, '=' * 7, '=' * 11, '=' * 12))
	resposta = int(input('Escolha uma das Opções - '))
	if resposta == 1:
		dificuldade()
	elif resposta == 2:
		print('Obrigado por jogar')
	
menu()
