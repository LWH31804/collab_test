def div(a, b):
    if b == 0:
        return None  # 또는 예외 처리
    return a / b
def reverse(s):
    if not isinstance(s, str):
        return None
    return s[::-1]
def is_even(n):
    return n % 2 == 0