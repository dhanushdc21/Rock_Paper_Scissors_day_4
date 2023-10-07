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
while True:
 print("What do you choose? Type Rock, Paper or Scissors")
 choice_initial=input()
 choice=choice_initial.lower()
 if choice[0]=="r":
   print(rock)
 elif choice[0]=="p":
   print(paper)
 elif choice[0]=="s":
   print(scissors)
 else:
   print("You have to choose from the three options only. Thats the game.")
 print("Computer's choice :\n")
 comp_choice=random.randint(0,2)
 if comp_choice==0:
   print(rock)
 elif comp_choice==1:
   print(paper)
 else:
   print(scissors)
 print("This reply has exited. Run again?")  
 reply=input().lower()
 if reply[0]=="n":
   break