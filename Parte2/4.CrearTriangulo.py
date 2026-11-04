TITLE_BORDER = "-------------------------------------"
TITLE_TEXT = "        CREADOR DE TRIÁNGULOS"
TEXT_ASK_NUMBER = "Introduce la altura del triángulo: "
TEXT_ERROR_MIN = "La altura tiene que ser mayor que 0"
TEXT_ERROR_NOT_NUMBER = "Tienes que introducir un número entero"
TEXT_CONTINUE = "¿Quieres continuar? (S/N): "
TEXT_ERROR_ANSWER = "Tienes que responder S o N"
CONTINUE_ANSWER = "S"
EXIT_ANSWER = "N"
SYMBOL = "*"
MIN_NUMBER = 1


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


def PrintTriangle(number):
    for n in range(1, number + 1):
        print(SYMBOL * n)


WriteTitle()
keepGoing = True
while keepGoing:
    PrintTriangle(
        AskNumber()
    )
    keepGoing = AskContinue()
