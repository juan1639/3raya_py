from settings import *

def check_event(pygame, sys, turno, array_tablero):
    """Funcion para detectar ESC, salir y CLICS del raton de forma unica"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print("\n[+]Fin programa\n")
            pygame.quit()
            sys.exit()
            
        # CORRECCIÓN: Detectar el clic aquí evita que se mantenga pulsado infinitamente
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and turno:
            # Ponemos turno a False:
            turno = False

            # Captura de coordenadas raton:
            px, py = event.pos

            # Calcular en qué casilla se hizo clic
            casilla_x = px // SIZE_CASILLA
            casilla_y = py // SIZE_CASILLA
            index = casilla_x + casilla_y * DIM_CUADRICULA[0]
            
            # Si la casilla está vacía, ponemos una X (1)
            if array_tablero[index] == 0:
                array_tablero[index] = 1
                print(f"Click en casilla index {index}. Tablero: {array_tablero}")

    return turno

def dibuja_cuadricula(pygame, pantalla, ancho_casilla, alto_casilla, dimensiones, color):
    for x in range(1, dimensiones[0]):
        pygame.draw.line(pantalla, color, (x * ancho_casilla, 0), (x * ancho_casilla, alto_casilla * dimensiones[1]), 1)
        pygame.draw.line(pantalla, color, (0, x * alto_casilla), (ancho_casilla * dimensiones[1], x * alto_casilla), 1)

def dibuja_x(pygame, pantalla, casilla_index, color=VERDE):
    """Dibuja la X en base al INDEX fijo del tablero, no del ratón"""
    # Convertir el índice del tablero de nuevo a coordenadas de cuadrícula (x, y)
    x = casilla_index % DIM_CUADRICULA[0]
    y = casilla_index // DIM_CUADRICULA[0]

    pad = int(SIZE_CASILLA * 0.15)

    # Línea diagonal 1
    pygame.draw.line(pantalla, color,
        (x * SIZE_CASILLA + pad, y * SIZE_CASILLA + pad),
        (x * SIZE_CASILLA + SIZE_CASILLA - pad, y * SIZE_CASILLA + SIZE_CASILLA - pad), GROSOR)
    
    # Línea diagonal 2
    pygame.draw.line(pantalla, color,
        (x * SIZE_CASILLA + SIZE_CASILLA - pad, y * SIZE_CASILLA + pad),
        (x * SIZE_CASILLA + pad, y * SIZE_CASILLA + SIZE_CASILLA - pad), GROSOR)

def tirada_IA(random, turno, array_tablero):
    # Return si NO es el turno de la IA:
    if turno:
        return turno

    # Tablero lleno:
    if 0 not in array_tablero:
        return True
    
    while True:
        casilla_rnd = random.randrange(TOTAL_CASILLAS)
        
        # Si la casilla está vacía (vale 0), la ocupamos
        if array_tablero[casilla_rnd] == 0:
            array_tablero[casilla_rnd] = 2  # 2 representa la ficha de la IA
            print(f"La IA ha elegido la casilla: {casilla_rnd} | Tablero: {array_tablero}")
            break # Salimos del bucle while porque ya encontramos casilla
    
    return True


