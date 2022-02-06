from main import log_decorator, parametrized_decor





@log_decorator
def foo1(a, b):
    c = a + b
    return c

three = foo1(1, 2)
five = foo1(2, 3)

result = foo1(three, five)




path1 = 'D:\\task_one_test\\проффесиональная работа с Python\\домашние задание к 5 лекции\\log'

foo1(4,5)



@parametrized_decor(parameter = path1)
def foo():
 pass

foo()