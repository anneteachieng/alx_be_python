#task reminders

Task = input("What is the task?: ")
Priority = input("What is the task priority, (high, medium, low): ")
Time_bound = input("Is the task time-bound, (yes or no): ")

match Priority:
    case "high":
        if Time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if Time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "low":
        if Time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Not on the list")
