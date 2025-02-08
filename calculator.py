import math


def main():
    exp = expressionSplitterandInput()
    #sortExp = PEMDASsort(exp)
    ans = calculation(exp)
    print(f"Answer: {ans}")
    while True:
        
        e = input("Would you like to continue? Y/N ")
        if e.upper() == "Y":
            exp = expressionSplitterandInput()
            ans = calculation(exp)
            print(f"Answer: {ans}")
        elif e.upper() == "N":
            print("Quitting...")
            quit()
        else:
            print("Invalid entry")
            

def expressionSplitter(parans):
    mathlist = []
    for elem in parans:
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
    
    return mathlist

def expressionSplitterandInput():
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
                return expressionSplitterandInput()
            else:
                val = False
        
        if elem == " ": #skip iteration if there is a space
            continue  
    

        #ensures entered character is a digit, or a math operator
        if elem not in ["+", "-", "/", "x", "*", "(", ")"] and not elem.isdigit():
            print("Invalid character detected. Please enter a new expression.")
            return expressionSplitterandInput()
        
        
        #if block to sort a subtraction expression into negative number, I.E "4 - 2" becomes [4,-2]
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

    if mathlist[-1] in ["+", "-", "/", "x", "*"]:
        print("You cannot end an expression with a math operator. Please enter a valid expression.")
        return expressionSplitterandInput()
    
    
        
            
            

    return mathlist #returns math expression with correct notation ("2 - 4 * 10" becomes [2,-4,*,10])



def calculation(toBeCalculated):
    finalval = 0
    numBool = False
    #use recursion for parentheses statements, then solve the rest of the equation
    
    """
    if elem[0] == "(":
                print("Parentheses detected")
                temp = []
                temp.append(toBeCalculated.pop(0))
                while toBeCalculated[0] != ")":
                    temp.append(toBeCalculated.pop(0))
                temp.append(toBeCalculated.pop(0))
                print(temp)
                temp.pop(0)
                temp.pop(-1)
                print(temp)
                temp = calculation(temp)
                toBeCalculated.insert(0, temp)
                print(toBeCalculated)
                continue """

    while len(toBeCalculated) > 0:

        #this block of code is used to determine if there is a parentheses statement in the list, if so, it will calculate that value first
        #and then insert it back into the list to be calculated as an integer. This will allow the while loop to continue parsing the list

        #print("toBeCalculated: ", toBeCalculated)
        if toBeCalculated[0]== "(":
            #print(toBeCalculated[0])
            i = 0
            j = 1
            while toBeCalculated[j] != ")":
                j += 1
            paranVal = toBeCalculated[i+1:j]
            del toBeCalculated[i:j+1]
            print("ParanVal b4 calc", paranVal)
            paranVal = calculation(paranVal)
            
            #print(paranVal)
            toBeCalculated.insert(i, paranVal)
            print(toBeCalculated)
            continue
        
        #this block of code is used to determine if there is a parentheses statement in the list AFTER the first two elements, IE 10 + (2 * 4)

        if len(toBeCalculated) >= 3 and (toBeCalculated[2] == "(" or toBeCalculated[1] == "("):
            #print(toBeCalculated[0])
            print("doubleBalls")
            if toBeCalculated[2] == "(":
                i = 2
                j = 3
            else:
                i = 1   
                j = 2

            while toBeCalculated[j] != ")":
                j += 1
            paranVal = toBeCalculated[i+1:j]
            del toBeCalculated[i:j+1]
            #print("ParanVal b4 calc", paranVal)
            paranVal = calculation(paranVal)
            
            #print(paranVal)
            toBeCalculated.insert(i, paranVal)
            #print(toBeCalculated)
            continue

   
        #if the list is 1 elem long, it is the final value, add it to the finalval and return the answer
        if len(toBeCalculated) == 1:
            finalval += toBeCalculated[0]
            #print("Breaking")
            break
            
            
    
        
    
        elif toBeCalculated[0] not in ["+", "-", "/", "x", "*"] and toBeCalculated[1] not in ["+","-","/", "x", "*"]: #
            
            #in the case where the next two elem in the list do not have a math operator
            #I.E. [-2, 4] = 2
            toBeCalculated[0] = int(toBeCalculated[0])
            toBeCalculated[1] = int(toBeCalculated[1])
            #print(finalval)
            print(toBeCalculated[0], toBeCalculated[1])
            finalval += (toBeCalculated[0] + toBeCalculated[1])
            print(finalval)
            del toBeCalculated[0 : 2]
            print("Two Elem" ,toBeCalculated) 
            numBool = True

        elif toBeCalculated[0] in ["-","+","/", "x", "*"] and toBeCalculated[1] not in ["+", "-", "/", "x", "*"]:

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

            elif toBeCalculated[0] == "-": 
                finalval -= toBeCalculated[1]

            else:
                print("balls")
            
            del toBeCalculated[0 : 2]
            print("After + x: ", toBeCalculated)
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
        
        
        

             
    return finalval



if __name__ == '__main__':
    main()