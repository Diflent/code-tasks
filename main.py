"""gcd_recursive — рекурсивное вычисление НОД"""
def gcd_recursive(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)