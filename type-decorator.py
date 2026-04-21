
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **keywargs):
            x = func(*args, ** keywargs)
            return type_of_output(x)
        return wrapper
    return decorator
@type_converter(str)

def return_int():
    return 5




@type_converter(int)
def return_string():
    return "not a number"

y =return_int()
print(type(y).__name__)

try:
    y= return_string()
    print("shouldn't det here!")
except ValueError:
    print("can't conver that string to an integer!")


    

