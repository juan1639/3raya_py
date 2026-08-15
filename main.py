import pygame
import sys
import random
from functions import *
from settings import *

pygame.init()

# Inicialización
pantalla = pygame.display.set_mode(SIZE_PANTALLA)
pygame.display.set_caption(" 3 en Raya | Tic Tac Toe ")
reloj = pygame.time.Clock()

# Inicializar tablero vacío [0,0,0,0,0,0,0,0,0]
array_tablero = [0] * TOTAL_CASILLAS

# Turno (True = Jugador | False = IA)
turno = True

# Bucle principal del juego:
while True:
    # Gestor de eventos (ahora controla también el clic del ratón)
    turno = check_event(pygame, sys, turno, array_tablero)

    # Dibujado
    pantalla.fill(GRIS_FONDO)
    dibuja_cuadricula(pygame, pantalla, SIZE_CASILLA, SIZE_CASILLA, DIM_CUADRICULA, GRIS_CUADRICULA)

    # Tirada IA:
    turno = tirada_IA(random, turno, array_tablero)

    # Iteramos usando el INDEX para saber exactamente DÓNDE dibujar
    for index in range(TOTAL_CASILLAS):
        if array_tablero[index] == 1:
            dibuja_x(pygame, pantalla, index, VERDE)
        elif array_tablero[index] == 2:
            dibuja_x(pygame, pantalla, index, ROJO)

    pygame.display.flip()
    reloj.tick(FPS)



