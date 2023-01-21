import operator
import random

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

op1 = "" # Just defining the variables for my operators
op2 = ""
op3 = ""
nth_num = 1
list_num1 = int(input("Enter number 1: "))
list_num2 = int(input("Enter number 2: "))
list_num3 = int(input("Enter number 3: "))
list_num4 = int(input("Enter number 4: "))
    
num1 = 0 # Just defining the variables for my numbers
num2 = 0
num3 = 0
num4 = 0

super_count = 0

while super_count < 10000:
    my_numbers = [list_num1, list_num2, list_num3, list_num4]
    para_total_b4 = 0
    para_total_3num = 0 
    para_total = 0 # Total value of the 2 random numbers in () combined
    my_operators = ["+","-","/","*"] # List of operators
    first_combo = 0 # First two numbers put together.  Sets the variable.
    second_combo = 0 # Last two numbers put together.  Sets the Variable
    total = 0 # Puts the first_combo and second_combo together to get the total value
   
    # Sets all the numbers to a random number out of the list of numbers
    num1 = (random.choice(my_numbers))
    my_numbers.remove(num1)
    num2 = (random.choice(my_numbers))
    my_numbers.remove(num2)
    num3 = (random.choice(my_numbers))
    my_numbers.remove(num3)
    num4 = (random.choice(my_numbers))
    my_numbers.remove(num4)
   
    parathenses = [num1,num2,num3,num4] # List to randomly choose numbers and assign them to be done first (or act like they are in parathenses)
    
    # Sets operators to a random operator out of the four
    op1 = (random.choice(my_operators))
    op2 = (random.choice(my_operators))
    op3 = (random.choice(my_operators))
    op_one = operatorlookup.get(op1) # Gets a random operator and uses it for the first 2 numbers
    op_two = operatorlookup.get(op2) # Gets a random operator and uses it for the last 2 numbers
    op_three = operatorlookup.get(op3) # Gets a random operator and uses it for combining the first_combo and second_combo
   
    # Parantheses Code
    x = 0
    if super_count > 2000:
        while x < 200:
            # Chooses two random numbers to go into ()
            parathenses = [num1,num2,num3,num4]
            para1 = (random.choice(parathenses))
            parathenses.remove(para1)
            para2 = (random.choice(parathenses))
            parathenses.remove(para2)

            # Chooses two random numbers to go outside of ()
            after_para_num1 = (random.choice(parathenses))
            parathenses.remove(after_para_num1)
            after_para_num2 = (random.choice(parathenses))
            parathenses.remove(after_para_num2)
        
            if op1 == "/" and para2 == 0: # Checks to make sure not dividing by 0 in ()
                para2 = 100
                break
            
            para_combo = op_one(para1, para2) # Combines numbers in ()
            
            if op3 == "*" or op3 == "/": #Checks if has to do pemdas
                after_para = op_three(after_para_num1, after_para_num2)
                
                if para_combo == 0 and op2 == "/": # Checks to make sure not dividing by 0
                    para_combo = 100
                    
                para_total = op_two(after_para, para_combo)
                if para_total == 10:
                    break
                else:
                    para_combo = 100
            
            if op2 == "/" and after_para_num1 == 0: # Checks to make sure not dividing by 0
                after_para_num1 = 100
                
            after_para = op_two(para_combo, after_para_num1)
                
            if op3 == "/" and after_para_num2 == 0: # Checks to make sure not dividing by 0
                after_para_num2 = 100 
                    
            para_total = op_three(after_para, after_para_num2)
            x = x + 1 # Counter to only check the four randomly chose numbers 200 times in parantheses
                             
            if para_total == 10:
                x = 201
                break
        
            if after_para_num2 == 0 and op1 == "/" or para2 == 0 and op3 == "/":
                after_para_num2 = 100
                para2 = 100
            
            if op2 == "*" or op2 == "/":
                para_combo = op_one(para1, para2)
                
                if op2 == "/" and para_combo == 0:
                    para_combo = 100
                    
                b4_para = op_two(after_para_num2, para_combo)
                
                if op3 == "/" and after_para_num1 == 0:
                    after_para_num1 = 100
                    
                para_total_b4 = op_three(b4_para, after_para_num1)
            
            if para_total_b4 == 10:
                break
                    
            after_para = op_three(after_para_num1, after_para_num2)
            para_combo = op_one(para1, para2)
                    
            if op2 == "/" and para_combo == 0:
                para_combo = 100
                    
            para_total = op_two(after_para, para_combo)
            
            if para_total == 10:
                break
            
    if para_total == 10 or para_total_b4 == 10:
        break
    
    
    x = 0
    if super_count > 2000:
        while x < 200:
            parathenses = [num1,num2,num3,num4]
            para1 = (random.choice(parathenses))
            parathenses.remove(para1)
            para2 = (random.choice(parathenses))
            parathenses.remove(para2)
            para3 = (random.choice(parathenses))
            parathenses.remove(para3)
            
            after_para_num1 = (random.choice(parathenses))
            parathenses.remove(after_para_num1)
            
            if para2 == 0 and op1 == "/" or para3 == 0 and op2 == "/" or op3 == "/" and after_para_num1 == 0:
                para2 = 100
                para3 = 100
                after_para_num1 = 100
        
            para_combo = op_one(para1, para2)
            para_combo2 = op_two(para_combo, para3)
            para_total_3num = op_three(para_combo2, after_para_num1)
            
            if op2 == "*" or op2 == "/":
                para_combo = op_two(para2, para3)
                
                if op1 == "/" and para1 == 0:
                    para1 = 100
                    
                para_combo2 = op_one(para_combo, para1)
                para_total_3num = op_three(para_combo2, after_para_num1)
                
            if para_total_3num == 10:
                super_count = 10001
                break
            x = x + 1
    
    if para_total_3num == 10:
        break
   
    if op1 == "/" and num2 == 0 or op2 == "/" and num3 == 0 or op3 == "/" and num4 == 0: # Divide by 0!!
            num2 = 100
            num3 = 100
            num4 = 100
        
    first_combo = op_one(num1, num2) # Combines the first 2 numbers together with a random operator
    second_combo = op_three(num3, num4) # Combines the last 2 numbers together with a random operator
   
    if second_combo == 0 and op2 == "/": # If the second combination of the last 2 numbers = 0 then it sets the 0 to 100 so that it is not dividing by 0 anymore
        second_combo = 100 # Divide by 0!!
       
    total = op_two(first_combo, second_combo) # Combines the first_combo and second_combo with a random operator
   
    if op2 == "*" or op2 == "/": # If the middle operator is * or / it does changes the order of how things are combined
        
        pemdas = 0
        pemdas2 = 0
        
        if op1 == "*" or op1 == "/": # If the first operator is also * or / it does this first then the rest to do order of operations
            pemdas = op_one(num1, num2)
            pemdas2 = op_two(pemdas, num3)
            total = op_three(pemdas2, num4)
            
        elif op3 == "*" or op3 == "/": # If the last operator is * or / then it combines the 2nd number and 3rd then the 4th and finally the 1st number
            pemdas = op_two(num2, num3)
            pemdas2 = op_three(pemdas, num4)
            
            if op1 == "/" and pemdas2 == 0: # Divide by 0!!
                pemdas2 = 100
                
            total = op_one(num1, pemdas2)
            
        else: # If the middle operator is * or / it does this first then combines the rest of the numbers
            pemdas = op_two(num2, num3) # Sets a variable to do 2nd number (* or /) the 3rd number
            
            if op1 == "/" and pemdas == 0: # Divide by 0!!
                pemdas = 100
                
            pemdas2 = op_one(num1, pemdas) # Then combines pemdas to 1st number
            total = op_three(pemdas2, num4) # Then combines pemdas 2 to the 4th number
    
    super_count = super_count + 1
   
    if total == 10: # If the total is 10 then it prints what combo got it and breaks out of while loop
        break

if para_total == 10:
    print("The solution is: (" + str(para1) + op1 + str(para2) + ")" + op2 + str(after_para_num1) + op3 + str(after_para_num2) + " = 10 ")
elif para_total_3num == 10:
    print("The solution is: (" + str(para1) + op1 + str(para2) + op2 + str(para3) + ")" + op3 + str(after_para_num1) + " = 10")
elif total == 10:
    print("The solution is: " + str(num1) + op1 + str(num2) + op2 + str(num3) + op3 + str(num4) + " = 10")
elif para_total_b4 == 10:
    print("The solution is: " + str(after_para_num1) + op3 + str(after_para_num2) + op2 + "(" + str(para1) + op1 + str(para2) + ") = 10")
else:
    print("welp didnt work")
