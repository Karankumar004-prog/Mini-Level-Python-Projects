import random

# Get the number of players
num_players = int(input("Enter the number of players: "))
players = [input(f"Enter the name of player {i + 1}: ") for i in range(num_players)]
survivors = players.copy()

# Display game choices
print("Enter your game choice:")
print("1. Classic")
print("2. One Bullet Chance")
print("3. Custom Bullet Chance")

choice = int(input("Choose a game mode (1-3): "))

if choice == 1:
    # Classic mode (One bullet in a 6-chamber revolver, shell rolls every shot)
    all_survived = True
    for player in survivors[:]:
        input(f"{player}, press Enter to pull the trigger...")
        bullet = random.randint(1, 6)
        shot = random.randint(1, 6)
        if shot == bullet:
            print(f"BANG!!! {player} is dead...")
            survivors.remove(player)
            all_survived = False
        else:
            print(f"CLICK!!! {player} survived this round...")
    if all_survived:
        print("\nCongratulations! Everyone survived this round!")
    else:
        print(f"\nThe luckiest one who survived till the end is {survivors[0]}!" if survivors else "All of us are dead.")

elif choice == 2:
    # One Bullet Chance (One bullet is permanently placed, game continues until only one survives)
    bullet = random.randint(1, 6)
    index = 0
    while len(survivors) > 1:
        player = survivors[index % len(survivors)]
        input(f"{player} pulls the trigger... Press Enter to continue.")
        shot = random.randint(1, 6)
        if shot == bullet:
            print(f"Bang! {player} is dead...")
            survivors.remove(player)
            if not survivors:
                print("\nAll of us are dead.")
                break
            print("Survivors so far:", ", ".join(survivors))
        else:
            print(f"Click! {player} survived.")
        index += 1
    print(f"\nThe luckiest one who survived till the end is {survivors[0]}!" if survivors else "All of us are dead.")

elif choice == 3:
    # Custom Bullet Chance (Each player takes a turn, custom bullets, game continues until one survives)
    bullets = int(input("Enter the number of bullets (1-6): "))
    cylinder = [0] * 6
    bullet_positions = random.sample(range(6), bullets)
    for pos in bullet_positions:
        cylinder[pos] = 1
    index = 0
    while len(survivors) > 1:
        player = survivors[index % len(survivors)]
        input(f"{player}, press Enter to pull the trigger...")
        shot = random.randint(0, 5)
        if cylinder[shot] == 1:
            print(f"Bang! {player} is dead...")
            survivors.remove(player)
            if not survivors:
                print("\nAll of us are dead.")
                break
            print("Survivors so far:", ", ".join(survivors))
        else:
            print(f"Click! {player} survived.")
        index += 1
    print(f"\nThe luckiest one who survived till the end is {survivors[0]}!" if survivors else "All of us are dead.")

else:
    print("Invalid choice! Please restart the game and select a valid option.")
