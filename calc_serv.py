import socket
import os

serverHost = 'localhost'
serverPort = 2000

os.system('clear')
print('                   CALCULADORA                        ')
print('------------------------------------------------------')
print(' Esperando Operacao                                   ')

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))


soma = 0
while True:

	message, clientAddress = serverSocket.recvfrom(2048)
	os.system('clear')
	#print('Conexão de: ', clientAddress)
    #Processa a stringe para lestras maiusculas

	mens = message.decode('utf-8')

	operacao = mens.split()

	print('                   CALCULADORA                        ')
	print('------------------------------------------------------')
	print(' Esperando Operacao                                   ')


	print(' Conexao de : ', clientAddress)

	if operacao[0] == 'soma':
		soma = int(operacao[1]) + int(operacao[2])
		print(' Calcular a %s entre %s e %s = %s \n ' %(operacao[0], operacao[1], operacao[2], soma))
		message = str(soma).encode('utf-8')
	
	elif operacao[0] == 'raiz':
		raiz = (int(operacao[1])**0.5)
		print(' Calcular a Raiz Quadradade de %s = ' %(operacao[1]), raiz)
	
	
		message = str(raiz).encode()
	

	serverSocket.sendto(message, clientAddress)
