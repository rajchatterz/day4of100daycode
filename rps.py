print("What do you Choose? Type 0 for Rock, 1 for paper or 2 for Scissor.")
user_input = str(input())
import random
computer_choice = random.choice("123")
if computer_choice=="1":
    print('''
                    ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'     
          
          ''')
elif computer_choice=="2":
    print('''
          
          $$$$$$$$$$$$$$$$Q$$$$$$
$$$$$$$$$$$$' $ `$$$$$$
$$$$$$$$$$$$  $  $$$$$$
$$$$$$  $$$$  $  $$"'$$
$$$$$$$  '$$  $  $' .$$
$$$$$$$$.  "  $ .! .$$$
$$$$$$$$$.    '    $$$$
$$^^$$$$$'        J$$$$
$$$   ~""   `.   .$$$$$
$$$$$e,      ;  .$$$$$$
$$$$$$$$$$$.'   $$$$$$$
$$$$$$$$$$$$.    $$$$$$
$$$$$$$$$$$$$     $$$$$

          ''')
    
elif computer_choice=="3":
    print('''
          
          $$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$'`$$$$$$$$$$$$$'`$$$
$$$$$$  $$$$$$$$$$$  $$$$
$$$$$$$  '$/ `/ `$' .$$$$
$$$$$$$$. i  i  /! .$$$$$
$$$$$$$$$.--'--'   $$$$$$
$$^^$$$$$'        J$$$$$$
$$$   ~""   `.   .$$$$$$$
$$$$$e,      ;  .$$$$$$$$
$$$$$$$$$$$.'   $$$$$$$$$
$$$$$$$$$$$$.    $$$$$$$$
$$$$$$$$$$$$$     $by&TL$
-------------------------
       I LOVE YOU

          
          
          ''')
    
if user_input==computer_choice:
    print("Both tie")