### Cube representation in Python. Prototype for C implementation.
### Will Store cube state and have moves to rotate each face 90 degress each direction.
### Current plan is to have 6 2D arrays to represent the cube in it's state.

import copy


### 2D array is Row - Column
class Cube:
    """
    A class that represents a 3x3 rubiks cube and supports rotation of each of the faces in both directions with default being clockwise.
    Method is present for creating a fully solved cube.
    TODO : Complete roatation functions for
        top face
        bottom face
        right face
        left face
    TODO : Generate Random Cube - generate solved and move faces randomly?
        concern - could be slow
        might not be though.
    TODO : Check cube validity on random generation maybe?

    """
    def __init__(self):
        self._rows, self._cols = 3, 3
        self._topFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._frontFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._leftFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._rightFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._backFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._bottomFace = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
    
    #default is clockwise
    def rotateFrontFace(self, default):
        if (default):    
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
        else:
            temp = copy.deepcopy(self._leftFace)
            self._leftFace[0][2] = self._topFace[2][0]
            self._leftFace[1][2] = self._topFace[2][1]
            self._leftFace[2][2] = self._topFace[2][2]

            self._topFace[2][0] = self._rightFace[0][0]
            self._topFace[2][1] = self._rightFace[1][0]
            self._topFace[2][2] = self._rightFace[2][0]

            self._rightFace[0][0] = self._bottomFace[0][0]
            self._rightFace[1][0] = self._bottomFace[0][1]
            self._rightFace[2][0] = self._bottomFace[0][2]

            self._bottomFace[0][0] = temp[0][2]
            self._bottomFace[0][1] = temp[1][2]
            self._bottomFace[0][2] = temp[2][2]
    
    def rotateBackFace(self, default):
        if (default):    
            temp = copy.deepcopy(self._rightFace)
            self._rightFace[0][2] = self._topFace[0][0]
            self._rightFace[1][2] = self._topFace[0][1]
            self._rightFace[2][2] = self._topFace[0][2]

            self._topFace[0][0] = self._leftFace[0][0]
            self._topFace[0][1] = self._leftFace[1][0]
            self._topFace[0][2] = self._leftFace[2][0]

            self._leftFace[0][0] = self._bottomFace[2][0]
            self._leftFace[1][0] = self._bottomFace[2][1]
            self._leftFace[2][0] = self._bottomFace[2][2]

            self._bottomFace[2][0] = temp[0][2]
            self._bottomFace[2][1] = temp[1][2]
            self._bottomFace[2][2] = temp[2][2]
        else:
            temp = copy.deepcopy(self._leftFace)
            self._leftFace[0][0] = self._topFace[0][0]
            self._leftFace[1][0] = self._topFace[0][1]
            self._leftFace[2][0] = self._topFace[0][2]

            self._topFace[0][0] = self._rightFace[0][2]
            self._topFace[0][1] = self._rightFace[1][2]
            self._topFace[0][2] = self._rightFace[2][2]

            self._rightFace[0][2] = self._bottomFace[2][0]
            self._rightFace[1][2] = self._bottomFace[2][1]
            self._rightFace[2][2] = self._bottomFace[2][2]

            self._bottomFace[2][0] = temp[0][0]
            self._bottomFace[2][1] = temp[1][0]
            self._bottomFace[2][2] = temp[2][0]
    def rotateTopFace(self, default):
        if (default):    
            pass
        else:
            pass
    def rotateBottomFace(self, default):
        if (default):    
            pass
        else:
            pass
    def rotateLeftFace(self, default):
        if (default):
            pass
        else:
            pass
    def rotateRightFace(self, default):
        if (default):
            pass
        else:
            pass

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
        print()


    def _display_frontFace(self):
        print("Front:")
        for a in range(3):
            print(self._frontFace[a])

    def _display_topFace(self):
        print("Top:")
        for a in range(3):
            print(self._topFace[a])

    def _display_leftFace(self):
        print("Left:")
        for a in range(3):
            print(self._leftFace[a])

    def _display_rightFace(self):
        print("Right:")
        for a in range(3):
            print(self._rightFace[a])

    def _display_bottomFace(self):
        print("Bottom:")
        for a in range(3):
            print(self._bottomFace[a])

    def _display_backFace(self):
        print("Back:")
        for a in range(3):
            print(self._backFace[a])

        
