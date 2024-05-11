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
choice01 = (input("You are at a crossroads. Do you want to go left or right?\n"))
choice01 = choice01.lower()

if choice01 == "left":
          print("You come to a lake. There is an island in the middle of the lake.")
          choice02 = input("Do you want to swim or wait?\n")
          choice02 = choice02.lower()

          if choice02 == "wait":
                    print("You come to a house with three doors. One red, one yellow and one blue.")
                    choice03 = input("Which door do you choose--red, yellow or blue?\n")
                    choice03 = choice03.lower()

                    if choice03 == "yellow":
                              print("You win!")
                    elif choice03 == "red":          
                              print("You get sent back to Start--it is your Groundhog Day! Game over.") 
                    elif choice03 == "blue":          
                              print("You step into a Parallel Universe. Game over.") 
                    else:
                              print("Game over.") 
          
          elif choice02 == "swim":          
                    print("You are attacked by a trout. Game over.") 
          else:
                    print("You are attacked by a trout. Game over.") 
       
elif choice01 == "right":          
          print("You fall into a hole. Game over.") 
else:
          print("You fall into a hole. Game over.") 

