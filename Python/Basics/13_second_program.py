# Referencias: Build 10 Real World Applications(Udemy)
#Este programa reune los conocimientos de los principios basicos de python

def string (user_input):
    user_input_splited = user_input.split()

    if user_input_splited[0].lower() in questions:
        if user_input[-1] != "?":
            user_input = user_input+"?"
    else:
        if user_input[-1] != ".":
            user_input = user_input+"."

    return user_input.capitalize()


questions = ["how", "when", "what", "why"]
user_inputs = []


while True:
    user_input = input("Say something: ")
    if user_input == "\End":
        break
    else:
        user_inputs.append(string(user_input))


final_str = ""
for i in user_inputs:
    final_str = f"{final_str}{i} "


print(final_str)
