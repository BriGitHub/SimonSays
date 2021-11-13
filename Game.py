"""
This is the final version of the game, I hope you enjoy
The game now has a background color, a different window title, text on the main screen with the game’s title and
a key at the bottom, a game over and victory screen that plays music and tells the user how many rounds they got
to, new screen for input so the user does not need to type in the console, pop-up to start the game that includes
brief instructions, a retry button when they lose, and adds a pop-up that asks the user how many rounds they
would like to play.
"""

# Defines the canvas so the turtle can interact with it and draw the graphics.
import turtle
from turtle import *
import time
# import pygame
import sys
from random import randint


def game():
   screen = Screen()
   screen.bgcolor("#ADD8E6")
   # pygame.mixer.init()

   # Defines the squares that turtle will draw
   red_square = RawTurtle(screen, "square")
   orange_square = RawTurtle(screen, "square")
   yellow_square = RawTurtle(screen, "square")
   green_square = RawTurtle(screen, "square")
   blue_square = RawTurtle(screen, "square")
   pink_square = RawTurtle(screen, "square")
   purple_square = RawTurtle(screen, "square")
   gray_square = RawTurtle(screen, "square")
   black_square = RawTurtle(screen, "square")
   blink_square = RawTurtle(screen, "square")

   # Checks guesses by using the .pop method combined with the given array.
   def check_guesses(times, arr1, arr2):
       # Uses k as an arbitrary variable. Loops through 10 times, once for each round.
       # rnd represents the iterations within each round.
       for k in range(times):
           rnd = k+1
           # Blink the appropriate square, based on what the x and y coordinates were.
           for n in range(rnd):
               if arr1[n] == 7:
                   blink(-110, 110, rnd)
               elif arr1[n] == 4:
                   blink(-110, 0, rnd)
               elif arr1[n] == 1:
                   blink(-110, -110, rnd)
               elif arr1[n] == 8:
                   blink(0, 110, rnd)
               elif arr1[n] == 5:
                   blink(0, 0, rnd)
               elif arr1[n] == 2:
                   blink(0, -110, rnd)
               elif arr1[n] == 9:
                   blink(110, 110, rnd)
               elif arr1[n] == 6:
                   blink(110, 0, rnd)
               else:
                   blink(110, -110, rnd)

           # This for loop will check each of the user's guess to make sure it is right before they guess the next square
           for j in range(rnd):
               try:
                   user_guess = int(turtle.numinput("Enter Here!", "Enter the number at index " + str(j+1) + " .", default=None, minval=1, maxval=9))
                   arr2.append(user_guess)
               except:
                   # If the user doesn't type anything into the guess box and they press cancel this will make sure the
                   # program properly ends.
                   you_lose(j+1)
               if k == 0:
                   if arr2.pop() == arr1[j]:
                       print("Got the " + str(j+1) + " guess.")
                   else:
                       print("You missed the one at index " + str(j+1) + ". Game Over!")
                       you_lose(rnd)
                       return
               else:
                   if arr2.pop() == arr1[j]:
                       print("Got the " + str(j+1) + " guess.")
                       # Only run this if they have made it to the final index, and gotten it correct.
                       if j == (times-1):
                           print("You Won!")
                           you_win(rnd)
                           return
                   else:
                       print("You missed the one at index " + str(j+1) + ". Game Over!")
                       you_lose(rnd)
                       return

   # The function that tells turtle how to make each square.
   def color_square(color, x, y, square):
       square.penup()
       square.color(color)
       square.setposition(x, y)
       square.shapesize(5, 5)

   # Creates a blinking animation by replacing a given square with a white square and then re-creating the color square.
   def blink(x, y, rounds):
       color_square("#ADD8E6", x, y, blink_square)
       time.sleep(.35)
       # Based on the x coordinates, the different color squares are used. cross referencing those with the y tells us
       # which color we need to use. Ex: the square at -110,110 is red.
       for r in range(rounds):
           if x == -110:
               if y == 110:
                   color_square("red", x, y, red_square)
               if y == 0:
                   color_square("green", x, y, green_square)
               if y == -110:
                   color_square("purple", x, y, purple_square)
           if x == 0:
               if y == 110:
                   color_square("orange", x, y, orange_square)
               if y == 0:
                   color_square("blue", x, y, blue_square)
               if y == -110:
                   color_square("gray", x, y, gray_square)
           if x == 110:
               if y == 110:
                   color_square("yellow", x, y, yellow_square)
               if y == 0:
                   color_square("pink", x, y, pink_square)
               if y == -110:
                   color_square("black", x, y, black_square)

   # This function will call the functions to begin the game, only when the user is ready to start
   def start_game():
       sentinel = 0
       make_text()

       # This while loop will pop up brief instructions explaining the game and when the user wants to start the
       #  game they
       # Will press 1 in the text box.
       while sentinel != 1:
           sentinel = turtle.numinput("Enter Here!", """
   HOW TO PLAY:
   This game is a memory test, and will check your ability to memorize sequences.
   When prompted, enter the blinked square's number and press enter. The cycle
    will repeat, showing you the first square again, and then a new square. Then
    enter the square's numbers, one by one, separated by pressing the enter key.
                                     Good Luck!     Enter 1 to start the game.""", default=1, minval=0, maxval=2)
           if sentinel == 1:
               # Creates the needed arrays, and checks how many numbers the user wants to guess.
               simon_list = []
               user_arr = []
               try:
                   # Asks the user how many rounds they would like to play
                   times = int(turtle.numinput("Hi There!", "How many rounds would you like to memorize?", default=10, minval=5, maxval=50))
               except:
                   # If the user puts no number in and presses cancel it will safely end the program
                   times = 0
                   you_lose(1)
               # Populate the array the user is trying to guess.
               for m in range(times):
                   pos = randint(1, 9)
                   simon_list.append(pos)
               check_guesses(times, simon_list, user_arr)

   # Re-names the turtle window, to the title of the game
   screen.title("Simon Says")

   # Makes the squares by calling the color_square function
   color_square("red", -110, 110, red_square)
   color_square("orange", 0, 110, orange_square)
   color_square("yellow", 110, 110, yellow_square)
   color_square("green", -110, 0, green_square)
   color_square("blue", 0, 0, blue_square)
   color_square("pink", 110, 0, pink_square)
   color_square("purple", -110, -110, purple_square)
   color_square("gray", 0, -110, gray_square)
   color_square("black", 110, -110, black_square)

   # Makes the graphic on the screen that tells the user the information about the game
   def make_text():
       # Makes the title above the square
       turtle.penup()
       turtle.hideturtle()
       turtle.setposition(0, 200)
       turtle.write("Simon Says...", move=True, align="center", font=("Berlin Sans FB Demi", 59, "bold"))

       # Makes the key at the bottom of the screen
       turtle.setposition(-135, -275)
       turtle.write("""
             On your number pad:
       7=Red       8=Orange  9=Yellow
       4=Green   5=Blue       6=Pink
       1=Purple   2=Grey       3=Black
       """, move=True, align="left", font=("Berlin Sans FB", 14, "normal"))

   # Makes a game over screen that we will use if the user gets the guess wrong
   def you_lose(score):
       #pygame.mixer.music.load("Game_Over.mp3")
       #pygame.mixer.music.play(loops=1, start=0.0)
       turtle.clearscreen()
       screen.bgcolor("#777777")
       turtle.penup()
       turtle.hideturtle()
       turtle.pencolor("#c30101")
       turtle.write("GAME OVER", move=True, align="center", font=("Berlin Sans FB DemI", 70, "bold"))
       turtle.setposition(0, -100)
       turtle.write("You made it to round: " + str(score-1), move=True, align="center", font=("Berlin Sans FB", 30, "normal"))
       retry = turtle.numinput("Retry?", "Type 1 to play again", default=1, minval=0, maxval=1)
       if retry == 1:
           # pygame.mixer.music.stop()
           turtle.clearscreen()
           game()
       sys.exit()

   # Makes a victory screen to let the user know they beat the game and the game is finished
   def you_win(score):
       #pygame.mixer.music.load("Victory_Music.mp3")
       #pygame.mixer.music.play(loops=1, start=0.0)
       turtle.clearscreen()
       screen.bgcolor("green")
       turtle.penup()
       turtle.hideturtle()
       turtle.pencolor("yellow")
       turtle.write("VICTORY", move=True, align="center", font=("Berlin Sans FB DemI", 70, "bold"))
       turtle.setposition(0, -100)
       turtle.write("You completed round: " + str(score), move=True, align="center", font=("Berlin Sans FB", 30, "normal"))
       time.sleep(6)


# Runs the program
   start_game()
game()
