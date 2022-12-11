
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
            self.array[rowTarget-1][index] = round(self.array[rowTarget-1][index] * scalar, 3)


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

    def rowAdittion(self, rowTarget, rowSelect, rowScalar):
        for index in range(len(self.array[rowTarget-1])):
            self.array[rowTarget-1][index] = round(self.array[rowTarget-1][index] + (self.array[rowSelect-1][index] * rowScalar),3)


    def switchRows(self,targetOne, targetTwo):
        if targetOne <= len(self.array) and targetTwo <= len(self.array):
            tempRow = self.array[targetOne-1]

            self.array[targetOne-1] = self.array[targetTwo-1]
            self.array[targetTwo-1] = tempRow
        else:
            print("Error: Target row does not exist")

    def inverseMatrix(self):
        if self.rowSize == self.columnSize:
            #checks if square matrix
            identityArray = []
            for i in range(self.rowSize):
                tempRow = []
                for j in range(self.columnSize):
                    if i == j:
                        tempRow.append(1)
                    else:
                        tempRow.append(0)
                identityArray.append(tempRow)
            identityMatrix = Matrix(self.rowSize,  self.columnSize, identityArray)
            #Sets up the identity matrix

            if self.array[0][0] == 1:
                pass
            elif self.array[0][0] == 0:
                for indexRow, row in enumerate(self.array):
                    if row[0] != 0:
                        self.switchRows(1, indexRow+1)
                        identityMatrix.switchRows(1, indexRow+1)
                        break
            #makes it so that (0,0) is a non zero number


            #ORDER OF SOLVING FOR: (0,0) (1,0) (2,0) (1,1) (2,1) (2,2)
            #Staircase down, go column by column

            #If target is 1, and the number is  not zero, multiply the row by 1/number
            #if target is 1 and the number is zero, find a row where the same column has a non zero number and the numbers before it are zero and add that row so it makes it one
            #If target is 0 and in the jth  column, subtract the row by number * rj, because j,j will be 1, because work downwards





        else:
            print("Error: Not a square matrix; inverse does not exist")





m1 = Matrix(3,3, [[1,0,3],
                  [1,0,4],
                  [1,5,3]])
m2 = Matrix(3,2, [[10,11],
                  [20,21],
                  [30,31]])
m1.printMatrix()
m1.inverseMatrix()
