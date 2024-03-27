# imports os module necesary for clear_screen function definded below
import os

# function clears terminal using command 'cls' or 'clear' depending on OS system ('nt' = Windows)
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear') 

# function prints castle
def print_castle():
  print('''
                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'' ''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------
''')

# function prints vampire
def print_vampire():
  print('''
          .         __      '        .       '       .
    *            _-~  ~-_      .         '      .
   .   .        /___  ___\  '             .             .
               / (O)  (o) \         *         ___    *  .
     __,-~-~-,/    -..-    \  .-~~-.   __..-~~   ~~-.._
  .-~  `V~V~V'`\ -v----v-   \/     /.-~  //..  \   \.  `~-._
    //.     \.' `\..___..---/    /''    .    '   .   ..
                       ''/ \\..'  \'   V~V~V'  //  /  ' .  ' /  \ . '  \\\ \ \
                       
  ''')

# function prints arrows
def print_arrows():
  print('''
        _.-"/______________________//          \\\_____________________\"-._
        `'-.\~~~~~~~~~~~~~~~~~~~~~~\\\          //~~~~~~~~~~~~~~~~~~~~~/.-'
  ''')

# function prints gargoyle
def print_gargoyle():
  print('''
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠶⠃⢸⠀⠀⠀⠀⠀⣰⣿⠀⠀⠀⠀⠀⡦⣄⠀⠀⠀⠀⠀⢨⡇⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠃⠀⠀⠸⡄⠀⠀⠀⣴⠀⠉⠒⠒⠒⠒⠒⠃⠈⡇⠀⠀⠀⢠⠎⠁⠀⠀⠈⡲⡀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⢠⠖⠃⠀⠀⠀⠀⠀⠑⡀⠀⠀⠱⡀⠀⠣⠀⠤⠀⠞⠀⢠⠎⠀⠀⢠⠊⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⣠⡟⠏⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⢸⡀⠀⣀⠀⡀⠀⢠⡷⠀⢀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠺⠵⠀⠀⠀⠀⠀
      ⠀⠀⢀⣘⡟⠓⠀⠀⡀⠀⠀⠀⢸⡇⠀⠀⠀⠑⡄⠀⢑⡀⡀⠀⢈⣠⡊⠀⢠⠋⠁⠀⠀⢸⡇⠀⠀⡀⠀⠀⠻⢛⣃⠀⠀⠀
      ⠀⠀⣘⡏⠋⠀⠀⡘⠁⠀⠀⠀⠘⢇⠀⣀⠤⠤⠼⠤⠊⠀⠑⣠⠃⠀⠑⠤⡣⠤⠤⣀⠀⡸⠃⠀⠀⠘⢂⠀⠀⠛⣙⣀⠀⠀
      ⠀⣤⣿⠉⠀⠀⠐⡇⠀⠀⠀⠀⠀⢨⠊⠁⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠈⢓⡁⠀⠀⠀⠀⢸⠀⠀⠀⠙⣽⣤⠀
      ⣬⣿⣯⠀⠀⠀⢀⡧⠤⠠⢤⠀⠀⢸⠀⠀⠀⠀⢀⠀⠀⠀⠀⠿⠀⠀⠀⢀⣀⠀⠀⠀⢈⡇⠀⢀⠤⠤⠼⢄⠀⠀⠀⣭⣿⣄
      ⣭⣽⣥⠀⠀⠀⣌⠀⠀⠀⠀⠁⢲⣮⡀⠀⠀⠠⢾⠉⠀⠀⠉⡤⠉⠀⠀⢉⡽⠂⠀⠀⢈⣕⠖⠈⠀⠀⠀⠀⢳⡄⠀⣮⣿⣬
      ⣭⣶⡦⠀⠀⠀⡧⠀⠀⠀⠀⠀⠀⠃⠳⡀⠀⠀⠀⢳⠀⠀⠉⡅⠁⠀⠀⠈⡆⠀⠀⢀⠖⠊⠀⠀⠀⠀⠀⠀⢸⡇⠀⣖⣿⣦
      ⠶⠶⠶⠀⠀⠀⠙⢄⠀⠀⠀⠀⢠⡀⠀⠣⡀⠀⠀⠫⡀⠀⠁⠀⠀⠀⢀⠜⠁⠀⢀⠎⠀⢀⡄⠀⠀⠀⠀⡰⠋⠀⠀⠶⠾⠶
      ⠀⠾⠶⠀⠀⠀⠀⠈⠑⢄⠀⠀⠀⠑⡀⠀⠱⡀⠀⠀⢣⣀⣀⣀⣀⣀⠞⠀⠀⢠⠊⠀⢠⠊⠀⠀⠀⡰⠛⠀⠀⠀⠀⠶⠿⠀
      ⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⢉⣄⠀⠀⠑⡤⡄⠱⡀⠀⠀⠡⡀⠀⠀⡎⠀⠀⢠⠊⢠⢴⠃⠀⠀⡰⠉⠀⠀⠀⠀⠀⠀⠿⠀⠀
      ⠀⠀⠘⢛⠀⠀⠀⡐⠋⠉⠉⢬⡆⠀⠀⠘⡜⠤⢔⠀⠀⡽⠄⠠⠠⡇⠀⠠⡧⠤⣧⠃⠀⠀⣴⠉⠉⠙⢄⠀⠀⢀⡻⠃⠀⠀
      ⠀⠀⠀⠀⠣⠀⠀⡇⠀⠀⠀⠀⠈⡷⠂⠀⠘⡄⠸⢀⣀⣿⠀⠀⠀⠓⠄⠄⠇⢰⡁⠀⠀⢖⠁⠀⠀⠀⢸⠀⢀⡊⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠱⠐⡇⠀⠀⠀⢀⡌⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⢣⠀⠀⠀⢸⢀⠎⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠙⠧⡀⠀⠀⣼⣤⣤⡤⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢤⣤⣤⡇⠀⢀⡼⠉⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀
  ''')

# function prints evil lord
def print_lord():
  print('''
                     _.--.    .--._
                   ."  ."      ".  ".
                  ;  ."    /\    ".  ;
                  ;  '._,-/  \-,_.`  ;
                  \  ,`  / /\ \  `,  /
                   \/    \/  \/    \/
                   ,=_    \/\/    _=,
                   |  "_   \/   _"  |
                   |_   '"-..-"'   _|
                   | "-.        .-" |
                   |    "\    /"    |
                   |      |  |      |
           ___     |      |  |      |     ___
       _,-",  ",   '_     |  |     _'   ,"  ,"-,_
     _(  \  \   \"=--"-.  |  |  .-"--="/   /  /  )_
   ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
  !     \  \  \   \                  /   /  /  /     !
  :      \  \  \   \                /   /  /  /      : . .
  ''')

# function prints rip tombstone
def print_rip():
  print('''
                           _____  _____
                          <     `/     |
                           >          (
                          |   _     _  |
                          |  |_) | |_) |
                          |  | \ | |   |
                          |            |
           ______.______%_|            |__________  _____
         _/                                       \|     |
        |                 Y O U   D I E D                <
        |_____.-._________              ____/|___________|
                          | * fi/ll/in |
                          | + 19/10/97 |
                          |            |
                          |            |
                          |   _        <
                          |__/         |
                           / `--.      |
                         %|            |%
                     |/.%%|          -< @%%%
                     `\%`@|     v      |@@%@%%    
                   .%%%@@@|%    |    % @@@%%@%%%%
              _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%
  ''')

# function prints skyrim symbol
def print_skyrim():
  print('''       
                            MM       MM                                  
                           MM         M                                  
                           MM  M      MM                                 
                          MM   M       MM                                
                         MMM   MMM=    MMM                               
                        MMM   MMM=MM   MMM                               
                        MMM   M     M   M M                              
                       MMMM         M   MMMM                             
                      MMMMM       MM    MMMM                             
                      MMMM     MM        MMMM                            
                     MMMM     MM         MMMMM                           
                    MMMMM     MMMM        MMMMM                          
                   MMMMMM   MMMMMMM MMM   MMMMM                          
                    MMMMM=MMMMMMMMMMMMMMMMMMMMM                          
                    MMMMMMMMMMMMMMMMMMMMMMMMMM                           
                     MMM=MMMMMMMMMMMMMMMMMMMMM                           
                      MMMMMMMMMMMMMMMMMMMMMMM                            
                       MMMM  M MMMMM M  MMM                              
                       MMMM  M  MMM     MMM                              
                        MMM      MM     MMM                              
                         MM      MMM    MM                               
                         MMMM     MM  MMM                                
                          MMM    MM  MMMM                                
                           MM   MM   MMM                                 
                           MM  MM                                        
                            M   M                                        
                                M                                        
                               M                                         
                              M                                          
                               M  MM                                     
                                MMM                                      
                                MM                                       
                                 M                                                    
''')

# function to validate if player wants to keep playing
def try_again():
  global play_game
  message = 'Wanna try again? Type "Y" or "N".\n'
  while True:
      answer = input(message).lower()
      if (answer == 'y'):
          play_game = True
          clear_screen()
          return play_game
      elif (answer == 'n'):
          play_game = False
          print("Thanks for Playing!!!")
          return play_game
      else:
          print("Please enter a valid option.")

# defined global game variable
play_game = True

# global while loop to keep game running as long as play_game var is "True"
while play_game:
    
  print_castle()
  print("Welcome to Evil Castle.")
  print("Your mission is to defeat the Evil Lord.")

  # validates user input
  while True:
      one = input('You enter the castle and see two stairs, one goes up and the other goes down. Where do you want to go? Type "U" or "D".\n').lower()
      if (one == "u") or (one == "d"):
          break
      else:
          print("Please enter a valid option.")
          continue
  
  clear_screen()

  # checks first user choice
  if (one == "d"):
      print_vampire()
      print("You were eaten by a feral vampire!! you died. Game over.")
      try_again()
  else:
      print_arrows()
    
      # validates user input again
      while True:
          two = input('You find two corridors, one to the left and one to the right. Where do you want to go? Type "L" or "R".\n').lower()
          if (two == "l") or (two == "r"):
              break
          else:
              print("Please enter a valid option.")   
              continue
      
      clear_screen()

      # checks second user choice
      if (two == "l"):
          print_gargoyle()
          print("You were attacked by a bunch of gargoyle!! you died. Game over.")
          try_again()
      else:
          print_lord()

          # validates user input a third time
          while True:
              three = input('You find the Evil Lord, but he was expecting you!! How do you want to approche him? Type "(P)arley", "(W)eapon", or "(M)agic".\n').lower()
              if (three == "p") or (three == "w") or (three == "m"):
                  break
              else:
                  print("Please enter a valid option.")
                  continue
          
          clear_screen()

          # checks third user choice
          if (three == "w") or (three == "m"):
              print_rip()
              print("He is far too powerful!! you died. Game over.")
              try_again()
          else:
              print_skyrim()
              print('"Parley" my a**. FUS-RO-DAH!!!!! you are the dragonborn anyways😎 . You win!!')
              try_again()
