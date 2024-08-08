# initialize the house points
gryffindor = 0;
ravenclaw = 0;
hufflepuff = 0;
slytherin = 0;

# Ask the user the first question
print("Q1) Do you like Dawn or Dusk?: ")
print("    1) Dawn")
print("    2) Dusk")
answer = int(input('Enter your answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravencalw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong Input")

# Ask the user the second question
print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")

answer = int(input('Enter your answer (1-4): '))
if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print("Wrong Input")

# Ask the user the third question
print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")

answer = int(input('Enter your answer (1-4): '))
if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print("Wrong Input")

# Calculate the house points
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print("🦁 Gryffindor!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print("🦅 Ravenclaw!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
  print("🦡 Hufflepuff!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print("🐍 Slytherin!")
else:
  print("You have not met any of the requirements.")