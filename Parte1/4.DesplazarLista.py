cantidadNumeros = 10

preguntaNumero = "Número: "
errorEntero = "Error: tiene que ser un número entero."
textoOriginal = "Lista original:"
textoDesplazada = "Lista desplazada:"
respuestaSi = "s"
respuestaNo = "n"
preguntaSeguir = "¿Quieres seguir? (" + respuestaSi + "/" + respuestaNo + "): "
errorSeguir = "Error: escribe " + respuestaSi + " o " + respuestaNo + "."

while True:
    lista = []
    while len(lista) < cantidadNumeros:
        try:
            numero = int(input(preguntaNumero))
            lista.append(numero)
        except ValueError:
            print(errorEntero)

    print(textoOriginal, lista)

    listaDesplazada = [lista[cantidadNumeros - 1]]
    for i in range(cantidadNumeros - 1):
        listaDesplazada.append(lista[i])

    print(textoDesplazada, listaDesplazada)

    respuesta = input(preguntaSeguir).strip().lower()
    while respuesta != respuestaSi and respuesta != respuestaNo:
        print(errorSeguir)
        respuesta = input(preguntaSeguir).strip().lower()
    if respuesta == respuestaNo:
        break
