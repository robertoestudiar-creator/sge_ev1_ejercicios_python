import math

textoTitulo = "Ecuación de segundo grado: ax^2 + bx + c = 0"
preguntaA = "Introduce a: "
preguntaB = "Introduce b: "
preguntaC = "Introduce c: "
errorNumero = "Error: a, b y c tienen que ser números."
textoNoValida = "Esa ecuación no es válida."
textoPrimerGrado = "No es de segundo grado. x ="
textoX1 = "x1 ="
textoX2 = "x2 ="
textoSinSoluciones = "No tiene soluciones reales."
respuestaSi = "s"
respuestaNo = "n"
preguntaSeguir = "¿Quieres seguir? (" + respuestaSi + "/" + respuestaNo + "): "
errorSeguir = "Error: escribe " + respuestaSi + " o " + respuestaNo + "."

while True:
    print(textoTitulo)

    while True:
        try:
            a = float(input(preguntaA))
            b = float(input(preguntaB))
            c = float(input(preguntaC))
            break
        except ValueError:
            print(errorNumero)

    if a == 0:
        if b == 0:
            print(textoNoValida)
        else:
            x = -c / b
            print(textoPrimerGrado, x)
    else:
        discriminante = b ** 2 - 4 * a * c

        if discriminante >= 0:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            print(textoX1, x1)
            print(textoX2, x2)
        else:
            print(textoSinSoluciones)

    respuesta = input(preguntaSeguir).strip().lower()
    while respuesta != respuestaSi and respuesta != respuestaNo:
        print(errorSeguir)
        respuesta = input(preguntaSeguir).strip().lower()
    if respuesta == respuestaNo:
        break
