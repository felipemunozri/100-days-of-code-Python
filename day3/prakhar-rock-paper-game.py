# Rock Paper Scissor Tournament
 
import random
import os
 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
 
 
player = [rock, paper, scissors]
 
player_name_string = ["rock 🪨", "paper 📝", "scissors ✂️"]
 
 
 
print("Welcome to the Rock Paper Scissor game. The oldest game i know since my childhood.")
 
print("Remember the rules.")
print(
    '''
    Rock beats scissor \n 
    Scissor beats paper \n
    paper beats rock \n
    and the draw is when both the players got the same player.
'''
)
 
play_game = True
 
user_score = 0
ai_score = 0
 
total_game_round = 6
 
 
# This function clears the screen after the end of a game round so, complete 6 rounds from `total_game_round`
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
 
 
while play_game :  # A outside while loop keeps up the process of checking try and errors.
 
    while total_game_round > 0:  # this is the main functional loop that keeps the game going.
 
        # for i in range(total_game_round) :
 
        total_game_round -= 1
 
        try :
 
            user = int(input("Type '0 for Rock', '1 for Paper', and '2 for Scissor': "))
 
            if ( user > 2 or user < 0) :
                print("It's a wrong input... please choose between 0 --> `rock`, 1 --> 'paper` and 2 --> `scissor`")
                continue
 
        except ValueError :
            print("It's a wrong input... please choose between 0 --> `rock`, 1 --> 'paper` and 2 --> `scissor`")
            continue
        
        print(f"You chose: {player_name_string[user]}")
        print(f"Your score: {user_score}")
        print(player[user])
 
        ai = random.randint(0, 2)
 
        print("-----------------------------------")
 
        print(f"AI 🤖 chooses...{player_name_string[ai]}")
        print(f"AI score:  {ai_score}")
 
        print(player[ai])
 
        choice_matrix = [
 
            ["Oh! It's a Draw!", "AI wins. Paper 📃 covers the rock. 🪨", "You wins. Rock 🪨 smashes the scissor ✂️"],
            # 1) paper for all the 3 cases
 
            ["You wins. Paper 📃 covers the rock 🪨", "Oh! It's a Draw!", "AI wins. Scissor ✂️ cuts the paper 📃"],
 
            # 2) scissors for all 3 cases
            ["AI wins. Rock 🪨 smashes the scissor ✂️", "You wins. Scissor ✂️ cuts the paper 📃", "Oh! It's a Draw!"]
 
            ]
        
        
        print(choice_matrix[user][ai])
 
 
        # ------------FOR adding the user and ai score based on who wins using matrix --------------------
 
        # pick only those spots where user wins.
 
        if ( choice_matrix[user][ai] == choice_matrix[0][2] or choice_matrix[user][ai] == choice_matrix[1][0] or choice_matrix[user][ai] == choice_matrix[2][1]) :
            user_score += 1
 
            # pick only those spots where AI wins.
        elif (choice_matrix[user][ai] == choice_matrix[0][1] or choice_matrix[user][ai] == choice_matrix[1][2] or choice_matrix[user][ai] == choice_matrix[2][0]) :
            ai_score += 1
 
        # ---------------------------if user exit the game, check the final score or else continue the game-----------
            
        if (total_game_round == 0) :
            user_answer = input("wanna take a break? Type 'y' to stop it or 'n' to continue: ").lower()
 
            if user_answer == 'y' :
                # check who wins...
                if (user_score > ai_score) :
                    print(f"You 🍻 win by {user_score - ai_score} scores. Your total score is:  {user_score} VS AI total score is:  {ai_score}")
                elif user_score < ai_score:
                    print(f"AI 🤖  wins by {ai_score - user_score} scores. AI's total score is:  {ai_score} VS your score is:  {user_score} ")
                else : # Its probability is very low.
                    print(f"you both got the same point, it's a DRAW  . your score: {user_score} and AI score: {ai_score}")
                # exit()
                play_game = False
                break  # it will stop the while loop .
 
            else :
                input("\nPress Enter to continue the game 🚀 ...")
                clear_screen()
                total_game_round =  7
                continue    # continue keyword, lets the while loop run continuously, when play game is true.