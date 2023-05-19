def arithmetic_arranger(problems, answerYes = False):
    # Checking for correct input
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    
    array = [None] * 3
    for i in range(3):
        array[i] = [None] * len(problems)

    for i in range(len(problems)):
        equation = problems[i]
        if equation == True:
            answerYes = True
            break

        firstOperand, operator, secondOperand = equation.split()

        if not (operator == '+' or operator == '-'):
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        
        if not firstOperand.isdigit() or not secondOperand.isdigit():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
        
        if len(firstOperand) > 4 or len(secondOperand) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
        
        array[0][i] = firstOperand
        array[1][i] = operator
        array[2][i] = secondOperand
    
    #print(array)
    # Main logic
    resultarray = []
    if answerYes:

        for i in range(len(problems)):
            if array[1][i] == '+':
                result = int(array[0][i]) + int(array[2][i])
            else:
                result = int(array[0][i]) - int(array[2][i])
            
            resultarray.append(result)

    #print(resultarray)
    resultString1 = ''
    resultString2 = ''
    resultString3 = ''
    resultString4 = ''
    for i in range(len(array[0])):
        if len(array[0][i]) == len(array[2][i]):
            lenSpaceFirst = 2
            lenSpaceSecond = 1
        lenSpaceFirst = 2 if len(array[0][i]) > len(array[2][i]) else len(array[2][i]) - len(array[0][i]) + 2
        lenSpaceSecond = len(array[0][i]) - len(array[2][i]) + 1 if len(array[0][i]) > len(array[2][i]) else 1
        
        
        if i < (len(array[0]) - 1):
            resultString1 += ' ' * lenSpaceFirst + array[0][i] + '    '
            blockLength = len(' ' * lenSpaceFirst + array[0][i])
            resultString2 += array[1][i] + (' ' * lenSpaceSecond) + array[2][i] + '    '
            resultString3 += '-' * blockLength + '    ' 

            if answerYes:
                resultString4 +=  ' ' * (blockLength - len(str(resultarray[i]) )) + str(resultarray[i]) + '    '

        else:
            resultString1 += ' ' * lenSpaceFirst + array[0][i]
            resultString2 += array[1][i] + (' ' * lenSpaceSecond) + array[2][i]
            blockLength = len(' ' * lenSpaceFirst + array[0][i])
            resultString3 += '-' * (len(' ' * lenSpaceFirst + array[0][i]))
            if answerYes:
                resultString4 +=  ' ' * (blockLength - len(str(resultarray[i]) )) + str(resultarray[i])
        

    arranged_problems = resultString1 + '\n' + resultString2 + '\n' + resultString3
    arranged_problems += '\n' + resultString4  if answerYes else ''

    #print(arranged_problems)
    return arranged_problems

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "3 - 3"], True))