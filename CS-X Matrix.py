
class Matrix():
    def __init__(self, rowSize, columnSize, matrixArray):
        self.rowSize = rowSize
        self.columnSize = columnSize
        self.array = matrixArray

    def printMatrix(self):
        for row in self.array:
            for item in row:
                print(item, end=' ')

            print('')

    def plusMatrix(self, m2):
        if self.rowSize == m2.rowSize and self.columnSize == m2.columnSize:
            for indexRow, row in enumerate(self.array):
                #print("ROW", indexRow, ":", row)
                for indexCol, item in enumerate(row):
                    self.array[indexRow][indexCol] += m2.array[indexRow][indexCol]
        else:
            print("Not Same Size, Addition can't be performed")

    def scalarTimesRow(self, scalar, rowTarget):
        for index, item in enumerate(self.array[rowTarget-1]):
            self.array[rowTarget-1][index] *= scalar




m1 = Matrix(3,2, [[5,6],
                  [4,3],
                  [1,2]])
m2 = Matrix(3,2, [[3,3],
                  [3,3],
                  [1,4]])
m1.printMatrix()
print('')
m1.scalarTimesRow(2,3)
m2.scalarTimesRow(2,3)
m1.plusMatrix(m2)
m1.printMatrix()

