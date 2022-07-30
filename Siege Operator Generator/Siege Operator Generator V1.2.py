"""
The purpose of this program is to randomly generate operators in Tom Clancy's Rainbow Six Siege based on what operators are available and/or if you choose to retrict the
list of operators by removing them based on their main roles (mostly opinionated by myself).

Version 1.0 (Release 05/07/2022) - Note: Code is stable but any variation in user input outside of specified loops will cause operators when banning and/or restrictions
                                         when choosing to still be playable rather than unplayable.
Version 1.1 (05/07/2022) - Added 'Press Enter to Exit' input command due to not seeing final output in real environment.
Version 1.2 (14/07/2022) - Fixed issues stated in Version 1.0 comments and streamlined functions. Future improvements: operators with multiple roles instead of single
                                roles (how to remove keys based on one value when there could be 3+ values? eg. dict={ A : [1,2,3], ....}) 
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
            print(msg +("\n"))
            break
        else:
            print(y[n:n+5:1])
            n+=5

#Takes user input to ban operators. If in list and dictionary then removes from both so it can't be used again later. Loop created for invalid inputs.
    # x = input variable
    # y = corresponding dictionary
    # z = original list
    # msg1 = custom message for the input
    # msg2 = custom message for input error
    # a = count variable
    # msgl = repeat list message
def Ban_Input(y,z,msg1,msg2,a,msgl):
    x=str.lower(input(msg1))
    for i in z:
        if x=="na":
            break
        elif i==x.title():
            y.pop(i)
            z.remove(i)
            break
        elif i!=z[-1]:
            continue
        else:
            Sel_Msg(a,z,msgl)
            print(msg2)
            Ban_Input(y,z,msg1,msg2,a,msgl)


#Takes user input to remove operators based on their role (value). If in list and dictionary then removes from both so it can't be used again later. Loop created for invalid inputs.
    # x = input variable
    # ya = attacker dictionary
    # yd = defender dictionary
    # z = restrictions list
    # msg1 = custom message for the input
    # msg2 = custom message for input error
    # a = count variable
    # msgl = repeat list message
def Res_Input(ya,yd,z,msg1,msg2,a,msgl):
    x=str.lower(input(msg1))
    for i in z:
        if x=="na":
            break
        elif i==x.title():
            for k in list(ya.keys()):
                if ya[k] == i:
                    del ya[k]
            for k in list(yd.keys()):
                if yd[k] == i:
                    del yd[k]
            z.remove(i)
            break
        elif i!=z[-1]:
            continue
        else:
            Sel_Msg(a,z,msgl)
            print(msg2)
            Res_Input(ya,yd,z,msg1,msg2,a,msgl)

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
        print("\n")
        print("\n--------------------------------Finished!!!---------------------------------\n")
        print("\n")
        input("Press Enter to Exit")
        sys.exit()

#Attacker Dictionary (Will be adding a new key:value every 3-6 months to keep up to date)
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

#To have a list of operators to work against
AttL=list(AttD.keys())

#To end printing the list (length will get changed as new key:values are added)
AttC=len(AttL)

#Defender Dictionary (Will be adding a new key:value every 3-6 months to keep up to date)
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

#To have a list of operators to work against
DefL=list(DefD.keys())

#To end printing the list (length will get changed as new key:values are added)
DefC=len(DefL)

#Opening Title
print("\n-----------Welcome to the Rainbow Six Siege - Operator Randomiser-----------\n")

#ATTACKER BANS
#Bans up to 2 Attackers (Sel_Msg separate for aesthetic purposes in executed code)
Sel_Msg(AttC,AttL,"Ban an Attacker from the list. If there is a 'No Ban', type NA.")
Ban_Input(AttD,AttL,"Attacker Ban 1: ","Invalid Operator. Please try again.",AttC,"Ban an Attacker from the list. If there is a 'No Ban', type NA.")
Sel_Msg(AttC,AttL,"Ban an Attacker from the list. If there is a 'No Ban', type NA.")
Ban_Input(AttD,AttL,"Attacker Ban 2: ","Invalid Operator. Please try again.",AttC,"Ban an Attacker from the list. If there is a 'No Ban', type NA.")

print("\n----------------------------------------------------------------------------\n")

#DEFENDER BANS
#Bans up to 2 Defenders (Sel_Msg separate for aesthetic purposes in executed code)
Sel_Msg(DefC,DefL,"Ban a Defender from the list. If there is a 'No Ban', type NA.")
Ban_Input(DefD,DefL,"Defender Ban 1: ","Invalid Operator. Please try again.",DefC,"Ban Defender from the list. If there is a 'No Ban', type NA.")
Sel_Msg(DefC,DefL,"Ban a Defender from the list. If there is a 'No Ban', type NA.")
Ban_Input(DefD,DefL,"Defender Ban 2: ","Invalid Operator. Please try again.",DefC,"Ban Defender from the list. If there is a 'No Ban', type NA.")

print("\n----------------------------------------------------------------------------\n")

#STARTING SIDE
#Defines for final code if you are attacking or defending first
while True:
        x=str.lower(input("Which side are you starting on, Attack or Defence? "))
        S=x.title()
        if S=="Attack":
            break
        elif S=="Defence":
            break
        else:
            print("Invalid Starting Side. Please try again.")
            continue

print("\n----------------------------------------------------------------------------\n")

#RESTRICTIONS PRECURSOR
#User choice to reduce operator pool further through restrictions
while True:
        x=str.lower(input("Do you want to restrict the remaining operator pool by their classes (eg. remove shield operators), Yes or No? "))
        Res=x.title()
        if Res=="Yes":
            break
        elif Res=="No":
            break
        else:
            print("Invalid Input. Please try again.")
            continue

print("\n----------------------------------------------------------------------------\n")

#FINAL OUTPUT 1
#If user chooses to use all available operators, otherwise code will continue
if Res == "No":
    if S=="Attack":
        Side(AttD.keys(),DefD.keys())
    else:
        Side(DefD.keys(),AttD.keys())

#RESTRICTIONS
#Creates non duplicated value list for restrictions
AttV=list(AttD.values())
DefV=list(DefD.values())
ResV=AttV+DefV
ResL=list(dict.fromkeys(ResV))

#To end printing the list (length will get changed as new key:values are added)
ResC=len(ResL)

#Takes user input in turn and removes the operators that have the corresponding value
Sel_Msg(ResC,ResL,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")
Res_Input(AttD,DefD,ResL,"Restrictor 1 / 5: ","Invalid Role. Please try again.",ResC,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")

Sel_Msg(ResC,ResL,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")
Res_Input(AttD,DefD,ResL,"Restrictor 2 / 5: ","Invalid Role. Please try again.",ResC,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")

Sel_Msg(ResC,ResL,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")
Res_Input(AttD,DefD,ResL,"Restrictor 3 / 5: ","Invalid Role. Please try again.",ResC,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")

Sel_Msg(ResC,ResL,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")
Res_Input(AttD,DefD,ResL,"Restrictor 4 / 5: ","Invalid Role. Please try again.",ResC,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")

Sel_Msg(ResC,ResL,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")
Res_Input(AttD,DefD,ResL,"Restrictor 5 / 5: ","Invalid Role. Please try again.",ResC,"Pick a role that you would like to remove. If not all options are used/needed, type NA.")

print("\n----------------------------------------------------------------------------\n")

#FINAL OUTPUT 2
#If user chose to restrict operator pool
if S=="Attack":
    Side(AttD.keys(),DefD.keys())
else:
    Side(DefD.keys(),AttD.keys())

#END CODE