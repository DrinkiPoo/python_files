command = ''
started = False
while True:
    command = input('>').lower()
    if command == 'quit':
        break
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit the game
        ''')
    elif command == 'quit':
        break
    elif command == 'start':
        if started:
            print('The car has already started! Please make another selection')
        else:
            print('The car started.')
            started = True
    elif command == 'stop':
        if not started:
            print('The car is already stopped! Please make another selection')
        else:
            print('The car stopped.')
            started = False
    else:
        print("I don't understand this shit!")


print('Game ended!')