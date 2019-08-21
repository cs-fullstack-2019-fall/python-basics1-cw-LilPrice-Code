# Problem 1:
#
# Create two variables. One should equal “My name is: “ and the other should equal your actual name. Print the two variables in one print message.
#
sentence = "My name is: "
name = "Shoshard"

print (sentence + name)

# Problem 2:
#
# Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.
#

extra = int(input("Enter extra Credit "))
if extra > 20:
    print("That’s too much extra credit")
elif extra < 5:
    print("That’s not enough extra credit.")

# Problem 3:#
# Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.
#
password = input('Enter a password ')
repassword = input("Re-enter paswword ")
if password == repassword:
    print("Correct")
else:
    print("INCORRECT")
#
# Problem 4:
#
# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”

card1 = int(input("Enter a number "))
card2 = int(input("Enter a number "))
sum = card1 + card2

if sum < 21:
    print('The total is ' +str(sum))
elif sum > 21:
    print("BUST")
elif sum == 21:
    print("BLACKJACK!!")