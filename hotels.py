def decline_computers(n: int) -> str:
    if n % 10 == 1 and n % 100 != 11:
        return f"{n} компьютер"
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return f"{n} компьютера"
    else:
        return f"{n} компьютеров"


def common_divisors(numbers: list[int]) -> list[int]:
    # find the minimum number in the list
    min_number = min(numbers)

    # collect all its devisors
    divisors = [i for i in range(1, min_number // 2 + 1) if min_number % i == 0]

    # filter out the divisors that are not divisors of all the other numbers
    divisors = [d for d in divisors if all(n % d == 0 for n in numbers)]

    return divisors


def primes_between(start: int, end: int) -> list[int]:
    return [num for num in range(max(start, 2), end + 1)
             if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]


def multiply_table(n: int) -> str:
    # Находим максимальную длину числа в таблице
    max_length = len(str(n*n))

    # Формируем таблицу умножения
    table = '\n'.join([''.join([f'{i*j:{max_length}} ' for j in range(1, n+1)]) for i in range(1, n+1)])

    return table


