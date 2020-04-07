### A simple math game that throws up 4 numbers and 3 operators
### Your goal is to select which ones were used to calculate one of the other and select the operatr used
from operator import add, sub, mul, truediv
from random import randint

operator = {'+': add, 
    '-': sub, 
    'x': mul, 
    '/': truediv}

oplist = []
for key in operator:
    oplist.append(key)

#creating random numbers for the calculation

num1 = randint(3, 30)
num2 = randint(3, 30)
numr = randint(3, 20)
op1 = oplist[randint(0, 3)]
opr = oplist[randint(0, 3)]
ans = operator.get(op1)(num1,num2)
ansr = randint(1, (int(abs(ans))+5))

print("Find the 3 numbers used in the calculation: \n")
print(num1, numr, num2, op1, opr, ans, "\n")

select1 = int(input("Select a number 1:  "))
select2 = int(input("Select a number 2:  "))
select3 = int(input("Select a number 3:  "))

#setting the requrements for correct answer
def select_ans(s1,s2,s3):
    if (s1 == ans or s1 == num1 or s1 == num2):
        pass
    if (s2 == ans or s2 == num1 or s2 == num2):
        pass
    if (s3 == ans or s3 == num1 or s3 == num2):
        print("Well one!!")
        print(f"{num1} {op1} {num2} = {ans}")
    else: 
        print("Try again!!")

select_ans(select1, select2, select3)

#def user_ans():
 #   select = input("Choose the 3 items used: ")
  #  if select.isdigit
        
   # return select



