preguntaPrimero = "Primer número: "
preguntaSegundo = "Segundo número: "
errorEntero = "Error: tienen que ser números enteros."
errorPositivo = "Error: los dos tienen que ser mayores que 0."
textoResultado = "El MCD es"
respuestaSi = "s"
respuestaNo = "n"
preguntaSeguir = "¿Quieres seguir? (" + respuestaSi + "/" + respuestaNo + "): "
errorSeguir = "Error: escribe " + respuestaSi + " o " + respuestaNo + "."


def MaximoComunDivisor(dividendo, divisor):
    while divisor != 0:
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto
    return dividendo


while True:
    while True:
        try:
            primerNumero = int(input(preguntaPrimero))
            segundoNumero = int(input(preguntaSegundo))
        except ValueError:
            print(errorEntero)
            continue

        if primerNumero > 0 and segundoNumero > 0:
            break
        print(errorPositivo)

    print(textoResultado, MaximoComunDivisor(primerNumero, segundoNumero))

    respuesta = input(preguntaSeguir).strip().lower()
    while respuesta != respuestaSi and respuesta != respuestaNo:
        print(errorSeguir)
        respuesta = input(preguntaSeguir).strip().lower()
    if respuesta == respuestaNo:
        break
