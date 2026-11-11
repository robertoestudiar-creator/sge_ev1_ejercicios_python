from Personas import *

BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "              PERSONAS"
TEXTO_NOMBRES = "Nombres:"
TEXTO_FECHAS = "Fechas de nacimiento:"
TEXTO_CANTIDAD = "Cantidad de personas: "
TEXTO_REPETIDOS = "Cumpleaños repetidos:"
TEXTO_MAS_COMUN = "El nombre más común es: "
TEXTO_PEDIR_DIA = "Introduce el día de tu cumpleaños: "
TEXTO_PEDIR_MES = "Introduce el mes de tu cumpleaños: "
TEXTO_ERROR_RANGO = "El número tiene que estar entre "
TEXTO_Y = " y "
TEXTO_ERROR_NO_NUMERO = "Tienes que introducir un número entero"
TEXTO_DE = " de "
TEXTO_GUION = " - "
TEXTO_ESPACIO = " "
TEXTO_MI_CUMPLE = "Cumplen años el mismo día que tú:"
TEXTO_NADIE = "Nadie"
TEXTO_CONTINUAR = "¿Quieres continuar? (S/N): "
TEXTO_ERROR_RESPUESTA = "Tienes que responder S o N"
RESPUESTA_CONTINUAR = "S"
RESPUESTA_SALIR = "N"
MIN_DIA = 1
MAX_DIA = 31
MIN_MES = 1
MAX_MES = 12
NOMBRE = 0
APELLIDO = 1
FECHA = 2
DIA = 0
MES = 1
ANIO = 2
MESES = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre',
}

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

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

def NombreCompleto(persona):
    return persona[NOMBRE] + TEXTO_ESPACIO + persona[APELLIDO]

def ImprimirNombres(personas):
    for persona in personas:
        print(persona[NOMBRE])

def ImprimirFechas(personas):
    for persona in personas:
        fecha = persona[FECHA]
        print(str(fecha[DIA]) + TEXTO_DE + MESES[fecha[MES]] + TEXTO_DE + str(fecha[ANIO]))

def CuantasPersonas(personas):
    return len(personas)

def MiCumple(personas):
    miDia = PedirNumero(TEXTO_PEDIR_DIA, MIN_DIA, MAX_DIA)
    miMes = PedirNumero(TEXTO_PEDIR_MES, MIN_MES, MAX_MES)
    mismoDia = []
    for persona in personas:
        fecha = persona[FECHA]
        if fecha[DIA] == miDia and fecha[MES] == miMes:
            mismoDia.append(NombreCompleto(persona))
    return mismoDia

def MismoCumple(persona, otra):
    fecha = persona[FECHA]
    otraFecha = otra[FECHA]
    return fecha[DIA] == otraFecha[DIA] and fecha[MES] == otraFecha[MES]

def CumplesRepetidos(personas):
    repetidos = []
    for persona in personas:
        for otra in personas:
            if persona != otra and MismoCumple(persona, otra):
                if persona not in repetidos:
                    repetidos.append(persona)
    return repetidos

def NombreMasComun(personas):
    cuentas = {}
    for persona in personas:
        nombre = persona[NOMBRE]
        if nombre not in cuentas:
            cuentas[nombre] = 0
        cuentas[nombre] += 1

    masComun = ""
    maximo = 0
    for nombre in cuentas:
        if cuentas[nombre] > maximo:
            masComun = nombre
            maximo = cuentas[nombre]
    return masComun

def MostrarCumplesRepetidos(personas):
    for persona in CumplesRepetidos(personas):
        fecha = persona[FECHA]
        print(NombreCompleto(persona) + TEXTO_GUION + str(fecha[DIA]) + TEXTO_DE + MESES[fecha[MES]])

def MostrarMiCumple(mismoDia):
    print(TEXTO_MI_CUMPLE)
    if len(mismoDia) == 0:
        print(TEXTO_NADIE)
    for nombre in mismoDia:
        print(nombre)

EscribirTitulo()
print(TEXTO_NOMBRES)
ImprimirNombres(PERSONAS)
print(TEXTO_FECHAS)
ImprimirFechas(PERSONAS)
print(TEXTO_CANTIDAD + str(CuantasPersonas(PERSONAS)))
print(TEXTO_REPETIDOS)
MostrarCumplesRepetidos(PERSONAS)
print(TEXTO_MAS_COMUN + NombreMasComun(PERSONAS))
seguir = True
while seguir:
    MostrarMiCumple(
        MiCumple(PERSONAS)
    )
    seguir = PreguntarContinuar()
