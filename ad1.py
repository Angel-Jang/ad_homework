import random
import sys

enteredLocation = ""
passcode = "Begin"
location = "Docked at: Home Base"
days = 0
shipHealth = 100
travelTime = 0
treasureCount = 0
missileCounter = 25
enemyCount = 0
captain = ""
shipName = ""
option = ""
counter = 0



def passwordCheck():
    passcodeAttempt = input("Passcode required to begin, Please enter Passcode: ")
    while passcodeAttempt != passcode:
        print("Passcode incorrect, Please try again.")
        passcodeAttempt = input("Please enter Passcode: ")



def userInformation():
    global captain, shipName
    while 1:
        captain = input("Please enter a Username: ")
        shipName = input("Please enter your Ship's Name: ")
        print("Warning!!! After game begins Username and Ship's Name CANNOT be changed. Type \"yes\" to confirm.")
        condition = input()
        if condition == "yes":
            break



def welcomeScreen():
    print("\"Welcome to Recon 12 Captain {0:s}. You will now be the handler of the {1:s}.\"".format(captain, shipName))
    print("\"Today is day {0:d} of being a member of Recon 12.\"".format(days))



def dockedGreeting():
    print("***********************")
    print("\"Greetings Captain {0:s}. The {1:s} is at your command.".format(captain, shipName))
    print("We are currently {0:s}".format(location))
    print("What would you like to do today?\"")


def sailingGreeting():
    print("***********************")
    print("\"Greetings Captain {0:s}. The {1:s} is at your command.".format(captain, shipName))
    print("We are {0:d}days away from {1:s}\"".format((travelTime-counter), enteredLocation))

    
def status():
    print("")
    print("~~~~~~~~~~~~~~~~~~")
    print("Current Day:", days)
    print("Ship Health:", shipHealth)
    print("Missiles:", missileCounter)



def option0phrase():
    choice = ""
    while choice != "yes" :
        print("")
        print("\"Do you really want to leave so soon?\"\nType \"yes\" to confirm exit(Data will NOT be Saved)")
        choice = str(input())
        if choice == "yes":
            return choice
        elif choice != "yes":
            return choice



def endphrase():
    print("")
    print("__________________________")
    print("Game Over")
    print("Enemies Defeated =", enemyCount)
    print("Days Survived =", days)
    print("Treasure Found =", treasureCount)



def dockedOptions():
    global location, travelTime, option, shipHealth, missileCounter, enteredLocation, days
    while 1:
        if shipHealth < 100:
            print("")
            print("1. Leave port")
            print("2. Restock Supplies")
            print("3. Enjoy Island")
            print("4. View Ship Status")
            print("5. Repair Ship")
            print("0. Leave Game")
            option = str(input())
            if option == "1":
                option = ""
                print("")
                enteredLocation = input("Engines ready, Please Enter Desired Location: ")
                print("Traveling to:", enteredLocation)
                print("")
                if enteredLocation in location:
                    print("\"We are currently at {0:s}. Please enter another location or select a different option\"".format(enteredLocation))
                else:
                    print("Traveling to:", enteredLocation)
                    location = "Sailing to " + enteredLocation
                    travelTime = random.randint(1, 5)
                    print("Approximate time: {0:d}days until arrival.".format(travelTime))
                    break
            elif option == "2":
                option = ""
                print("")
                print("Supplies Restocked to 100%.")
                missileCounter = 25
            elif option == "3":
                option = ""
                print("")
                print("\"You sit under a coconut tree and enjoy the cool island breese. :)\"")
                days += 1
            elif option == "4":
                status()
            elif option == "5":
                option = ""
                print("")
                print("Ship Repaired")
                shipHealth = 100
                break
            elif option == "0":
                if option0phrase() == "yes":
                    endphrase()
                    sys.exit()
                else:
                    print("")
                    print("\"Phew, thaught you were leaving me for a sec there\"")
        else:
            print("")
            print("1. Leave port")
            print("2. Restock Supplies")
            print("3. Enjoy Island")
            print("4. View Ship Status")
            print("0. Leave Game")
            option = str(input())
            if option == "1":
                option = ""
                print("")
                enteredLocation = input("Engines ready, Please Enter Desired Location: ")
                print("Traveling to:", enteredLocation)
                print("")
                if enteredLocation in location:
                    print("\"We are currently at {0:s}. Please enter another location or select a different option\"".format(enteredLocation))
                else:
                    print("Traveling to:", enteredLocation)
                    location = "Sailing to " + enteredLocation
                    travelTime = random.randint(1, 5)
                    print("Approximate time: {0:d}days until arrival.".format(travelTime))
                    break
            elif option == "2":
                option = ""
                print("")
                print("Supplies Restocked to 100%")
                missileCounter = 25
            elif option == "3":
                option = ""
                print("")
                print("\"You sit under a coconut tree and enjoy the cool island breese. :)\"")
                days += 1
            elif option == "4":
                status()
            elif option == "0":
                if option0phrase() == "yes":
                    endphrase()
                    sys.exit()
                else:
                    print("")
                    print("\"Phew, thaught you were leaving me for a sec there\"")
        option = ""

                


def sailingOptions():
    global location, option, shipHealth, missileCounter, enemyCount, treasureCount, counter
    while travelTime > counter:
        sailingGreeting()
        print("")
        print("1. Rest")
        print("2. Battle Enemy Ship")
        print("3. Fish for Treasure")
        print("4. View Ship Status")
        print("0. Leave Game")
        option = str(input())
        if option == "1":
            option = ""
            print("")
            print("\"You get up to grab a canned lemonade, kick back in your captains seat and watch the slow waves flow by.\"")
            counter += 1
        elif option == "2":
            option = ""
            print("")
            print("\"You spot an enemy Ship across the water and decide to attack.\"")
            enemyHealth = 30
            damage = 0
            attackNumber = 0    
            while 1:
                print("")
                attackNumber += 1
                damage = random.randint(1, 25)
                missileCounter -= 1
                enemyHealth -= damage
                damage = random.randint(1, 25)
                shipHealth -= damage
                print("Attack No:", attackNumber)
                print("Ship Health:", shipHealth)
                if shipHealth <= 0:
                    endphrase()
                    sys.exit()
                elif missileCounter <= 0:
                    endphrase()
                    sys.exit()
                elif enemyHealth <= 0:
                    print("\"You've succesfully defeated an enemy\"")
                    enemyCount += 1
                    break
            counter += 1
        elif option == "3":
            print("")
            chance = random.randint(1,3)
            print("\"You throw your line into the water with hopes to hook onto treasure\"")
            if chance == 1:
                treasureCount += 1 
                print("\"Wow, You actually managed to find something good\"")
            elif chance == 2:
                print("\"You feel something on the end of your line and excitedly reel in\"")
                print("\"Just to find a boot\"" + "\U0001F603")
            elif chance == 3:
                print("\"You somehow managed reel in a missile\"")
                missileCounter += 1
            counter += 1
        elif option == "4":
                status()
        elif option == "0":
                    if option0phrase() == "yes":
                        endphrase()
                        sys.exit()
                    else:
                        print("")
                        print("\"Phew, thaught you were leaving me for a sec there\"")
        option = ""
    location = "Docked at: " + enteredLocation
    counter = 0


def main():
    global days
    passwordCheck()
    userInformation()
    welcomeScreen()
    while 1:
        if "Dock" in location:
            dockedGreeting()
            dockedOptions()
        else:
            sailingOptions()
            days += 1

            
            
main()
