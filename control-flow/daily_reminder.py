#task reminders

task = input("input a task description: ")
priority = input("What is the taskd priority, (high, medium, low): ")
time_bound = input("Is the task time-bound, (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Not on the list")
