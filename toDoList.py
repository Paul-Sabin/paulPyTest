import os, time

taskList = [['Run', 'Monday', 'High'], ['Think', 'Noon', 'Medium'], ['Clean', 'Saturday', 'Low'], ['Brush teeth', 'This evening', 'High'], ['Check email', 'Now', 'Medium'], ['Hug Alice', '6pm', 'Low']]

def addTask():
  print()
  description = input("What is the task? ")
  deadline = input("When is it due by? ")
  priority = input("Type 'High', 'Medium' or 'Low' to set the priority ")
  newTask = [description, deadline, priority]
  taskList.append(newTask)
  print()
  print("Thanks, this task has been added.")

def prettyPrintAll():
  os.system("clear")
  time.sleep(1)
  taskNumber = 1
  print()
  for i in taskList:
    print(f"{taskNumber}: {i[0]}    Deadline: {i[1]}    Priority: {i[2]}")
    print()
    taskNumber +=1

def prettyPrintHigh():
  os.system("clear")
  time.sleep(1)
  taskNumber = 1
  print()
  for i in taskList:
    if i[2] != "High":
      continue
    print(f"{taskNumber}: {i[0]}    Deadline: {i[1]}    Priority: {i[2]}")
    print()
    taskNumber +=1
  print()
  print("Now, quietly do the next most necessary thing.")

def prettyPrintMedium():
  os.system("clear")
  time.sleep(1)
  taskNumber = 1
  print()
  for i in taskList:
    if i[2] != "Medium":
      continue
    print(f"{taskNumber}: {i[0]}    Deadline: {i[1]}    Priority: {i[2]}")
    print()
    taskNumber +=1
  print()
  print("Now, quietly do the next most necessary thing.")

def prettyPrintLow():
  os.system("clear")
  time.sleep(1)
  taskNumber = 1
  print()
  for i in taskList:
    if i[2] != "Low":
      continue
    print(f"{taskNumber}: {i[0]}    Deadline: {i[1]}    Priority: {i[2]}")
    print()
    taskNumber +=1
  print()
  print("Now, quietly do the next most necessary thing.")

def viewTasks():
  while True:
    print()
    viewType = input("Would you like to view All tasks, High priority, Medium or Low? ")
    if viewType.title() == "A":
      prettyPrintAll()
      break
    elif viewType.title() == "H":
      prettyPrintHigh()  
      break
    elif viewType.title() == "M":
      prettyPrintMedium()
      break
    elif viewType.title() == "L":
      prettyPrintLow()  
      break
    else:
      print("Please type the first letter to select from the menu")
      time.sleep(1)

def editTask():
  while True:
    print()
    taskToEdit = input("Which task would you like to edit? ")
    for currentTask in taskList:
      if taskToEdit in currentTask:
        while True:
          print()
          desiredChange = input("Press T to change task description, D to change the deadline or P to change priority: ")
          if desiredChange.title() == "T":
            print()
            currentTask[0] = input("Enter new task description: ")
            print("Okay, here's your updated list")
            time.sleep(1)
            prettyPrintAll()
            return
          elif desiredChange.title() == "D":
            print()
            currentTask[1] = input(f"Enter new deadline for {currentTask[0]}: ")
            print("Okay, here's your updated list")
            time.sleep(1)
            prettyPrintAll()
            return  
          elif desiredChange.title() == "P":
            print()
            currentTask[2] = input(f"Type 'High', 'Medium' or 'Low' to set the priority for {currentTask[0]}: ")
            print("Okay, here's your updated list")
            time.sleep(1)
            prettyPrintAll() 
            return
          else:
            print("Sorry, I didn't recognise that input.")
            time.sleep(1)
            os.system("clear")    
        
def removeTask():
  while True:
    print()
    doneTask = input("Which task would you like to remove? ")
    for currentTask in taskList:
      if doneTask.title() == currentTask[0].title():
        taskList.remove(currentTask)
        print()
        print("Okay, job done! Here's your updated list:")
        time.sleep(1)
        prettyPrintAll() 
        return
    print()
    print("Sorry, I couldn't find that task.")
    time.sleep(1)
    os.system("clear")

print("\U0001FAE3  Life Organiser \U0001F549")

while True:
  time.sleep(1)
  print()
  option = input("Welcome to the life organiser. Do you want to Add, View, Edit or Remove an item, or Quit? ")
  if option.title() == "A":
    addTask()
  elif option.title() == "V":
    viewTasks()
  elif option.title() == "E":
    editTask()  
  elif option.title() == "R":
    removeTask()
  elif option.title() == "Q":
    print()
    print("Okay, see you soon!")
    break
  else:
    print()
    print("Please tap the first letter of the menu item you require.")
    time.sleep(1)