def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
inner_function()  # функция inner_function не определена, так как является локальной для функции test_function