import os
os.system('clear')

def foo(a):
    a=[*a]
    for i in range (len(a)):
        if a[i] == 5:
            a[i] = 3
            
        return a 

test = [5, 5, 5, 5, 5]

res = foo(test)

print (test)
print (res)
