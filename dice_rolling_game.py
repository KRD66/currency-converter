import random

while True:
  choice = input("Roll the dice?(y/n):  " ).lower()
  if choice == 'y':
     die1 = random.radint(1, 6)
     die2 = random.radint(1, 6)
     print(f'({die1}, {die2})')
  elif choice =='n':
    print ('thank you message!')
    break
  else:
   print ('invalid choice!')  
   