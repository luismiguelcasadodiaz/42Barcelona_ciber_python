#!/usr/bin/python3


"""
Objective
The goal of the exercise is to tackle the notion inheritance of class.

Instructions
Create a GotCharacter class and initialize it with the following attributes:
• first_name,
• is_alive (by default is True).

"""


class GotCharacter:
    """
        A Class representing a Game's character.
    """
    def __init__(self, first_name="No Name given", is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):

        if self.is_alive:
            return f"I am '{self.first_name}' and i am alive"
        else:
            return f"I an the soul of '{self.first_name}' that passed away"

    def __repr__(self):
        return f"GotCharacter('{self.first_name}', {self.is_alive})"


"""
Pick up a GoT House (e.g., Stark, Lannister...) and create a child class
that inherits from GotCharacter and define the following attributes:
• family_name (by default should be the same as the Class)
• house_words (e.g., the House words for the Stark House is:
    "Winter is Coming")
"""


class Lannister(GotCharacter):
    """
        A Class representing the Lannister family.
        or when bad things happen to good people.
    """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=True)
        self.famivacialy_name = "Lannister"
        self.house_words = "Hear Me Roar"

    """
    Add two methods to your child class:
    • print_house_words: prints the House words,
    • die: changes the value of is_alive to False.
    """
    def print_house_words(self):
        print(self.house_words)
        return

    def die(self):
        if self.is_alive:
            self.is_alive = False
        else:
            print(f"deaths can not die twice")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first_name},{self.is_alive})"

    def __str__(self):
        result = f"Instance of {self.__class__.__name__}:\n"
        for k, v in self.__dict__.items():
            result = result + f"\t{k}:{v}\n"
        result = result + "=" * 20
        return result


if __name__ == "__main__":
    pepe = GotCharacter("LUis")
    print("pepe", pepe)
    pepo = eval(repr(pepe))
    print("Pepo", pepo)
    arya = Lannister("Arya")
    print(arya)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
    arya.die()
    print(arya.__doc__)
    print(arya)
    pepe = GotCharacter("")
    print("pepe", pepe)
