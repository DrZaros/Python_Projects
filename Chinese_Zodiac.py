#Program to associate a year with a Chinese Zodiac symbol

def main():
    print("Welcome to the Chinese Zodiac program!")
    zodiac()

def zodiac(): 
    user_year = int(input("Put your birth year here: ")) 
    zodiac_number = user_year % 12

    if zodiac_number == 0:
          symbol = 'Monkey'

    elif zodiac_number == 1:
          symbol = 'Rooster'

    elif zodiac_number == 2:
          symbol = 'Dog'

    elif zodiac_number == 3:
          symbol = 'Pig'

    elif zodiac_number == 4:
          symbol = 'Rat'
          
    elif zodiac_number == 5:
          symbol = 'Ox'

    elif zodiac_number == 6:
          symbol = 'Tiger'

    elif zodiac_number == 7:
          symbol = 'Rabbit'

    elif zodiac_number == 8:
          symbol = 'Dragon'

    elif zodiac_number == 9:
          symbol = 'Snake'

    elif zodiac_number == 10:
          symbol = 'Horse'

    elif zodiac_number == 11:
          symbol = 'Sheep'

    else: 
        print('Invalid input, try again!')
        main()

    print("That is the year of the", symbol,'.')

main()
        
