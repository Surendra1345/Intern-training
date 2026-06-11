# Multiplication
num=int(input("Enter the number"))
for i in range(1,11):
    result=num*i
    print(f"{num}*{i}={result}")


#Sum of every number from 1 to 100
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

#FizzBuzz
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        

#Guessing number using while loop
import random
target=random.randint(1,100)
attempts=0
while True:
    num=int(input("Enter the number"))
    attempts+=1
    if num<target:
        print("Too Low")
    elif num>target:
        print("Too High")
    else:
        print(f"You found the number at{attempts}")
        break