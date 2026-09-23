"""рекурсивное вычисление НОД"""
def gcd_recursive(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

"""lcm — вычисление НОК"""
def lcm(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    return a * b // gcd_recursive(a, b)
def find_gcd_slow(a: int, b: int) -> int:
    """Находит НОД двух целых чисел методом последовательного вычитания.

    Принцип работы:
    из большего числа вычитается меньшее до тех пор,
    пока оба числа не станут равными.

    :param a: первое целое число
    :param b: второе целое число
    :return: наибольший общий делитель
    """
    a = abs(a)
    b = abs(b)

    # Обрабатываем случай, когда одно из чисел равно нулю
    if a == 0:
        return b
    if b == 0:
        return a

    # Постепенно уменьшаем большее из двух чисел
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b

    return a

def gcd_iterative_fast(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a