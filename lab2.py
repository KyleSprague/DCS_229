
class Matrix:

    __slots__ = ('_matrix_info', '_num_cols', '_num_rows')

    def __init__(self, rows: int, cols: int, matrix_entries: list) -> list:
        '''
            The goal of this function is to initialize our instance variable and
            return the instance variable given that the matrix dimensions given and result is
            correct

            Parameters:
                int -- rows: the number of rows for the given matrix as an integer
                int -- cols: the number of columns for the given matrix as an integer
                list -- matrix: the matrix entries in row column order for the given matrix

            Returns:
                a list within the instance variable containing the given values in the matrix

        '''
        if rows*cols == len(matrix_entries) or len(matrix_entries) == 1:
            self._matrix_info = [[rows, cols], matrix_entries]
        else:
            matrix_length = len(matrix_entries)
            raise ValueError(f"For your rows and cols, ({rows}*{cols}) != matrix length ({matrix_length}). No operations can be performed")

    def getNumRows(self) -> int:
        '''
            Get the number of rows using the self instance variable

            Parameters:
                list -- self: the values of the matrix and the corresponding number of colums, rows as a list

            Return:
                the number of rows for the given matrix
        '''
        return self._matrix_info[0][0]

    def getNumCols(self) -> int:
        '''
            Get the number of columns using the instance variable

            Parameters:
                list -- self: the values of the matrix and the corresponding number of colums, rows as a list

            Return:
                the number of columns for the given matrix
        '''
        return self._matrix_info[0][1]

    def __str__(self) -> str:
        '''
            gives the matrix in fancy notation

            Parameters:
                list -- self: the values of the matrix and the corresponding number of colums, rows as a list

            Return:
                the matrix list organized according to rows and columns with a specified notation
        '''

        matrix_list = self._matrix_info[1]
        longest = len(str(matrix_list[0]))
        for i in range(len(matrix_list)):
            if len(str(matrix_list[i])) > longest:
                longest = len(str(matrix_list[i]))

        #idea to use oython .rjust method from Felix King on Stack Overflow

        row_number = self.getNumRows()
        column_number = self.getNumCols()

        #if column number is bigger, iterate through columns
        string_matrix_list = [str(entry).rjust(longest, " ") for entry in matrix_list]
        #print(string_matrix_list)

        matrix_list = string_matrix_list.copy()
        matrix_string = "|"
        for k in range(len(matrix_list)):
            if k%column_number == 0 and k!= 0:
                end_character = k
                adjustment = "  |\n|"
                matrix_string = matrix_string + adjustment
                matrix_string = matrix_string + "  " + matrix_list[k]
            else:
                matrix_string = matrix_string + "  " + matrix_list[k]
        matrix_string = matrix_string + "  |"


        return matrix_string

        #formatted_matrix = "|"
        #for j in range(len(matrix_list)):
            #formatted_matrix = formatted_matrix + (longest*"" + str(matrix_list[j]))


    def __getitem__(self, row_col: "tuple[int]") -> int:
        '''
            Find the specified element in the matrix

            Parameters:
                list -- self: the values of the matrix and the corresponding number of colums, rows as a list
                row_col -- tuple[int]: specified row,column location in matrix

            Returns:
                The entry at the specified location as an integer
        '''
        row, column = row_col
        column_number = self.getNumCols()
        row_number = self.getNumRows()
        matrix_list = self._matrix_info[1]
        #print(len(matrix_list))
        composite_list = []
        start = 0
        for i in range(0, len(matrix_list)+1,column_number):
            new_list = []
            for j in range(start, i):
                #print(j)
                new_list.append(matrix_list[j])
                #print(new_list)
            if len(new_list) == column_number:
                composite_list.append(new_list)
            start = start+i

        value = composite_list[row][column]

        return value


    def __eq__(self, other: 'Matrix') -> bool:
        '''
            Determine if the matrices are of equal size and have the same values

            Paramters:
                list -- self, other: the values of the matrix and the corresponding number of colums, rows as a list

            Returns:
                True if the matrices are equal and false if not

        '''
        if self._matrix_info == other._matrix_info:
            return True
        else:
            return False

    def __add__(self, other: 'Matrix') -> 'Matrix':
        '''
            Add the given matrices

            Paramters:
                list -- self, other: the values of the matrix and the corresponding number of colums, rows as a list

            Returns: sum of the given matrices at a matrix
        '''


        if self._matrix_info[0][0] != other._matrix_info[0][0] or self._matrix_info[0][1] != other._matrix_info[0][1]:
            raise ValueError(f"the number of rows and colums for the input matrices must be equal")
        else:
            result = []
            for i in range(len(self._matrix_info[1])):
                result.append(self._matrix_info[1][i] + other._matrix_info[1][i])

        row_col = [self._matrix_info[0][0], self._matrix_info[0][1]]
        print(row_col)

        new_matrix = Matrix(row_col[0], row_col[1], result) #WHY THIS NOT WORKING
        return new_matrix

    def transpose(self) -> 'Matrix':
        '''
            Take the transpose of the given matrix

            Paramters:
                list -- self, other: the values of the matrix and the corresponding number of colums, rows as a list

            Returns:
                The transpose of the given matrix
        '''


        rows = self._matrix_info[0][0]
        num_cols = self._matrix_info[0][1]

        transpose_rows = num_cols
        transpose_cols = rows
        transpose_list = []
        for i in range(num_cols):
            for j in range(i, len(self._matrix_info[1]), num_cols):
                print(self._matrix_info[1][j])
                transpose_list.append(self._matrix_info[1][j])

        print(transpose_list)

        transpose = Matrix(transpose_rows, transpose_cols, transpose_list)

        return transpose


    def __mul__(self, other: 'Matrix') -> 'Matrix':
        '''
            Take the product of the given matrices

            Paramters:
                list -- self, other: the values of the matrix and the corresponding number of colums, rows as a list

            Returns:
                the product of the given matrices as a matrix

        '''



        a_rows = self._matrix_info[0][0]
        a_cols = self._matrix_info[0][1]

        b_rows = other._matrix_info[0][0]
        b_cols = other._matrix_info[0][1]
        if a_cols != b_rows:
            raise ValueError(f"rows of first matrix must be equal to columns of second to /n perform matrix multiplication: {a_cols} != {b_rows}")
        else:


            a_with_row_lists = []
            for i in range(0, len(self._matrix_info[1]), a_cols):
                temp_row_list = []
                for j in range(i, a_cols + i):
                    temp_row_list.append(self._matrix_info[1][j])
                a_with_row_lists.append(temp_row_list)

            b_with_row_lists = []
            for k in range(0, len(other._matrix_info[1]), b_cols):
                temp_row_list = []
                for x in range(k, b_cols + k):
                    temp_row_list.append(other._matrix_info[1][x])
                b_with_row_lists.append(temp_row_list)
                print(b_with_row_lists)

            composite_matrix = []
            row_value_list = []
            column_value_list = []

            for r in range(a_rows):
                #row_value_list.append(self._matrix_info[1][r])
                for c in range(b_cols):
                    var = 0
                    for s in range(a_cols):
                        var += a_with_row_lists[r][s] * b_with_row_lists[s][c]
                    composite_matrix.append(var)

        result = Matrix(a_rows, b_cols, composite_matrix)
        return result
    #ensure that any provided objects are immutable?



def main():

    ################STRING PRINT TESTS#########################
    print("############### STRINT PRINT TESTS ####################")
    a = Matrix(2,4, [36, -32, 499, -432, 8799, 6000002, -49833, -9999999999])
    print(a)

    v = Matrix(3,2, [1,2,3,4,5,6])
    print(v)

    ################EXCEPTION TESTS#############################
    #dumb_matrix_1 = Matrix(2,3, [32,33,0]) #expected: value error

    #dumb_matrix_2 = Matrix(0,0, [30, 20, 40]) #expected: value error

    ############# __getitem__ TESTS ############################

    print("############### GET ITEM TESTS ####################")
    m = Matrix(2, 3, [12,234,3456,12345,23,3])
    m_result = (m[1,1]) #print 23
    print(f"expected: 23, result: {m_result}")


    l = Matrix(1,1, [34])
    print(l)
    l_result = (l[0,0])
    print(f"expected: 34, result: {l_result}")

    print("############## EQUIVALENCY TESTS ##################")

    j = Matrix(1,2, [42, 17])
    k = Matrix(3,2, [80, 14, 89, 23, 34, 90])
    print(f"expected result is False and acutal result is {j == k}")

    o = Matrix(1,3, [23, 23, 45])
    f = Matrix(1,3, [23, 23, 45])
    print(f"expected result is True and actual result {o == f}")

    print(f"################ ADD TESTS ###################")

    p = Matrix(1,1, [2])
    print(p)
    u = Matrix(1,1, [3])
    print(u)
    print(f" expected result is 5 and actual result is {u + p}")

    print(f"################## TRANSPOSE TESTS ######################")

    x = Matrix(3,2, [1,2,4,6,3,9])
    result = x.transpose()
    expected = Matrix(2,3, [1,4,3,2,6,9])
    print(f"True if expected = result: Result: {result == expected} ")

    print(f"################ MULTIPLY TESTS ########################")

    e = Matrix(2,3, [2,2,3,4,1,2])
    f = Matrix(3,3, [3,2,1,4,7,1,5,2,2])
    result = e*f
    expectation = Matrix(2,3, [29, 24, 10, 26, 19, 9])
    print(f"result of e*f is {result} and expectation is {expectation}")






if __name__ == "__main__":
  main()
