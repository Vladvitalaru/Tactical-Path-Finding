#Vlad Vitalaru
#CS 450 
#HW 5 Tactical Path Finding

import sys
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
    def __init__(self, tile, cost):
        self.tile = tile
        self.cost = cost
        
''' Matrix class holding grid & Dijksras algorithm'''
class Matrix():
    def __init__(self, grid, start, destination):
        self.grid = grid
        self.start = start
        self.destination = destination
        
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
            if tile == "0":
                start = (y, x) #index of start (row, col)
            elif tile == "2": 
                destination = (y, x) #index of destination (row, col)
                
            x += 1
            node = Node(tile, tiles[tile])
            row.append(node)
        
        grid.append(row)
        x = 0
        
    matrix = Matrix(grid, start, destination)
    matrix.display(grid)

if __name__ == '__main__':
    main()