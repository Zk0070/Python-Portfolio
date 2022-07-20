print('Welcome to the auction application devloped by Zabi Khan!!')

print('****************************************************')
print('''
                     888   d8b                 
                        888   Y8P                 
                        888                       
 8888b. 888  888 .d8888b888888888 .d88b. 88888b.  
    "88b888  888d88P"   888   888d88""88b888 "88b 
.d888888888  888888     888   888888  888888  888 
888  888Y88b 888Y88b.   Y88b. 888Y88..88P888  888 
"Y888888 "Y88888 "Y8888P "Y888888 "Y88P" 888  888

''')
print('************************************')
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
end_of_auction=False
while not end_of_auction:
    name=input('Enter the name of the bidder: ').lower()
    price=int(input('Enter the value of bid offered in $: '))
    dic={}
    dic[name]=price
    print(dic)
    contd=input('Would you like to continue the bidding yes or no: ').lower()
    if contd=='no':
        end_of_auction=True
        find_highest_bidder(dic)
    elif contd=='yes':
        continue
      

        

    