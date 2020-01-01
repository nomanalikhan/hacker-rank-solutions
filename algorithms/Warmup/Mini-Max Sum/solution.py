import os
import glob
import numpy as np

# numpy solution
# def getMinMaxSum(arr):
# 	total_sum_arr = []
# 	for i in range(len(arr)):
# 		new_arr = np.delete(arr, i)
# 		total_sum_arr.append(new_arr.sum())

# 	return ('%s %s' % (np.min(total_sum_arr), np.max(total_sum_arr)))

# classic solution
def getMinMaxSum(arr):
	total_sum_arr = []
	for i in range(len(arr)):
		new_arr = arr[:]
		new_arr.pop(i)
		total_sum_arr.append(sum(new_arr))

	return ('%s %s' % (min(total_sum_arr), max(total_sum_arr)))

arr = [1, 2, 3, 4, 5]

print(getMinMaxSum(arr))



# execute all test cases
# outputs = [];
# inp_path = './testcases/input/*'
# out_path = './testcases/output/*'

# for file in glob.glob(inp_path):
# 	inpfile = open(file, 'r')
	
# 	# take the inputs from first file
# 	num1 = int(inpfile.readline())
# 	num2 = int(inpfile.readline())

# 	res = solveMeFirst(num1, num2)
# 	# push the output to array to check with output file later on
# 	outputs.append(res)

# for index, file in enumerate(glob.glob(out_path)):
# 	inpfile = open(file, 'r')
	
# 	# take the inputs from first file
# 	expected_out = int(inpfile.readline())

# 	status = 'failed'
# 	if(expected_out == outputs[index]):
# 		status = 'passed'

# 	tc = 'testcase# %s: %s' % ((index + 1), status)
# 	print(tc)