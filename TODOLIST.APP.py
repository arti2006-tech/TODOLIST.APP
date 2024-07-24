def task():
    tasks = []  # empty list
    print("----WELCOME TO THE TO DO LIST APP :)----")
    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")
    
    while True:
        try:
            CHOICE = int(input("Enter \n1-Add a task\n2-edit a task\n3-Delete\n4-View\n5-Exit\n"))
            if CHOICE == 1:
                add = input("Enter task you want to add = ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")
            elif CHOICE == 2:
                edit_val = input("Enter the task name you want to edit = ")
                if edit_val in tasks:
                    edit = input("Enter new task = ")
                    ind = tasks.index(edit_val)
                    tasks[ind] = edit
                    print(f"edit task '{edit_val}' to '{edit}'.")
                else:
                    print("Task not found.")
            elif CHOICE == 3:
                del_val = input("Which task you want to delete = ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task '{del_val}' has been deleted.")
                else:
                    print("Task not found.")
            elif CHOICE == 4:
                print(f"Total tasks = {tasks}")
            elif CHOICE == 5:
                print("...THANK YOU....")
                break
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

task()
