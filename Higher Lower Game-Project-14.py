import random
from art import logo,vs
from game_data import data
print('Welcome to the Higher and lower game develped by Zabi Khan!!')
print('*******************************')
print(logo)
score=0
account_b=random.choice(data)
end_of_game=False
while not end_of_game:
  account_a=account_b
  account_b=random.choice(data)
  while account_a==account_b:
    account_b=random.choice(data)
  accounta_name=account_a['name']
  accounta_desr=account_a['description']
  accounta_count=account_a['country']
  accounta_follow=account_a['follower_count']

  print(f'Compare A:{accounta_name},a {accounta_desr}, from {accounta_count}')
  print(vs)
  accountb_name=account_b['name']
  accountb_desr=account_b['description']
  accountb_count=account_b['country']
  accountb_follow=account_b['follower_count']
  print(f'Against B:{accountb_name},a {accountb_desr}, from {accountb_count}')
  guess=input('Who do you think has more followers, A or B: ').lower()
  if accounta_follow>accountb_follow and guess=='a':
    score+=1
    print(f'You are right and your current score is {score}')
  elif accountb_follow>accounta_follow and guess=='b':
    score+=1
    print(f'You are right and your current score is {score}')
  else:
    end_of_game=True
    print(f'Sorry you are wrong,Your final score is {score}')
    
  