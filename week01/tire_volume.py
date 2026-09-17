"""
Name: King David Olaribigbe
program: Tire Volume Calculator

Enhancement:
This program asks the user if they would like to purchase tires with the specified 
dimensions. If the user answers yes, the program collects contact information and 
stores it in the volumes.txt file.
"""

# Import modules
import math
import datetime
current_date = datetime.datetime.now()

#Open and manipilate the file
with open("volumes.txt", "at") as volume_file:
    width = float(input("\nEnter the width of the tire: "))
    
    aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
    diameter = float(input("Enter the diameter of the wheel in inches: "))

    #Calculate the volume of the tire
    volume = (
        math.pi * width **2 * aspect_ratio * 
        (width * aspect_ratio + 2540 * diameter)) / 10000000000

    #Add the results to the file
    print(
        f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, "
        f"{volume:.2f}", file=volume_file)
    
    #Display the results
    print(f"\nThe approximate volume is {volume:.2f} liters.")

    #Prompt the user to provide contact information
    yes_no = input(
        "\nWould you like to purchase a set of tires "
        "with these dimensions? (yes/no) ").lower()

    if yes_no == "yes":
        contact = input("\nGreat! Please provide your contact information: ")

        print(f"Contact:{contact}", file=volume_file)

        print(
            "Thank you for your information. "
            "Our customer service team will reach out to you shortly.\n")
        
    else:
        print("\nThank you for using the tire volume calculator. ")
        print("Have a great day!\n")