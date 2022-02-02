from main import log_decorator





@log_decorator
def foo(a, b):
    c = a + b
    return c



foo(4, 7)
foo(4, 5)
foo(4, 8)