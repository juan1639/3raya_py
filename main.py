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

# Resultado y lista de resultados:
resultados = ['En juego...', 'Has ganado!', 'Has perdido', 'Empate']
resultado = 0

# ====================================
#  Bucle principal del juego:
# 
# ====================================
while True:
    # Reset values:
    resultado = 0
    rejugar = False
    tirada_hecha = False

    # Turno (True = Jugador | False = IA)
    #turno = True
    turno = random.choice([True, False])

    # Inicializar tablero vacío [0,0,0,0,0,0,0,0,0]
    array_tablero = [0] * TOTAL_CASILLAS

    while resultado == 0:
        # Turnos alternativos mediante un if:
        if turno:
            # Gestor de eventos (ahora controla también el clic del ratón)
            tirada_hecha, rejugar = check_event(pygame, sys, turno, tirada_hecha, array_tablero, resultado, rejugar)
        else:
            # Tirada IA:
            tirada_IA(random, turno, array_tablero)

        # Check empate:
        if 0 not in array_tablero:
            resultado = 3

        # Check Si hay ganador:
        if check_3raya(turno, array_tablero):
            resultado = 1 if turno else 2
        
        # Cambio de turno:
        if resultado == 0:
            if turno and tirada_hecha:
                turno = False
            else:
                turno = True
                tirada_hecha = False
        
        # Pintar fondo y dibuja cuadricula:
        pantalla.fill(GRIS_FONDO)
        dibuja_cuadricula(pygame, pantalla, SIZE_CASILLA, SIZE_CASILLA, DIM_CUADRICULA, GRIS_CUADRICULA)
        dibuja_tablero_dinamicamente(pygame, pantalla, array_tablero)

        # Refresco de pantalla y reloj a 60 FPS
        pygame.display.flip()
        reloj.tick(FPS)

    # =============================================================
    #   Game Over (resultado final)
    # 
    # =============================================================
    print(resultados[resultado])

    while not rejugar:
        # Gestor de eventos (ahora controla también el clic del ratón)
        tirada_hecha, rejugar = check_event(pygame, sys, turno, tirada_hecha, array_tablero, resultado, rejugar)

        # Pintar fondo y dibuja cuadricula:
        pantalla.fill(GRIS_FONDO)
        dibuja_cuadricula(pygame, pantalla, SIZE_CASILLA, SIZE_CASILLA, DIM_CUADRICULA, GRIS_CUADRICULA)
        dibuja_tablero_dinamicamente(pygame, pantalla, array_tablero)

        fuente = pygame.font.Font(None, 90) 
        superficie_texto = fuente.render(resultados[resultado], True, AMARILLO)
        rect_texto = superficie_texto.get_rect()
        rect_texto.center = (SIZE_PANTALLA[0] // 2, SIZE_PANTALLA[1] // 2)
        pantalla.blit(superficie_texto, rect_texto)

        fuente = pygame.font.Font(None, 32) 
        superficie_texto = fuente.render(" ENTER - Otra partida       Esc. Salir ", True, BLANCO)
        rect_texto = superficie_texto.get_rect()
        rect_texto.center = (SIZE_PANTALLA[0] // 2, SIZE_PANTALLA[1] // 1.1)
        pantalla.blit(superficie_texto, rect_texto)

        # Refresco de pantalla y reloj a 60 FPS
        pygame.display.flip()
        reloj.tick(FPS)


