BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "               ZODIACO"
TEXTO_PEDIR_ANIO = "Introduce el año de nacimiento: "
TEXTO_PEDIR_MES = "Introduce el mes de nacimiento: "
TEXTO_PEDIR_DIA = "Introduce el día de nacimiento: "
TEXTO_ERROR_RANGO = "El número tiene que estar entre "
TEXTO_Y = " y "
TEXTO_ERROR_NO_NUMERO = "Tienes que introducir un número entero"
TEXTO_RESULTADO = "Tu signo es: "
TEXTO_CONTINUAR = "¿Quieres continuar? (S/N): "
TEXTO_ERROR_RESPUESTA = "Tienes que responder S o N"
RESPUESTA_CONTINUAR = "S"
RESPUESTA_SALIR = "N"
MIN_ANIO = 1900
MAX_ANIO = 2100
MIN_MES = 1
MAX_MES = 12
MIN_DIA = 1
MAX_DIA = 31
SIGNOS = {
    'aries':       ((3, 21), (4, 20)),
    'tauro':       ((4, 21), (5, 21)),
    'geminis':     ((5, 22), (6, 21)),
    'cancer':      ((6, 22), (7, 23)),
    'leo':         ((7, 24), (8, 23)),
    'virgo':       ((8, 24), (9, 23)),
    'libra':       ((9, 24), (10, 23)),
    'escorpio':    ((10, 24), (11, 22)),
    'sagitario':   ((11, 23), (12, 21)),
    'capricornio': ((12, 22), (1, 20)),
    'acuario':     ((1, 21), (2, 19)),
    'piscis':      ((2, 20), (3, 20)),
}

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

def PedirFechaNacimiento():
    anio = PedirNumero(TEXTO_PEDIR_ANIO, MIN_ANIO, MAX_ANIO)
    mes = PedirNumero(TEXTO_PEDIR_MES, MIN_MES, MAX_MES)
    dia = PedirNumero(TEXTO_PEDIR_DIA, MIN_DIA, MAX_DIA)
    return (anio, mes, dia)

def PedirNumero(texto, minimo, maximo):
    numeroPedido = input(texto)
    while not ComprobarNumero(numeroPedido, minimo, maximo):
        numeroPedido = input(texto)
    return int(numeroPedido)

def ComprobarNumero(valor, minimo, maximo):
    try:
        if minimo <= int(valor) <= maximo:
            return True
        print(TEXTO_ERROR_RANGO + str(minimo) + TEXTO_Y + str(maximo))
        return False
    except ValueError:
        print(TEXTO_ERROR_NO_NUMERO)
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

def DeterminarSigno(fechaDeNacimiento):
    mes = fechaDeNacimiento[1]
    dia = fechaDeNacimiento[2]
    for signo in SIGNOS:
        inicio = SIGNOS[signo][0]
        fin = SIGNOS[signo][1]
        mesInicio = inicio[0]
        diaInicio = inicio[1]
        mesFin = fin[0]
        diaFin = fin[1]
        if mes == mesInicio and dia >= diaInicio:
            return signo
        if mes == mesFin and dia <= diaFin:
            return signo

def MostrarSigno(signo):
    print(TEXTO_RESULTADO + signo)

EscribirTitulo()
seguir = True
while seguir:
    MostrarSigno(
        DeterminarSigno(
            PedirFechaNacimiento()
        )
    )
    seguir = PreguntarContinuar()
