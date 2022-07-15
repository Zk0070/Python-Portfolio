import random
print('Welcome to the game of Rock paper scissors devloped by Zabi Khan!')
print('**********************************')
print('The rules for the game are below and they are very simple!')
print('Rule#1: rock beats scissor,scissor beats paper and paper beats rock')
print('Rule#2:The choices should be either rock,paper or scissor only!')
print('**********************************')
# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice_list=['rock','paper','scissor']
user_choices=input('Enter your choice for the game:rock,paper or scissor: ')
print(f'You chose:{user_choices}')
user_choice=user_choices.lower()
machine_choice=random.choice(choice_list)
if user_choice=='rock' and machine_choice=='scissor':
    print(rock)
    print(f' Machine chose:{machine_choice}')
    print(scissor)
    print('Final result:You won')
elif user_choice=='scissor' and machine_choice=='paper':
    print(scissor)
    print(f' Machine chose:{machine_choice}')
    print(paper)
    print('Final result:You won!')
elif user_choice=='paper' and machine_choice=='rock':
    print(paper)
    print(f' Machine chose:{machine_choice}')
    print(rock)
    print('Final result:You won!')
elif machine_choice=='rock' and user_choice=='scissor':
    print(scissor)
    print(f' Machine chose:{machine_choice}')
    print(rock)
    print('Final result:Machine Won!')
elif machine_choice=='scissor' and user_choice=='paper':
    print(paper)
    print(f' Machine chose:{machine_choice}')
    print(scissor)
    print('Final result:Machine Won!')
elif machine_choice=='paper' and user_choice=='rock':
    print(rock)
    print(f' Machine chose:{machine_choice}')
    print(paper)
    print('Final result:Machine Won!')
elif user_choice==machine_choice:
    if user_choice=='rock':
        print(rock)
        print(f' Machine chose:{machine_choice}')
        print(rock)
        print('Final result: It is a draw!')
    elif user_choice=='paper':
        print(paper)
        print(f' Machine chose:{machine_choice}')
        print(paper)
        print('Final result: It is a draw!')
    elif user_choice=='scissor':
        print('scissor')
        print(f' Machine chose:{machine_choice}')
        print('scissor')
        print('Final result: It is a draw!')
        