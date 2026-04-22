import random
s1 = {random.randint(1,10),random.randint(1,10),random.randint(1,10)}
while len(s1) > 0:
    guess = int(input("The computer has picked three numbers from 1 - 10. Try to guess them."))
    if guess in s1:
        print("Well done! That is one of the numbers")
        s1.remove(guess)
    else:
        print("That is not one of the numbers. Better luck next time!")
print("Congratulations, you have beat the game!")