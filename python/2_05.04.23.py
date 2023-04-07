import os
os.system('clear')


def foo(data):
    result=[]
    if type (data) is list:
        for d in data:
            result= result + foo(d)
    else:
        result.append(data)
    return result

a=[
    [
        [1,2,3],
        [4,5,6]
    ],
    ['a']
]


print(foo(a))

