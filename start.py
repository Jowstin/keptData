import os
tries=0
newUser=input("Are you a new user?(yes or no): ").lower()
if newUser == "yes":
    username=input("Please enter a username.: ")
    pin=input("Please enter a pin.: ")
    pData = int(pin)
    os.chdir("accounts")
    fileName='{}.py'.format(username)
    with open(fileName, 'a') as f:
        f.write('"userPin =" \n{}'.format(pData))
    f.close()
elif newUser == "no":
    os.chdir("accounts")
    entUser=input("What is your username?: ")
    if os.path.exists('{}.py'.format(entUser)) == True:
        while True:
            if tries < 3:
                entPin=int(input("What is your pin?: "))
                tries+=1
                global accounts
                namUser=entUser+".py"
                with open(namUser, 'r') as f:
                    acPin="placeholder"# Just a placeholder for acPin
                    f.readline()
                    acPin=int(f.readline())
                if entPin == acPin:
                    print("You are",entUser+"!")
                    break
            elif tries == 3:
                print("You entered the pin wrong 3 times.")
                break
    else:
        print("Didn't work")

