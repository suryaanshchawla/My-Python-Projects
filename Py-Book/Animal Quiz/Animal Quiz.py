print("Welcome to", "'Guess the Animal'","Quiz!")

score=0

Validity=False
Chances= 3

#Q1
while Validity==False and Chances!=0:
    Q1=input("Which bear lives in the North Pole?").title()
    if Q1 == "Polar Bear":
        print("Correct!")
        score+=1
        Validity=True
    elif Q1 != "Polar Bear":
        print("Ah Oh, Please Try Again :( ")
        Validity=False
        Chances -= 1
if Chances==0:
    print("Game Over! Your score is 0")
    print("Thanks for playing! your score is", score, "If you have any ideas or bugs realted to this project, then please tell it on, https://github.com/suryaanshah/My-Python-Projects/discussions/new")
    exit()

#Q2
Validity=False
Chances= 3
while Validity==False and Chances!=0:
    Q2=input("Which is the fastest land animal?").title()
    if Q2 == "Chitah":
        print("Correct!")
        score+=1
        Validity=True
    elif Q2 != "Chitah":
        print("Ah Oh, Please Try Again :( ")
        score+=1
        Validity=False
        Chances -= 1
if Chances==0:
    print("Game Over! Your score is 0")
    print("Thanks for playing! your score is", score, "If you have any ideas or bugs realted to this project, then please tell it on, https://github.com/suryaanshah/My-Python-Projects/discussions/new")
    exit()

#Q3
Validity=False
Chances= 3
while Validity==False and Chances!=0:
    Q3=input("Which is the largest animal?").title()
    if Q3 == "Blue Whale":
        print("Correct!")
        score+=1
        Validity=True
    elif Q3 != "Blue Whale":
        print("Ah Oh, Please Try Again :( ")
        Validity=False
        Chances -= 1
print("Thanks for playing! your score is", score, "If you have any ideas or bugs realted to this project, then please tell it on, https://github.com/suryaanshah/My-Python-Projects/discussions/new")
