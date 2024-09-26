#Rock, paper,scissor game
import random
user_choice=int(input(print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")))
computer_choice=random.randint(0,2)

print("computer choice")
print(computer_choice)
if computer_choice==user_choice:
  print("its a draw.")
elif  computer_choice > user_choice:
  print("you lose.")
elif user_choice > computer_choice:
  print("you win.")
elif computer_choice==0 and user_choice==2:
  print("you lose.")
elif user_choice==0  and computer_choice==2:
  print("you win.")