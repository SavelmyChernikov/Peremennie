import os
os.system("clear")


namee={
    "name":"Andrey",
    "age" : 34

}
def foo(name='vanya',age=17):

    print(f'Your name is: {name}.And your age is: {age}.')

foo(**namee)