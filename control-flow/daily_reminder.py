task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

msg = ""
match priority:
    case "high":
        priority = "high"

    case "medium":
        priority = "medium"
        # a = f"Reminder: '{task}' is a {priority} priority task"
    case "low":
        priority = "low"


if time_bound == "yes":
    msg = f"Reminder: '{task}' is a {
        priority} priority task that requires immediate attention today!"
else:
    msg = f"Note: '{task}' is a {
        priority} priority task. Consider completing it when you have free time."

print(msg)
