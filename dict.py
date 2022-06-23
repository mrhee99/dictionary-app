import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    # turning the input word into lowercase
    word = word.lower()
    # if the word is in the dataset, it will give out the definition
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    # if the user makes a mistake in spelling, the program will suggest similar one
    elif len(get_close_matches(word, data.keys()))>0:
        # the wrong user input will be replaced with the closest matching word suggested
        yn=input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please try again."
        else:
            return "We did not understand your entry."

    else:
        return "The word does not exist. Please try again."

# get the user input and go back to the function and find the word
word = input("Welcome to the dictionary! Look up your word: ")
# print out the definition
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)