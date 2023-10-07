import random
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
attack=[rock,paper,scissors]
while True:
 print("What do you choose? Type Rock, Paper or Scissors")
 choice_initial=input()
 choice=choice_initial.lower()
 human_choice=["r","p","s"]
 if choice[0]==human_choice[0] or choice[0]==human_choice[1] or choice[0]==human_choice[2]:
   print(attack[human_choice.index(choice[0])])#index=human_choice.index(choice[0])  This is the code to find the index position.
 # if choice[0]=="r":
 #   print(rock)
 # elif choice[0]=="p":
 #   print(paper)
 # elif choice[0]=="s":
 #   print(scissors)
 else:
   print("You have to choose from the three options only. Thats the game.")
   break
 print("Computer's choice :\n")
 comp_choice=random.randint(0,2)
 print(attack[comp_choice])
 if ((choice[0]=="r" and comp_choice==2) or (choice[0]=="p" and comp_choice==0) or (choice[0]=="s" and comp_choice==1)):
   print("You Win!!!")
 elif((choice[0]=="r" and comp_choice==0) or (choice[0]=="p" and comp_choice==1) or (choice[0]=="s" and comp_choice==2)):
   print("It's a Draw.")
 else:
   print("You lost.")
 print("This reply has exited. Run again?")  
 reply=input().lower()
 if reply[0]=="n":
   break
