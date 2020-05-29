#-*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

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
cocupadas=[#color de las ocupadas hola qtal
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
	def casillaocupada(self):
		return self.casy,self.casx
	def movlineal(self,movmax=8):
		casi = 0
		oriz = ordr = vrab = vrar = True
		while casi < movmax:
			casi+=1
			if 0 < self.casy <= 8 and 0 < self.casx-casi <= 8 and oriz:
				oriz = cocupadas[self.casy][self.casx-casi] != self.color
				if oriz:
					self.casposibles.append((self.casx-casi,self.casy))
					oriz = cocupadas[self.casy][self.casx-casi] != 3-self.color
			if 0 < self.casy <= 8 and 0 < self.casx+casi <= 8 and ordr:
				ordr = cocupadas[self.casy][self.casx+casi] != self.color
				if ordr:
					self.casposibles.append((self.casx+casi,self.casy))
					ordr = cocupadas[self.casy][self.casx+casi] != 3-self.color				
			if 0 < self.casy-casi <= 8 and 0 < self.casx <= 8 and vrab:		
				vrab = cocupadas[self.casy-casi][self.casx] != self.color
				if vrab:
					self.casposibles.append((self.casx,self.casy-casi))
					vrab = cocupadas[self.casy-casi][self.casx] != 3-self.color
			if 0 < self.casy+casi <= 8 and 0 < self.casx <= 8 and vrar:		
				vrar = cocupadas[self.casy+casi][self.casx] != self.color
				if vrar:
					self.casposibles.append((self.casx,self.casy+casi))
					vrar = cocupadas[self.casy+casi][self.casx] != 3-self.color
		return self.casposibles
		
	def movdiagonal(self,movmax=8):
		casi = 0
		ariz = abdr = ardr = abiz = True
		while casi < movmax:
			casi+=1
			if 0 < self.casy-casi <= 8 and 0 < self.casx-casi <= 8 and ariz:		
				ariz = cocupadas[self.casy-casi][self.casx-casi] != self.color
				if ariz:
					self.casposibles.append((self.casx-casi,self.casy-casi))
					ariz = cocupadas[self.casy-casi][self.casx-casi] != 3-self.color
			if 0 < self.casy+casi <= 8 and 0 < self.casx+casi <= 8 and abdr:		
				abdr = cocupadas[self.casy+casi][self.casx+casi] != self.color
				if abdr:
					self.casposibles.append((self.casx+casi,self.casy+casi))
					abdr = cocupadas[self.casy+casi][self.casx+casi] != 3-self.color
			if 0 < self.casy-casi <= 8 and 0 < self.casx+casi <= 8 and ardr:		
				ardr = cocupadas[self.casy-casi][self.casx+casi] != self.color
				if ardr:
					self.casposibles.append((self.casx+casi,self.casy-casi))
					ardr = cocupadas[self.casy-casi][self.casx+casi] != 3-self.color
			if 0 < self.casy+casi <= 8 and 0 < self.casx-casi <= 8 and abiz:		
				abiz = cocupadas[self.casy+casi][self.casx-casi] != self.color
				if abiz:
					self.casposibles.append((self.casx-casi,self.casy+casi))
					abiz = cocupadas[self.casy+casi][self.casx-casi] != 3-self.color
		return self.casposibles




class metarey(metapieza):
	def movrey(self):
		posimov=[]
		posimov+=metapieza.movlineal(self,1)
		posimov+=metapieza.movdiagonal(self,1)

		if self.movida == 0:
			if (torreblanca.movida == 0) and \
			cocupadas[self.casy][self.casx-3] == 0 and cocupadas[self.casy][self.casx-2] == 0 \
			and cocupadas[self.casy][self.casx-1] == 0:
				self.casposibles.append((self.casx-2,self.casy))
			posimov+=self.casposibles
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

ud7 = [0,2,7]

tablero = pygame.image.load('tablero-ajedrez.png')			
puntoazul = pygame.image.load('puntoazul.png')
gblancas = pygame.image.load('gblancas.png')
gnegras = pygame.image.load('gnegras.png')

#torreblanca = [0]

#for c in (1,2):
#	torreblanca.append(Torreblanca(pow(c,3)))
torreblanca = Torreblanca()
reyblanco = Reyblanco()

click=[]

fichamover=""
turno="blancas"

while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		if evento.type == MOUSEBUTTONDOWN:
			click.append(pygame.mouse.get_pos())

	visor.blit(tablero,(0,0))

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
			if fichamover.color == 1:
				turno = "negras"
			else:
				turno = "blancas"

	#refrescos y representaciones
	if reyblanco.casx < 9:		
		visor.blit(torreblanca.foto,torreblanca.pos)
		visor.blit(reyblanco.foto,reyblanco.pos)
		
	
	if len(click) > 1:
		click=[]
		fichamover=""
	if len(click) > 0:
		for pos in posimov:
			visor.blit(puntoazul,(casilla[pos[0]],casilla[pos[1]]))
            
	elif reyblanco.casx > 8:
		visor.blit(gnegras,(0,0))

	pygame.display.update()
	
	pygame.time.wait(20)#limita a 50 fps para ahorrar cpu
