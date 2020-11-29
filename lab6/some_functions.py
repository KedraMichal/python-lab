def is_number(number):
    if not type(number) in (float, int):
        raise ValueError("U need to pass a float, not string")


def linear_or_square_equation(a, b, c):
    is_number(a), is_number(b), is_number(c)
    if a != 0:
        delta = b**2-4*a*c
        if delta > 0:
            x1 = (-b-delta**(1 / 2)) / (2*a)
            x2 = (-b+delta**(1 / 2)) / (2*a)
            return x1, x2
        elif delta == 0:
            x0 = -b/(2*a)
            return x0
        else:
            return None
    elif b != 0:
        x = -c/b
        return x
    elif c == 0:
        return "Infinitely many solutions"
    else:
        return None


def equation_of_a_straight_line(x1, y1, x2, y2):
    is_number(x1), is_number(y1), is_number(x2), is_number(y2)
    if x1 == x2 and y1 == y2:
        return "Many equations of a straight line"
    elif x1 == x2:
        return "x={}".format(x1)
    elif y1 == y2:
        return "y={}".format(y1)

    a = (y1-y2) / (x1-x2)
    b = y1 - x1*a
    if b >= 0:
        return "y={}x+{}".format(a, b)

    return "y={}x{}".format(a, b)
