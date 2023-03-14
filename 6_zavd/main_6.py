"""Module"""

import cemetery

first = cemetery.Side("First part")
first.set_description("This is the darkest part of the cemetery...")

second = cemetery.Side("Second part")
second.set_description(
    "There you can see a small light. Maybe something good?")

third = cemetery.Side("Third part")
third.set_description("What is it? A scream?")

yard = cemetery.Side("Yard")
yard.set_description("Peaceful place for trees and flowers")

first.link_side(second, "south")
second.link_side(first, "north")
second.link_side(yard, "west")
yard.link_side(third, "east-south")
third.link_side(second, "east")

ghost = cemetery.Enemy("Ghost-dog", "Just a small dead doggy")
ghost.set_conversation("-Bark! Bark! Grrr...")
ghost.set_weakness("bone")
yard.set_character(ghost)

vincent = cemetery.Enemy("Vincent", "Forever young vampire")
vincent.set_conversation("-Are you ready for death, my dear?")
vincent.set_weakness("garlic")
second.set_character(vincent)

john = cemetery.Enemy("John", "Is it my old friend-werewolf?..")
john.set_conversation("-Run... Or I`ll kill you...")
john.set_weakness("gun")
first.set_character(john)

gun = cemetery.Item("gun")
gun.set_description("a extremely powerful gun with silver bullets")
third.set_item(gun)

bone = cemetery.Item("bone")
bone.set_description("a little fresh bone")
second.set_item(bone)

garlic = cemetery.Item("garlic")
garlic.set_description("an extreme garlic from your grandma")
first.set_item(garlic)

current_room = second
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    print("Commands are: take, fight, talk, side")
    command = input("> ")

    if command in ["north", "south", "east", "west", "east-south"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        print(f"You have: {backpack}")
        if inhabitant is not None:
            if inhabitant is not ghost:
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with):
                        # What happens if you win?
                        print("You are a brave human!")
                        current_room.character = None
                        if inhabitant.get_defeated() == 2:
                            print("Congratulations, you are not dead!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("Oh fck, you lost the fight.")
                        print("That's the end... Bye")
                        dead = True
                else:
                    print("You lost a " + fight_with + "somewhere... Sht.")
            else:
                print("You want to kill a dog, mthrfckr?\nWhat do you want really:\
 give a bone (give) or not (no)?")
                choice = input("> ")
                if choice == "give":
                    print("You gave a bone to doggy. You are a good person")
                    backpack.remove("bone")
                elif choice == "no":
                    print("Find a bone, looser!")
                else:
                    print("Are you deaf? Fck off!")
        else:
            print("There is no one here")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your pocket")
            backpack.append(item.get_name())
            current_room.set_item(None)
            print(f"You have: {backpack}")
        else:
            print("There's nothing to take, sweetie!")
    else:
        print("I don't know how to " + command)
