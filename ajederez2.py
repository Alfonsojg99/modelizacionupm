import pygame, sys, time
from pygame.locals import *
from main import clasnim, sumdig, decabin

pygame.init()
visor = pygame.display.set_mode((660,560))
pygame.display.set_caption("ajedrez")

casilla=[0,0,70,140,210,280,350,420,490,560,999]

ocupadas=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 0]]

ocupadas2=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0]]

Rey = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 2, 1, 2, 1, 2, 1, 2, 1],
       [0, 1, 0, 3, 0, 3, 0, 3, 0],
       [0, 2, 3, 2, 1, 2, 1, 2, 1],
       [0, 1, 0, 1, 0, 3, 0, 3, 0],
       [0, 2, 3, 2, 3, 2, 1, 2, 1],
       [0, 1, 0, 1, 0, 1, 0, 3, 0],
       [0, 2, 3, 2, 3, 2, 3, 2, 1],
       [0, 1, 0, 1, 0, 1, 0, 1, 0]]
Torre = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 1, 2, 3, 4, 5, 6, 7],
         [0, 1, 0, 3, 2, 5, 4, 7, 6],
         [0, 2, 3, 0, 1, 6, 7, 4, 5],
         [0, 3, 2, 1, 0, 7, 6, 5, 4],
         [0, 4, 5, 6, 7, 0, 1, 2, 3],
         [0, 5, 4, 7, 6, 1, 0, 3, 2],
         [0, 6, 7, 4, 5, 2, 3, 0, 1],
         [0, 7, 6, 5, 4, 3, 2, 1, 0]]

class metapieza():
	def __init__(self,x,y):
		self.casx=x
		self.casy=y
		self.pos=(casilla[x],casilla[y])
		self.casposibles=[]
		if self.casx < 9 and self.casy < 9:
			if ocupadas[self.casy][self.casx] != 0:
				ocupadas2[self.casy][self.casx] = self
			else:
				ocupadas[self.casy][self.casx] = self

	def cambiasilla(self,x,y):
		if ocupadas2[self.casy][self.casx] == 0:
			ocupadas[self.casy][self.casx] = 0
		else:
			ocupadas[self.casy][self.casx] = ocupadas2[self.casy][self.casx]
			ocupadas2[self.casy][self.casx] = 0
		self.__init__(x,y)

	def cambiasilla2(self,x,y):
		ocupadas2[self.casy][self.casx] = 0
		self.__init__(x,y)

	def movlineal(self, movmax=8):
		casi = 0
		while casi < movmax:
			casi += 1
			if 0 < self.casy <= 8 and 0 < self.casx + casi <= 8:
				self.casposibles.append((self.casx + casi, self.casy))
			if 0 < self.casy + casi <= 8 and 0 < self.casx <= 8:
				self.casposibles.append((self.casx, self.casy + casi))
		return self.casposibles

	def movdiagonal(self):
		casi = 1
		if 0 < self.casy + casi <= 8 and 0 < self.casx + casi <= 8:
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

def	sacapieza2(casx,casy):
	return ocupadas2[casy][casx]


def sacasilla(posraton):
	for i in range(9):
		if casilla[i] < posraton[0] <= casilla[i+1]:
			x = i
		if casilla[i] < posraton[1] <= casilla[i+1]:
			y = i
	return x,y

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  inputbox.display_box(screen, question + ": " + "".join(current_string))
  while 1:
    inkey = inputbox.get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    inputbox.display_box(screen, question + ": " + "".join(current_string))

  return "".join(current_string)


tablero = pygame.image.load('tablero-ajedrez.png')
puntoazul = pygame.image.load('puntoazul.png')
ganas = pygame.image.load('hasGanado.png')
pierdes = pygame.image.load('hasPerdido.png')

botonRey = pygame.image.load('botonrey.png')
botonTorre = pygame.image.load('botontorre.png')
botonRey2 = pygame.image.load('botonrey1.png')
botonTorre2 = pygame.image.load('botontorre1.png')


torreblanca = Torreblanca()
reyblanco = Reyblanco()

click=[]
click2=[]

fichamover=""
turno=1
piezaAtras = False
posimov=[]
pieza=''
dobleFicha = False
while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		if evento.type == MOUSEBUTTONDOWN:
			click.append(pygame.mouse.get_pos())
			print(click)

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
				if ocupadas2[i][j] != 0:
					lista.append(ocupadas2[i][j].nombre)
					posX.append(j)
					posY.append(i)
		if lista[0] == "rey":
			fichamoverRey = sacapieza(posX[0], posY[0])
			posimovRey = fichamoverRey.puedemovera()
			if posX[0] == posX[1] and posY[0] == posY[1]:
				fichamoverTorre = sacapieza2(posX[1], posY[1])
				posimovTorre = fichamoverTorre.puedemovera()
			else:
				fichamoverTorre = sacapieza(posX[1], posY[1])
				posimovTorre = fichamoverTorre.puedemovera()

		else:
			fichamoverTorre = sacapieza(posX[0], posY[0])
			posimovTorre = fichamoverTorre.puedemovera()
			if posX[0] == posX[1] and posY[0] == posY[1]:
				fichamoverRey = sacapieza2(posX[1], posY[1])
				posimovRey = fichamoverRey.puedemovera()
			else:
				fichamoverRey = sacapieza(posX[1], posY[1])
				posimovRey = fichamoverRey.puedemovera()

		if len(posimovRey) == 0 and len(posimovTorre) == 0:
			time.sleep(1)
			visor.blit(pierdes, (0, 0))
			pygame.display.update()
			time.sleep(1)
			break
		if len(click) == 1:#primer click
			posraton = click[0]
			if posraton[0] > 560:
				click=[]
				continue
			casillax,casillay=sacasilla(posraton)
			fichamover=sacapieza(casillax,casillay)
			fichamover2=sacapieza2(casillax, casillay)
			if fichamover2 != 0:
				dobleFicha = True
			else:
				if (fichamover == 0):
					fichamover=""#anula movimientos del otro turno
				else:
					posimov = fichamover.puedemovera()
				if fichamover=="":
					click=[]

		if len(click) == 2 and not dobleFicha:#segundo click
			posraton = click[1]
			nuevacasillax,nuevacasillay = sacasilla(posraton)
			if (nuevacasillax,nuevacasillay) in posimov:
				fichamover.cambiasilla(nuevacasillax,nuevacasillay)
				turno = 2

		if len(click) == 2 and dobleFicha:
			#visor.blit(botonRey, (560, 0))
			#visor.blit(botonTorre, (560, 100))
			botonx = 0
			botony = 0
			posimov = []
			botonx, botony = click[1]
			if botonx > 560 and botony > 175 and botony < 275:
				pieza = 'rey'
			elif botonx > 560 and botony > 285 and botony < 385:
				pieza = 'torre'

			if pieza == 'rey':
				if fichamover.nombre == 'rey':
					posimov = fichamover.puedemovera()
				else:
					posimov = fichamover2.puedemovera()
					piezaAtras=True
			elif pieza == 'torre':
				if fichamover.nombre == 'torre':
					posimov = fichamover.puedemovera()
				else:
					posimov = fichamover2.puedemovera()
					piezaAtras=True

		if len(click) == 3:
			posraton = click[2]
			nuevacasillax,nuevacasillay = sacasilla(posraton)
			if (nuevacasillax,nuevacasillay) in posimov:
				if piezaAtras:
					fichamover2.cambiasilla2(nuevacasillax, nuevacasillay)
					print('y')
				else:
					fichamover.cambiasilla(nuevacasillax,nuevacasillay)
					print('z')
				turno = 2
				dobleFicha = False



	#refrescos y representaciones
		visor.blit(torreblanca.foto,torreblanca.pos)
		visor.blit(reyblanco.foto,reyblanco.pos)
		visor.blit(botonRey, (560, 175))
		visor.blit(botonTorre, (560, 285))
		if len(click) > 1 and not dobleFicha:
			click=[]
			fichamover=""
		if len(click) > 0 and not dobleFicha:
			for pos in posimov:
				visor.blit(puntoazul,(casilla[pos[0]],casilla[pos[1]]))

		if len(click) == 3  and not dobleFicha:
			click=[]
			fichamover=""
			pieza = ''
			pygame.display.flip()

		if len(click) == 2 and dobleFicha:
			for pos in posimov:
				visor.blit(puntoazul,(casilla[pos[0]],casilla[pos[1]]))

		if len(click) == 1 and dobleFicha:
			visor.blit(botonRey2, (560, 175))
			visor.blit(botonTorre2, (560, 285))

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
				if ocupadas2[i][j] != 0 :
					lista.append(ocupadas2[i][j].nombre)
					posX.append(j)
					posY.append(i)

		TorreAtras=False
		ReyAtras = False
		if lista[0] == "rey":
			valorRey = Rey[posX[0]][posY[0]]
			valorTorre = Torre[posX[1]][posY[1]]
			fichamoverRey = sacapieza(posX[0], posY[0])
			posimovRey = fichamoverRey.puedemovera()
			if posX[0] == posX[1] and posY[0] == posY[1]:
				fichamoverTorre = sacapieza2(posX[1], posY[1])
				posimovTorre = fichamoverTorre.puedemovera()
				TorreAtras=True
			else:
				fichamoverTorre = sacapieza(posX[1], posY[1])
				posimovTorre = fichamoverTorre.puedemovera()

		else:
			valorRey = Rey[posX[1]][posY[1]]
			valorTorre = Torre[posX[0]][posY[0]]
			fichamoverTorre = sacapieza(posX[0], posY[0])
			posimovTorre = fichamoverTorre.puedemovera()
			if posX[0] == posX[1] and posY[0] == posY[1]:
				fichamoverRey = sacapieza2(posX[1], posY[1])
				posimovRey = fichamoverRey.puedemovera()
				ReyAtras=True
			else:
				fichamoverRey = sacapieza(posX[1], posY[1])
				posimovRey = fichamoverRey.puedemovera()

		if len(posimovRey) == 0 and len(posimovTorre) == 0:
			time.sleep(1)
			visor.blit(ganas,(0,0))
			pygame.display.update()
			time.sleep(1)
			break


		sincambiar = True
		for (nuevacasillax,nuevacasillay) in posimovTorre:
			if sincambiar:
				nuevovalorTorre = Torre[nuevacasillay][nuevacasillax]
				sumav = sumdig([valorRey, nuevovalorTorre])
				if sumav == 0:
					if TorreAtras:
						fichamoverTorre.cambiasilla2(nuevacasillax, nuevacasillay)
					else:
						fichamoverTorre.cambiasilla(nuevacasillax, nuevacasillay)
					sincambiar = False
		if sincambiar:
			for (nuevacasillax, nuevacasillay) in posimovRey:
				if sincambiar:
						nuevovalorRey = Rey[nuevacasillay][nuevacasillax]
						sumav = sumdig([nuevovalorRey, valorTorre])
						if sumav == 0:
							if ReyAtras:
								fichamoverRey.cambiasilla2(nuevacasillax, nuevacasillay)
							else:
								fichamoverRey.cambiasilla(nuevacasillax, nuevacasillay)
							sincambiar = False
		if sincambiar:
			if 0 < fichamoverTorre.casy + 1 <= 8 and 0 < fichamoverTorre.casx <= 8:
				fichamoverTorre.cambiasilla(fichamoverTorre.casy + 1, fichamoverTorre.casx)
				sincambiar = False
			elif 0 < fichamoverTorre.casy <= 8 and 0 < fichamoverTorre.casx + 1 <= 8:
				fichamoverTorre.cambiasilla(fichamoverTorre.casy, fichamoverTorre.casx + 1)
				sincambiar = False

		if sincambiar:
			if 0 < fichamoverRey.casy + 1 <= 8 and 0 < fichamoverRey.casx <= 8:
				fichamoverRey.cambiasilla(fichamoverRey.casy + 1, fichamoverRey.casx)
				sincambiar = False
			elif 0 < fichamoverRey.casy <= 8 and 0 < fichamoverRey.casx + 1 <= 8:
				fichamoverRey.cambiasilla(fichamoverRey.casy, fichamoverRey.casx + 1)
				sincambiar = False


		visor.blit(torreblanca.foto, torreblanca.pos)
		visor.blit(reyblanco.foto, reyblanco.pos)
		pygame.display.update()

		turno = 1