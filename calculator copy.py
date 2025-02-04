import dudraw
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
    minusVal = False
    for elem in mathexp:
        elem = elem.lower()
        if val == True:
            if elem in ["+", "/", "x", "*"]: 
                print("You cannot use a math operator before an input number, please enter a valid expression.")
                return expressionInput()
            else: 
                val = False

        if elem == " ":
            continue 

        if elem not in ["+", "-", "/", "x", "*", "(", ")"] and not elem.isdigit():
            print("Invalid character detected. Please enter a new expression.")
            return expressionInput()
        
        else:
            if elem == "-":
                mathlist.append(temp)
                temp = ''
                temp += elem
            if elem.isdigit() :
                temp += elem

            else:
                if temp:  
                    mathlist.append(temp) 
                mathlist.append(elem)
                temp = ''  
    
    print(mathlist)
    return mathlist
            

        

        
        
    if not any(operator in mathlist for operator in ["+", "-", "/", "x", "*", "(", ")"]):
        print(f"No math operator present, your answer is {mathlist[0]}")
        return expressionInput()


    
    print(mathlist)
    return mathlist

def calculation(expList):
    finalval = 0
    count = 0
    firstnum = 0
    firstop = None
    for elem in expList:
        if elem.isdigit():
            print(elem)
            temp = int(elem)
        else:
            print(elem)
            firstop = elem
            

        count += 1

        if (count % 3 != 0) and firstop == None:
            firstnum = int(temp)
        
        if count % 3 == 0:
        
            if firstop == "+":
                if finalval != 0:
                    finalval += temp
                else:
                    finaltemp = firstnum + temp
                    finalval += finaltemp
            if firstop == "-":
                if finalval != 0:
                    finalval -= temp
                else:
                    finaltemp = firstnum + temp
                    finalval += finaltemp
            if firstop == "/":
                if finalval != 0:
                    finalval /= temp
                else:
                    finaltemp = firstnum / temp
                    finalval += finaltemp
            if firstop == "x" or firstop == "*":
                if finalval != 0:
                    finalval *= temp
                else:
                    finaltemp = firstnum * temp
                    finalval += finaltemp
            count += 1
            firstnum = 0
            firstop = None

    print(f"Answer: {finalval}")     
    return finalval



if __name__ == '__main__':
    main()