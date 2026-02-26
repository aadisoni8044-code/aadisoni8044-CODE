def greetings():
    print("hello")                #1
greetings()



def add2numbers(a,b):
    result_ = a + b
    print("The sum is",result_)     #2
add2numbers(5,3)




def add2numbers(a,b):
    result = a + b
    print("The sum is",result)      #3
add2numbers(a=10, b=10)



def add3numbers(a,b,c):
    _result_ = a + b + c
    print("The sum is",_result_)      #4
add3numbers(5,3,100)



def add2num(a,b):
    return a+b
sum2num = add2num(10,2)             #5
print(sum2num)



def celsius_to_fahernheit(celsius):
    fahrenheit = (celsius * 9/5) + 32       #6 
    print(fahrenheit)
celsius_to_fahernheit(50)


def celsius_to_fahernheit(celsius):
    fahrenheit = (celsius * 9/5) + 32         #7
    return fahrenheit
temp_f = celsius_to_fahernheit(25)
print(temp_f)



def kuchbhi():
    pass
print("Hello")                        #8

