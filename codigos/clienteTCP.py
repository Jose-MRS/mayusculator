from socket import *
serviNombre = '10.1.2.203'
serviPuerto = 12000
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((serviNombre, serviPuerto))
mensaje = input('Mete una linea en minusculas: ')
socketCliente.send(bytes(mensaje,encoding='utf-8'))
mensajeMayu = socketCliente.recv(1024)
print(mensajeMayu.decode('utf-8'))
socketCliente.close()
