import os
import glob
import datetime


# classic solution
def timeConversion(t):
	return datetime.datetime.strptime(t, '%I:%M:%S%p').time()

inp = '07:05:45PM'
out = '19:05:45'




print(timeConversion(inp))



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