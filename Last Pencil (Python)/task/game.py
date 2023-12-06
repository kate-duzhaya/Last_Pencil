import random


def change_player_index(ind):
    global player_index
    if ind + 1 == len(players):
        player_index = 0
    else:
        player_index += 1


def deduct_pencils():
    global num_pencils, deduct
    num_pencils -= deduct
    print("|" * num_pencils)
    change_player_index(player_index)


players = ["Human", "Bot"]
print("How many pencils would you like to use:")
while True:
    try:
        num_pencils = int(input())
        if num_pencils > 0:
            break
        elif num_pencils == 0:
            print("The number of pencils should be positive")
        else:
            print("The number of pencils should be numeric (the minus sign is not a numeric)")
    except ValueError:
        print("The number of pencils should be numeric")
print(f"Who will be the first ({str(', '.join(players))}):")
while True:
    first_player = input()
    if first_player.capitalize() in players:
        break
    else:
        print(f"Choose between {str(' and '.join(players))}")

player_index = players.index(f"{first_player.capitalize()}")
print("|" * num_pencils)
while num_pencils > 0:
    print(f"{players[player_index]}'s turn:")
    if player_index != 1:
        while True:
            try:
                deduct = int(input())
                if deduct <= 0 or deduct > 3:
                    print("Possible values: '1', '2' or '3'")
                elif num_pencils - deduct < 0:
                    print("Too many pencils were taken")
                else:
                    deduct_pencils()
                    break
            except ValueError:
                print("Possible values: '1', '2' or '3'")
    else:
        if num_pencils % 4 == 0:
            deduct = 3
            print(deduct)
            deduct_pencils()
        elif num_pencils == 1 or num_pencils % 2 == 0:
            deduct = 1
            print(deduct)
            deduct_pencils()
        elif num_pencils % 4 == 1:
            deduct = random.choice([1, 2, 3])
            print(deduct)
            deduct_pencils()
        elif num_pencils % 2 == 1:
            deduct = 2
            print(deduct)
            deduct_pencils()

print(f"{players[player_index]} won")
