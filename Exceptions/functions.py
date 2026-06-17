## Contact book

contact_book={}

def add_contact(name,phone):
    contact_book[name]=phone
    print(f"{name} is added Successfully")
def find_contact(name):
    if name in contact_book:
        print("Contact found")
        print(f"{name} :{contact_book[name]}")
    else:
        print(f"{name} was not found in contacts")
def list_contacts():
    if len(contact_book)==0:
        print("No contacts")
    else:
        print("Contacts")
        for name,phone in contact_book.items():
            print(f"{name}:{phone}")



# ToDo list

todos=[]

def add_task(task):
    todos.append(task)
    print(f"{task} task is added")
def remove_task(task):
   if task in todos:
      todos.remove(task)
      print(f"{task} task is removed")
   else:
      print(f"{task} task is not found")
def show_task():
   if len(todos)==0:
      print("No tasks")
   else:
      print("Tasks")
      for i,task in enumerate(todos,1):
         print(f"{i}:{task}")
