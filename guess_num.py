import random
n=random.randint(1,101)
a=0
guess=0
while (a!=n):
    guess+=1
    a=int(input("Guess the number"))
    if(a<n):
        print("give hegher number")
    elif(a>n):
        print("give lower number")
print(f"you guessed currect number{n}at guess{guess}")