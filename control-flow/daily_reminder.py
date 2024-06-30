task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
istimebound = input("Is it time-bound? (yes/no):")

if istimebound == "yes":
    print(
        f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")

else:
    print(
        f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
