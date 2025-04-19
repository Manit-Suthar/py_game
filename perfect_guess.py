from random import randint

class NumberGuess:
    def __init__(self,n):
        self.n = n
    def fun(self):
        guessList = []
        guessedNum = int(input("Guess the number : "))
        guessList.append(guessedNum)
        while(guessedNum!= self.n):
            if(guessedNum > self.n):
                guessedNum = int(input("Your number is greater than computer's num\nNext guess: "))
                guessList.append(guessedNum)
            elif(guessedNum < self.n):
                guessedNum = int(input("Your number is smaller than computer's num\nNext guess: "))
                guessList.append(guessedNum)
        return guessList
    


print("Hey there!!Let's play a number guessing game:\nI have selected a number from 1 to 100:\nLet's see in how many turns you guess it right:")
compNum = randint(1,100)
obj = NumberGuess(compNum)
guess = obj.fun()
for i in range(len(guess)):
    print(f"{guess[i]}::", end ="")
print(f"\nComputer selected {compNum} and you took {len(guess)-1} wrong guess to guess the correct number. ")


