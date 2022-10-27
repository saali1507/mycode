#!usr/bin/env python3


print ("Welcome to Hiker")

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

african_ranges = ["Atlas Mountains", "Drakensberg", "Ethiopian Highlands"

print("Which continent would you like to visit?")
userChoice = input()
if (userChoice.lower() == "Antartica".lower()):
    print("Sorry that it unavailable at this time.")
elif (userChoice.lower() == "South America".lower()):
    print("Great choice! Here are a few ranges")
elif (userChoice.lower() == "North America".lower()):
    print("Plenty of choices from there")
elif (userChoice.lower() == "Africa".lower()):
    print("We have a couple of suggestions you might like")
elif (userChoice.lower() == "Asia".lower()):
    print("Get ready for an adventure")
elif (userChoice.lower() == "Europe".lower()):
    print("The Alps await...")
elif (userChoice.lower() == "Australia".lower()):
    print("Gathering more data on this area, please try a different continent")
else:
    print("Please try again")
