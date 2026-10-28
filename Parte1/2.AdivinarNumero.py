import random

minimo = 1
maximo = 100

textoTitulo = "Adivina el número entre " + str(minimo) + " y " + str(maximo)
preguntaNumero = "Tu número: "
errorEntero = "Error: tiene que ser un número entero."
errorRango = "Error: tiene que estar entre " + str(minimo) + " y " + str(maximo) + "."
textoMayor = "Mayor"
textoMenor = "Menor"
textoAcierto = "Has acertado, era el"
textoIntentos = "Intentos:"
respuestaSi = "s"
respuestaNo = "n"
preguntaSeguir = "¿Quieres seguir? (" + respuestaSi + "/" + respuestaNo + "): "
errorSeguir = "Error: escribe " + respuestaSi + " o " + respuestaNo + "."

while True:
    numeroAleatorio = random.randint(minimo, maximo)
    intentos = 0
    acertado = False

    print(textoTitulo)
    while not acertado:
        try:
            numeroIntroducido = int(input(preguntaNumero))
        except ValueError:
            print(errorEntero)
            continue

        if numeroIntroducido < minimo or numeroIntroducido > maximo:
            print(errorRango)
            continue

        intentos = intentos + 1

        if numeroIntroducido < numeroAleatorio:
            print(textoMayor)
        elif numeroIntroducido > numeroAleatorio:
            print(textoMenor)
        else:
            acertado = True

    print(textoAcierto, numeroAleatorio)
    print(textoIntentos, intentos)

    respuesta = input(preguntaSeguir).strip().lower()
    while respuesta != respuestaSi and respuesta != respuestaNo:
        print(errorSeguir)
        respuesta = input(preguntaSeguir).strip().lower()
    if respuesta == respuestaNo:
        break
