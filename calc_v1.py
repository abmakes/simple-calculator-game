import tkinter as tk
import random
from random import randint, shuffle

root = tk.Tk()
root.grid()


randomlist = []
answerlist = [0,0]

'''generate random numbers for the correct answer'''
num1 = randint(15, 30)
randomlist.append(num1)

num2 = randint(5, 20)
randomlist.append(num2)

answer = num1 + num2

showanswer = tk.StringVar(value=answer)

'''Generate the incorrect numbers and change them if the same'''
randomnr1 = randint(5, 30)

if randomnr1 == num1 or randomnr1 == num2:
    randomnr1 = randint(31,40)
else:
    pass
randomlist.append(randomnr1)

randomnr2 = randint(5, 30)

if randomnr2 == num2 or randomnr2 == num1:
    randomnr2 = randint(1, 4)
else:
    pass
randomlist.append(randomnr2)

'''Shuffle list to allow for random button possitions.'''
randomlist1 = random.sample(randomlist, k=4)

'''check itermediate results'''
print(randomlist) 
print("shuffled ", randomlist1)


'''Append answers on button press'''
def answer_append0():
    answerlist.append(randomlist1[0])
    update_answer()
    print(answerlist)

def answer_append1():
    answerlist.append(randomlist1[1])
    update_answer()
    print(answerlist)  

def answer_append2(): 
    answerlist.append(randomlist1[2])
    update_answer()
    print(answerlist)
    
def answer_append3(): 
    answerlist.append(randomlist1[3])
    update_answer()
    print(answerlist)


'''function for submit button'''
def correct():
    if num1 == answerlist[-1] and num2 == answerlist[-2] or num2 == answerlist[-1] and num1 == answerlist[-2]:
        print("Correct")
    else:
        print("Incorrect")


'''display the value or the variables on the buttons in the GUI'''
for item in randomlist1:
    if item == randomlist1[0]:
        textnum = tk.StringVar(value=randomlist1[0])
        button1 = tk.Button(root, textvariable=textnum, command=answer_append0)
        button1.grid(row=0)
    if item == randomlist1[1]:
        textnum = tk.StringVar(value=randomlist1[1])
        button2 = tk.Button(root, textvariable=textnum, command=answer_append1)
        button2.grid(row=1)
    if item == randomlist1[2]:
        textnum = tk.StringVar(value=randomlist1[2])
        button3 = tk.Button(root, textvariable=textnum, command=answer_append2)
        button3.grid(row=0, column=1)
    if item == randomlist1[3]:
        textnum = tk.StringVar(value=randomlist1[3])
        button4 = tk.Button(root, textvariable=textnum, command=answer_append3)
        button4.grid(row=1, column=1)


'''Answer dsplay area'''
def update_answer():
    textnum = tk.StringVar(value=answerlist[-2])
    label1.configure(textvariable=textnum)
    textnum1 = tk.StringVar(value=answerlist[-1])
    label3.configure(textvariable=textnum1)


labelf = tk.LabelFrame(root, text='Answer:')
labelf.grid(row=3, columnspan=5)

selected_answer1 = answerlist[-2]

selected_answer2 = answerlist[-1]

label1 = tk.Label(labelf, textvariable=selected_answer1)
label1.grid(row=3, column=0)

label2 = tk.Label(labelf, text=" + ")
label2.grid(row=3, column=1)

label3 = tk.Label(labelf, textvariable=selected_answer2)
label3.grid(row=3, column=2)

label4 = tk.Label(labelf, text=" = ")
label4.grid(row=3, column=3)

label5 = tk.Label(labelf, textvariable=showanswer)
label5.grid(row=3, column=4)

submitbutton = tk.Button(root, text="SUBMIT", command=correct)
submitbutton.grid(row=4)

root.mainloop()
