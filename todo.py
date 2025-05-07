class Task:
  def __init__(self, title):
    self.title = title
    self.completed = False

  def mark_completed(self):
    self.completed = True
  
  def __str__(self):
    status = "Done" if self.completed else "Not Done"
    return f"{self.title} [{status}]"
  
def main():

  tasks = []

  task1 = Task("Exercise")
  print(task1)

  task1.mark_completed()
  print(task1)


  while True:
    print("To-do list")
    print("Select options (1-5)")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark as Complete")
    print("4. Delete Tasks")
    print("5. Exit")

    choice = input("Enter your option (1-5)")

    if choice == "1":
      task = input("Enter what is the task to be done: ")
      tasks.append(Task(task))
    
    elif choice == "2":
      print("The list of all your tasks and their status")
      if not tasks:
        print("No tasks are added")
      else:
        print("Your tasks")
        for idx, task in enumerate(tasks, 1):
          print(f"{idx}. {task}")

    elif choice == "3":
      if not tasks:
        print("There are no tasks added")
      else:
        for idx, task in enumerate(tasks, 1):
          print(f"{idx}. {task}")
      try:
        task_no = int(input("Enter the completed task no "))
        if 1 <= task_no <= len(tasks): 
          tasks[task_no-1].mark_completed()
          print(tasks[task_no-1])
        else:
          print("Enter a valid task number")
      except ValueError:
        print("Please enter a valid task number")
      
    elif choice == "4":
      if not tasks:
        print("No tasks available")
      else:
        for idx, task in enumerate(tasks, 1):
          print(f"{idx}. {task}")
      try:
        task_no = int(input("Enter the task number to be deleted: "))
        if 1 <= task_no <= len(tasks):
          deleted_task = tasks.pop(task_no - 1)
          print(f"The deleted task is {deleted_task.title}")
        else:
          print("Enter valid task number")
      except ValueError:
        print("Please enter a valid task number")

    elif choice == "5":
      print("Thank you for using the app")
      break

    else:
      print("Invalid choice. Please try again")




if __name__ == "__main__":
  main()