BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "        CAMPEONATO DE FÚTBOL"
TEXTO_EQUIPOS = "Equipos:"
TEXTO_POSICIONES = "Tabla de Posiciones:"
TEXTO_PUNTO = ". "
TEXTO_GUION = " - "
TEXTO_PUNTOS_DIFERENCIA = " puntos, diferencia "
TEXTO_PEDIR_EQUIPO = "Introduce un equipo: "
TEXTO_ERROR_EQUIPO = "Ese equipo no ha jugado el campeonato"
TEXTO_PUNTOS = "Puntos: "
TEXTO_DIFERENCIA = "Diferencia de goles: "
TEXTO_CONTINUAR = "¿Quieres continuar? (S/N): "
TEXTO_ERROR_RESPUESTA = "Tienes que responder S o N"
RESPUESTA_CONTINUAR = "S"
RESPUESTA_SALIR = "N"
PUNTOS_VICTORIA = 3
PUNTOS_EMPATE = 1
RESULTADOS = {
    ('Honduras', 'Chile'):    (0, 1),
    ('España',   'Suiza'):    (0, 1),
    ('Suiza',    'Chile'):    (0, 1),
    ('España',   'Honduras'): (3, 0),
    ('Suiza',    'Honduras'): (0, 0),
    ('España',   'Chile'):    (2, 1),
}

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

def PedirEquipo():
    equipo = input(TEXTO_PEDIR_EQUIPO).strip().capitalize()
    while not ComprobarEquipo(equipo):
        equipo = input(TEXTO_PEDIR_EQUIPO).strip().capitalize()
    return equipo

def ComprobarEquipo(equipo):
    if equipo in ObtenerListaEquipos(RESULTADOS):
        return True
    print(TEXTO_ERROR_EQUIPO)
    return False

def PreguntarContinuar():
    respuesta = input(TEXTO_CONTINUAR).strip().upper()
    while not ComprobarRespuesta(respuesta):
        respuesta = input(TEXTO_CONTINUAR).strip().upper()
    if respuesta == RESPUESTA_SALIR:
        return False
    return True

def ComprobarRespuesta(respuesta):
    if respuesta == RESPUESTA_CONTINUAR or respuesta == RESPUESTA_SALIR:
        return True
    print(TEXTO_ERROR_RESPUESTA)
    return False

def ObtenerListaEquipos(resultados):
    equipos = []
    for partido in resultados:
        for equipo in partido:
            if equipo not in equipos:
                equipos.append(equipo)
    return equipos

def GolesMarcados(equipo, partido, goles):
    if partido[0] == equipo:
        return goles[0]
    return goles[1]

def GolesRecibidos(equipo, partido, goles):
    if partido[0] == equipo:
        return goles[1]
    return goles[0]

def CalcularPuntos(equipo, resultados):
    puntos = 0
    for partido in resultados:
        if equipo in partido:
            marcados = GolesMarcados(equipo, partido, resultados[partido])
            recibidos = GolesRecibidos(equipo, partido, resultados[partido])
            if marcados > recibidos:
                puntos += PUNTOS_VICTORIA
            elif marcados == recibidos:
                puntos += PUNTOS_EMPATE
    return puntos

def CalcularDiferenciaDeGoles(equipo, resultados):
    diferencia = 0
    for partido in resultados:
        if equipo in partido:
            diferencia += GolesMarcados(equipo, partido, resultados[partido]) - GolesRecibidos(equipo, partido, resultados[partido])
    return diferencia

def CalcularGolesTotales(equipo, resultados):
    total = 0
    for partido in resultados:
        if equipo in partido:
            total += GolesMarcados(equipo, partido, resultados[partido])
    return total

def VaPorDelante(primero, segundo, resultados):
    puntosPrimero = CalcularPuntos(primero, resultados)
    puntosSegundo = CalcularPuntos(segundo, resultados)
    if puntosPrimero != puntosSegundo:
        return puntosPrimero > puntosSegundo
    diferenciaPrimero = CalcularDiferenciaDeGoles(primero, resultados)
    diferenciaSegundo = CalcularDiferenciaDeGoles(segundo, resultados)
    if diferenciaPrimero != diferenciaSegundo:
        return diferenciaPrimero > diferenciaSegundo
    return CalcularGolesTotales(primero, resultados) > CalcularGolesTotales(segundo, resultados)

def Posiciones(resultados):
    equipos = ObtenerListaEquipos(resultados)
    tabla = []
    while len(equipos) > 0:
        mejor = equipos[0]
        for equipo in equipos:
            if VaPorDelante(equipo, mejor, resultados):
                mejor = equipo
        tabla.append(mejor)
        equipos.remove(mejor)
    return tabla

def MostrarEquipos(resultados):
    print(TEXTO_EQUIPOS)
    for equipo in ObtenerListaEquipos(resultados):
        print(equipo)

def MostrarPosiciones(resultados):
    print(TEXTO_POSICIONES)
    posicion = 1
    for equipo in Posiciones(resultados):
        puntos = CalcularPuntos(equipo, resultados)
        diferencia = CalcularDiferenciaDeGoles(equipo, resultados)
        print(str(posicion) + TEXTO_PUNTO + equipo + TEXTO_GUION + str(puntos) + TEXTO_PUNTOS_DIFERENCIA + str(diferencia))
        posicion += 1

def MostrarDatosEquipo(equipo, resultados):
    print(TEXTO_PUNTOS + str(CalcularPuntos(equipo, resultados)))
    print(TEXTO_DIFERENCIA + str(CalcularDiferenciaDeGoles(equipo, resultados)))

EscribirTitulo()
MostrarEquipos(RESULTADOS)
MostrarPosiciones(RESULTADOS)
seguir = True
while seguir:
    MostrarDatosEquipo(
        PedirEquipo(),
        RESULTADOS
    )
    seguir = PreguntarContinuar()
