MSG_INPUT_NUMBER = 'Введите число: '
MSG_PRIME = 'Простое'
MSG_COMPOSITE = 'Составное'
MSG_NOT_PRIME = 'Не простое'
RANGE = 100_000 + 1


def is_prime(number) -> str:
    """Проверяет простое ли число"""
    if number in (0, 1):
        return MSG_NOT_PRIME

    for d in range(2, int(number ** 0.5) + 1):
        if not number % d:
            return MSG_COMPOSITE

    return MSG_PRIME


