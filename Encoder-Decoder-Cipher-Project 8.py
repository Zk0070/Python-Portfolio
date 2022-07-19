print('Welcome to the Cipher secret message encoder/decoder devleloped by Zabi Khan!!')
print('****************************')
print( """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
print('******************************')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(wordtext,shift_numb,cipherdirection):
    endtext=""
    if cipherdirection=='encode':
        for letter in wordtext:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=position+shift_numb
                endtext +=alphabet[new_position]
            else:
                endtext +=letter
        print(f'Your encoded text is :{endtext}')
        
    elif cipherdirection=='decode':
        for letter in wordtext:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=position-shift_numb
                new_letter=alphabet[new_position]
                endtext+=alphabet[new_position]
        print(f'Your decoded text is :{endtext}')
        
should_end=False
while not should_end:
    cipherdirection=input('Do you want to encode or decode using tool:')
    word=input('Enter your message:').lower()
    shift_num=int(input('Enter the shift code: '))
    shift_num=shift_num%27
    
    caesar(wordtext=word,shift_numb=shift_num,cipherdirection=cipherdirection)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
    
    

        
        
