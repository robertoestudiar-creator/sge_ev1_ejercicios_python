BORDE_TITULO = "-------------------------------------"
TEXTO_TITULO = "        PRODUCCIÓN DE COCHES"
TEXTO_UNIDADES = "Unidades semanales necesarias:"
TEXTO_COSTES_COCHE = "Coste total de un coche de cada modelo:"
TEXTO_DOS_PUNTOS = ": "
TEXTO_TOTAL = "Coste total de la producción semanal: "
MODELOS = ['Sedán', 'Camioneta', 'Económico']
CONCEPTOS = ['Material', 'Personal', 'Impuestos', 'Transporte']
COSTES = [
    [7, 8, 5],
    [10, 9, 7],
    [5, 3, 2],
    [2, 3, 1],
]
PRODUCCION_SEMANAL = [60, 40, 90]
PRECIOS_UNIDAD = [5, 15, 7, 2]

def EscribirTitulo():
    print(BORDE_TITULO)
    print(TEXTO_TITULO)
    print(BORDE_TITULO)

def CalcularUnidadesSemanales(costes, produccion):
    unidades = []
    for concepto in range(len(CONCEPTOS)):
        total = 0
        for modelo in range(len(MODELOS)):
            total += costes[concepto][modelo] * produccion[modelo]
        unidades.append(total)
    return unidades

def CalcularCostesCoche(costes, precios):
    costesCoche = []
    for modelo in range(len(MODELOS)):
        total = 0
        for concepto in range(len(CONCEPTOS)):
            total += costes[concepto][modelo] * precios[concepto]
        costesCoche.append(total)
    return costesCoche

def CalcularCosteSemanal(costesCoche, produccion):
    total = 0
    for modelo in range(len(MODELOS)):
        total += costesCoche[modelo] * produccion[modelo]
    return total

def MostrarLista(titulo, nombres, valores):
    print(titulo)
    for n in range(len(nombres)):
        print(nombres[n] + TEXTO_DOS_PUNTOS + str(valores[n]))

EscribirTitulo()
costesCoche = CalcularCostesCoche(COSTES, PRECIOS_UNIDAD)
MostrarLista(TEXTO_UNIDADES, CONCEPTOS, CalcularUnidadesSemanales(COSTES, PRODUCCION_SEMANAL))
MostrarLista(TEXTO_COSTES_COCHE, MODELOS, costesCoche)
print(TEXTO_TOTAL + str(CalcularCosteSemanal(costesCoche, PRODUCCION_SEMANAL)))
