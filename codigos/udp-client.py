from socket import *
NomSer = '10.1.2.203'
PueSer = 12000
CliSock = socket(AF_INET, SOCK_DGRAM)
CliSock.connect((NomSer, PueSer))
mensaje = input('Introduce un mensaje: ')
CliSock.send(bytes(mensaje,encoding='utf-8'))
mensajeMayu = CliSock.recv(1024)
print(mensajeMayu.decode('utf-8'))
CliSock.close()

