BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "             DISTANCIAS"
TEXTO_PEDIR_CIUDADES = "¿Cuántas ciudades?"
TEXTO_INGRESE_NOMBRES = "Ingrese los nombres:"
TEXTO_PEDIR_DISTANCIA = "¿Distancia "
TEXTO_GUION = "-"
TEXTO_FIN_PREGUNTA = "?"
TEXTO_PEDIR_ITINERARIO = "¿Cuántas ciudades tiene el itinerario?"
TEXTO_INGRESE_ITINERARIO = "Ingrese las ciudades del itinerario:"
TEXTO_ERROR_VACIO = "El nombre no puede estar vacío"
TEXTO_ERROR_REPETIDA = "Esa ciudad ya está en la lista"
TEXTO_ERROR_CIUDAD = "Esa ciudad no está en la lista"
TEXTO_ERROR_MINIMO = "El número tiene que ser como mínimo "
TEXTO_ERROR_NO_NUMERO = "Tienes que introducir un número entero"
TEXTO_CONTINUAR = "¿Quieres continuar? (S/N): "
TEXTO_ERROR_RESPUESTA = "Tienes que responder S o N"
RESPUESTA_CONTINUAR = "S"
RESPUESTA_SALIR = "N"
MIN_CIUDADES = 2
MIN_DISTANCIA = 1

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

def PedirNumero(texto, minimo):
    print(texto)
    numeroPedido = input()
    while not ComprobarNumero(numeroPedido, minimo):
        print(texto)
        numeroPedido = input()
    return int(numeroPedido)

def ComprobarNumero(valor, minimo):
    try:
        if int(valor) >= minimo:
            return True
        print(TEXTO_ERROR_MINIMO + str(minimo))
        return False
    except ValueError:
        print(TEXTO_ERROR_NO_NUMERO)
        return False

def PedirCiudades():
    cantidad = PedirNumero(TEXTO_PEDIR_CIUDADES, MIN_CIUDADES)
    print(TEXTO_INGRESE_NOMBRES)
    ciudades = []
    while len(ciudades) < cantidad:
        ciudad = input().strip()
        if ComprobarCiudadNueva(ciudad, ciudades):
            ciudades.append(ciudad)
    return ciudades

def ComprobarCiudadNueva(ciudad, ciudades):
    if ciudad == "":
        print(TEXTO_ERROR_VACIO)
        return False
    if ciudad in ciudades:
        print(TEXTO_ERROR_REPETIDA)
        return False
    return True

def PedirDistancias(ciudades):
    distancias = []
    for i in range(len(ciudades)):
        fila = []
        for j in range(len(ciudades)):
            if i == j:
                fila.append(0)
            elif j < i:
                fila.append(distancias[j][i])
            else:
                pregunta = TEXTO_PEDIR_DISTANCIA + ciudades[i] + TEXTO_GUION + ciudades[j] + TEXTO_FIN_PREGUNTA
                fila.append(PedirNumero(pregunta, MIN_DISTANCIA))
        distancias.append(fila)
    return distancias

def PedirItinerario(ciudades):
    cantidad = PedirNumero(TEXTO_PEDIR_ITINERARIO, MIN_CIUDADES)
    print(TEXTO_INGRESE_ITINERARIO)
    itinerario = []
    while len(itinerario) < cantidad:
        ciudad = input().strip()
        if ComprobarCiudad(ciudad, ciudades):
            itinerario.append(ciudad)
    return itinerario

def ComprobarCiudad(ciudad, ciudades):
    if ciudad in ciudades:
        return True
    print(TEXTO_ERROR_CIUDAD)
    return False

def Kms(itinerario, ciudades, distancias):
    total = 0
    for n in range(len(itinerario) - 1):
        origen = ciudades.index(itinerario[n])
        destino = ciudades.index(itinerario[n + 1])
        total += distancias[origen][destino]
    return total

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

def MostrarKms(total):
    print(total)

EscribirTitulo()
listaCiudades = PedirCiudades()
tablaDistancias = PedirDistancias(listaCiudades)
seguir = True
while seguir:
    MostrarKms(
        Kms(
            PedirItinerario(listaCiudades),
            listaCiudades,
            tablaDistancias
        )
    )
    seguir = PreguntarContinuar()
