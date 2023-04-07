import os
os.system("clear")


def perfect_num(a):
    num=[]
    for i in range(1, a):
        if a % i== 0:
            num.append(i)
    return sum(num) == a


for s in range(1, 51):
    print (s)
    print(perfect_num(s))
    


