from SignosCompatibles import *

BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "    COMPATIBILIDAD ENTRE PERSONAS"
TEXTO_PRIMERA_PERSONA = "Primera persona"
TEXTO_SEGUNDA_PERSONA = "Segunda persona"
TEXTO_PEDIR_NOMBRE = "Nombre: "
TEXTO_PEDIR_GENERO = "Género (M/F): "
TEXTO_PEDIR_EDAD = "Edad: "
TEXTO_PEDIR_MUSICA = "Música favorita: "
TEXTO_PEDIR_SIGNO = "Signo zodiacal: "
TEXTO_ERROR_VACIO = "No puede estar vacío"
TEXTO_ERROR_GENERO = "Tienes que responder M o F"
TEXTO_ERROR_SIGNO = "Ese signo no existe (escríbelo sin tildes)"
TEXTO_ERROR_MINIMO = "La edad no puede ser negativa"
TEXTO_ERROR_NO_NUMERO = "Tienes que introducir un número entero"
TEXTO_Y = " y "
TEXTO_COMPATIBLES = " son compatibles"
TEXTO_NO_COMPATIBLES = " no son compatibles"
TEXTO_CONTINUAR = "¿Quieres continuar? (S/N): "
TEXTO_ERROR_RESPUESTA = "Tienes que responder S o N"
RESPUESTA_CONTINUAR = "S"
RESPUESTA_SALIR = "N"
HOMBRE = "M"
MUJER = "F"
EDAD_MINIMA = 0
DIFERENCIA_MAXIMA_EDAD = 10
NOMBRE = 0
GENERO = 1
EDAD = 2
MUSICA = 3
SIGNO = 4
SIGNOS = ['aries', 'tauro', 'geminis', 'cancer', 'leo', 'virgo',
'libra', 'escorpio', 'sagitario', 'capricornio', 'acuario', 'piscis']

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

def PedirPersona(titulo):
    print(titulo)
    nombre = PedirTexto(TEXTO_PEDIR_NOMBRE)
    genero = PedirGenero()
    edad = PedirEdad()
    musica = PedirTexto(TEXTO_PEDIR_MUSICA).lower()
    signo = PedirSigno()
    return (nombre, genero, edad, musica, signo)

def PedirTexto(texto):
    valor = input(texto).strip()
    while not ComprobarTexto(valor):
        valor = input(texto).strip()
    return valor

def ComprobarTexto(valor):
    if valor != "":
        return True
    print(TEXTO_ERROR_VACIO)
    return False

def PedirGenero():
    genero = input(TEXTO_PEDIR_GENERO).strip().upper()
    while not ComprobarGenero(genero):
        genero = input(TEXTO_PEDIR_GENERO).strip().upper()
    return genero

def ComprobarGenero(genero):
    if genero == HOMBRE or genero == MUJER:
        return True
    print(TEXTO_ERROR_GENERO)
    return False

def PedirEdad():
    edad = input(TEXTO_PEDIR_EDAD)
    while not ComprobarEdad(edad):
        edad = input(TEXTO_PEDIR_EDAD)
    return int(edad)

def ComprobarEdad(valor):
    try:
        if int(valor) >= EDAD_MINIMA:
            return True
        print(TEXTO_ERROR_MINIMO)
        return False
    except ValueError:
        print(TEXTO_ERROR_NO_NUMERO)
        return False

def PedirSigno():
    signo = input(TEXTO_PEDIR_SIGNO).strip().lower()
    while not ComprobarSigno(signo):
        signo = input(TEXTO_PEDIR_SIGNO).strip().lower()
    return signo

def ComprobarSigno(signo):
    if signo in SIGNOS:
        return True
    print(TEXTO_ERROR_SIGNO)
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

def Compatibles(p1, p2):
    if p1[GENERO] == p2[GENERO]:
        return False
    if abs(p1[EDAD] - p2[EDAD]) >= DIFERENCIA_MAXIMA_EDAD:
        return False
    if p1[MUSICA] != p2[MUSICA]:
        return False
    if p1[GENERO] == MUJER:
        mujer = p1
        hombre = p2
    else:
        mujer = p2
        hombre = p1
    return (mujer[SIGNO], hombre[SIGNO]) in SIGNOS_COMPATIBLES

def MostrarResultado(p1, p2):
    if Compatibles(p1, p2):
        print(p1[NOMBRE] + TEXTO_Y + p2[NOMBRE] + TEXTO_COMPATIBLES)
    else:
        print(p1[NOMBRE] + TEXTO_Y + p2[NOMBRE] + TEXTO_NO_COMPATIBLES)

EscribirTitulo()
seguir = True
while seguir:
    MostrarResultado(
        PedirPersona(TEXTO_PRIMERA_PERSONA),
        PedirPersona(TEXTO_SEGUNDA_PERSONA)
    )
    seguir = PreguntarContinuar()
