def two_positive_ints_input():
    int1, int2 = 0, 0
    while type(int1) != int or type(int2) != int or int1 <= 0 or int2 <= 0:
        try:
            int1 = int(input("Choose positive int: "))
            int2 = int(input("Choose second positive int: "))
        except:
            print("You need to pass positive integers")

    return int1, int2


def get_prime_factors(int_number):
    prime_factors = {}
    int_number_copy = int_number
    while int_number_copy > 1:
        for i in range(2, int_number + 1):
            if int_number_copy % i == 0:
                int_number_copy = int_number_copy / i
                if i in prime_factors.keys():
                    prime_factors[i] += 1
                else:
                    prime_factors[i] = 1
                break

    return prime_factors


def greatest_common_divisor(int1, int2):
    int1_prime_factors = get_prime_factors(int1)
    int2_prime_factors = get_prime_factors(int2)
    prime_factors_union = {}
    for k, v in int1_prime_factors.items():
        if k in int2_prime_factors.keys():
            prime_factors_union[k] = min(int1_prime_factors[k], int2_prime_factors[k])

    if not prime_factors_union:
        prime_factors_union[1] = 1

    gcd = 1
    for prime_fac, quantity in prime_factors_union.items():
        gcd *= prime_fac ** quantity

    return gcd


if __name__ == "__main__":
    print(greatest_common_divisor(*two_positive_ints_input()))
