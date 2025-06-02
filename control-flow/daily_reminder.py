task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
isTimebond = input("Is it time bond? (yes/no): ")

match priority:
    case "high":
        if isTimebond == "yes":
            print("Reminder:","'", task,"'", "is a high priority task that requires immediate attention today! ")
        else:
            print("Reminder:","'", task,"'", "is a high priority task ! ")
    
    case "low":
        if isTimebond == "no":
            print("'", task,"'", "is a low priority task consider completing it when you have free time ")
        else:
            print("'", task,"'", "is a low priority task but it is time bond ")
    
    case "medium":
        if isTimebond == "yes":
            print("'", task,"'", "is a medium priority task consider completing it today")
        else:
            print("'", task,"'", "is a medium priority task consider completing it when you have free time ")