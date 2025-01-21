
tuple_ = 1, 2, 'b', True
immutable_var = tuple_
print('Immutable tuple: ', immutable_var)
print(tuple_[2])
# tuple_[2] = 2020
# print(tuple_)
# Все элементы, которые находятся в кортеже, они как бы находятся в хранилище, которое нельзя изменять. Можно добавлять, но менять не получится

mutable_list = [8, 800, 'all', False]
print('Mutable list: ', mutable_list)
mutable_list = ([8, 800, 'all', False] + ['Modified'])
mutable_list[3] = True
print('Mutable list: ', mutable_list)