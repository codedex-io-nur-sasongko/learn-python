import random
import time

# Initial game setup
player_hp = 100
werewolf_hp = 100
game_over = False
day = 1

# Introduction
print("******************************************************************")
print("Welcome to the Werewolf Game!")
print("You are a villager trying to survive the night.")
print("A werewolf is on the prowl. Make the right choices to survive.\n")
print("Build by @nur-sasongko using Python")
print("******************************************************************\n")

# Character creation
name = input("What is your name, brave villager?: ")
print(f"Hello, {name}! The night is dark and full of terrors.")
print("You must be cautious and make the right decisions to survive.\n")


while not game_over:
    print(f"\n--- Day {day} ---")
    print(f"Your HP: {player_hp}")
    print(f"Werewolf's HP: {werewolf_hp}\n")

    print("You have the following options:")
    print("1. Attack the werewolf")
    print("2. Hide in your house")
    print("3. Run into the forest")
    
    choice = input("What do you choose? (1/2/3): ")
    
    if choice == '1':
        print("\nYou decide to fight the werewolf!")
        player_attack = random.randint(10, 30)
        werewolf_attack = random.randint(10, 30)
        
        werewolf_hp -= player_attack
        player_hp -= werewolf_attack
        
        print(f"You dealt {player_attack} damage to the werewolf!")
        print(f"The werewolf attacked you back and dealt {werewolf_attack} damage!\n")
        
    elif choice == '2':
        print("\nYou hide in your house, hoping the werewolf doesn't find you.")
        hide_success = random.choice([True, False])
        
        if hide_success:
            print("The werewolf didn't find you. You are safe for now.\n")
        else:
            print("The werewolf found you and attacked!")
            player_attack = random.randint(10, 30)
            player_hp -= player_attack
            print(f"The werewolf dealt {player_attack} damage to you!\n")
            
    elif choice == '3':
        print("\nYou run into the forest, trying to lose the werewolf.")
        escape_success = random.choice([True, False])
        
        if escape_success:
            print("You managed to escape the werewolf. You are safe for now.\n")
        else:
            print("The werewolf caught up to you and attacked!")
            player_attack = random.randint(10, 30)
            player_hp -= player_attack
            print(f"The werewolf dealt {player_attack} damage to you!\n")
    
    # Check if the game is over
    if player_hp <= 0:
        print("You have been defeated by the werewolf. Game over.")
        game_over = True
    elif werewolf_hp <= 0:
        print("Congratulations! You defeated the werewolf. You win!")
        game_over = True
    else:
        print("The night continues...\n")
        day += 1
        time.sleep(1)

print("Thank you for playing the Werewolf Game!")