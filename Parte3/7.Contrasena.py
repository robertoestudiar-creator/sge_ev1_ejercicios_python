BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "             CONTRASEÑA"
TEXTO_PEDIR_FRASE = "Introduce la frase: "
TEXTO_PEDIR_CANTIDAD = "¿Cuántos caracteres quieres reemplazar?: "
TEXTO_PEDIR_CARACTER = "Carácter a reemplazar: "
TEXTO_PEDIR_REEMPLAZO = "Reemplazarlo por (vacío para borrarlo): "
TEXTO_PEDIR_VECES = "¿Cuántas veces cambiar cada carácter? (0 = todas): "
TEXTO_ERROR_VACIA = "La frase no puede estar vacía"
TEXTO_ERROR_CARACTER = "Tiene que ser un solo carácter"
TEXTO_ERROR_REPETIDO = "Ese carácter ya está en la lista"
TEXTO_ERROR_MINIMO = "El número tiene que ser como mínimo "
TEXTO_ERROR_NO_NUMERO = "Tienes que introducir un número entero"
TEXTO_RESULTADO = "La contraseña es: "
TEXTO_CONTINUAR = "¿Quieres continuar? (S/N): "
TEXTO_ERROR_RESPUESTA = "Tienes que responder S o N"
RESPUESTA_CONTINUAR = "S"
RESPUESTA_SALIR = "N"
CANTIDAD_MINIMA = 1
VECES_MINIMAS = 0
TODAS_LAS_VECES = 0

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

def PedirFrase():
    frase = input(TEXTO_PEDIR_FRASE)
    while not ComprobarFrase(frase):
        frase = input(TEXTO_PEDIR_FRASE)
    return frase

def ComprobarFrase(frase):
    if frase.strip() != "":
        return True
    print(TEXTO_ERROR_VACIA)
    return False

def PedirNumero(texto, minimo):
    numeroPedido = input(texto)
    while not ComprobarNumero(numeroPedido, minimo):
        numeroPedido = input(texto)
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

def PedirDiccionario():
    diccionario = {}
    cantidad = PedirNumero(TEXTO_PEDIR_CANTIDAD, CANTIDAD_MINIMA)
    while len(diccionario) < cantidad:
        caracter = input(TEXTO_PEDIR_CARACTER)
        if ComprobarCaracter(caracter, diccionario):
            diccionario[caracter] = input(TEXTO_PEDIR_REEMPLAZO)
    return diccionario

def ComprobarCaracter(caracter, diccionario):
    if len(caracter) != 1:
        print(TEXTO_ERROR_CARACTER)
        return False
    if caracter in diccionario:
        print(TEXTO_ERROR_REPETIDO)
        return False
    return True

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

def Cambia(frase, diccionario, veces=TODAS_LAS_VECES):
    for caracter in diccionario:
        if veces == TODAS_LAS_VECES:
            frase = frase.replace(str(caracter), str(diccionario[caracter]))
        else:
            frase = frase.replace(str(caracter), str(diccionario[caracter]), veces)
    return frase

def MostrarContrasena(contrasena):
    print(TEXTO_RESULTADO + contrasena)

EscribirTitulo()
seguir = True
while seguir:
    MostrarContrasena(
        Cambia(
            PedirFrase(),
            PedirDiccionario(),
            PedirNumero(TEXTO_PEDIR_VECES, VECES_MINIMAS)
        )
    )
    seguir = PreguntarContinuar()
