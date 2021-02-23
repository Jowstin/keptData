import accounts
import os
tries=0
newUser=input("Are you a new user?(yes or no): ").lower()
if newUser == "yes":
    username=input("Please enter a username.: ")
    pin=input("Please enter a pin.: ")
    pData = pin
    os.chdir("accounts")
    fileName='{}.py'.format(username)
    with open(fileName, 'a') as f:
        f.write('userPin = "{}"'.format(pData))
    f.close()
    os.chdir("..")
elif newUser == "no":
    os.chdir("accounts")
    entUser=input("What is your username?: ")
    if os.path.exists('{}.py'.format(entUser)) == True:
        while True:
            if tries < 3:
                entPin=int(input("What is your pin?: "))
                if entPin == accounts.entUser.userPin:
                    break
                    print("You are",entUser+"!")
            elif tries == 3:
                print("You entered the pin wrong 3 times.")
    else:
        print("Didn't work")

