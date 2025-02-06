import math


def main():
    exp = expressionInput()
    ans = calculation(exp)
    while True:
        
        e = input("Would you like to continue? Y/N ")
        if e.upper() == "Y":
            exp = expressionInput()
            ans = calculation(exp)
        elif e.upper() == "N":
            print("Quitting...")
            quit()
        else:
            print("Invalid entry")
            

    

def expressionInput():
    temp = ''
    mathlist = []
    mathexp = input("Please input your mathematical expression: ")
    val = True
    
    for i, elem in enumerate(mathexp):
        elem = elem.lower()
        
        if val: #checks if math operator is attempting to be used before an actual number or expression
                #only runs on first pass of loop

            if elem in ["+", "/", "x", "*", ")"]:
                print("You cannot use a math operator before an input number, please enter a valid expression.")
                return expressionInput()
            else:
                val = False
        
        if elem == " ": #skip iteration if there is a space
            continue  
    

        #ensures entered character is a digit, or a math operator
        if elem not in ["+", "-", "/", "x", "*", "(", ")"] and not elem.isdigit():
            print("Invalid character detected. Please enter a new expression.")
            return expressionInput()
        

        #if block to sort a subtraction expression into negative number, I.E [4,-,2] becomes [4,-2]
        if elem == "-":
            if temp:
                mathlist.append(temp)  # Append previous number
            temp = "-"  # Start new negative number
        elif elem.isdigit():
            temp += elem
        else:
            if temp:
                mathlist.append(temp)
                temp = ""
            mathlist.append(elem)
    
    if temp: #if any elem is missed, add to end of expression list
        mathlist.append(temp)
    
    #ensures no expression can end with a math operator, while loop would be unable to parse

    if mathlist[-1] in ["+", "-", "/", "x", "*", "(", ")"]:
        print("You cannot end an expression with a math operator. Please enter a valid expression.")
        return expressionInput()
    
    print(mathlist)
    return mathlist #returns math expression with correct notation ("2 - 4 * 10" becomes [2,-4,*,10])



def calculation(toBeCalculated):
    finalval = 0
    numBool = False
    #use recursion for parentheses statements, then solve the rest of the equation
   

    while len(toBeCalculated) > 0:
        if len(toBeCalculated) == 1:
            toBeCalculated[0] = int(toBeCalculated[0])
            finalval += toBeCalculated[0]
            print(toBeCalculated)
            toBeCalculated.pop()
            print(toBeCalculated)
        

        elif toBeCalculated[0] not in ["+", "-", "/", "x", "*", "(", ")"] and toBeCalculated[1] not in ["+","/", "x", "*", "(", ")"]: #
            
            #in the case where the next two elem in the list do not have a math operator
            #I.E. [-2, 4] = 2

            toBeCalculated[0] = int(toBeCalculated[0])
            toBeCalculated[1] = int(toBeCalculated[1])
            print(toBeCalculated[0], toBeCalculated[1])
            finalval += (toBeCalculated[0] + toBeCalculated[1])
            del toBeCalculated[0 : 2]
            print(toBeCalculated)
            numBool = True

        elif toBeCalculated[0] in ["+","/", "x", "*", "(", ")"] and toBeCalculated[1] not in ["+", "-", "/", "x", "*", "(", ")"]:

            #this case handles where the first elem is a math operator, this usually runs after the first pass of the 
            #while loop, when the first 3 term polynomial is calculated and subsequently removed from the list.
            #I.E. numBool = True [+, 4] = finalval += 4

            toBeCalculated[1] = int(toBeCalculated[1])
            if toBeCalculated[0] == "/":
                finalval /= toBeCalculated[1]

            elif toBeCalculated[0] == "x" or toBeCalculated[0] == "*":
                finalval *= toBeCalculated[1]

            elif toBeCalculated[0] == "+":
                finalval += toBeCalculated[1]

            else:
                print("balls")
            
            del toBeCalculated[0 : 2]
            print(toBeCalculated)
            numBool = True
        
        if numBool == False:

            #only runs on the first pass if necessary, checks if any value has been calculated, if not, sets the 
            #finalnum equal to toBeCalculated[0] and pops it from list. This will then allow the while loop to continue
            #parsing the rest of the list using the above elif functions (IE where a math operator falls first or
            #if there are two back to back digits (if a negative number is being added))

            toBeCalculated[0] = int(toBeCalculated[0])
            finalval += toBeCalculated[0]
            toBeCalculated.pop(0)
            numBool = True
        
        
        

        
    print(f"Answer: {finalval}")     
    return finalval



if __name__ == '__main__':
    main()