class GameCharacter:

    # Fields
    # Default params
    speed = 5

    # Constructor
    # self refers to the instance of the class. It is automatically passed as an
    # argument when the method is called with dot notation. i.e: instance.method 
    def __init__(self, name, width, height, x_pos, y_pos):
        """help text"""
        # self.name refers to the field name of the object.
        # name is the argument passed to the constructor.
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    # Method
    def move(self, by_x_amount, by_y_amount):
        """help text"""
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


# New instance of the class, must pass the values required by constructor
character_0 = GameCharacter("char_0", 50, 100, 100, 100)

# Reassign values to object fields
character_0.name = "Andres"

# Call a method of the object
character_0.move(50, 100)

# Check the class of an object
character_0.__class__

# Class name as a string
character_0.__class__.__name__

# check attribute in object
hasattr(character_0, "speed") # true