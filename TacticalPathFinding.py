#Vlad Vitalaru
#CS 450 
#HW 5 Tactical Path Finding

import sys
import heapq as heap
import math
import time 
totaltime = time.time_ns()


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
        
''' Matrix class holding grid & Dijkstras algorithm'''
class Matrix():
    def __init__(self, grid, start):
        self.grid = grid        #tile map
        self.start = start      #start index
        self.visited = []       #visited array
        self.pq = []            #priority que
        self.final = 0          #final path score
        self.Dijkstras()        #run Dijkstras
        self.Display(self.grid) #print final tile map
        print(f'\nTotal Cost: {self.final}')
        
    '''Main Dijkstras loop pushing and popping from priority que'''
    def Dijkstras(self):
        #Add starting node to visited
        self.visited.append(self.grid[self.start[0]][self.start[1]]) 
        
        #Set start node totalCost to 0
        self.grid[self.start[0]][self.start[1]].totalCost = 0   

        #Push start node onto heap
        heap.heappush(self.pq, self.grid[self.start[0]][self.start[1]])  
        
        while self.pq:
            #Pop node with smallest totalCost off que
            next = heap.heappop(self.pq) 
            
            #if we have found destination
            if next.tile == "2": 
                self.final = next.totalCost
                cursor = next.prev  #loop backwards through prev for shortest path
                while cursor.prev:  
                    if cursor.tile == "0": 
                        return
                    else:
                        cursor.tile = "*"
                        cursor = cursor.prev
            
            #Grab neighboring nodes        
            self.Neighbors(next.row, next.col)
            
        return 
        
    '''Checks neighboring nodes of row, col, adds to visited list & pushes to priority queue'''
    def Neighbors(self, row, col):
        original = (row, col)
        #totalCost of currentNode        
        originalCost = self.grid[original[0]][original[1]].totalCost 
        #for row value
        for rowAdd in range(-1, 2): 
            newRow = row + rowAdd
            
            if newRow >= 0 and newRow <= len(self.grid)-1: 
                #for col value
                for colAdd in range(-1, 2): 
                    newCol = col + colAdd
                    
                    #if index within boundary
                    if newCol >= 0 and newCol <= len(self.grid)-1: 
                        
                        #if at the current node, skip
                        if newCol == col and newRow == row:
                            continue
                        
                        #if we have already visited, skip
                        elif self.grid[newRow][newCol] in self.visited: 
                            continue
                        
                        #if other player occupies tile, skip
                        elif self.grid[newRow][newCol].cost < 0: 
                            continue
                        
                        #if neighbor at NW or SE nodes, 1.5x neighbor cost 
                        elif (rowAdd and colAdd == -1) or (rowAdd and colAdd == 1): 
                            newCost = originalCost + (self.grid[newRow][newCol].cost * 1.5)
                            
                        #if neighbor at SW or NE nodes, 1.5x neighbor cost 
                        elif (rowAdd == 1 and colAdd == -1) or (rowAdd == - 1 and colAdd == 1):  
                            newCost = originalCost + (self.grid[newRow][newCol].cost * 1.5)
                            
                        else: #Else, newCost is original + neighbor cost
                            newCost = originalCost + self.grid[newRow][newCol].cost
                        
                        #Update total cost for neighbor nodes
                        self.grid[newRow][newCol].totalCost = newCost
                        
                        #Set current node as previous for neighbor nodes
                        self.grid[newRow][newCol].prev = self.grid[original[0]][original[1]]
                        
                        #Add to visited 
                        self.visited.append(self.grid[newRow][newCol])
                         
                        #push tile onto heap
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
    y = -1    #row
    x = -1    #col
    
    #Loop through STDIN
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