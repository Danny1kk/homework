import random

def get_cipher():
    numbers = list(range(3, 21))
    return random.choice(numbers)

def get_passcode(n):
    result = ''

    for a in range(1, n):
        for b in range(a + 1, n):
            if a + b == n:
                if n % (a + b) == 0:
                    result += str(a) + str(b)

    return result

n = get_cipher()
result = get_passcode(n)

print('Пары чисел:', n)
print('Введите пароль:', result, 'во вторую вставку')
print('Путь свободен!')