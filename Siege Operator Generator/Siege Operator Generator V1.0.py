"""
The purpose of this program is to randomly generate operators in Tom Clancy's Rainbow Six Siege based on what operators are available and/or if you choose to retrict the
list of operators by removing them based on their main roles (mostly opinionated by myself).

Version 1.0 (Release 05/07/2022) - Note: Code is stable but any variation in user input outside of specified loops will cause operators when banning and/or restrictions
                                         when choosing to still be playable rather than unplayable.
"""
#To end the code once the desired result has been achieved
import sys

#To help with the randomising process
import random

#Defines a pop up message with a readable list for user to choose what to input
    # x = count variable
    # y = list
    # msg = custom message for the list
def Sel_Msg(x,y,msg):
    n=0
    while True:
        if n>=x:
            print("CASE SENSITIVE: " + msg +("\n"))
            break
        else:
            print(y[n:n+5:1])
            n+=5

#Takes the input of banned operators and removes from corresponding dictionary
    # x = List of keys from dictionary
    # y = User inputted value
    # z = Corresponding dictionary
def ban(x,y,z):
    for i in x:
        if i==y:
            z.pop(y)

#Defines the final output of randomised operators given depending on starting side
    # x = Starting side (Attack or Defence) dictionary input
    # y = Opposite side (Defence or Attack) dictionary input
def Side(x,y):
        print("Round 1: "+ random.choice(list(x)))
        print("Round 2: "+ random.choice(list(x)))
        print("Round 3: "+ random.choice(list(x)))
        print("Round 4: "+ random.choice(list(y)))
        print("Round 5: "+ random.choice(list(y)))
        print("Round 6: "+ random.choice(list(y)))
        print("Round 7: "+ random.choice(list(x)) + " or " + random.choice(list(y)))
        print("Round 8: "+ random.choice(list(y)) + " or " + random.choice(list(x)))
        print("Round 9: "+ random.choice(list(x)) + " or " + random.choice(list(y)))
        print("\n----------------------------------------------------------------------------\n")
        print("\n--------------------------------Finished!!!---------------------------------\n")
        print("\n----------------------------------------------------------------------------\n")
        sys.exit()

#Attacker Dictionary
    # Key = Operators
    # Value = Main Role
AttD={"Sledge":"Soft Breach",
    "Thatcher":"Disable",
    "Ash":"Soft Breach",
    "Thermite":"Hard Breach",
    "Twitch":"Disable",
    "Montagne":"Shield",
    "Glaz":"Rush/Roam",
    "Fuze":"Disable",
    "Blitz":"Shield",
    "IQ":"Disable",
    "Buck":"Soft Breach",
    "Blackbeard":"Rush/Roam",
    "Capitao":"Area Denial",
    "Hibana":"Hard Breach",
    "Jackal":"Anti Roam",
    "Ying":"Rush/Roam",
    "Zofia":"Soft Breach",
    "Dokkaebi":"Anti Roam",
    "Lion":"Anti Roam",
    "Finka":"Buff",
    "Maverick":"Hard Breach",
    "Nomad":"Anti Roam",
    "Gridlock":"Anti Roam",
    "Nokk":"Rush/Roam",
    "Amaru":"Rush/Roam",
    "Kali":"Disable",
    "Iana":"Intel Gatherer",
    "Ace":"Hard Breach",
    "Zero":"Intel Gatherer",
    "Flores":"Disable",
    "Osa":"Area Denial",
    "Sens":"Area Denial"}

#Defender Dictionary
    # Key = Operators
    # Value = Main Role
DefD={"Smoke":"Area Denial",
    "Mute":"Intel Denial",
    "Castle":"Secure",
    "Pulse":"Intel Gatherer",
    "Doc":"Buff",
    "Rook":"Buff",
    "Kapkan":"Trap",
    "Tachanka":"Area Denial",
    "Jager":"Secure",
    "Bandit":"Anti Hard Breach",
    "Frost":"Trap",
    "Valkyrie":"Intel Gatherer",
    "Caveira":"Rush/Roam",
    "Echo":"Intel Gatherer",
    "Mira":"Intel Gatherer",
    "Lesion":"Trap",
    "Ela":"Trap",
    "Vigil":"Rush/Roam",
    "Maestro":"Intel Gatherer",
    "Alibi":"Trap",
    "Clash":"Shield",
    "Kaid":"Anti Hard Breach",
    "Mozzie":"Intel Denial",
    "Warden":"Rush/Roam",
    "Goyo":"Area Denial",
    "Wamai":"Secure",
    "Oryx":"Rush/Roam",
    "Melusi":"Secure",
    "Aruni":"Secure",
    "Thunderbird":"Buff",
    "Thorn":"Trap",
    "Azami":"Area Denial"}

#Opening Title
print("\n----------------------------------------------------------------------------\n")
print("\n-----------Welcome to the Rainbow Six Siege - Operator Randomiser-----------\n")
print("\n----------------------------------------------------------------------------\n")

#ATTACKER BANS
#To have a list of operators to work against
AttL=list(AttD.keys())
#To end printing the list
AttC=len(AttL)
Sel_Msg(AttC,AttL,"Ban 2 Attackers from the list. If there is a 'No Ban', then leave blank.")
#Bans up to 2 Attackers (Currently no failsafe against incorrect/incomplete/case sensitive answers)
AttB1=input("Attacker Ban 1: ")
ban(AttL,AttB1,AttD)
AttB2=input("Attacker Ban 2: ")
ban(AttL,AttB2,AttD)

print("\n----------------------------------------------------------------------------\n")

#DEFENDER BANS
#To have a list of operators to work against
DefL=list(DefD.keys())
#To end printing the list
DefC=len(DefL)
Sel_Msg(DefC,DefL,"Ban 2 Defenders from the list. If there is a 'No Ban', then leave blank.")
#Bans up to 2 Defenders (Currently no failsafe against incorrect/incomplete/case sensitive answers)
DefB1=input("Defender Ban 1: ")
ban(DefL,DefB1,DefD)
DefB2=input("Defender Ban 2: ")
ban(DefL,DefB2,DefD)

print("\n----------------------------------------------------------------------------\n")

#Starting side of your game
while True:
        S=input("CASE SENSITIVE: Which side are you starting on, Attack or Defence? ")
        if S=="Attack":
            print("\n----------------------------------------------------------------------------\n")
            break
        elif S=="Defence":
            print("\n----------------------------------------------------------------------------\n")
            break
        else:
            print("\n----------------------------------------------------------------------------\n")
            continue

#User choice to reduce operator pool further through restrictions
while True:
        Res=input("CASE SENSITIVE: Do you want to restrict the remaining operator pool by their classes, Yes or No? ")
        if Res=="Yes":
            print("\n----------------------------------------------------------------------------\n")
            break
        elif Res=="No":
            print("\n----------------------------------------------------------------------------\n")
            break
        else:
            print("\n----------------------------------------------------------------------------\n")
            continue

#Final Output 1 if no restrictions are chosen (if Res=="Yes", code continues further)
if Res == "No":
    if S=="Attack":
        Side(AttD.keys(),DefD.keys())
    else:
        Side(DefD.keys(),AttD.keys())

#RESTRICTIONS
#Defining restrictions with the main roles from both dictionaries
ResL=["Soft Breach", "Hard Breach", "Shield",
"Trap", "Anti Roam", "Anti Hard Breach",
"Disable", "Buff", "Area Denial",
"Rush/Roam", "Intel Gatherer", "Intel Denial",
"Secure"]
#To end printing the list
ResC=len(ResL)
if Res=="Yes":
    Sel_Msg(ResC,ResL,"Pick up to 5 classes that you would like to remove. If not all options are used/needed, then leave blank.")
#Takes user input in turn and removes the operators that have the corresponding value (Currently no failsafe against incorrect/incomplete/case sensitive answers)
Res1=input("Restrictor 1: ")
AttD1={k:v for k,v in AttD.items() if v!=Res1}
DefD1={k:v for k,v in DefD.items() if v!=Res1}
Res2=input("Restrictor 2: ")
AttD2={k:v for k,v in AttD1.items() if v!=Res2}
DefD2={k:v for k,v in DefD1.items() if v!=Res2}
Res3=input("Restrictor 3: ")
AttD3={k:v for k,v in AttD2.items() if v!=Res3}
DefD3={k:v for k,v in DefD2.items() if v!=Res3}
Res4=input("Restrictor 4: ")
AttD4={k:v for k,v in AttD3.items() if v!=Res4}
DefD4={k:v for k,v in DefD3.items() if v!=Res4}
Res5=input("Restrictor 5: ")
AttD5={k:v for k,v in AttD4.items() if v!=Res5}
DefD5={k:v for k,v in DefD4.items() if v!=Res5}

print("\n----------------------------------------------------------------------------\n")

#Final Output 2 if restrictions are chosen
if S=="Attack":
    Side(AttD5.keys(),DefD5.keys())
else:
    Side(DefD5.keys(),AttD5.keys())
