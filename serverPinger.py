import os #os is used for the ping
import platform

f2p_list = [1, 8, 16, 26, 35, 81, 82, 83, 84, 85, 93, 94] #list of all the F2P servers

def servers():
    print(parameters)
    for i in range(1, 94): #there are currently 94 OSRS servers
        hostname = "oldschool"+ str(i) + ".runescape.com" #pinging server 1 through 94
        print("\n*** Pinging server: ", str(i), " hostname: ", hostname, "***") #displaying which server that is currently being pinged
        response = os.system("ping " + hostname) #get the ping

def p2p():
    print('Only members (P2P) servers will be pinged.')
    for i in range (0, 94): #server 1 is F2P and can be skipped in the range
        if i in f2p_list: #if a server is part of the F2P list then skip it with continue
            continue

        hostname = "oldschool"+ str(i) + ".runescape.com"
        print("\n*** Pinging server: ", str(i), " hostname: ", hostname, "***")
        response = os.system("ping " + hostname)


def f2p():
    print('Only Free to Play (F2P) servers will be pinged.')
    for i in range(0, len(f2p_list)):
        hostname = "oldschool"+ str(f2p_list[i]) + ".runescape.com"
        print("\n*** Pinging server: ", str(f2p_list[i]), " hostname: ", hostname, "***")
        response = os.system("ping " + hostname)

def specificServer(serverType):
    hostname = "oldschool"+ str(serverType) + ".runescape.com"
    print("\n*** Pinging server: ", str(serverType), " hostname: ", hostname, "***")
    response = os.system("ping " + hostname)

def start(): #take input from user to what filter for the pinging should be used
    serverType = input("Do you want to ping ALL servers, Memebers only or Free to Play only? \nYou can also ping a specific world by typing in the number (eg. 2 for world 2)\n").lower()
    if 'all' in serverType:
        servers()
    elif 'mem' in serverType or 'p2p' in serverType or 'pay' in serverType:
        p2p()
    elif 'f' in serverType:
        print("Free to play (F2P) servers will now be pinged.")
        f2p()
    else:
        try: #if non of the above and the input is an integer then continue to the specific server check
            intInput = int(serverType)
            if intInput >= 1 and intInput <= 94:
                specificServer(serverType)
            else:
                print("Sorry, that number does not seem to be associated with any server. Try a number between 1 and 94. \n")
                start()
        except ValueError:
            print("Sorry, I did not get that. Please try again. \n")
            start()


print ("Oldschool Runescape Server Pinger v0.1")
print ("By Walid Sodki \n")
start()
print ("\n*** Ping process is now done. ***")
