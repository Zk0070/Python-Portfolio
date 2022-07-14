print('''
  888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888
''')

print('Welcome to the Treasure land of Zabi Khan!')
print('Your mission is to find the treasure in this mysterious place...all the best!')
choice_1=input('You have begun and you are at a cross road which has two turns\n left ,right choice is yours watch out because it is dangerous!! \n for left press l for right press r:')
choice1=choice_1.lower()
if choice1=='l':
    print('Good choice you are safe at this point!')
    choice_2=input('You have arrived at a lake now  you have two choices to wait for a boat to cross the river or to swim choice is yours watch out because it is dangerous!!\n for boat press b for swim press s:')
    choice2=choice_2.lower()
    if choice2=='b':
        print('Good choice you are for the second time!')
        choice_3=input('You have successfully crossed the lake and arrived at the treasure door  now but wait the danger is not over yet!!you have select 1  door out of the 3 red ,green and yellow doors correct door will lead you to they treasure wrong will end your life  choice is yours watch out!! \n for red door press r for green door press g and for yellow door press y:')
        choice3=choice_3.lower()
        if choice3=='y':
            print('Great choice you found the treasure and won the game lucky guy!!!')
        elif choice3=='r' or choice3=='g' :
                print('Bad choice you fall of the mountain as there is no end the door.. bad luck try next time Game over!!!')
    elif choice2=='s':
        print('Bad choice you are in a lake full of aligators who are ready to feast on you Game over!!!')
elif choice1=='r':
    print('Bad choice you are in a zone  full of beasts who are ready to feast on you Game over!!!')
   