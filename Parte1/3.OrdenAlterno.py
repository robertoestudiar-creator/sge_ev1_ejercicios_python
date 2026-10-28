cantidadNumeros = 10

preguntaNumero = "Número: "
errorEntero = "Error: tiene que ser un número entero."
textoResultado = "Resultado:"
respuestaSi = "s"
respuestaNo = "n"
preguntaSeguir = "¿Quieres seguir? (" + respuestaSi + "/" + respuestaNo + "): "
errorSeguir = "Error: escribe " + respuestaSi + " o " + respuestaNo + "."

while True:
    numeros = []
    while len(numeros) < cantidadNumeros:
        try:
            numero = int(input(preguntaNumero))
            numeros.append(numero)
        except ValueError:
            print(errorEntero)

    ordenAlterno = []
    for i in range(cantidadNumeros // 2):
        ordenAlterno.append(numeros[i])
        ordenAlterno.append(numeros[cantidadNumeros - 1 - i])
    if cantidadNumeros % 2 == 1:
        ordenAlterno.append(numeros[cantidadNumeros // 2])

    print(textoResultado, ordenAlterno)

    respuesta = input(preguntaSeguir).strip().lower()
    while respuesta != respuestaSi and respuesta != respuestaNo:
        print(errorSeguir)
        respuesta = input(preguntaSeguir).strip().lower()
    if respuesta == respuestaNo:
        break
