#-*- coding: utf-8 -*-
import pygame, sys, time
from pygame.locals import *
from main import clasnim, sumdig, decabin

pygame.init()
visor = pygame.display.set_mode((560,560))
pygame.display.set_caption("ajedrez")

casilla=[0,0,70,140,210,280,350,420,490,560,999]

ocupadas=[
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]

Rey = [[2, 1, 2, 1, 2, 1, 2, 1],
       [1, 0, 3, 0, 3, 0, 3, 0],
       [2, 3, 2, 1, 2, 1, 2, 1],
       [1, 0, 1, 0, 3, 0, 3, 0],
       [2, 3, 2, 3, 2, 1, 2, 1],
       [1, 0, 1, 0, 1, 0, 3, 0],
       [2, 3, 2, 3, 2, 3, 2, 1],
       [1, 0, 1, 0, 1, 0, 1, 0]]
Torre = [[0, 1, 2, 3, 4, 5, 6, 7],
         [1, 0, 3, 2, 5, 4, 7, 6],
         [2, 3, 0, 1, 6, 7, 4, 5],
         [3, 2, 1, 0, 7, 6, 5, 4],
         [4, 5, 6, 7, 0, 1, 2, 3],
         [5, 4, 7, 6, 1, 0, 3, 2],
         [6, 7, 4, 5, 2, 3, 0, 1],
         [7, 6, 5, 4, 3, 2, 1, 0]]

class metapieza():
	def __init__(self,x,y):
		#self.movida = 0
		self.casx=x
		self.casy=y
		self.pos=(casilla[x],casilla[y])
		self.casposibles=[]
		if self.casx < 9 and self.casy < 9:
			ocupadas[self.casy][self.casx] = self

	def cambiasilla(self,x,y):
		ocupadas[self.casy][self.casx] = 0
		self.__init__(x,y)
		#self.movida = 1

	def movlineal(self,movmax=8):
		casi = 0
		ordr = vrar = True
		while casi < movmax:
			casi+=1
			if 0 < self.casy <= 8 and 0 < self.casx+casi <= 8 and ordr:
					ordr = ocupadas[self.casy][self.casx + casi] == 0
					if ordr:
						self.casposibles.append((self.casx+casi,self.casy))
			if 0 < self.casy+casi <= 8 and 0 < self.casx <= 8 and vrar:
					vrar = ocupadas[self.casy + casi][self.casx] == 0
					if vrar:
						self.casposibles.append((self.casx,self.casy+casi))
		return self.casposibles

	def movdiagonal(self):
		casi = 1
		if 0 < self.casy + casi <= 8 and 0 < self.casx + casi <= 8:
			abdr = ocupadas[self.casy + casi][self.casx + casi] == 0
		if 0 < self.casy + casi <= 8 and 0 < self.casx + casi <= 8 and abdr:
			self.casposibles.append((self.casx + casi, self.casy + casi))
		return self.casposibles


class metarey(metapieza):
	def movrey(self):
		posimov=[]
		posimov+=metapieza.movlineal(self,1)
		posimov+=metapieza.movdiagonal(self)
		return posimov

class Torreblanca(metapieza):
	def __init__(self,x=3,y=1):
		self.nombre = "torre"
		self.foto = pygame.image.load('torreblanca.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metapieza.movlineal(self)

class Reyblanco(metarey):
	def __init__(self,x=1,y=2):
		self.nombre = "rey"
		self.foto = pygame.image.load('reyblanco.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metarey.movrey(self)


def	sacapieza(casx,casy):
	return ocupadas[casy][casx]


def sacasilla(posraton):
	for i in range(9):
		if casilla[i] < posraton[0] <= casilla[i+1]:
			x = i
		if casilla[i] < posraton[1] <= casilla[i+1]:
			y = i
	return x,y


tablero = pygame.image.load('tablero-ajedrez.png')
puntoazul = pygame.image.load('puntoazul.png')
ganas = pygame.image.load('hasGanado.png')
pierdes = pygame.image.load('hasPerdido.png')


torreblanca = Torreblanca()
reyblanco = Reyblanco()

click=[]

fichamover=""
turno=1
while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		if evento.type == MOUSEBUTTONDOWN:
			click.append(pygame.mouse.get_pos())

	visor.blit(tablero,(0,0))

	if turno == 1:
		lista = []
		posX = []
		posY = []
		for i in range(len(ocupadas)):
			for j in range(len(ocupadas[i])):
				if ocupadas[i][j] != 0:
					lista.append(ocupadas[i][j].nombre)
					posX.append(j)
					posY.append(i)
		if lista[0] == "rey":
			fichamoverRey = sacapieza(posX[0], posY[0])
			posimovRey = fichamoverRey.puedemovera()
			fichamoverTorre = sacapieza(posX[1], posY[1])
			posimovTorre = fichamoverTorre.puedemovera()
		else:
			fichamoverRey = sacapieza(posX[1], posY[1])
			posimovRey = fichamoverRey.puedemovera()
			fichamoverTorre = sacapieza(posX[0], posY[0])
			posimovTorre = fichamoverTorre.puedemovera()

		if len(posimovRey) == 0 and len(posimovTorre) == 0:
			visor.blit(pierdes, (0, 0))
			pygame.display.update()
			time.sleep(5)
			break

		if len(click) == 1:#primer click
			posraton = click[0]
			casillax,casillay=sacasilla(posraton)
			fichamover=sacapieza(casillax,casillay)
			if (fichamover == 0):
				fichamover=""#anula movimientos del otro turno
			else:
				posimov = fichamover.puedemovera()
			if fichamover=="":
				click=[]

		if len(click) == 2:#segundo click
			posraton = click[1]
			nuevacasillax,nuevacasillay = sacasilla(posraton)
			if (nuevacasillax,nuevacasillay) in posimov:
				fichamover.cambiasilla(nuevacasillax,nuevacasillay)
				turno = 2

	#refrescos y representaciones

		visor.blit(torreblanca.foto,torreblanca.pos)
		visor.blit(reyblanco.foto,reyblanco.pos)
		if len(click) > 1:
			click=[]
			fichamover=""
		if len(click) > 0:
			for pos in posimov:
				visor.blit(puntoazul,(casilla[pos[0]],casilla[pos[1]]))


		pygame.display.update()
		time.sleep(0.5)

	#pygame.time.wait(20)#limita a 50 fps para ahorrar cpu

	if turno == 2:
		lista = []
		posX = []
		posY= []
		for i in range(len(ocupadas)):
			for j in range(len(ocupadas[i])):
				if ocupadas[i][j] != 0 :
					lista.append(ocupadas[i][j].nombre)
					posX.append(j)
					posY.append(i)

		print(lista)
		print(posX)
		print(posY)
		if lista[0] == "rey":
			valorRey = Rey[posX[0] - 1][posY[0] - 1]
			valorTorre = Torre[posX[1] - 1][posY[1] - 1]
			fichamoverRey = sacapieza(posX[0], posY[0])
			posimovRey = fichamoverRey.puedemovera()
			fichamoverTorre = sacapieza(posX[1], posY[1])
			posimovTorre = fichamoverTorre.puedemovera()
		else:
			valorRey = Rey[posX[1] - 1][posY[1] - 1]
			valorTorre = Torre[posX[0] - 1][posY[0] - 1]
			fichamoverRey = sacapieza(posX[1], posY[1])
			posimovRey = fichamoverRey.puedemovera()
			fichamoverTorre = sacapieza(posX[0], posY[0])
			posimovTorre = fichamoverTorre.puedemovera()
		valorNim = sumdig([valorRey, valorTorre])
		print(valorNim)
		print(posimovRey)
		print(posimovTorre)
		if len(posimovRey) == 0 and len(posimovTorre) == 0:
			visor.blit(ganas,(0,0))
			pygame.display.update()
			time.sleep(5)
			break
		sincambiar = True
		for (nuevacasillax,nuevacasillay) in posimovTorre:
			if sincambiar:
				print (nuevacasillax,nuevacasillay)
				nuevovalorTorre = Torre[nuevacasillax-1][nuevacasillay-1]
				sumav = sumdig([valorRey, nuevovalorTorre])
				if sumav == 0:
					fichamoverTorre.cambiasilla(nuevacasillax,nuevacasillay)
					sincambiar = False
		if sincambiar:
			for (nuevacasillax, nuevacasillay) in posimovRey:
				if sincambiar:
						nuevovalorRey = Rey[nuevacasillax - 1][nuevacasillay - 1]
						sumav = sumdig([nuevovalorRey, valorTorre])
						if sumav == 0:
							fichamoverRey.cambiasilla(nuevacasillax, nuevacasillay)
							sincambiar = False



		turno = 1

