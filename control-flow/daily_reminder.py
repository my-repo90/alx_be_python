task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()

match priority :
    case "high" :
        if(input("Is it time-bound? (yes/no): ").lower() == "yes"):
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else :
            print(f"Reminder: '{task}' is a {priority} task .Consider completing it when you have free time.")

    case "medium" :
        if(input("Is it time-bound? (yes/no): ").lower() == "yes"):
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else :
            print(f"Reminder: '{task}' is a  {priority} task .Consider completing it when you have free time.")

    case "low" : 
        if(input("Is it time-bound? (yes/no): ").lower() == "yes"):
            print(f"Note: '{task}' is a {priority} priority task that require immediate attention today!")
        else :
            print(f"Note: '{task}' is a {priority} priority task .Consider completing it when you have free time.")

            

