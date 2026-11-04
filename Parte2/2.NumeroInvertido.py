TITLE_BORDER = "-------------------------------------"
TITLE_TEXT = "           NÚMERO INVERTIDO"
TEXT_ASK_NUMBER = "Introduce un número de tres dígitos: "
TEXT_ERROR_DIGITS = "El número tiene que tener tres dígitos"
TEXT_ERROR_NOT_NUMBER = "Tienes que introducir un número entero"
TEXT_RESULT = "El número invertido es: "
TEXT_CONTINUE = "¿Quieres continuar? (S/N): "
TEXT_ERROR_ANSWER = "Tienes que responder S o N"
CONTINUE_ANSWER = "S"
EXIT_ANSWER = "N"
MIN_NUMBER = 100
MAX_NUMBER = 999


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
        if MIN_NUMBER <= int(value) <= MAX_NUMBER:
            return True
        print(TEXT_ERROR_DIGITS)
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


#Separa el número en centenas, decenas y unidades y lo vuelve a montar con las cifras al revés: las unidades pasan a centenas y las centenas a unidades.
def ReverseNumber(num):
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    return units * 100 + tens * 10 + hundreds


def PrintNumber(number):
    print(TEXT_RESULT + str(number))


WriteTitle()
keepGoing = True
while keepGoing:
    PrintNumber(
        ReverseNumber(
            AskNumber()
        )
    )
    keepGoing = AskContinue()
