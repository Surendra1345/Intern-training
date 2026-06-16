# Bank Account
class Bankaccount:
    def __init__(self,name,account_no,balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance
        self.statement=[]
    def check_balance(self):
        print(f"Balance :{self.balance}")
    def deposit(self,amount):
        if amount<=0:
            print(f"Enter valid amount")
        else:
            self.balance+=amount
            self.statement.append(f"deposited :{amount}")
            print(f"{amount} is deposited Successsfully | Balance :{self.balance}")
    def withdrawl(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            self.statement.append(f"Withdrawl : {amount}")
            print(f"{amount} is withdrawl Successfully | Remaining balance :{self.balance}")

    def show_statements(self):
        if len(self.statement)==0:
            print("No Transactions")
        else:
            print("Statements")
            for records in self.statement:
                print(records)
            print(f"Current balance :{self.balance}")
customer=Bankaccount("Surendra",112233232,10000)
print()
customer.check_balance()
print()
customer.deposit(20000)
print()
customer.withdrawl(5000)
print()
customer.withdrawl(20000)
print()
customer.show_statements()
        

#Student class

class Student:
    def __init__(self,name,grade,marks):
        self.name=name
        self.grade=grade
        self.marks=marks
    def show_info(self):
        print(f"Name : {self.name} | Grade:{self.grade} |marks :{self.marks} ")
    def pass_or_fail(self):
        if self.marks>=50:
            print(f"{self.name} is passed with {self.marks} marks")
        else:
            print(f"{self.name} is failed with {self.marks} marks")
    def show_grade(self):
        if self.marks>=90:
            print("A")
        elif self.marks>=80:
            print("B")
        elif self.marks>=70:
            print("C")
        elif self.marks>=50:
            print("D")
        else:
            print("F")


student1=Student("Surendra","10th",90)
student2=Student("Suri","10th",85)
student3=Student("Mohan","10th",77)
student4=Student("Afzl","10th",65)
student5=Student("Sai","10th",49)
print()
student1.show_info()
student2.show_info()
student3.show_info()
student4.show_info()
student5.show_info()
print()
student1.pass_or_fail()
student3.pass_or_fail()
student5.pass_or_fail()
print()
student2.show_grade()
student3.show_grade()
student4.show_grade()
 