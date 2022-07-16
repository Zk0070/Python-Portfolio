import random
print('***********************************')
print('Welcome to the Random password generator created by Zabi Khan!')
print('100% assured unhackable passwords!!')
print('************************************')
letters=int(input('Enter the number of letters you want in your password: '))
symbols=int(input('Enter the number of symbols you want in your password: '))
numbers=int(input('Enter the number of numerical elements  you want in your password: '))
Letters=['A','B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N','O','P','Q','R','S','T','U','V', 'W', 'X','Y', 'Z']
Symbols=['!','*','#','@','$','%','(',')']
Numbers=['1','2','3','4','5','6','7','8','9','10']

password_list=[]
for l in range(0,letters+1):
    password_list.append(random.choice(Letters))
for s in range(0,symbols+1):
    password_list.append(random.choice(Symbols))
for n in range(0,numbers+1):
    password_list.append(random.choice(Numbers))
    
random.shuffle(password_list)
password=''.join(password_list)
print(f'Your suggested password recommendation is:{password}')
    