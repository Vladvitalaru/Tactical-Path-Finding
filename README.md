# Tactical Path Finding :chart_with_upwards_trend:

Given a tile map with varying terrain, find the shortest path from player "0" to player "2" using Dijkstras algorithm

## Terrain :mountain:

- Road: '.' cost: 1
- Grass: ',' cost: 2
- Rocks: 'o' cost: 3
- Walls: '=', cost: 50

If a player moves diagonally, it counts as 1.5x the cost.

## Characters :bust_in_silhouette:

- '0' represents the player character
- '1' represents a friendly character,
- '2' represents the target character 
- '3' represents an enemy character

Two humans cannot be on the same tile, so no cost is listed.

## Tile Maps
<img width="126" alt="Screenshot 2022-12-05 at 3 15 28 PM" src="https://user-images.githubusercontent.com/78878935/205763745-898319b2-6d4c-4b36-8eeb-61e212f238b3.png"> <img width="126" alt="Screenshot 2022-12-05 at 3 19 23 PM" src="https://user-images.githubusercontent.com/78878935/205764290-7cc17343-7493-4e89-a343-94877a56c6bb.png">

## Output Maps

Shortest path: \*

<img width="126" alt="Screenshot 2022-12-05 at 3 31 48 PM" src="https://user-images.githubusercontent.com/78878935/205767208-40242a2b-52ae-4196-add5-a43f368acdba.png"> <img width="126" alt="Screenshot 2022-12-05 at 3 31 03 PM" src="https://user-images.githubusercontent.com/78878935/205767167-24208391-d0fc-4336-81e9-17f15f29947e.png">
