
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(10, 'новая строка', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, 'Заглавная строка', 229]
value_dict = {'a': False, 'b': 'строчная строка', 'c': 16}
print_params(*values_list)
print_params(**value_dict)

values_list_2 = [3.14, 'Строка']
print_params(*values_list_2, 42)