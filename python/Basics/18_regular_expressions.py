import re     # Regular expressions module


patterns = ['term1', 'term2']


text = 'This is a string with term1, not the other'


for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern, text):     # Retronara verdadero si encuentra el patron dentro del texto
        print("Match")
    else:
        print("No Match")
