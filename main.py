from functools import reduce

import pygame, random
from pygame.locals import MOUSEBUTTONDOWN

N, LCel = 8, 50
DimVentana = (N * LCel, N * LCel)
Blanco, Gris, Azul, Negro = (255, 255, 255), (220, 220, 220), (38, 77, 198), (0, 0, 0)
color = {0: Blanco, 1: Azul, 2: Negro}
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

def dibujaPosicion(P, Ventana):
    R = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            R[i][j] = pygame.Rect(j * LCel, i * LCel, LCel, LCel)
            pygame.draw.rect(Ventana, color[P[i][j]], R[i][j])
            pygame.draw.circle(Ventana, color[2], (i * LCel + 25, j * LCel + 25), 20, 0)
    for i in range(N + 1):
        pygame.draw.line(Ventana, Gris, [0, i * LCel], [N * LCel, i * LCel], 1)
        pygame.draw.line(Ventana, Gris, [i * LCel, 0], [i * LCel, N * LCel], 1)

def sumdig(L):
    '''Obtiene la suma digital de los elementos de L'''
    return reduce(lambda x, y: x ^ y, L)

def clasnim(posN):
    posP = posN[:]
    suma = sumdig(posN)
    estado = posN
    if suma == 0:
        print("Se encuentra en una posición P")
    else:
        bin = len(decabin(suma))
        encontrado = False
        i = 0
        while not encontrado:
            if len(decabin(posN[i])) >= bin and decabin(posN[i])[-bin] == 1:
                encontrado = True
            else:
                i += 1
        estado.pop(i)
        estado.insert(i, sumdig(estado))
        print("Estado inicial:" + str(posP))
        print("Estado tras el mejor primer movimiento: " + str(estado))


def decabin(dec):
    bina = []
    while dec:
        bina.insert(0, dec & 1)
        dec >>= 1
    return bina


def main(P):
    Ventana = pygame.display.set_mode(DimVentana)
    pygame.display.set_caption("Practica Modelizacion")
    dibujaPosicion(P, Ventana)
    pygame.display.update()

    Final = False
    while not Final:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: Final = True

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    Pr = [[1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1]]
    main(Pr)
