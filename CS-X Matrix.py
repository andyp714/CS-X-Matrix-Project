print("hello world")

class Matrix():
    def __init__(self, rowNumber, columnNumber, matrixArray):
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        self.array = matrixArray

    def printMatrix(self):
        for row in self.array:
            for item in row:
                print(item, end=' ')

            print('')



m1 = Matrix(3,2, [[2,1],[1,2], [0,1]])
m1.printMatrix()
print("test")