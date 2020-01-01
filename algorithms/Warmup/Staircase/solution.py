import os
import glob

def drawStaircase(n):
	hashes_len = 1
	spaces_len = n - 1
	shape = ''
	for i in range(n):
		symbols = ''
		# draw spaces symbols
		for j in range(spaces_len):
			symbols += ' '

		# draw hashes symbols
		for j in range(hashes_len):
			symbols += '#'
		
		hashes_len += 1
		spaces_len -= 1
		shape += '%s \n' % symbols

	return(shape)

shape = drawStaircase(4)
print(shape)

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