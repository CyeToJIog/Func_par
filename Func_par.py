# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('первая')
print_params('первая', 24, 'hours')

print_params(c=[1, 2, 3])
print_params(b=25)

# Распаковка параметров:

values_list = ['Меня зовут', 'Денис', True]
values_dict = {'a': 'Мне', 'b': 30, 'c': 'лет'}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:

values_list_2 = [3, '<']
print_params(*values_list_2, 42)
