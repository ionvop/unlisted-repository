import random
import time


def main():
    items = ["beer", "handcuffs", "cigarette", "knife", "magnifying glass"]
    player_items = []
    opponent_items = []
    player_health = 6
    opponent_health = 6
    double_damage = False
    player_skip_turn = False
    opponent_skip_turn = False
    opponent_knows = False
    phase = "draw"
    turn = "player"
    load = []
    user_in = ""
    opponent_in = ""

    while True:
        clear_console()

        if phase == "draw":
            player_received_items = []
            opponent_received_items = []

            for i in range(random.randint(1, 5)):
                player_received_items.append(items[random.randint(0, 4)])
                opponent_received_items.append(items[random.randint(0, 4)])

            for element in player_received_items:
                player_items.append(element)

            for element in opponent_received_items:
                opponent_items.append(element)

            print("You received:")

            for element in player_received_items:
                print(element)

            time.sleep(3)
            phase = "load"
            continue
        elif phase == "load":
            load = []

            for i in range(random.randint(1, 4)):
                load.append("live")

            for i in range(random.randint(1, 4)):
                load.append("blank")

            random.shuffle(load)
            print("Load:")

            for element in load:
                print(element)

            random.shuffle(load)
            time.sleep(3)
            phase = "action"
            continue
        elif phase == "action":
            if player_health <= 0 or opponent_health <= 0:
                phase = "end"
                continue

            if len(load) <= 0:
                phase = "draw"
                continue

            if turn == "player":
                if player_skip_turn:
                    turn = "opponent"
                    player_skip_turn = False
                    print("Your turn is skipped")
                    time.sleep(3)
                    continue

                print("Opponent's health: " + str(opponent_health))
                print("Your health: " + str(player_health))
                print()
                print("Opponent's items:")

                for element in opponent_items:
                    print(element)

                print()
                print("Your items:")

                for element in player_items:
                    print(element)

                print()
                print("Type the name of the item to use")
                print("Type 'shoot' to start shooting")
                print()
                user_in = input("Enter command: ")

                if player_items.count(user_in) > 0:
                    phase = "item"
                    continue
                elif user_in == "shoot":
                    phase = "shoot"
                    continue
                else:
                    print("Invalid command")
                    time.sleep(3)
                    continue
            elif turn == "opponent":
                opponent_in = ""

                if opponent_skip_turn:
                    turn = "player"
                    opponent_skip_turn = False
                    print("Opponent's turn is skipped")
                    time.sleep(3)
                    continue

                if len(opponent_items) > 0:
                    if random.randint(1, 3) != 1:
                        opponent_in = opponent_items[random.randint(0, len(opponent_items) - 1)]

                if opponent_in == "":
                    opponent_in = "shoot"

                if opponent_items.count(opponent_in) > 0:
                    phase = "item"
                    continue
                elif opponent_in == "shoot":
                    phase = "shoot"
                    continue
        elif phase == "item":
            if turn == "player":
                player_items.remove(user_in)

                if user_in == "beer":
                    print("You racked the shotgun...")
                    
                    if load[0] == "live":
                        print("A live comes out")
                    elif load[0] == "blank":
                        print("A blank comes out")

                    load = load[1:]
                    time.sleep(3)
                    phase = "action"
                    continue
                elif user_in == "handcuffs":
                    print("You used the handcuffs on the opponent")
                    opponent_skip_turn = True
                    time.sleep(3)
                    phase = "action"
                    continue
                elif user_in == "cigarette":
                    print("You smoked a cigarette")
                    print("You earned a charge")
                    player_health += 1

                    if player_health > 6:
                        player_health = 6

                    time.sleep(3)
                    phase = "action"
                    continue
                elif user_in == "knife":
                    print("You sawed off the shotgun")
                    print("Shotgun now deals 2 damage for this turn")
                    double_damage = True

                    time.sleep(3)
                    phase = "action"
                    continue
                elif user_in == "magnifying glass":
                    print("You used the magnifying glass")
                    
                    if load[0] == "live":
                        print("It's a live")
                    elif load[0] == "blank":
                        print("It's a blank")

                    time.sleep(3)
                    phase = "action"
                    continue
            elif turn == "opponent":
                opponent_items.remove(opponent_in)

                if opponent_in == "beer":
                    print("The opponent racks the shotgun...")
                    
                    if load[0] == "live":
                        print("A live comes out")
                    elif load[0] == "blank":
                        print("A blank comes out")

                    load = load[1:]
                    time.sleep(3)
                    phase = "action"
                    continue
                elif opponent_in == "handcuffs":
                    print("The opponent uses the handcuffs on you")
                    player_skip_turn = True
                    time.sleep(3)
                    phase = "action"
                    continue
                elif opponent_in == "cigarette":
                    print("The opponent smokes a cigarette")
                    print("The opponent earns a charge")
                    player_health += 1

                    if player_health > 6:
                        player_health = 6

                    time.sleep(3)
                    phase = "action"
                    continue
                elif opponent_in == "knife":
                    print("The opponent saws off the shotgun")
                    print("Shotgun now deals 2 damage for this turn")
                    double_damage = True

                    time.sleep(3)
                    phase = "action"
                    continue
                elif opponent_in == "magnifying glass":
                    print("The opponent uses the magnifying glass")
                    print("Interesting...")
                    opponent_knows = True
                    time.sleep(3)
                    phase = "action"
                    continue
        elif phase == "shoot":
            if turn == "player":
                print("Who will you shoot?")
                print()
                print("opponent")
                print("yourself")
                print()
                print("Type 'back' to return")
                print()
                user_in = input("Enter command: ")

                if user_in == "yourself":
                    print("You try to shoot yourself")

                    if load[0] == "live":
                        print("The shotgun fires")
                        player_health -= 1

                        if double_damage:
                            print("It dealt 2 damage")
                            player_health -= 1
                        
                        double_damage = False
                        time.sleep(3)
                        turn = "opponent"
                        phase = "action"
                        load = load[1:]
                        continue
                    if load[0] == "blank":
                        print("It's a blank")
                        double_damage = False
                        time.sleep(3)
                        turn = "player"
                        phase = "action"
                        load = load[1:]
                        continue
                elif user_in == "opponent":
                    print("You try to shoot the opponent")

                    if load[0] == "live":
                        print("The shotgun fires")
                        opponent_health -= 1

                        if double_damage:
                            print("It dealt 2 damage")
                            opponent_health -= 1

                        double_damage = False
                        time.sleep(3)
                        turn = "opponent"
                        phase = "action"
                        load = load[1:]
                        continue
                    elif load[0] == "blank":
                        print("It's a blank")
                        double_damage = False
                        time.sleep(3)
                        turn = "opponent"
                        phase = "action"
                        load = load[1:]
                        continue
                elif user_in == "back":
                    phase = "action"
                    continue
                else:
                    print("Invalid command")
                    time.sleep(3)
                    continue
            elif turn == "opponent":
                opponent_in = ""

                if double_damage:
                    opponent_in = "player"

                if opponent_knows:
                    if load[0] == "live":
                        opponent_in = "player"
                    elif load[0] == "blank":
                        opponent_in = "opponent"

                if opponent_in == "":
                    if random.randint(1, 3) == 1:
                        opponent_in = "opponent"
                    else:
                        opponent_in = "player"

                if opponent_in == "player":
                    print("The opponent tries to shoot you")
                    
                    if load[0] == "live":
                        print("The shotgun fires")
                        player_health -= 1

                        if double_damage:
                            print("It dealt 2 damage")
                            player_health -= 1
                            
                        double_damage = False
                        time.sleep(3)
                        turn = "player"
                        phase = "action"
                        load = load[1:]
                        continue
                    elif load[0] == "blank":
                        print("It's a blank")
                        double_damage = False
                        time.sleep(3)
                        turn = "player"
                        phase = "action"
                        load = load[1:]
                        continue
                elif opponent_in == "opponent":
                    print("The opponent tries to shoot themselves")

                    if load[0] == "live":
                        print("The shotgun fires")
                        opponent_health -= 1

                        if double_damage:
                            print("It dealt 2 damage")
                            opponent_health -= 1

                        double_damage = False
                        time.sleep(3)
                        turn = "player"
                        phase = "action"
                        load = load[1:]
                        continue
                    elif load[0] == "blank":
                        print("It's a blank")
                        double_damage = False
                        time.sleep(3)
                        turn = "opponent"
                        phase = "action"
                        load = load[1:]
                        continue
        elif phase == "end":
            if opponent_health <= 0:
                print("You won!")
            elif player_health <= 0:
                print("You lose!")

            time.sleep(3)
            exit()


def clear_console():
    for i in range(100):
        print()


if __name__ == "__main__":
    main()
