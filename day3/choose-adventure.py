import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear') 

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

def print_arrows():
  print('''
        _.-"/______________________//          \\\_____________________\"-._
        `'-.\~~~~~~~~~~~~~~~~~~~~~~\\\          //~~~~~~~~~~~~~~~~~~~~~/.-'
  ''')

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

print_castle()
print("Welcome to Evil Castle.")
print("Your mission is to defeat the Evil Lord.")

one = input('You enter the castle. Where do you want to go? Type "up" or "down".\n').lower()
clear_screen()
if one == "down":
  print_vampire()
  print("You were eaten by a feral vampire!! you died. Game over.")
else:
  print_arrows()
  two = input('You find two corridors, one to the left and one to the right. Where do you want to go? Type "left" or "right".\n').lower()
  clear_screen()
  if two == "left":
    print_gargoyle()
    print("You were attacked by a bunch of gargoyle!! you died. Game over.")
  else:
    print_lord()
    three = input('You find the Evil Lord, but he was expecting you!! How do you want to approche him? Type "parley", "weapon", or "magic".\n')
    clear_screen()
    if (three == "weapon") or (three == "magic"):
      print_rip()
      print("He is far too powerful!! you died. Game over.")
    else:
      print_skyrim()
      print('"Parley" my a**. FUS-RO-DAH!!!!! You win!!')
