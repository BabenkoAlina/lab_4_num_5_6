"""Module documentation"""


class Room:
    """Class module"""

    def __init__(self, name_r) -> None:
        """Func init
        """
        self.name_r = name_r
        self.description = None
        self.link = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """Func set desc
        """
        self.description = description

    def get_description(self):
        """Func get desc
        """
        return self.description

    def link_room(self, object: "Room", position):
        """Func link room
        """
        self.link[position] = object

    def set_character(self, name):
        """Func set ch
        """
        self.character = name

    def get_character(self):
        """Func get ch
        """
        return self.character

    def set_item(self, weapon):
        """Func set item
        """
        self.item = weapon

    def get_item(self):
        """Func get item
        """
        return self.item

    def get_details(self):
        """Func get det
        """
        print(f"{self.name_r}\n--------------------\n{self.description}\n")
        for side, room in self.link.items().__reversed__():
            print(f"The {room.name_r} is {side}")

    def move(self, command):
        """Func move
        """
        if self.link.get(command) is not None:
            return self.link.get(command)
        return self


COUNT = 0


class Character:
    """Class ch
    """

    def __init__(self, name, description) -> None:
        """Func init
        """
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def describe(self):
        """Func desc
        """
        print(self.description)

    def set_conversation(self, text):
        """Func set con
        """
        self.conversation = text

    def talk(self):
        """Func talk
        """
        print(self.conversation)

    def fight(self, item):
        """Func fight
        """
        if item == self.weakness:
            global COUNT
            COUNT += 1
            print(f"You fend {self.name} off with the {self.weakness}")
            return True
        print(f"{self.name} crushes you, puny adventurer")
        return False

    def get_defeated(self):
        """Func get def
        """
        return COUNT


class Enemy(Character):
    """Class enemy
    """

    def __init__(self, name, description) -> None:
        """Func init
        """
        super().__init__(name, description)

    def describe(self):
        """Func desc
        """
        print(f"{self.name} is here!\n{self.description}")

    def set_weakness(self, item_enemy):
        """Func set w
        """
        self.weakness = item_enemy


class Item:
    """Class item
    """

    def __init__(self, name_item) -> None:
        """Func init
        """
        self.name_item = name_item
        self.desc = None

    def set_description(self, text):
        """Func set desc
        """
        self.desc = text

    def get_name(self):
        """Func get name
        """
        return self.name_item

    def describe(self):
        """Func desc
        """
        print(f"The [{self.name_item}] is here - {self.desc}")
