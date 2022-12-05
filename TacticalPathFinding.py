#Vlad Vitalaru
#CS 450 
#HW 5 Tactical Path Finding

import sys
import heapq as heap
import math
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

The priority queue / heap in Python is called "heapq"
'''

''' Node class holding information about each tile '''
class Node():
    def __init__(self, tile, cost, row, col):
        self.tile = tile            #tile type
        self.cost = cost            #tile type cost
        self.prev = None            #Previous node in path
        self.totalCost = math.inf   #initial totalCost
        self.row = row              #row index
        self.col = col              #column index
        
    def __lt__(self, next):
        return self.cost < next.cost
        
''' Matrix class holding grid & Dijksras algorithm'''
class Matrix():
    def __init__(self, grid, start):
        self.grid = grid
        self.start = start
        # self.destination = destination
        self.visited = []   #visited array
        self.Dijksras()
        
        
    def Dijksras(self):
        
        self.visited.append(self.start) #Add starting node to visited
        self.grid[self.start[0]][self.start[1]].totalCost = 0       #Set start node totalCost to 0
        
        pq = []
        heap.heappush(pq, self.grid[self.start[0]][self.start[1]])  #Push start node onto heap
        
        # print(self.grid[start[0]][start[1]].totalCost)
        # visited.add(self.grid[start[0]][start[1]])
        # print(visited[0].tile)
        # neighbors = self.neighbors(self.grid, start[0], start[1])
        
        # neighbors = self.neighbors(self.grid, 3, 5)
        while pq:
            next = heap.heappop(pq)
            self.visited.append(next)
            
            neighbors = self.Neighbors(next.row, next.col)
        
            print()
            for x in neighbors:
                print(x.tile, end=" ")
            print()
        
    def Neighbors(self, row, col):
        original = (row, col)
        print(original)
        print()
        result = []
        for rowAdd in range(-1, 2):
            newRow = row + rowAdd
            
            if newRow >= 0 and newRow <= len(self.grid)-1:
                for colAdd in range(-1, 2):
                    newCol = col + colAdd
                    
                    if newCol >= 0 and newCol <= len(self.grid)-1:
                        if newCol == col and newRow == row:
                            continue
                        
                        if self.grid[newRow][newCol] in self.visited: #if we have already visited, move on
                            continue
                        
                        print(newRow, newCol) 
                        result.append(self.grid[newRow][newCol])

        return result
        
    ''' Print out the Matrix to STDOUT '''
    def display(self, grid):
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
    # print(grid[start[0]][start[1]].row)
    # print(f'tile = {grid[3][5].tile}')
    # print(f'tile = {grid[0][0].tile}')
    # print(f'col = {grid[0][0].col}')
    # print(f'row = {grid[0][8].row}', f'col = {grid[0][8].col}')

    matrix = Matrix(grid, start)
    matrix.display(grid)

if __name__ == '__main__':
    main()