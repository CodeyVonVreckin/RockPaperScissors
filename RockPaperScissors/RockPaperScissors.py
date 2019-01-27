#////////////
#Startup File
#////////////

import sys 
from GameFunctions import *

areYouReady = input("Are your ready to lose BITCH !?!?? Y/N ")

while areYouReady !="Y" and areYouReady !="y" and areYouReady !="yes":
    areYouReady = input("AHHH Come On!! Don't be a little punk ass. Y/N ")
    # can have it loop about 3 times with differnt reposnes. make it impossible to say Y

print("Ok homie listen up, cause I'm only going to say this once. We be playin street rules ya dig? First to 10 wins")

start = input("Type 'start' to start that ass whoopin. ")

if start == "start":
    #displayScore()
    keepPlaying ="Y"
    while keepPlaying == "Y":
        keepPlaying = startGame()
else:
    print("I understand you can't handle all this hawt action!")
