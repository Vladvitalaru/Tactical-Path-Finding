#Vlad Vitalaru
#CS 450 
#HW 5 Tactical Path Finding

import sys
import heapq as heap
import math
import time 
totaltime = time.time_ns()


'''
Road: '.' cost: 1
Grass: ',' cost: 2
Rocks: 'o' cost: 3
Walls: '=', cost: 50
Character: '0', '1', '2', or '3'
('0' represents the controlled character, '1' represents a friendly character,
'2' represents the target character, and '3' represents a non-target enemy character)
(two humans cannot be in the same tile, so no cost is listed)

Additionally, if a player moves diagonally, it counts as 1.5x the number of movement points
as the tile type indicates (so moving diagonally into rocks costs 4.5 points).

You will read in the input and determine the shortest path between the character '0' and the character '2'. 
The final square must be the closest adjacent square to the 2 (not the 2 itself, two characters may not occupy the same tile).
'''

''' Node class holding information about each tile '''
class Node():
    def __init__(self, tile, cost, row, col):
        self.tile = tile            #tile type
        self.cost = cost            #tile type cost
        self.totalCost = math.inf   #initial totalCost
        self.prev = None            #Previous node in path
        self.row = row              #row index
        self.col = col              #column index
        
    def __lt__(self, next):
        return self.totalCost < next.totalCost
        
''' Matrix class holding grid & Dijksras algorithm'''
class Matrix():
    def __init__(self, grid, start):
        self.grid = grid        #tile map
        self.start = start      #start index
        self.visited = []       #visited array
        self.pq = []            #priority que
        self.final = 0          #final path score
        self.Dijksras()         #run Dijkras
        self.Display(self.grid) #print final tile map
        print(f'\nTotal Cost: {self.final}')
        
        
    def Dijksras(self):
        
        self.visited.append(self.grid[self.start[0]][self.start[1]]) #Add starting node to visited
        
        self.grid[self.start[0]][self.start[1]].totalCost = 0        #Set start node totalCost to 0

        heap.heappush(self.pq, self.grid[self.start[0]][self.start[1]])  #Push start node onto heap
        
        while self.pq:
            next = heap.heappop(self.pq)
                
            if next.tile == "2": #if we have found destination
                self.final = next.totalCost
                cursor = next.prev
                while cursor.prev:  #loop backwards through prev for path
                    if cursor.tile == "0": 
                        return
                    else:
                        cursor.tile = "*"
                        cursor = cursor.prev
                    
                   
            self.Neighbors(next.row, next.col)
        return 
        
    def Neighbors(self, row, col):
        original = (row, col)
                
        originalCost = self.grid[original[0]][original[1]].totalCost #totalCost of currentNode
        
        for rowAdd in range(-1, 2): #for rows around
            newRow = row + rowAdd
            
            if newRow >= 0 and newRow <= len(self.grid)-1: #for cols around
                
                for colAdd in range(-1, 2):
                    newCol = col + colAdd
                    
                    if newCol >= 0 and newCol <= len(self.grid)-1: #if index within boundary
                        if newCol == col and newRow == row:
                            continue
                        
                        if self.grid[newRow][newCol] in self.visited: #if we have already visited, move on
                            continue
                        
                        if self.grid[newRow][newCol].cost < 0: #If other player occupies tile, skip
                            continue
                                                
                        if (rowAdd and colAdd == -1) or (rowAdd and colAdd == 1): #if neighbor at NW or SE nodes
                            newCost = originalCost + (self.grid[newRow][newCol].cost * 1.5)
                            
                        elif (rowAdd == 1 and colAdd == -1) or (rowAdd == - 1 and colAdd == 1): #if neighbor at SW or NE nodes 
                            newCost = originalCost + (self.grid[newRow][newCol].cost * 1.5)
                            
                        else:
                            newCost = originalCost + self.grid[newRow][newCol].cost
                        
                        self.grid[newRow][newCol].totalCost = newCost
                        self.grid[newRow][newCol].prev = self.grid[original[0]][original[1]]
                        
                        self.visited.append(self.grid[newRow][newCol]) #Add to visited 
                        heap.heappush(self.pq,self.grid[newRow][newCol]) #push tile onto heap
        return
        
    ''' Print out the Matrix to STDOUT '''
    def Display(self, grid):
        for x in grid:
            print()
            for y in x:
                print(y.tile, end =" ")

def main():
    tiles = {
        "." : 1, #Road
        ",": 2,  #Grass
        "o": 3,  #Rocks
        "=": 50, #Wall
        "0": 0,  #Start
        "1": -1, #Friendly
        "2": 0,  #Destination
        "3": -1, #Enemy
        }
    
    grid = [] #Grid 
    y = -1 #row
    x = -1 #col
    
    for line in sys.stdin.readlines():
        y += 1
        row = []
        for tile in line.split():
            x += 1
            if tile == "0":
                start = (y, x) #index of start (row, col)
            elif tile == "2": 
                destination = (y, x) #index of destination (row, col)
                
            node = Node(tile, tiles[tile], y, x)
            row.append(node)
        
        grid.append(row)
        x = -1

    Matrix(grid, start)
    time_taken_in_microseconds = ( time.time_ns() - totaltime ) / 1000.0 
    print(f"Time taken in microseconds: {time_taken_in_microseconds} ", end = " ")
if __name__ == '__main__':
    main()