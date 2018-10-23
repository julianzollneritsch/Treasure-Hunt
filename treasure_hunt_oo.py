'''
This module solves the Treasure Hunt with an object oriented programming approach.
Input is a space separated 5x5 matrix. Output is a sequence of coordinates,
also space separated, that finds the treasure.
by Julian Zollneritsch
'''

class TreasureHunt:
    '''
    This class provides the necessary variables and functions. An instance can
    be created with an user defined starting point within the table.
    '''
    def __init__(self, start_x, start_y):
        '''To initialize the class, starting point coordinates have to be provided.
        An empty matrix, solution list and the range is also created.
        '''
        self.ma = []
        self.range = 5
        self.solution = []
        self.start_x = start_x
        self.start_y = start_y
    
    def get_matrix(self):
        '''This function creates the table where the treasure is hidden. 
        Argument is only the instance, return value is the table the user provided.
        '''        
        for n in range(self.range): #dimension of the table
            line = [int(clue) for clue in input().split()] #save space separated numbers in list (line), doesn't check for correct input
            self.ma.append(line) #save list (line) in table
        
        return(self.ma)
    
    def find_treasure(self):
        '''This function looks for the new clue. If the treasure is found the 
        solution is printed. Otherwise it looks for the next clue.
        Argument is only the instance'''
        while True:        
            clue1 = int(str(self.ma[self.start_x-1][self.start_y-1])[0]) #Save new line coordinate
            clue2 = int(str(self.ma[self.start_x-1][self.start_y-1])[1]) #Save new row coordinate
            self.solution.append([self.start_x, self.start_y]) #CSave coordinates in solution list
            if self.start_x == clue1 and self.start_y == clue2:  #If the treasure was found...
                for clue in self.solution: #...the solution is printed...
                    print(*clue)
                break #...and the loop is exited
            elif len(self.solution) == 25: #If not, it is checked if already all clues were visited...
                print("NO TREASURE") #...NO TREASURE is printed...
                break #...and the loop is exited
            else:
                self.start_x = clue1 #If the treasure wasn't found and still clues are missing...
                self.start_y = clue2 #...the coordinates reset and the loop starts over

def main():
    '''
    This is the main function of the module.
    '''
    ma = TreasureHunt(1, 1) #Create instance
    ma.get_matrix() #Create table
    ma.find_treasure() #Find treasure...or not.
    
if __name__ == "__main__":
    main()
        