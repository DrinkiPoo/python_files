bleep = {
    "fuck": "f**k",
    "motherfucker": "motherf****er"
}
message = input("Please enter a dirty message: ")
words = message.split(" ")
clean = ""

for word in words:
    clean += bleep.get(word, word) + " "

print(clean)
