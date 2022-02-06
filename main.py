import os
import datetime

def log_decorator(function):
    def new_fanction(*args, **kwargs):
        now = datetime.datetime.now()
        name_file = 'log-file' + f'{now.strftime("%d-%m-%Y-%H-%M-%S")}' + '.txt'
        my_file = open(name_file, "w+")
        my_file.close()
        result = function(*args, **kwargs)
        path = os.path.os.getcwd()
        with open(os.path.join(os.getcwd(), name_file), 'w') as log:
            log.write(f'{now.strftime("%d-%m-%Y %H:%M:%S")}'+'|'+f'{function.__name__}'+' | '+f'аргументы {args, kwargs}'+' | '+f'с результатом {result}'+' | '+f'{path}')
        return result
    return new_fanction


def parametrized_decor(parameter):
    def log_decorator1(function):
        def new_fanction(*args, **kwargs):
            now = datetime.datetime.now()
            name_file = 'log-file' + f'{now.strftime("%d-%m-%Y-%H-%M-%S")}' + '.txt'
            my_file = open(name_file, "w+")
            my_file.close()
            result = function(*args, **kwargs)
            path = parameter
            with open(os.path.join(path, name_file), 'w') as log:
                log.write(
                    f'{now.strftime("%d-%m-%Y %H:%M:%S")}' + '|' + f'{function.__name__}' + ' | ' + f'аргументы {args, kwargs}' + ' | ' + f'с результатом {result}' + ' | ' + f'{path}')
            return result
        return new_fanction
    return log_decorator1








