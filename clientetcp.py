import os,socket
host = '127.0.0.1'
port = 5000

conexao = socket.socket(socket.AF_INET,	socket.SOCK_STREAM)

destino = (host, port)

conexao.connect(destino)

print("Para sair digite ctrl+x \n")
msg = input()
while msg != '\x18':	
	conexao.send(msg.encode())
	retorno = conexao.recv(1024)
	print(retorno.decode('utf-8'))
	msg = input()

conexao.close
