### Cube representation in Python. Prototype for C implementation.
### Will Store cube state and have moves to rotate each face 90 degress each direction.
### Current plan is to have 6 2D arrays to represent the cube in it's state.

import copy


### 2D array is Row - Column
class Cube:
    def __init__(self):
        self._rows, self._cols = 3, 3
        self._topFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._frontFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._leftFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._rightFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._backFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._bottomFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
    
    #default is clockwise
    def rotateFrontFace(self):
        temp = copy.deepcopy(self._rightFace)
        self._rightFace[0][0] = self._topFace[2][0]
        self._rightFace[1][0] = self._topFace[2][1]
        self._rightFace[2][0] = self._topFace[2][2]

        self._topFace[2][0] = self._leftFace[0][2]
        self._topFace[2][1] = self._leftFace[1][2]
        self._topFace[2][2] = self._leftFace[2][2]

        self._leftFace[0][2] = self._bottomFace[0][0]
        self._leftFace[1][2] = self._bottomFace[0][1]
        self._leftFace[2][2] = self._bottomFace[0][2]

        self._bottomFace[0][0] = temp[0][0]
        self._bottomFace[0][1] = temp[1][0]
        self._bottomFace[0][2] = temp[2][0]
        
        


    def createSolvedCube(self):
        for row in range (self._rows):
            for col in range(self._cols):
                self._topFace[row][col] = "W"
        for row in range (self._rows):
            for col in range(self._cols):
                self._frontFace[row][col] = "B"
        for row in range (self._rows):
            for col in range(self._cols):
                self._leftFace[row][col] = "R"
        for row in range (self._rows):
            for col in range(self._cols):
                self._rightFace[row][col] = "O"
        for row in range (self._rows):
            for col in range(self._cols):
                self._backFace[row][col] = "G"
        for row in range (self._rows):
            for col in range(self._cols):
                self._bottomFace[row][col] = "Y"

    def displayCube(self):
        self._display_topFace()
        print()
        self._display_frontFace()
        print()
        self._display_leftFace()
        print()
        self._display_rightFace()
        print()
        self._display_backFace()
        print()
        self._display_bottomFace()


    def _display_frontFace(self):
        for a in range(3):
            print(self._frontFace[a])
    def _display_topFace(self):
        for a in range(3):
            print(self._topFace[a])
    def _display_leftFace(self):
        for a in range(3):
            print(self._leftFace[a])
    def _display_rightFace(self):
        for a in range(3):
            print(self._rightFace[a])
    def _display_bottomFace(self):
        for a in range(3):
            print(self._bottomFace[a])
    def _display_backFace(self):
        for a in range(3):
            print(self._backFace[a])
        
