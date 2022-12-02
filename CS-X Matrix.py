
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


    def matrixMultiply(self, m2):
        newArray = []
        #sets up a blank array
        if self.columnSize == m2.rowSize:
            #checks if able to multiply
            #New size of Matrix is m1 Row by m2 column, so the for loops are looping for that amount
            for indexRow in range(self.rowSize):
                newRow = []
                #sets up a blank list
                for indexCol in range(m2.columnSize):
                    newNum = 0
                    #sets up a blank number to keep track of the sum
                    for index, item in enumerate(m1.array[indexRow]):
                        #for each new number in a list, you have to sum n products, where n how many columns there are in m1. So this loops n times, adding the products together
                        newNum += m1.array[indexRow][index] * [i[indexCol] for i in m2.array][index]
                        #adds the product of the first number of m1 row and the first number of m2 column. which m1 row depends on the row of the new matrix. which m2 column depends on the column of the new matrix
                        #the [i[indexCol] for i in m2.array] is a list of the column. First it takes the row, then takes a specifc index of row corresponding to the column. It then takes all the results from the for loop and makes it a list
                    newRow.append(newNum)
                    #adds the sum, or the result to a list

                newArray.append(newRow)
                #appends each newrow to this new matrix
            m1.array = newArray



        else:
            print("Unable to multiply: Column size does not match row size. ")




m1 = Matrix(2,2, [[1,2],
                  [4,5]])
m2 = Matrix(3,2, [[10,11],
                  [20,21],
                  [30,31]])
#m1.printMatrix()
m1.matrixMultiply(m1)
m1.printMatrix()

