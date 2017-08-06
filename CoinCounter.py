# Sample Data

# coding: utf-8

# |Value|0.05|0.1|0.2|0.5|1|2 |total
# |------|------|
# |Number|32|40|33|13|29|50|
# |Total |1.6|4|6.6|6.5|20|100|147.7

# In[ ]:

from __future__ import print_function
#from IPython.display import clear_output

def ask_choice():
     while True:
        try:    
            choice = int(raw_input('Please input your coin value: (1-6; 1:5c,2:10c,3:20c,4:50c,5:$1,6:$2)'))
        except ValueError:
            print("Sorry, please input a number between 1-6.")
            continue
        else:
            if choice not in range(1,7):
                print("Sorry, please input a number between 1-6.")
                continue
            else:
                return choice

def ask_number():
    while True:
        try:    
            number = int(raw_input('Please input the number of your related coin value: '))
        except ValueError:
            print("Sorry, please input an integer.")
            continue
        else:
            return number

def ask_reset():
    while True:
        try:    
            reset = int(raw_input('Would you like to restart? 1:Restart; 2: Keep on going'))
        except ValueError:
            print("Sorry, please input a number between 1-2.")
            continue
        else:
            if reset not in range(1,3):
                print("Sorry, please input a number between 1-2.")
                continue
            else:
                if reset == 1:
                    return True
                else:
                    return False


#The main function starts from here      
name = [' ','5 cents','10 cents','20 cents','50 cents','1 dollar','2 dollars']
val = [0,0.05,0.10,0.20,0.50,1.00,2.00]
num = [0]*7
total = [0]*7
newturn = False

while True:
    print("Welcome to Cong's Coin Counter Application!")
    while not newturn:
        choice = ask_choice()
        num[choice] = ask_number()
        total[choice] += val[choice] * num[choice]
        #clear_output()
        for i in range(1,7):
            print(name[i] + ' | '+ str(num[i]) + " pieces | " + str(total[i]))
        print("Total" + ' | '+ "      | " + str(sum(total)))
        newturn = ask_reset()
    num = [0]*7
    total = [0]*7
    newturn = False
    #clear_output()



