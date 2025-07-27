
# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case for priority reactions
match priority:
    case "high":
        level = "high priority"
    case "medium":
        level = "medium priority"
    case "low":
        level = "low priority"
    case _:
        level = "unspecified priority"

# Print customized reminder
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {level} task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {level} task. Consider completing it when you have free time.")

