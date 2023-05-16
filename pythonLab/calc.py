INPUT_PROMPT = "Please input an arithmetic expression to evaluate in the following format: {a} {operator} {b}\n"
INPUT_ERROR_PROMPT = "MALFUNCTION! NEED INPUT!"

inputResponse = {
    'q': lambda x: False,
    'quit': lambda x: False
}

operatorFunctions = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y
}


def tryParseExpression(expression):
    args = [element.strip() for element in expression.split(' ')]
    if isValidArithmeticExpression(args):
        result = operatorFunctions.get(args[1])(int(args[0]), int(args[2]))
        print(f'{expression} = {result}')
        return True
    else:
        return invalidInput()


def isValidArithmeticExpression(args):
    return len(args) == 3 \
        and args[0].isdigit() \
        and args[2].isdigit()


def invalidInput():
    print(INPUT_ERROR_PROMPT)
    return True


inputLoop = True
while inputLoop:
    userInput = input(INPUT_PROMPT)
    inputLoop = inputResponse.get(
        userInput.strip().lower(), tryParseExpression)(userInput)
