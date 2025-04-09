import random                               #importing the random mudule to generate random number
'''
    converting game in mathemetical form
    key      :   values
    --------------------
    stone    :      1
    paper    :      2
    scissors :      3
'''

def gameOn():
         compChoice = random.choice([1,2,3]) #generating random number from range 1 to 3 by importing random module and using choice function

    

         usrChoice = input("***Press s for stone or Press p for paper or Press c for scissors: ") #taking input from usrer

         keyValueDict =  {
                                "s" : 1, 
                                "p" : 2,               # making key value pair using dictionary
                                "c" : 3
                        }
         valueKeyDict =  {
                                1: "stone", 
                                2: "paper",            # making value key pair using dictionary
                                3: "scissors"                  
                        }
         print(f"\nusr choice is '{valueKeyDict[keyValueDict[usrChoice]]}' and computer choice is '{valueKeyDict[compChoice]}'\n")
         return compChoice,usrChoice,keyValueDict,valueKeyDict

# setting conditions for win,loss and draw
compWinCount = 0
usrWinCount = 0
while(compWinCount<3 and usrWinCount<3):
    compChoice,usrChoice,keyValueDict,valueKeyDict= gameOn()
    if (keyValueDict[usrChoice] == compChoice):
        print("draw\n")
        print(f"Computer score : {compWinCount} and User score : {usrWinCount}\n")
    elif(valueKeyDict[compChoice] == "stone" and valueKeyDict[keyValueDict[usrChoice]]=="scissors"):
        print("Computer wins!!\n")
        compWinCount+=1
        print(f"Computer score : {compWinCount} and User score : {usrWinCount}\n")
    elif(valueKeyDict[compChoice] == "scissors" and valueKeyDict[keyValueDict[usrChoice]]=="paper"):
        print("Computer wins!!\n")
        compWinCount+=1
        print(f"Computer score : {compWinCount} and User score : {usrWinCount}\n")
    elif(valueKeyDict[compChoice] == "paper" and valueKeyDict[keyValueDict[usrChoice]]=="stone"):
        print("Computer wins!!\n")
        compWinCount+=1
        print(f"Computer score : {compWinCount} and User score : {usrWinCount}\n")
    elif(valueKeyDict[compChoice] =="paper"  and valueKeyDict[keyValueDict[usrChoice]]=="scissors"):
        print("User wins!!\n")
        usrWinCount+=1
        print(f"Computer score : {compWinCount} and User score : {usrWinCount}\n")
    elif(valueKeyDict[compChoice] =="stone"  and valueKeyDict[keyValueDict[usrChoice]]=="paper"):
        print("User wins!!\n")
        usrWinCount+=1
        print(f"Computer score : {compWinCount} and User score : {usrWinCount}\n")
    elif(valueKeyDict[compChoice] =="scissors"  and valueKeyDict[keyValueDict[usrChoice]]=="stone"):
        print("User wins!!\n")
        usrWinCount+=1
        print(f"Computer score : {compWinCount} and User score : {usrWinCount}\n")
    else:
        print("invalid choice")
print(f"Final score:\nComputer score : {compWinCount} and User score : {usrWinCount}\n")
if(compWinCount>usrWinCount):
    print("         Game Over!!\n         You lost !!  \n         Better luck next time!!\n")
else:
    print("         Game Over !!\n          You 'Win'!!\n")
    
    
    