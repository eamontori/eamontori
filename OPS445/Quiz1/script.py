#!/usr/bin/env python3

# Conversion factors
inches_to_cm = 2.54
cm_to_inches = 1 / inches_to_cm

# Display the menu
print("1. Convert inches -> cm")
print("2. Convert cm -> inches")

# Get the user's choice
choice = input("Make your selection (1,2): ")

# Execute based on user input
if choice == "1":
    inches = int(input("Enter inches: "))
    cm = inches * inches_to_cm
    print("Number of cm:", cm)
elif choice == "2":
    cm = int(input("Enter cm: "))
    inches = cm * cm_to_inches
    print("Number of inches:", inches)
else:
    print("Invalid entry")
