#-*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from main import clasnim, sumdig, decabin

pygame.init()
visor = pygame.display.set_mode((560,560))
pygame.display.set_caption("ajedrez")

casilla=[0,0,70,140,210,280,350,420,490,560,999]

ocupadas=[
[0,0,0,0,0,0,0,0,0],#esta linia y el 0 de mas es para kitar el 0 de los indices
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]
cocupadas=[#color de las ocupadas
[0,0,0,0,0,0,0,0,0],#esta linia y el 0 de mas es para kitar el 0 de los indices hola qu etal 
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
	def __init__(self,x,y,color):
		self.movida = 0
		self.casx=x
		self.casy=y
		self.pos=(casilla[x],casilla[y])
		self.color=color
		self.casposibles=[]
		if self.casx < 9 and self.casy < 9:
			ocupadas[self.casy][self.casx] = self
			cocupadas[self.casy][self.casx] = self.color

	def cambiasilla(self,x,y):
		ocupadas[self.casy][self.casx]=cocupadas[self.casy][self.casx] = 0
		self.__init__(x,y)
		self.movida = 1

	def movlineal(self,movmax=8):
		casi = 0
		ordr = vrar = True
		while casi < movmax:
			casi+=1
			if 0 < self.casy <= 8 and 0 < self.casx+casi <= 8 and ordr:
					self.casposibles.append((self.casx+casi,self.casy))
					ordr = cocupadas[self.casy][self.casx+casi] != 3-self.color				

			if 0 < self.casy+casi <= 8 and 0 < self.casx <= 8 and vrar:
					self.casposibles.append((self.casx,self.casy+casi))
					vrar = cocupadas[self.casy+casi][self.casx] != 3-self.color
		return self.casposibles
		
	def movdiagonal(self,movmax=8):
		casi = 0
		abdr  = True
		while casi < movmax:
			casi+=1
			if 0 < self.casy+casi <= 8 and 0 < self.casx+casi <= 8 and abdr:
					self.casposibles.append((self.casx+casi,self.casy+casi))
					abdr = cocupadas[self.casy+casi][self.casx+casi] != 3-self.color
		return self.casposibles


class metarey(metapieza):
	def movrey(self):
		posimov=[]
		posimov+=metapieza.movlineal(self,1)
		posimov+=metapieza.movdiagonal(self,1)
		return posimov

class Torreblanca(metapieza):
	def __init__(self,x=3,y=1):
		self.foto = pygame.image.load('torreblanca.png')
		metapieza.__init__(self,x,y,1)
	def puedemovera(self):
		return metapieza.movlineal(self)	

class Reyblanco(metarey):
	def __init__(self,x=1,y=2):
		self.foto = pygame.image.load('reyblanco.png')
		metapieza.__init__(self,x,y,1)
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
gblancas = pygame.image.load('gblancas.png')
gnegras = pygame.image.load('gnegras.png')

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
            
	#elif reyblanco.casx > 8:
	#	visor.blit(gnegras,(0,0))

		pygame.display.update()
	
	#pygame.time.wait(20)#limita a 50 fps para ahorrar cpu

	if turno == 2:
		lista = []
		posX = []
		posY= []
		for i in range(len(ocupadas)):
			for j in range(len(ocupadas[i])):
				if ocupadas[i][j] != 0 :
					lista.append(ocupadas[i][j])
					posX.append(i)
					posY.append(j)
		print(lista)
		print(posX)
		print(posY)
		valorTorre = Torre[posX[1]-1][posY[1]-1]
		valorRey = Rey[posX[0]-1][posY[0]-1]
		valorNim = sumdig([valorRey, valorTorre])
		print(valorNim)
		for i in range(len(Torre)):
			for j in range(len(Torre[i])):
				if ocupadas[i][j] != 0 :


		turno = 1

