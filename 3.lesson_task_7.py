"""
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().

"""


def int_func(input_text):
    return input_text.title()


print(int_func('hello bye hello bye!'))