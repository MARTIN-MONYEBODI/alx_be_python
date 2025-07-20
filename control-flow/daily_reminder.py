task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task. please complete it soon.")
    
    case "medium":
        if priority == "medium" and time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task. Please complete it soon.")
        else:
            print(f"Note: {task} is a medium priority task. You can complete it later.")
            
    case "low":
        if priority == "low" and time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note: {task} is a low priority task. You can complete it whenever you have time.")