'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def start():          # initiates the game and presents the player with options to choose a room to enter.
    global e,rkey,brownkey,pendant
    print("\n\t\t\t\tU look ahead and find 3 rooms. Which one would you like to enter?")
    print("\t\t\t\t\t1. Room 1\n\t\t\t\t\t2. Dining room\n\t\t\t\t\t3. Room 3")
    ch=int(input("enter choice:(1/2/3) "))
    if ch==1:
        room1()
    elif ch==2:
        dining()
    elif ch==3:
        room2()
    else:
        print("Invalid choice")
        start()

# Function to display and update energy level

def energy():
    global e,rkey,brownkey,pendant
    print("\nYour current energy level: ",e)
    inventory()
    print("\n")
    if e>0:
        pass
    else:
        print("\t\tOh no youR energy levels are at 0. Your energy levels must always be above 0.")
        print("\t\tU get too exhausted and fall to the ground.")
        print("\n\t\t\t\tGAME OVER")
        exit(0)
        
# Function to display items in inventory
def inventory():
    print("\nItems in inventory: ",l1)
   
# Maindoor escape --> 1st successful ending 
def maindoor(brownkey):
    global e,rkey,pendant
    energy()
    if brownkey=="yes":               #Checks if the player has the brown key to unlock the main door and win the game.
        print("\t\tCongrats! You won the game!")
        exit(0)
        
def room2():
    global e,rkey,brownkey,pendant
    energy()
    print("\t\tU enter Room 2 and walk inside.\n")
    print("\t\t\t\tCREAK!")
    print("\t\tOh no u stepped on a loose floorboard!")
    ghost_chase()
    print("\n\t\tYou have 2 places to hide.\n\t\t\t1. behind poster\n\t\t\t2. behind door")
    room2hide=int(input("\nWhere would u like to hide?(1/2): "))
    if room2hide==1:
        print("\n\t\tU hide behind the poster and hold your breath.You watch as the ghost silently slides into the room peeks around and leaves.")
        print("\t\tJust when u thought you'll be fine the ghost sees you! ")
        print("\t\tOh no! the ghost caught you!")
        print("\n\t\t\t\tGAME OVER")
        exit(0)
    elif room2hide==2:
        print("\n\t\tU hide behind the doorand hold your breath.You watch as the ghost silently slides into the room peeks around and leaves.")
        print("\t\tThankfully the ghost doesnt see you.")
        print("\t\tU come out of your hiding spot and notice something like a trapdoor leading to another room.")
        trapdoorinp=input("\nclimb trapdoor?(y/n): ")
        if trapdoorinp=="y":
            trapdoor()
        else:
            start()
    energy()      

def trapdoor():
    global e,rkey,brownkey,pendant
    energy()
    print("\n\t\tYou are now in a starnge room with various objects. Some of them include:")
    
    
    l=[1,2,3,4,5]
    while(len(l)>0):
        print("\t\t1. An antique vase")
        print("\t\t2. A wooden case")
        print("\t\t3. An expensive jewellery box")
        print("\t\t4. An old cabinet")
        print("\t\t5. Leave room")
        trapobj=int(input("\nWhich one would you like to examine?: "))
        if trapobj==1 and trapobj in l:
            print("\n\t\tU look into the antique vase. U dont find anything in it.")
            l.remove(1)
        elif trapobj==2 and trapobj in l:
            print("\n\t\tU go over to examine the large wooden case. U open it and discover a mysterious pendant.")
            print("\t\tSomething tells u that it might be useful later.\n")
            pendantobj=input("take pendant?(y/n) ")
            if pendantobj=="y":
                pendant="yes"
                print("\nU take the pendant and put it in your pocket.\n")
                l1.append("pendant")
                l.remove(2)
        elif trapobj==3 and trapobj in l:
            print("\n\t\tU open the shiny jewellery box and discover a red key inside it.\n")
            redkey=input("take red key?(y/n) ")
            if redkey=="y":
                rkey="found"
                print("\n\t\tU take it with you just in case.\n")
                l1.append("redkey")
                l.remove(3)
            elif redkey=="n":
                print("\t\tU leave the red key in the box itself.\n")
        elif trapobj==4  and trapobj in l:
            print("\n\t\tU go over to the old cabinet and open it.")
            print("\t\tOuch! To your surprise the ghost was hiding in there all along and before u know it, it attacks you.")
            print("\n\t\t\t\tGAME OVER")
            break;
            exit(0)
        elif trapobj==5 and trapobj in l:
            start()
            break;
        else:
            print("\n\t\tU already examined that.Invalid choice.\n")
            
        energy()  
    
def room1():
    global e,rkey,brownkey,pendant
    energy()
    print("\t\tU enter Room 1 and walk inside. U find 2 rusty drawers.\n")
    d1=input("\t\tOpen drawer 1?(y/n): ")
    if d1=="y":
        print("\t\tU found the brown key! Great! Now you can use it on the main door and get out safely!")
        brownkey="yes"
        l1.append("brownkey")
        maindoor(brownkey)
    else:
       d2=input("\t\tOpen drawer 2?(y/n): ")
       if d2=="y":
           print("\n\t\tEEK!! A giant spider jumps at you and you let out a shriek!")
           ghost_chase()
           #e=e-1
           print("\t\tHurry now!")
           start()
       else:
           start()
           
def dining():
    global e,rkey,brownkey,pendant
    energy()
    print("\t\tU enter the dining room and see a dazzling candle right in the middle of the dining table.")
    candle=input("\nExamine candle?(y/n) ")
    if candle=="y":
        print("\n\t\tOut of curiosity u go examine the candle. ")
        print("\t\tSuddenly the candle's flame turns purple and it explodes! BOOM!  ")
        ghost_chase()
        print("\n\t\tYou have 2 places to hide!")
        print("\n\t\t1.under the table\n\t\t2.behind the shelf")
        hide=int(input("\nWhere do u want to hide?(1/2): "))
        if hide==1:
            print("\n\t\tU hide under the table and watch as the ghost slides past you. After a moment or two it leaves the room")
            print("\t\tYou heave a sigh of relief. Its ok ",name, " you're fine.")
            print("\n\t\tYou have found a special spot to restore your energy levels!")
            e=4
            print("\t\tYour energy has been restored!")
            cupboard()
            
        elif hide==2:
            print("\n\t\tYou hide behind the shelf. Oh no! The ghost found you!")
            print("\n\t\t\t\tGAME OVER")
            exit(0)
    elif candle=="n":
        print("\n\t\tYou decide to not let curiosity get the better of you and go examine the cupboard.\n")
        cupboard()
    
            
def cupboard():
    global e,rkey,brownkey,pendant
    energy()
    cup=input("examine cupboard?(y/n) ")
    if cup=="y":
        print("\n\t\tYou walk towards the strange cupboard and discover that it needs a speacial key")
        if rkey=="found":
            print("\n\t\tYou have the key! U insert the key into the hole and voila! The cupboard opens up to a secret passage!")
            secret_passage()
        elif rkey=="notfound":
            print("\n\t\tYou dont have the key yet. Continue exploring.\n")
            start()
    else:
        start()
        
def ghost_chase():
    global e,rkey,brownkey,pendant
    print("\n\t\t\t\tOh no! The ghost heard you and is now chasing you!")
    print("\t\t\t\t\t\tGHOST CHASE!")
    e=e-1
    energy()
    
def secret_passage():
    global e,rkey,brownkey,pendant
    energy()
    print("You walk down the cold dark passage.U glance up and you're horrified to see a dozen bats hanging over you. U move cautiously and encounter 3 different paths.")
    print("\n\t\t1. Path 1")
    print("\t\t2. Path 2")
    print("\t\t3. Path 3")
    passage_path=int(input("\nWhich path would you like to take? "))
    if passage_path==1:
        print("\n\t\tU cross your fingers and walk down the first path. U see something at the end of the tunnel...")
        print("\t\tOh no! Its the ghost!")
        #pendant=input("\t\tdo u have the pendant?(y/n) ")
        if pendant=="yes":
            print("\nYou suddenly remember the pendant you pocketed earlier!")
            #print("\t\tYou pull out the pendant u retreived from the attic room.")
            #print("U grip it firmly and with an air of confidence and might u swiftly swing it at the ghost.")
            print("\t\tU pull it out and quickly open the locket. A beam of light as bright as an explosion flashes from it chasing away the ghost for good!")
            print("\t\tHow ironical!")
            print("\t\tHurray you got rid of the ghost!")
            print("\n\t\tU keep walking and soon u see light at the end of the tunnel...the light of daybreak!!")
            print("\n\t\t\t\tHurray u won the game!")
          
        elif pendant=="no":
            print("\n\t\tOh no u dont have the pendant yet to defeat the ghost! U try to run away but the ghost catches up to you. ")
            print("\n\t\t\t\tGAME OVER")
            
    elif passage_path==2:
        print("\n\t\tU cross your fingers and walk down the second path.")
        print("\n\t\tU keep walking and soon u see light at the end of the tunnel...the light of daybreak!!")
        print("\n\t\t\t\tHurray u won the game!")
      
    elif passage_path==3:
        print("\n\t\tU cross your fingers and walk down the third path")
        print("\t\tU keep walking and see something at the end of the tunnel...Oh no its a dead end!")
        print("\t\tU are too exhausted now and unable to continue.")
        print("\n\t\t\t\tGAME OVER")
      
    exit(0)
 
e=4
rkey="notfound"
brownkey="no"
pendant="no"
l1=[]
print("\t\t\t\t\t\t\t\tHello! Welcome to the Mansion escape\n")
name=input("\t\tENtEr YoUr NaMe..")
print("\n\tThe weather seems to be worsening just like the fear in your heart as you aimlessly wander in the woods hoping for a way out")
print("\n\tA sudden bolt of lightning hits one of the trees a few metres away and it sends shivers down your spine.")
print("\n\tCalm down ",name,"... ,you say to yourself.")
print("\n\tThe dark clouds seem to be swallowing the only few rays of the sun illuminating the sky.")
print("\n\tJust as you start losing hope that you'll ever get out you catch a glimpse of an old mansion ahead of you...")
print('\n\tWithout a second thought you run towards it with a pang of relief. Little did you know that the following turn of events might change your life forever...')
print("\n\tYou rush inside but before you can even catch your breath the door behind you slams SHUT! ")
print("\n\tAn eerie presence fills the massive hallway and you hear strange sounds of laughter coming from upstairs.\n")
print("\tOverwhelmed with fear you try to open the door only to find it locked...But how?\n")
print("\n\tOnly then it hits you that you're now trapped and have to find a way out before that ominous thing kills you.")
print("\n\n\t\t\t\t\t\t\t\tWELCOME TO MANSION ESCAPE.\n\n")
print("\n\tYour goal is to leave the mansion safely while evading a ghost thats hunting you down.")
print("\n\tNote that everytime the ghost chases you you start losing energy. If your energy level reaches 0 you'll collapse and the ghost will kill you")
print("\n\t\t\t\t\tPsst.....Hiding in a certain spot will restore your energy......")
print("\n\n\t\t\t\t\t\tGood luck.......",name,".....")
start()



