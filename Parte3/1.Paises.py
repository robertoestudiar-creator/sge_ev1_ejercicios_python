BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "               PAÍSES"
TEXTO_PERSONAS = "Personas:"
TEXTO_PEDIR_PRIMERA = "Introduce la primera persona: "
TEXTO_PEDIR_SEGUNDA = "Introduce la segunda persona: "
TEXTO_ERROR_PERSONA = "Esa persona no está en la lista"
TEXTO_RESULTADO = "Países visitados en común: "
TEXTO_CONTINUAR = "¿Quieres continuar? (S/N): "
TEXTO_ERROR_RESPUESTA = "Tienes que responder S o N"
RESPUESTA_CONTINUAR = "S"
RESPUESTA_SALIR = "N"
PAISES = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

def MostrarPersonas():
    print(TEXTO_PERSONAS)
    for persona in PAISES:
        print(persona)

def PedirPersona(texto):
    persona = input(texto).strip().capitalize()
    while not ComprobarPersona(persona):
        persona = input(texto).strip().capitalize()
    return persona

def ComprobarPersona(persona):
    if persona in PAISES:
        return True
    print(TEXTO_ERROR_PERSONA)
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

def CuantosEnComun(a, b):
    cantidad = 0
    for pais in PAISES[a]:
        if pais in PAISES[b]:
            cantidad += 1
    return cantidad

def MostrarResultado(numero):
    print(TEXTO_RESULTADO + str(numero))

EscribirTitulo()
MostrarPersonas()
seguir = True
while seguir:
    MostrarResultado(
        CuantosEnComun(
            PedirPersona(TEXTO_PEDIR_PRIMERA),
            PedirPersona(TEXTO_PEDIR_SEGUNDA)
        )
    )
    seguir = PreguntarContinuar()
