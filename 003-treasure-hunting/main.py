name = input("What's your name traveller?\n")
print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")

print(
    f"You are at the bay {name}, there is 2 ship in front of you, the left ship is go to the Treasure Iland, the right one is going to the Death Iland\nWhitch direction to you want to go {name}?\n'left'/'right'"
)

direction1 = input("")

if direction1 == "left":
    print("You are choosed the Treasure Iland ship. The ship starts slowly")
    print("~~~~~~~~~~~~~~~")
    print(
        f"The ship is arrived to the Treasure Iland.\nDo you leave the ship and start searching to the jungle, or you stay {name}?\n'leave'/'stay'"
    )
    direction2 = input("")
    if direction2 == "leave":
        print(
            "You going into the jungle, deeper and deeper, then you see a massive light between the trees shines to a box in the sand"
        )
        print("On the box is a lock with a sticker and with interactive buttons")
        print("The sticker say:\nThe password is 111")
        print("What password are u give to the interactive lock?\n")
        direction3 = input("")
        if direction3 == "111":
            print(
                "The box onpening slowly, and u get a golden seed, but not an ordinarry seed, it is a golden seed of a golden apple tree\nSuccessfully found the treasure, Victory!"
            )
        else:
            print(
                "The box start to shining purple, it transforms to a supermassive little black hole and devouring the earth in a blink of an eye\nGame Over "
            )
    else:
        print(
            "A giant meteor is falling from the sky and crushing the ship to atoms including you as well\nGame Over"
        )
else:
    print(
        "You chose the Death Iland ship.\nThe ship starts slowly\n~~~~~~~~\n The ship sink at the middle of the ocean\nGame Over"
    )
