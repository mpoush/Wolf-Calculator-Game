def Game():
    print("Welcome")
    print("You find yourself looking towards a bridge and a cave.")
    print("What do you do?")
    print("A Go into the cave")
    print("B Go across the bridge")
    print("C Jump of the bridge")
    C1 = input()
    if C1 == "A":
        print("You enter the cave and see two paths")
        print("A Go left")
        print("B Go right")
        C2 = input()
        if C2 == "A":
            print("You go down the left path and trip and fall and break your neck")
            print("Game Over")
        elif C2 == "B":
            print("You go down the right path and see a treasure chest, it has a marking that says 'one, th'")
            print("You ponder about what it means")
            print("You go to open it but suddenly feel blood trickle down your neck")
            print("Game Over")
    elif C1 == "B":
        print("You go across the bridge and see two paths")
        print("What do you do?")
        print("A Go left")
        print("B Go right")
        print("C Go back")
        C3 = input()
        if C3 == "C":
            print("You decide to go back across the bridge")
            print("but see a dark figure cutting the rope holding the bridge up and you plunge into the abyss")
            print("Game Over")
        elif C3 == "B":
            print("As you travel down the right path, you think you see a chest")
            print("But as you reach for it you suddenly fall into a hidden hole in the ground")
            print("You see a marking on the wall that says 'two, ek'")
            print("You try to escape bu someone drops a large rock on your head")
            print("Game Over")
        elif C3 == "A":
            print("As you start down the path you get a bad feeling and wonder if you should speed up, go back and cut the bridge, or hide in a bush")
            print("A Speed up")
            print("B Cut bridge")
            print("C Hide")
            C4 = input()
            if C4 == "A":
                print("You run faster and find yourself near a temple looking wall")
                print("There is an inscribing on the wall that reads")
                print("'You will find the key in death, numbered from one to four, put it together in the void, and destory the evil orb'")
                print("It makes no sense, so you keep walking but fall off a cliff and die")
                print("Game Over")
            elif C4 == "B":
                print("You head back to the bridge and cut it down")
                print("But as you turn to leave you get shoved into the abyss, never to be seen again")
                print("Game Over")
            elif C4 == "C":
                print("You quickly hide in a nearby bush, and just a few seconds later you hear somebody approaching")
                print("Right as he walks infront of the bush you are in, he turns and looks you right in the eye...")
                print("A Run")
                print("B Fight")
                C5 = input()
                if C5 == "B":
                    print("PLACEHOLDER: You fought.")
                    print("Game Over")
                elif C5 == "A":
                    print("PLACEHOLDER: You ran.")
                    print("Game Over")
    elif C1 == "C":
        print("You fall off the bridge and die, what did you expect lol")
        print("Game Over")

if __name__ == '__main__':
    while True:
        Game()
