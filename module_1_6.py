login_password = {'Kr1s_De': 'Qwerty123', 'quatrum11': '785_4569A', 'DDoki': 'oO896_325741'}
print('Login: Password: ', login_password)
print('Existing value: ', login_password['Kr1s_De'])
print('Not existing value: ', login_password.get('DeanW7'))
login_password.update({'DeanK1k': 'Mokld63_777',
                       'potatto_force': 'oao_0192838466'})
print('Deleted value: ', login_password.pop('Kr1s_De'))
print('Modified dictionary: ', login_password)


set_ = {'П = 3,14', 'Apple', 1, 2, 3, 'Оно', 'П = 3,14', 'П = 3,14', 'Apple', 1, 2, 'Оно', 6}
a = set_
print('Set: ', a)
a.update({36,
           (77, 35, 109)})
a.discard(a)
print('Modified dictionary: ', a)