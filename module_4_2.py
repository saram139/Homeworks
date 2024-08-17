def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
#inner_function() нельзя вызвать здесь, т.к. находится в локальной области видимости финкции test_function
