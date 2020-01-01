import os
import glob
import math


def search_top_to_bottom(rows, columns, mat, starting_row=0, starting_col=0, diamonds=0):
    row_index_greater_than_rows = starting_row == rows
    col_index_greater_than_columns = starting_col == columns

    if (row_index_greater_than_rows and col_index_greater_than_columns):
        return diamonds
    elif (row_index_greater_than_rows):
        return diamonds
        # return search_top_to_bottom(rows, columns, mat,
        #                             0, starting_col)
    elif (col_index_greater_than_columns):
        return search_top_to_bottom(rows, columns, mat,
                                    starting_row + 1, 0, diamonds)
    else:
        print('row: %s, col: %s, row_cond: %s, col_cond: %s' %
              (starting_row, starting_col, row_index_greater_than_rows, col_index_greater_than_columns))

        if(mat[starting_row][starting_col] == 1):
            diamonds = diamonds + 1
            # print('row: %s, col: %s' % (starting_row, starting_col))
            mat[starting_row][starting_col] = 0

        if(mat[starting_row][starting_col] == 0):
            return search_top_to_bottom(rows, columns, mat,
                                        starting_row, starting_col + 1, diamonds)
        if(mat[starting_row][starting_col] == -1):
            return search_top_to_bottom(rows, columns, mat,
                                        starting_row + 1, starting_col - 1, diamonds)

        return diamonds


def search_bottom_to_top(rows, columns, mat, starting_row=2, starting_col=2, diamonds=0):
    row_index_lesser_than_zero = starting_row == -1
    col_index_lesser_than_zero = starting_col == -1

    if (row_index_lesser_than_zero and col_index_lesser_than_zero):
        return diamonds
    elif (row_index_lesser_than_zero):
        return diamonds
        # return search_bottom_to_top(rows, columns, mat,
        #                             0, starting_col)
    elif (col_index_lesser_than_zero):
        return search_bottom_to_top(rows, columns, mat,
                                    starting_row - 1, starting_col + 2, diamonds)
    else:
        # print('row: %s, col: %s, row_cond: %s, col_cond: %s' %
        #       (starting_row, starting_col, row_index_lesser_than_zero, col_index_lesser_than_zero))
        # cell_val = mat[starting_row][starting_col]
        # print('val: %s' % (cell_val))
        if(mat[starting_row][starting_col] == 1):
            diamonds = diamonds + 1
            # print('row: %s, col: %s' % (starting_row, starting_col))
            mat[starting_row][starting_col] = 0

        if(mat[starting_row][starting_col] == 0):
            return search_bottom_to_top(rows, columns, mat,
                                        starting_row, starting_col - 1, diamonds)
        if(mat[starting_row][starting_col] == -1):
            return search_bottom_to_top(rows, columns, mat,
                                        starting_row - 1, starting_col + 1, diamonds)

        return diamonds


def collect_max(mat_rows, mat_columns, mat):
    print(mat)
    top_to_bottom_diamonds_count = search_top_to_bottom(
        mat_rows, mat_columns, mat)
    print(top_to_bottom_diamonds_count)
    print(mat)
    # bottom_to_top_diamonds_count = search_bottom_to_top(
    #     mat_rows, mat_columns, mat)
    # print(mat)
    return top_to_bottom_diamonds_count  # + bottom_to_top_diamonds_count


mat = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
# mat1 = [
#     [0, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
result = collect_max(3, 3, mat)
print(result)

# execute all test cases
# outputs = []
# inp_path = './testcases/input/*'
# out_path = './testcases/output/*'

# for file in glob.glob(inp_path):
#     inpfile = open(file, 'r')

#     # take the inputs from first file
#     mat_rows = int(inpfile.readline())
#     mat_columns = int(inpfile.readline())

#     # res = solveMeFirst(num1, num2)
#     # push the output to array to check with output file later on
#     outputs.append(res)

# for index, file in enumerate(glob.glob(out_path)):
#     inpfile = open(file, 'r')

#     # take the inputs from first file
#     expected_out = int(inpfile.readline())

#     status = 'failed'
#     if(expected_out == outputs[index]):
#         status = 'passed'

#     tc = 'testcase# %s: %s' % ((index + 1), status)
#     print(tc)
