'''
This module solves the Treasure Hunt with a functional programming approach.
Input is a space separated 5x5 matrix. Output is a sequence of coordinates,
also space separated, that finds the treasure.
by Julian Zollneritsch
'''

def get_matrix():
    '''This function creates the Treasure Hunt Table by asking for 5 lines.'''
    
    matrix = [] #set up the table
    
    for n in range(5): #set up the dimension of the table
        line = [int(clue) for clue in input().split()] #save space separated numbers in list (line), doesn't check for correct input
        matrix.append(line) #save list (line) in table
        
    return(matrix)
    
def get_next_step(ma, x, y, solution):
    '''This function looks for the new clue. If the treasure is found, the 
    solution is printed. Otherwise it looks through recursion for the next clue.
    The arguments are the table, the first coordinate, the second coordinate
    and the solution list.'''
    
    clue1 = int(str(ma[x-1][y-1])[0]) #Save new line coordinate
    clue2 = int(str(ma[x-1][y-1])[1]) #Save new row coordinate
    solution.append([x, y]) #Save coordinates in solution list
    if check_treasure([x, y], [clue1, clue2]): #If the treasure was found...
        for clue in solution: #...the solution is printed
            print(*clue)
    elif len(solution) == 25: #If not, it is checked if already all clues were visited
        print("NO TREASURE")
    else: #If the treasure wasn't found and still clues are missing, the function is called again
        get_next_step(ma, clue1, clue2, solution)
    
def check_treasure(coor, clue):
    '''This function checks whether the current clue is already the treasure. 
    The arguments are the position in the table and the clue.'''
    if coor == clue: #If the position equaled the clue, the treasure is found
        return True
    
if __name__ == "__main__":
    get_next_step(get_matrix(), 1, 1, [])
    
# tester_matrix = [[34, 21, 32, 41, 25], [14, 42, 43, 14, 31], [54, 45, 52, 42, 23], [33, 15, 51, 31, 35], [21, 52, 33, 13, 23]]
    