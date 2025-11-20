print("Welcome to my Python program!")
#User's Input
minutes = input("How many minutes did you drive today?")

#Error Handling
while True:
    try:
        minutes = float(minutes)
        break
    except ValueError:
        print("Please enter a valid number.")
        minutes = input()

#Unit Conversion and Calculation
weeklky_minutes = minutes * 7
print(f"Your estimated total driving time this week is {weeklky_minutes} minutes")
