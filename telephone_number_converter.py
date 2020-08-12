list = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

number = input('Please enter your telephone number: ')

string = ""
for x in number:
    string += " " + list.get(x, '!')

print(string)