print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

#Variables
action1 = None
action2 = None
action3 = None
action4 = None

#Users first choice
action1 = input("\nYou awake to find you're laying on the ground, do you stay laying down or stand up? L or S: ").upper()

if action1 == "L": # You die
  print("\nYou lay on the ground, not bothering to move, suddenly a horse comes racing past and tramples you to death.\n\nTHE END")
else: # You go on
  action2 = input("\nYou jump to your feet, just in time to step back and avoid a horse, racing down the lane.\
                  \nThere's something in the field opposite, do you want to investigate? Y or N: ").upper()
  if action2 =="N": # you die
    print("\nYou're too lazy to move, that damn horse comes flying back down the lane and tramples you to death.\n\nTHE END")
  else: # You go on
    action3 = input("\nYou cross the lane and walk into the field, it's a small mound of freshly dug soil.\
                      \nDo you want to start digging? Y or N: ").upper()
    if action3 =="N": # you die
      print("\nYou're too lazy to dig, you lay there on the grass and fall asleep.\n\nTHE END")
    else: # You go on
      action4 = input("\nYou dig down with your hands and find a small locked chest with 3 coloured keys.\
                      \nWhich key do you choose, Red, Yellow or Green? R,Y or G: ").upper()
      if action4 == "R" or action4 == "Y": # You die
        print("\nOh no, wrong key, it a trap!  The case explodes, blowing you to pieces!\n\nTHE END")
      else: # You WIN
        print("\nHooray!!! The chest opens and it's full of gold. Well done!")
