def is_number(str):
    try:
        _ = float(str)
        return True
    except ValueError:
        return False


# print(is_number("1.2"))
# print(is_number("1"))
# print(is_number("abc"))


def convert_number(str):
    return float(str)


# print(convert_number("1.2"))
# print(convert_number("1"))


def ask_for_a_number(force_valid_input):
    number = None
    while True:
        number = input("Enter a number: ")
        if force_valid_input:
            if not is_number(number):
                print("This didn't look like a number, try again")
                continue
            else:
                return convert_number(number)
        else:
            if not is_number(number):
                return None
            else:
                return convert_number(number)


# print(ask_for_a_number(True))

def is_valid_operator(operator):
    operator_list = ['+', '-', '*', '/']
    if operator in operator_list:
        return True
    else:
        return False


# print(is_valid_operator('z'))

def ask_for_an_operator(force_valid_input):
    operator = None
    while True:
        operator = input("Please provide an operator (one of +, -, *, /)!: ")
        if force_valid_input:
            if is_valid_operator(operator) is False:
                print("Unknown operator")
                continue
            else:
                return operator
        else:
            if is_valid_operator(operator) is False:
                return None
            else:
                return operator


# print(ask_for_an_operator(True))


def calc(operator, a, b):
    # if operator:
    if operator == '+':
        result = a + b
        return result
    elif operator == '-':
        result = a - b
        return result
    elif operator == '*':
        result = a * b
        return result
    elif operator == '/':
        if b != 0:
            result = a / b
            return result
        else:
            print("Error: Division by zero")
    else:
        return None
    # else:
    #     return None


# print(calc('z', 4, 0))

def main():
    while True:
        answer = input("Czy chcesz zakończyć program? (t/n) ")
        if answer == "t":
            print("Koniec programu")
            exit()
        else:
            simple_calculator()


def simple_calculator():
    a = ask_for_a_number(True)
    b = ask_for_a_number(True)
    operator = ask_for_an_operator(True)
    # return calc(operator, a, b)
    print(f"The result is {calc(operator, a, b)}")
    main()


if __name__ == '__main__':
    simple_calculator()



