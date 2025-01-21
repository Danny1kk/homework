
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()
test_function()

# inner_function()  # Попытка вызвать inner_function вне test_function приведет к ошибке NameError, потому что эта функция не существует в глобальной области видимости