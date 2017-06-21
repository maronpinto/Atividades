import socket
serverName = 'localhost'
serverPort = 2000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
operacao = input("Digite a operacao: ")
if operacao == 'soma':
	print("Calcular a soma\n")
	a = input("Digite o valor 1 ")
	b = input("Digite o valor 2 ")
	message = "soma " + a + " " +  b + "\n"
elif operacao == "raiz":
	print("Calcular raiz quadrade de\n")
	a = input("Digite o valor ")
elif operacao == 'quit':
	message = ""
    
byte_msg = message.encode('utf-8')

clientSocket.sendto(byte_msg, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
