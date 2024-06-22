print(
    '''
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
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice1 = input(
    "You arrive on the island and find two paths. Which way do you go: left or right?\n"
).lower()
if choice1 == "left":
    print("You chose wisely!")
    choice2 = input(
        "You reach the river dock, but see that there's a sign that says 'Will be back after 20 minutes'. Do you wait for the boat to return or swim across the river? Type 'wait' or 'swim'\n"
    ).lower()
    if choice2 == "wait":
        print("Your patience paid off! You can now cross the river with the boat")
        choice3 = input(
            "The treasure is close, but you find yourself staring at 3 doors with different colors: red, blue and yellow. Which door do you open?\n"
        ).lower()
        if choice3 == "red":
            print("A fire-breathing dragon awaited you behind the door. Game Over!")
        elif choice3 == "blue":
            print("You took an arrow to the knee. Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure! Congratulations!!")
        else:
            print("That door doesn't exist. Game Over!")
    else:
        print("You were attacked by a shark. Game Over!")
else:
    print("You fell into a spike trap. Game Over!")

print("Thanks for playing!")
