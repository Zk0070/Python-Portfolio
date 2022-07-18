import random
print('Welcome to the Hangman game devloped by Zabi Ulla Khan!')
print('*****************************************')
print('''                                          
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/               ''')
print('*****************************************')  
print('You just have 6 chances life for the game all the best!!!!')
stages=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=['zabi','riyan','taha']
rand_word=random.choice(word_list)
print(rand_word)
display=[]
lives=6
word_len=len(rand_word)
for _ in range(word_len):
    display+='_'
print(display)
endgame=False
while not endgame:
    guess=input('Enter a letter of your choice which could be part of the word: ').lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position  in range(word_len):
        letter=rand_word[position]
        if guess==letter:
            display[position]=letter
    print(display)
    if guess not in rand_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life be careful!.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose try next time!!.")
            break
    if '_' not in display:
            endgame=True
            print('Congratulations you have won!!!')
    print(stages[lives])
        
    
    

        
    
    