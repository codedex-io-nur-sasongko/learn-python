# Since 1927, "The Cyclone" rollercoaster has delighted riders visiting Coney Island in Brooklyn, New York. 🎢

# They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing the program for it!

# Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

# Use a combination of relational and logical operators to create the rules:

# If they are tall enough and have enough credits, print "Enjoy the ride!"
# Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
# Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
# Else, print a message saying they have not met either requirement.

height = int(input("What is your height in cm? "))
credits = int(input("How many credits do you have? "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")