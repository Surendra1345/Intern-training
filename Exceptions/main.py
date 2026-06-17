from functions import contact_book,todos,add_contact,find_contact,list_contacts,add_task,remove_task,show_task

class NotfoundError(Exception):
    pass


add_contact("Surendra",630303023283)
add_contact("Suri",9988007766)
add_contact("Sai",8899007766)
try:
    name="Surendra"
    if name not in contact_book:
        raise NotfoundError("Contact not found")
    find_contact(name)
except NotfoundError as e:
    print(f"Error : {e}")
else:
    print(f"Contact found :{name}")

try:
    if len(contact_book)==0:
        raise NotfoundError("No contacts")
except NotfoundError as e:
    print(f"Error :{e}")
else:
    for name,phone in contact_book.items():
        print(f"Name:{name} | Phone:{phone}")
finally:
    print("program finished without any crashes")




# ToDo list
add_task("Develop the frontend")
add_task("Complete the backend")
add_task("Complete functions")
try:
    task = "Develop the frontend"
    if task  not in todos:
        raise NotfoundError("Task not found")
    remove_task(task)
except NotfoundError as e:
    print(f"Error :{e}")
else:
    print(f"{task} task found ")

try:
    if len(todos)==0:
        raise NotfoundError("No tasks in todo list")
except NotfoundError as e:
    print(f" Error :{e}")
else:
    for task in show_task():
        print(f"{task}")
finally:
    print("Program is finished withot any crashes")