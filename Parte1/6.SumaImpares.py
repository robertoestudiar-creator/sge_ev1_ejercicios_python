preguntaCantidad = "Cuántos impares quieres sumar: "
errorEntero = "Error: tiene que ser un número entero."
errorPositivo = "Error: tiene que ser mayor que 0."
textoResultado = "La suma es"
respuestaSi = "s"
respuestaNo = "n"
preguntaSeguir = "¿Quieres seguir? (" + respuestaSi + "/" + respuestaNo + "): "
errorSeguir = "Error: escribe " + respuestaSi + " o " + respuestaNo + "."


def SumaImpares(cantidad):
    suma = 0
    impar = 1
    for i in range(cantidad):
        suma = suma + impar
        impar = impar + 2
    return suma


while True:
    while True:
        try:
            cantidad = int(input(preguntaCantidad))
        except ValueError:
            print(errorEntero)
            continue

        if cantidad > 0:
            break
        print(errorPositivo)

    print(textoResultado, SumaImpares(cantidad))

    respuesta = input(preguntaSeguir).strip().lower()
    while respuesta != respuestaSi and respuesta != respuestaNo:
        print(errorSeguir)
        respuesta = input(preguntaSeguir).strip().lower()
    if respuesta == respuestaNo:
        break
