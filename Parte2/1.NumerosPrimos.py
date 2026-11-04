TITLE_BORDER = "-------------------------------------"
TITLE_TEXT = "            NÚMEROS PRIMOS"
TEXT_ASK_NUMBER = "Introduce la cantidad de números primos a buscar: "
TEXT_ERROR_MIN = "El número tiene que ser mayor que 0"
TEXT_ERROR_NOT_NUMBER = "Tienes que introducir un número entero"
TEXT_CONTINUE = "¿Quieres continuar? (S/N): "
TEXT_ERROR_ANSWER = "Tienes que responder S o N"
CONTINUE_ANSWER = "S"
EXIT_ANSWER = "N"
MIN_NUMBER = 1
FIRST_PRIME = 2


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


def SearchPrimeNumbers(num):
    primeNumbers = []
    n = FIRST_PRIME
    while len(primeNumbers) < num:
        if IsPrime(n):
            primeNumbers.append(n)
        n += 1
    return primeNumbers


#Para comprobar si es primo, prueba a dividirlo entre todos los números desde el 2 hasta el anterior a él; si ninguno da resto 0, devuelve True
def IsPrime(num):
    for n in range(FIRST_PRIME, num):
        if num % n == 0:
            return False
    return True


def PrintNumbers(numbers):
    for n in numbers:
        print(n)


WriteTitle()
keepGoing = True
while keepGoing:
    PrintNumbers(
        SearchPrimeNumbers(
            AskNumber()
        )
    )
    keepGoing = AskContinue()
