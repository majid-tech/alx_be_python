# daily_reminder app...

user_task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match task_priority:
    case 'high' if time_bound == 'yes':
        print(f"Reminder: '{user_task}' is a high priority task that requires immediate attention today!")
    case _ if time_bound == 'no':
        print(f"Note: '{user_task}' is a low priority task. Consider completing it when you have free time.")