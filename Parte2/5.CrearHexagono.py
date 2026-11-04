TITLE_BORDER = "-------------------------------------"
TITLE_TEXT = "         CREADOR DE HEXÁGONOS"
TEXT_ASK_NUMBER = "Introduce el lado del hexágono: "
TEXT_ERROR_MIN = "El lado tiene que ser mayor que 0"
TEXT_ERROR_NOT_NUMBER = "Tienes que introducir un número entero"
TEXT_CONTINUE = "¿Quieres continuar? (S/N): "
TEXT_ERROR_ANSWER = "Tienes que responder S o N"
CONTINUE_ANSWER = "S"
EXIT_ANSWER = "N"
SYMBOL = "*"
MIN_NUMBER = 1
SIDES = 2
MULTIPLIER = 3
REDUCTION = 2
GROWTH = 2


def WriteTitle():
    print(TITLE_BORDER)
    print(TITLE_TEXT)
    print(TITLE_BORDER)


def AskNumber():
    numberAsked = input(TEXT_ASK_NUMBER)
    while not CheckNumber(numberAsked):
        numberAsked = input(TEXT_ASK_NUMBER)
    return int(numberAsked)


def CheckNumber(value):
    try:
        if int(value) >= MIN_NUMBER:
            return True
        print(TEXT_ERROR_MIN)
        return False
    except ValueError:
        print(TEXT_ERROR_NOT_NUMBER)
        return False


def AskContinue():
    answer = input(TEXT_CONTINUE).strip().upper()
    while not CheckAnswer(answer):
        answer = input(TEXT_CONTINUE).strip().upper()
    if answer == EXIT_ANSWER:
        return False
    return True


def CheckAnswer(answer):
    if answer == CONTINUE_ANSWER or answer == EXIT_ANSWER:
        return True
    print(TEXT_ERROR_ANSWER)
    return False


#Pinta el hexágono en 3 partes: la de arriba (va creciendo), la fila del centro (la más ancha) y la de abajo (va decreciendo)
def PrintHexagon(side):
    maxWidth = side * MULTIPLIER - REDUCTION
    PrintTop(side, maxWidth)
    PrintLine(maxWidth, maxWidth)
    PrintBottom(side, maxWidth)


#Parte de arriba: la primera fila tiene tantos asteriscos como el lado y cada fila suma 2 (uno por cada lado) hasta quedarse justo antes de la fila del centro
def PrintTop(side, maxWidth):
    for n in range(side, maxWidth, GROWTH):
        PrintLine(n, maxWidth)


#Parte de abajo: lo mismo que la de arriba pero al revés, empieza con 2 asteriscos menos que la fila del centro y va restando 2 hasta llegar otra vez al lado
def PrintBottom(side, maxWidth):
    for n in range(maxWidth - GROWTH, side - GROWTH, -GROWTH):
        PrintLine(n, maxWidth)


def PrintLine(asterisks, maxWidth):
    spaces = (maxWidth - asterisks) // SIDES
    print(" " * spaces + SYMBOL * asterisks)


WriteTitle()
keepGoing = True
while keepGoing:
    PrintHexagon(
        AskNumber()
    )
    keepGoing = AskContinue()
