
def decaration_func(wrapped_func):
    def wrapper():
        print(" привет мир ")
        print(wrapped_func)
        print("hi, niga")
        wrapped_func()
        print(" back, niga")
    return wrapper
@decaration_func
def Hello_workd():
    print("Hello_workd")
Hello_workd()


func = lambda x, y: x+y*2
res = func(2, 6)
print(res)

def square (res):
    '''
    принимает чило и возводит его в квадрат
    '''
print(square.__doc__)
