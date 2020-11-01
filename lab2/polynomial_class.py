class Polynomial:
    """
    Wielomian dziala w zbiorze licb rzeczywistych.
    Natomiast nie dziala w zbiorze liczb zespolonych.

    Defaultdict bylby raczej dobrym pomyslem, gdzie klucz-stopien wykladnika, wartosc- wspolczynik,
    a dla niezdefiniowanych wartosci dla danych kluczy zawsze zwracaloby 0.
    """

    def __init__(self, *coeffs):
        # (coeffs = 2,0,3) => 2x**2+0x+3
        self.coeffs_list = list(coeffs)

    def calculate(self, value):
        result = self.coeffs_list[-1]
        len_polynomial = len(self.coeffs_list)
        for c in (self.coeffs_list[:-1]):
            result += c * (value ** (len_polynomial - 1))
            len_polynomial -= 1
        return result

    def __add__(self, other):
        add_result = []
        coeffs1, coeffs2 = self.coeffs_list.copy(), other.coeffs_list.copy()
        if len(coeffs1) > len(coeffs2):
            while len(coeffs1) > len(coeffs2):
                coeffs2.insert(0, 0)
        else:
            while len(coeffs2) > len(coeffs1):
                coeffs1.insert(0, 0)

        for s, o in zip(coeffs1, coeffs2):
            add_result.append(s + o)

        return Polynomial(*add_result)

    def __iadd__(self, other):
        return self+other

    def __sub__(self, other):
        sub_result = []
        coeffs1, coeffs2 = self.coeffs_list.copy(), other.coeffs_list.copy()
        if len(coeffs1) > len(coeffs2):
            while len(coeffs1) > len(coeffs2):
                coeffs2.insert(0, 0)
        else:
            while len(coeffs2) > len(coeffs1):
                coeffs1.insert(0, 0)

        for s, o in zip(coeffs1, coeffs2):
            sub_result.append(s - o)

        return Polynomial(*sub_result)

    def __isub__(self, other):
        return self-other

    def __mul__(self, other):
        coeffs1 = self.coeffs_list
        coeffs2 = other.coeffs_list
        final_polynomial_len = len(coeffs1) + len(coeffs2) - 1
        mul_result = [0] * final_polynomial_len
        for ind1, co1 in enumerate(coeffs1):
            for ind2, co2 in enumerate(coeffs2):
                mul_result[ind1 + ind2] += co1 * co2

        return Polynomial(*mul_result)

    def __imul__(self, other):
        return self*other

    def __bool__(self):
        if self.coeffs_list == [0] * len(self.coeffs_list):
            return False
        else:
            return True

    def __str__(self):
        len_polynomial = len(self.coeffs_list)
        str_polynomial = ""
        for i in self.coeffs_list:
            if i >= 0 and str_polynomial != "":
                str_polynomial += "+"
            str_polynomial += str(i) + "x**" + str(len_polynomial - 1)
            len_polynomial -= 1

        return str_polynomial[:-4]


if __name__ == "__main__":
    poly1 = Polynomial(3, -2, 4)
    poly2 = Polynomial(2, 2, 4, 2, 2)
    poly0 = Polynomial(0, 0, 0)
    print("Polynomial 1: {}, polynomial 2: {}".format(poly1, poly2))
    print("Result of adding polynomials: {}".format(poly1 + poly2))
    print("Result of subtracting polynomials: {}".format(poly1 - poly2))
    print("Result of multiplying polynomials: {}".format(poly1 * poly2))
    print("Polynomial: {}, boolean value: {}".format(poly1, bool(poly1)))
    print("Polynomial: {}, boolean value: {}".format(poly0, bool(poly0)))




