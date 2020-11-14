def check_if_opening_round_bracket(symbol):
    if symbol == "(":
        return True
    else:
        return False


def check_if_closing_round_bracket(symbol):
    if symbol == ")":
        return True
    else:
        return False


def check_if_operator(symbol):
    if symbol == "&" or symbol == "|":
        return True
    else:
        return False


def check_if_variable_or_constant(symbol):
    variables_and_constants = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "0", "1"]
    if symbol in variables_and_constants:
        return True
    else:
        return False


def check_if_negation(symbol):
    if symbol == "~":
        return True
    else:
        return False


def check_if_blank(symbol):
    if symbol == " ":
        return True
    else:
        return False


def check_if_logical_expression_is_correct(expression):
    state = "letter state"
    counter = 0
    variable_used_after_negation = True
    variable_used_after_operator = True
    variable_used = False
    for i in expression:
        if counter < 0:
            return False

        if state == "letter state":
            if check_if_blank(i):
                pass
            elif check_if_negation(i):
                variable_used_after_negation = False
            elif check_if_closing_round_bracket(i):
                return False
            elif check_if_operator(i):
                return False
            elif check_if_opening_round_bracket(i):
                counter += 1
            elif check_if_variable_or_constant(i):
                variable_used_after_negation = True
                variable_used_after_operator = True
                variable_used = True
            else:
                return False

        if state == "operator state":
            if check_if_blank(i):
                pass
            elif check_if_negation(i):
                return False
            elif check_if_closing_round_bracket(i):
                counter -= 1
            elif check_if_operator(i):
                variable_used_after_operator = False
            elif check_if_opening_round_bracket(i):
                return False
            elif check_if_variable_or_constant(i):
                return False
            else:
                return False

        if check_if_variable_or_constant(i):
            state = "operator state"
        elif check_if_operator(i):
            state = "letter state"
        else:
            pass

    if counter == 0 and variable_used_after_negation and variable_used_after_operator and variable_used:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Checking correct logical expressions:")
    print(check_if_logical_expression_is_correct("a"))
    print(check_if_logical_expression_is_correct("a|b"))
    print(check_if_logical_expression_is_correct("a & b | a"))
    print(check_if_logical_expression_is_correct("(a &b) |c&~d"))
    print(check_if_logical_expression_is_correct("~~a"))
    print(check_if_logical_expression_is_correct("~(a|c)"))
    print(check_if_logical_expression_is_correct("(a)"))

    print("Checking incorrect logical expressions:")
    print(check_if_logical_expression_is_correct("~"))
    print(check_if_logical_expression_is_correct("a|"))
    print(check_if_logical_expression_is_correct("A|B"))
    print(check_if_logical_expression_is_correct("b~"))
    print(check_if_logical_expression_is_correct("(a|b"))
    print(check_if_logical_expression_is_correct("a|b)"))
    print(check_if_logical_expression_is_correct(") ("))
    print(check_if_logical_expression_is_correct(" "))


