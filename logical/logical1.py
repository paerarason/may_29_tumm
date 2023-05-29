def check_card(card_num):
   if card_num>=400_000_000_000_0 and card_num<=500_000_000_000_0:
      return check_syntactically_valid(card_num)
   elif card_num>=370_000_000_000_0000 and card_num<380_000_000_000_0000:
      return check_syntactically_valid(card_num)
   elif card_num>=600_000_000_000_000 and card_num<700_000_000_000_000:
      return check_syntactically_valid(card_num)
   else:
      return False
def check_syntactically_valid(num):
    number=[]
    while num:
        number.append(num%10)
        num//=10
    step_2=0
    step_3=0
    for i in range(1,len(number),2):
        temp=number[i]*2
        step_2+=add_digits(temp)
    for i in range(0,len(number),2):
        step_3+=number[i]

    if (step_2+step_3)%10==0:
       return True
    return False
         
def add_digits(number):
   res=0
   while number:
      res+=number%10
      number//=10
   return res

if check_card(int(input("ENTER the CARD Number: "))):
   print("Card Valid")
else:
   print("Card InValid")