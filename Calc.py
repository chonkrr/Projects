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
            

    #test

def expressionInput():
    temp = ''
    mathlist = []
    mathexp = input("Please input your mathematical expression: ")
    val = True
    
    for i, elem in enumerate(mathexp):
        elem = elem.lower()
        
        if val:
            if elem in ["+", "/", "x", "*", ")"]:
                print("You cannot use a math operator before an input number, please enter a valid expression.")
                return expressionInput()
            else:
                val = False
        
        if elem == " ":
            continue  
        
        if elem not in ["+", "-", "/", "x", "*", "(", ")"] and not elem.isdigit():
            print("Invalid character detected. Please enter a new expression.")
            return expressionInput()
        
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
    
    if temp:
        mathlist.append(temp)
    
    if mathlist[-1] in ["+", "-", "/", "x", "*", "(", ")"]:
        print("You cannot end an expression with a math operator. Please enter a valid expression.")
        return expressionInput()
    
    print(mathlist)
    return mathlist 



def calculation(expList):
    finalval = 0
    count = 0
    firstnum = 0
    firstop = None

    #use recursion for parentheses statements, then solve the rest of the equation

    while len(expList) > 0:
        if len(expList) == 1:
            expList[0] = int(expList[0])
            finalval += expList[0]
            print(expList)
            expList.pop()
            print(expList)

        elif expList[0] not in ["+", "-", "/", "x", "*", "(", ")"] and expList[1] not in ["+","/", "x", "*", "(", ")"]:
            expList[0] = int(expList[0])
            expList[1] = int(expList[1])
            print(expList[0], expList[1])
            finalval += (expList[0] + expList[1])
            del expList[0 : 2]
            print(expList)

        elif expList[0] in ["+","/", "x", "*", "(", ")"] and expList[1] not in ["+", "-", "/", "x", "*", "(", ")"]:
            expList[1] = int(expList[1])
            if expList[0] == "/":
                finalval /= expList[1]

            elif expList[0] == "x" or expList[0] == "*":
                finalval *= expList[1]

            elif expList[0] == "+":
                finalval += expList[1]

            else:
                print("balls")
            
            del expList[0 : 2]
            print(expList)

        
        
        

        
    print(f"Answer: {finalval}")     
    return finalval



if __name__ == '__main__':
    main()
