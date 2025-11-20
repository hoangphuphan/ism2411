print("Welcome to my Python program!")
minutes = input("How many minutes did you drive today?")
minutes = float(minutes)
weeklky_minutes = minutes * 7
print(f"Your estimated total driving time this week is {weeklky_minutes}")

try:
    minutes = float(minutes)
except ValueError:
    print("Please enter a valid number.")
    exit()


