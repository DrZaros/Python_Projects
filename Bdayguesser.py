#Card one and basic explanation of the game
print("Welcome to the birthday guessing game!")


print("1, 3, 5, 7" + "\n9, 11, 13, 15" + "\n17, 19, 21, 23" + "\n25, 27, 29, 31")
print("Is your birthday on set one?")
set_one = str(input("Enter yes or no: "))
set_one = set_one.title()

while set_one != 'Yes' and set_one != 'No':
    print('Invalid input! Try again.')
    set_one = str(input("Enter yes or no: "))
    set_one = set_one.title()

#Card Two
print("2, 3, 6, 7" + "\n10, 11, 14, 15" + "\n18, 19, 22, 23" + "\n26, 27, 30, 31")
print("Is your birthday on set two?")
set_two=str(input("Enter yes or no: "))
set_two = set_two.title()

while set_two != 'Yes' and set_two != 'No':
    print('Invalid input! Try again.')
    set_two = str(input("Enter yes or no: "))
    set_two = set_two.title()

#Card Three
print("4, 5, 6, 7" + "\n12, 13, 14, 15" + "\n20, 21, 22, 23" + "\n28, 29, 30, 31")
print("Is your birthday on set three?")
set_three=str(input("Enter yes or no: ")) 
set_three = set_three.title()

while set_three != 'Yes' and set_three != 'No':
    print('Invalid input! Try again.')
    set_three = str(input("Enter yes or no: "))
    set_three = set_three.title()

#Card Four
print("8, 9, 10, 11" + "\n12, 13, 14, 15" + "\n24, 25, 26, 27" + "\n28, 29, 30, 31")
print("Is your birthday on set four?")
set_four=str(input("Enter yes or no: "))
set_four = set_four.title()

while set_four != 'Yes' and set_four != 'No':
    print('Invalid input! Try again.')
    set_four = str(input("Enter yes or no: "))
    set_four = set_four.title()

#Card Five
print("16, 17, 18, 19" + "\n20, 21, 22, 23" + "\n24, 25, 26, 27" + "\n28, 29, 30, 31")
print("Is your birthday on set five?")
set_five=str(input("Enter yes or no: "))
set_five = set_five.title()

while set_five != 'Yes' and set_five != 'No':
    print('Invalid input! Try again.')
    set_five=str(input("Enter yes or no: "))
    set_five = set_five.title()
    
    


user_date=0 

if set_one == 'Yes':
    user_date=user_date +1;

if set_two == 'Yes':
    user_date=user_date +2;

if set_three == 'Yes':
    user_date=user_date+4;
    
if set_four == 'Yes':
    user_date=user_date+8;

if set_five == 'Yes':
    user_date=user_date+16;
    
print("Your birthdate is:", user_date, ".") 
    

    
