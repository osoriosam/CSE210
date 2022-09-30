#
#   Program:    Dice.py
#   Author:     Samuel Osorio
#   Purpose:    Dice game
#

import random

class Dice:
    #The responsability of a Dice is to display the result of roll dice
    def __init__(self) -> None:
        #A constructor, that inicializes one attribute.
        self.play_number = random.randint(1,6)

class Score:
    #The responsability of Score is to value whit points every number of Dice

    def __init__(self):
        #A constructor, that inicializes one attribute.
        self.roll_points = 0
    
    def what_points(self, number):
        #A method that return the points of roll number
        if number == 1:
            self.roll_points = 100
        elif number == 5:
            self.roll_points = 50

def main():
    #Main
    roll_y_n = ""
    sum_score_dice = 0
    while roll_y_n != "n":
        while roll_y_n != "n" and roll_y_n !="y":
            roll_y_n = input("Roll dice? [y/n] ")
        if roll_y_n == "y":
            result_dice = [0, 0, 0, 0, 0]
            this_score = 0
            for i in range(0,5):
                roll_dice = Dice()
                result_dice[i] = roll_dice.play_number
                score_play = Score()
                score_play.what_points(number = result_dice[i])
                this_score += score_play.roll_points
            sum_score_dice += this_score
            print(f"You rolled: {result_dice[0]} {result_dice[1]} {result_dice[2]} {result_dice[3]} {result_dice[4]} ")
            print(f"Your game score is: {this_score}")
            print(f"Your accumulated score is: {sum_score_dice} \n")
            if this_score == 0:
                roll_y_n = "n"
            else:
                roll_y_n = ""
    print("Game over, thanks for playing\n")

if __name__ == "__main__":
    main()
