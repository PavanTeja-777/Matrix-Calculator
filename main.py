"""
                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                            Copyrights © by 22233-CS-004
                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
'''
                                    ! This Matrix program is developed by using 2D list
'''

from time import sleep as stop                      # we are importing sleep form time because we want user that it is calculating.......
from time import strftime as currentime             # For getting the current time for wishing the user
from os.path import exists                          # For better user experience
from os import system as cmd                        # For better user experience


def wishMe():
    """ wishes user according to time """

    hour = int(currentime('%H'))
 
    if hour >= 0 and hour < 6:
        wish = f"It's {hour},Earrly morning work!!"

    elif hour >= 6 and hour < 12:
        wish = f'Its {hour},Good Morning!'
  
    elif hour >= 12 and hour < 15:
        wish = f"It's {hour},Good Afternoon!"

    elif hour >= 20:
        wish = f"It's {hour},Goto sleep!!!"

    else:
        wish = f"It's {hour},Good Evening!"

    print(wish)
    print("Welcome to Matrix Calculator")

def changeToInt(matrixx):
    ''' Changes the elements of matrix into int '''
    for i in range(len(matrixx)):                   # Gives ith row value
        for j in range(len(matrixx[i])):            # Gives jth column value
            matrixx[i][j] = int(matrixx[i][j])      # Changes to int

def changeToStr(matrixx):
    ''' Changes the elements of matrix into str
        For a better look we are modifiying the str    
    '''
    for i in range(len(matrixx)):                   # Gives ith row value
        for j in range(len(matrixx[i])):            # Gives jth column value
            ele = str(matrixx[i][j])                # Changes to str
            if '-' in ele:
                if len(ele) == 1:
                    temp = "-00" + str(abs(int(ele)))

                elif len(ele) == 2:
                    ele = "-0" + str(abs(int(ele)))

            else:
                if len(ele) == 1:
                    ele = "00"+ele

                elif len(ele) == 2:
                    ele = "0" + ele 

            matrixx[i][j] = ele

def takeMatrix(_):
    '''Takes Matrix input from the user

        Args:
        _ (str) : Matrix Name
    '''
    rows = int(input(f"Enter the number of rows for {_} matrix: "))

    columns = int(input(f"Enter the number of columns for {_} matrix: "))

    matrix = []                                     # Initialize an empty 2D list
    for i in range(rows):                           # Ask the user for each element in the matrix
        row = []
        for j in range(columns):
            element = input(f"Enter the element at ({i+1},{j+1}): ")
            row.append(element)
        matrix.append(row)

    try:
        changeToInt(matrix)                         # For checking the user inputed corrcet or not

    except:
        print("INVALID INPUT")
        takeMatrix(_)

    changeToInt(matrix)                             # We are changing to int for doing the calculations
    print(f"Done for the {_} matrix\n")
    return matrix

def mat_3(a, operator, b, r):
    '''Prints the matrixes with the given operator
    
    Args:
        a (2D_list): 1st matrix
        operator (str): perforemd operation
        b (2D_list): 2st matrix
        r (2D_list): result matrix
    '''
    changeToStr(a)
    changeToStr(b)
    changeToStr(r)
    for row in a:
        for element in row:
            print(f"{element}    ",end='')
        print()
    
    print("\n"+operator+"\n")

    for row in b:
        for element in row:
            print(f"{element}    ",end='')
        print()
    
    print("\n=\n")

    for row in r:
        for element in row:
            print(f"{element}    ",end='')
        print()
    changeToInt(a)
    changeToInt(b)

def matAdd(a, b):
    '''This funcion add the given matrix and stores into res matrix

    Args:
        a (2D_list): 1st matrix
        b (2D_list): 2st matrix
    '''
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Error: The matrices have different dimensions and cannot be added.")

    else:
        result = [[0 for _ in range(len(b[0]))]for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                result[i][j] = a[i][j] + b[i][j]

    return result

def matSub(a, b):
    '''
    This function subtracts the given matrix and stores into res matrix

    Args:
        a (2D_List): one matrix
        b (2D_List): another matrix
    '''
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Error: The matrices have different dimensions and cannot be added.")

    else:
        result = [[0 for _ in range(len(b[0]))]for _ in range(len(a))]

        opti = int(input("Want to do\n\t1)A-B\n\t2)B-A\n>>>"))

        if opti == 1:
            for i in range(len(a)):
                for j in range(len(a[0])):
                    result[i][j] = a[i][j] - b[i][j]

        elif opti == 2:
            for i in range(len(a)):
                for j in range(len(a[0])):
                    result[i][j] = b[i][j] - a[i][j]
    return result

def matMul(a, b):
    '''This funcion multiply the given matrix and stores into res matrix

    Args:
        a (2D_list): 1st matrix
        b (2D_list): 2st matrix
    '''
    # For matrix multiplication the number of columns in matrix 'a' must match the number of rows in matrix 'b'
    if len(a[0]) != len(b):
        print("ERROR: Invalid matrix dimensions for multiplication")
        return

    result = [[0 for _ in range(len(b[0]))]for _ in range(len(a))]

    
    for i in range(len(a)):                        # Loop through rows of matrix 'a'
        for j in range(len(b[0])):                 # Loop through columns of matrix 'b'
            result[i][j] = 0                       # Initialize the element in result matrix as 0
            for k in range(len(a[0])):             # Loop through columns of matrix 'a' and rows of matrix 'b'
                result[i][j] += a[i][k] * b[k][j]  # Multiply the corresponding elements and add to the result
    return result

def bye():
    '''A User Frienly Message for Quiting'''
    wantToExit = input("Do you want to exit(Y/N): ")
    if wantToExit.lower() == "y":
        print("See you soon.....")
        stop(2)
        cmd("taskkill /im cmd.exe /f")             # To stop the code ,If it's is running in Command Prompt
        cmd("taskkill /im powershell.exe /f")      # To stop the code ,If it's is running in Powershell
        exit()                                     # If the above line doesn't execute

    elif wantToExit.lower() == "n":
        cmd("cls")                                 # If the user wants to countinue then it clears the console

    return

def start():
    '''Starts the program'''
    global lastInput
    lastInput = "n"

    if exists("storeValues.txt"):
        lastInput = input("Want to take the matrix values from previos one___")

        if lastInput.lower() == "y":
            f = open("storeValues.txt", "r")
            a = f.readlines()
            A_matrix = eval(a[0])
            B_matrix = eval(a[1])

    if lastInput !="y":
        A_matrix, B_matrix = takeMatrix("A"), takeMatrix("B")
        f = open("storeValues.txt", "w")
        f.write(str(A_matrix)+"\n"+str(B_matrix))
        f.close()

    stop(2)

    cmd("cls")

    oper = input("Enter the operation should be done (+,-,* & Q for quit)\n>>>")

    if oper == "+":
        result_matrix = matAdd(A_matrix, B_matrix)
        mat_3(A_matrix, oper, B_matrix, result_matrix)

    elif oper == "-":
        result_matrix = matSub(A_matrix, B_matrix)
        mat_3(A_matrix, oper, B_matrix, result_matrix)

    elif oper == "*" or oper.lower() == "x":
        result_matrix = matMul(A_matrix, B_matrix)
        mat_3(A_matrix, oper, B_matrix, result_matrix)

    elif oper == "/":
        print("Rey thu pas yedhava matrix lo division undhadhu (Hey idiot there will be no division in matrix)")
    
    else:
        print("Invaild Input")

    bye()

    start()

cmd("cls")
wishMe()
start()
