from settings import *

# =========================================================================
def check_event(pygame, sys, turno, tirada_jugador_hecha, array_tablero, resultado, rejugar):
    """Funcion para detectar ESC, salir y CLICS del raton de forma unica"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print("\n[+]Fin programa\n")
            pygame.quit()
            sys.exit()

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) and resultado != 0:
            rejugar = True
        
        # CORRECCIÓN: Detectar el clic aquí evita que se mantenga pulsado infinitamente
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and turno and resultado == 0:
            # Captura de coordenadas raton:
            px, py = event.pos

            # Accion realizada:
            tirada_jugador_hecha = True

            # Calcular en qué casilla se hizo clic
            casilla_x = px // SIZE_CASILLA
            casilla_y = py // SIZE_CASILLA
            index = casilla_x + casilla_y * DIM_CUADRICULA[0]
            
            # Si la casilla está vacía, ponemos una X (1)
            if array_tablero[index] == 0:
                array_tablero[index] = 1
                print(f"Click en casilla index {index}. Tablero: {array_tablero}")

    return tirada_jugador_hecha, rejugar

# =========================================================================
def dibuja_cuadricula(pygame, pantalla, ancho_casilla, alto_casilla, dimensiones, color):
    """Dibuja la reticula (esto es solo estetico)"""
    for x in range(1, dimensiones[0]):
        pygame.draw.line(pantalla, color, (x * ancho_casilla, 0), (x * ancho_casilla, alto_casilla * dimensiones[1]), 1)
        pygame.draw.line(pantalla, color, (0, x * alto_casilla), (ancho_casilla * dimensiones[1], x * alto_casilla), 1)

# =========================================================================
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

# =========================================================================
def dibuja_o(pygame, pantalla, casilla_index, color=VERDE):
    """Dibuja la X en base al INDEX fijo del tablero, no del ratón"""
    # Convertir el índice del tablero de nuevo a coordenadas de cuadrícula (x, y)
    x = casilla_index % DIM_CUADRICULA[0]
    y = casilla_index // DIM_CUADRICULA[0]

    pygame.draw.circle(pantalla, color,
        (x * SIZE_CASILLA + SIZE_CASILLA // 2, y * SIZE_CASILLA + SIZE_CASILLA // 2), SIZE_CASILLA // 2.3, GROSOR)

# =========================================================================
def dibuja_tablero_dinamicamente(pygame, pantalla, array_tablero):
    # Iteramos usando el INDEX para saber exactamente DONDE dibujar
    for index in range(TOTAL_CASILLAS):
        if array_tablero[index] == 1:
            dibuja_x(pygame, pantalla, index, VERDE)
        elif array_tablero[index] == 2:
            dibuja_o(pygame, pantalla, index, ROJO)

# =========================================================================
def tirada_IA(random, turno, array_tablero):
    """Le toca jugar a la IA"""
    # Return si NO es el turno de la IA:
    if turno:
        return

    # Tablero lleno:
    if 0 not in array_tablero:
        return

    array_backup = array_tablero
    print("backup", array_backup)

    # IA hace 3 en raya (si es posible):
    for i in range(TOTAL_CASILLAS):
        if array_tablero[i] == 0:
            array_backup[i] = 2

            if check_3raya(False, array_backup):
                array_tablero[i] = 2 # 2 representa la ficha de la IA
                print(f"La IA ha elegido la casilla: {i} | Tablero: {array_tablero}")
                return
            else:
                array_backup[i] = 0 # Lo dejamos como estaba

    # Simulamos un tirada del jugador en todas las casillas posibles
    # y si vemos que hay 3 en raya, pues IA tira ahi, defendiendo:
    for i in range(TOTAL_CASILLAS):
        if array_tablero[i] == 0:
            array_backup[i] = 1

            if check_3raya(True, array_backup):
                array_tablero[i] = 2 # 2 representa la ficha de la IA
                print(f"La IA ha elegido la casilla: {i} | Tablero: {array_tablero}")
                return
            else:
                array_backup[i] = 0 # Lo dejamos como estaba

    # Como ultimo recurso, IA tira aleatorio:
    while True:
        casilla_rnd = random.randrange(TOTAL_CASILLAS)
        
        # Si la casilla está vacía (vale 0), la ocupamos
        if array_tablero[casilla_rnd] == 0:
            array_tablero[casilla_rnd] = 2  # 2 representa la ficha de la IA
            print(f"La IA ha elegido la casilla: {casilla_rnd} | Tablero: {array_tablero}")
            break # Salimos del bucle while porque ya encontramos casilla

# =========================================================================
def check_3raya(turno, array_tablero):
    """Checkeamos si ha habido 3 en raya (un ganador)"""
    jugador_ia = 1 if turno else 2

    check_targets = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for target in check_targets:
        if array_tablero[target[0]] == jugador_ia and array_tablero[target[1]] == jugador_ia and array_tablero[target[2]] == jugador_ia:
            return True

    return False




