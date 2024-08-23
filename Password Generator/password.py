import random
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
special_characters = '!@#$%^&*()-_=+[]{}|;:\'",.<>?/~`'
numbers = '0123456789'

def passwordRange():
    print('\nSet your password as you want\n')
    print('1) 4 Characters Password')
    print('2) 8 Characters Password')
    print('3) 12 Characters Password')
    choice = int(input('>'))
    if choice == 1:
        return 4
    elif choice == 2:
        return 8
    elif choice == 3:
        return 12
    else:
        print('Invalid Input, by default generate 5 characters password')
        return 5

def characters():
    charactersList = []
    print('\nYSelect Characters you want to ADD: ')
    print('Press "y" for Yes and "n" for No\n')
    
    if input('Upper Case e.g (L,E,W) (y/n): ').lower() == 'y':
        charactersList.append(uppercase_letters)

    if input('Lower Case e.g (l,e,w) (y/n): ').lower() == 'y':
        charactersList.append(lowercase_letters)
        
    if input('Special Characters e.g (@,#,$) (y/n): ').lower() == 'y':
        charactersList.append(special_characters)
        
    if input('Digits e.g (1,2,3) (y/n): ').lower() == 'y':
        charactersList.append(numbers)
    
    return charactersList

def passwordGenerator():
    passRange = passwordRange()
    charsList = characters()
    
    if not charsList:
        print("No character types selected. Please try again.")
        return ""
    
    all_characters = ''.join(charsList)
    password = ''.join(random.choice(all_characters) for _ in range(passRange))
    
    return password

myPassword = passwordGenerator()
print("\nGenerated Password:", myPassword)
print('\n')