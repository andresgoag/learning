# Somethimes is useful to define a subclass that has all the fields and methods
# of a superclass, and modify just the things that change. 
# This is called inheritance.
from .basics import GameCharacter

class PlayerCharacter(GameCharacter):

    speed = 10

    # Always has to have a constructor
    # The player character will be able to define only the x and y position.
    # The width and height are fixed.
    def __init__(self, name, x_pos, y_pos):
        # super() is a reference to the superclass. i.e: call the __init__ 
        # function of the parent class.
        super().__init__(name, 100, 100, x_pos, y_pos)

    # overwrite the move function to only be able to move in the y coordinate.
    def move(self, by_y_amount):
        super().move(0, by_y_amount)


player_character = PlayerCharacter("P_character", 500, 500)

print(player_character.name)
print(player_character.x_pos)
print(player_character.y_pos)
player_character.move(77)
print(player_character.x_pos)
print(player_character.y_pos)