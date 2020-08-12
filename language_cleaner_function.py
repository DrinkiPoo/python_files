#write a function to clean up the language

def language_cleaner():
    list = {
        "fuck": "fudge",
        "motherfucker": "mothertrucker",
        "shit": "shoot"
    }
    clean = ""
    message = input('Please enter your dirty message: ')
    words = message.split(" ")
    for word in words:
        clean += list.get(word, word) + " "

    return clean

print(language_cleaner())