import string

def slugify(userInput) :
    for char in userInput:
        if char not in string.ascii_letters and char != ' ':
            userInput = userInput.replace(char, '')

    output = userInput.lower().replace(' ', '-')

    for char in output:
        if char is output[-1] and char == '-':
            output = output[:-1]

    return output;