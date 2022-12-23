
class Matrix():
    def __init__(self, matrixArray):
        self.rowSize = len(matrixArray)
        self.columnSize = len(matrixArray[0])
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
            if round(self.array[rowTarget-1][index] * scalar, 3) == 0:
                self.array[rowTarget-1][index] = abs(round(self.array[rowTarget-1][index] * scalar, 5))
            else:
                self.array[rowTarget-1][index] = round(self.array[rowTarget-1][index] * scalar, 5)


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

    def rowAddition(self, rowTarget, rowSelect, rowScalar):
        for index in range(len(self.array[rowTarget-1])):
            if round(self.array[rowTarget-1][index] + (self.array[rowSelect-1][index] * rowScalar),3) == 0:
                self.array[rowTarget-1][index] = abs(round(self.array[rowTarget-1][index] + (self.array[rowSelect-1][index] * rowScalar),5))
            else:
                self.array[rowTarget-1][index] = round(self.array[rowTarget-1][index] + (self.array[rowSelect-1][index] * rowScalar),5)


    def switchRows(self,targetOne, targetTwo):
        if targetOne <= len(self.array) and targetTwo <= len(self.array):
            tempRow = self.array[targetOne-1]

            self.array[targetOne-1] = self.array[targetTwo-1]
            self.array[targetTwo-1] = tempRow
        else:
            print("Error: Target row does not exist")

    def inverseMatrix(self):
        try:
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
                identityMatrix = Matrix(identityArray)
                #Sets up the identity matrix

                if self.array[0][0] == 1:
                    pass
                elif self.array[0][0] == 0:
                    for indexRow, row in enumerate(self.array):
                        if row[0] != 0:
                            self.switchRows(1, indexRow+1)
                            identityMatrix.switchRows(1, indexRow+1)
                            break

                counter = 0
                for indexCol in range(self.columnSize):
                    indexRow = indexCol
                    for value in [i[indexCol] for i in self.array][counter:]:
                        if indexRow == indexCol:
                            if value != 0:
                                self.scalarTimesRow(1/value, indexRow+1)
                                identityMatrix.scalarTimesRow(1/value, indexRow+1)
                            else:
                                for indextempRow, row in enumerate(self.array[indexRow+1:]):
                                    if row[indexCol] != 0:
                                        break
                                self.rowAddition(indexRow+1, indextempRow + indexRow + 2, 1/row[indexCol])
                                identityMatrix.rowAddition(indexRow+1, indextempRow + indexRow + 2, 1/row[indexCol])
                        else:
                            if value != 0 and self.array[indexCol][indexCol] == 1:
                                self.rowAddition(indexRow+1, indexCol+1, -value)
                                identityMatrix.rowAddition(indexRow+1, indexCol+1,-value)

                        indexRow += 1
                    counter += 1

                    #self.printMatrix()

                for indexRow in range(self.rowSize-1, -1, -1):
                    for temp in range(0, self.columnSize - indexRow - 1):
                        indexCol = self.columnSize - temp - 1
                        value = self.array[indexRow][indexCol]
                        if self.array[indexRow][indexCol] != 0:
                            self.rowAddition(indexRow+1, indexCol + 1, -value)
                            identityMatrix.rowAddition(indexRow+1, indexCol+1,-value)

                #self.printMatrix()
                for indexRow, row in enumerate(identityMatrix.array):
                    for indexCol, col in enumerate(row):
                        identityMatrix.array[indexRow][indexCol] = round(identityMatrix.array[indexRow][indexCol],3)

                identityMatrix.printMatrix()

            else:
                print("Error: Not a square matrix; inverse does not exist")
        except:
            print("Inverse does not exist")










def main():

    print("Matrix Operations By Andy Pauley")
    matrixNumber = int(input("How many matrices would you like to enter?"))
    print('')
    listMatrices = []
    for k in range(1,matrixNumber+1):
        print("Matrix #" + str(k))
        rowSize = int(input("Input how many rows > "))
        colSize = int(input("Input how many columns > "))
        tempArray = []
        for i in range(1,rowSize+1):
            tempRow = []
            for j in range(1,colSize+1):
                inputValue = int(input("Input Value for (" + str(i) + ',' + str(j) + ") > "), 3)
                tempRow.append(inputValue)
            tempArray.append(tempRow)
        tempClass = Matrix(tempArray)
        tempClass.printMatrix()
        print('', end='')
        listMatrices.append(tempClass)

    continuation  = True
    while continuation == True:
        print("Choose Function:")
        print('[1] Print Matrix')
        print('[2] Add Matrices')
        print('[3] Multiply row by scalar')
        print('[4] Multiply two matrices')
        print('[5] Add one row multiplied by a scalar to another row')
        print('[6] Switch Rows')
        print('[7] Find the inverse')
        print('[8] Row reduce')
        functionChoice = int(input(" > "))

        if functionChoice == 1:
            print("Which matrix do you want to print?")
            for index, item in enumerate(listMatrices):
                print('Matrix [' + str(index+1) + ']', item.array)
            matrixChoice = int(input(" > ")) - 1
            listMatrices[matrixChoice].printMatrix()

        if functionChoice == 2:
            print("Which matrices would you like to add?")
            for index, item in enumerate(listMatrices):
                print('Matrix [' + str(index + 1) + ']', item.array)

if __name__ == "__main__":
    main()