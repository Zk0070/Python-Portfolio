print('Welcome to the tip calculator created by Zabi Khan in Python!')
Total_bill=float(input('Enter the total bill amount in $: '))
Tip_offered=int(input('Enter the amount of tip to be offered to the restaurant service 5%,10% or 15%:'))
people=int(input('Enter the number of people at the party: '))
Tip_amount=Tip_offered/100*Total_bill
Final_bill=Tip_amount+Total_bill
Share=Final_bill/people
Each_share=round(Share,2)
print(f'Your final bill is {Final_bill} $')
print(f'The amount to be shared by each member is {Each_share} $')