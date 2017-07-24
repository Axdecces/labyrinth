#Plan

what my game should do:
- player has to reach a special point of the labyrinth by finding a path
- character is controlled by wasd




##game

- game loop
- scene manager
- level manager
- tiles (16x16)

##specs

- tiles (16x16)
- square (20x20 tiles)

##objects

- character
- background
    - size of screen
- walls
    - square


##sprites
### squares filled with color

- character
    - red square (1 tile)
- background
    - light grey (whitish)
    - 20 x 20 tiles
- walls
    - squares (1 tile)
    - darker grey
    

##classes

- scene manager
    - level manager
        - level
- sprite class
    - square class
        - character class
            - should move
            - should check, if running against wall
        - wall class
            - should define walls for character
