
import os
os.system("clear")
def circle(r,pi=3.14):
    answer=pi*r**2
    return answer

r=int(input("Enter radius:"))
pip=input("You can use default pi or not:")
if pip=='yes':
    pi=3.14
else:
    pi=float(input("Your pi:"))


print(circle(r,pi=3.14))