from socket import *
PueSer = 12000
SerSock = socket(AF_INET, SOCK_DGRAM)
SerSock.bind(('', PueSer))
print('Servidor Mayusculator UDP')

while True:
	mensaje, CliDir = SerSock.recvfrom(2048)
	mensajeMayuscula = mensaje.upper()
	SerSock.sendto(mensajeMayuscula, CliDir)
