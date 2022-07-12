import enum

class Color(enum.Enum):
    red = '#ff0000'
    green = '#008000'
    blue = '#0000ff'


print(Color.green.name)  # green
print(Color.green.value)  # '#008000'
print(Color['green'].value)  # '#008000'


colors_list = [x.value for x in Color]
print(colors_list)
