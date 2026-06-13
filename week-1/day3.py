# positive/negative/Zero

num=int(input("Enter the number"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is Negative")
else:
    print("Zero")


#Even /odd

num=4
if num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")

#Score Card

marks=int(input("Enter the marks"))
if marks>=90:
    print("A")
elif marks >=80 and  marks<90:
    print("B")
elif marks >=70 and marks<80:
    print("C")
elif marks >=50 and marks<70:
    print("D")
else:
    print("F")

# password compare

stored_password="Surendra@630"
password=input("Enter the password")
if password==stored_password:
    print("Password is matched ")
else:
    print("Reenter the Password")

# Largest of three Numbers

a=int(input("Enter the Number"))
b=int(input("Enter the nuber"))
c=int(input("Enter the Number"))
if a>b and a>c:
    print(" a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print(" c is largest")

