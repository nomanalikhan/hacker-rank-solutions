import os
import glob
from functools import reduce

def aVeryBigSum(n, ar):
  # Complete this function
  return reduce((lambda x, y: x + y), ar)

# execute all test cases
outputs = [];
inp_path = './testcases/input/*'
out_path = './testcases/output/*'

for file in glob.glob(inp_path):
	inpfile = open(file, 'r')
	
	# take the inputs from file
	n = int(inpfile.readline().strip())
	ar = list(map(int, inpfile.readline().strip().split(' ')))
	res = aVeryBigSum(n, ar)

	# push the output to array to check with output file later on
	outputs.append(res)

for index, file in enumerate(glob.glob(out_path)):
	inpfile = open(file, 'r')
	
	# take the inputs from first file
	expected_out = int(inpfile.readline())

	status = 'failed'
	if(expected_out == outputs[index]):
		status = 'passed'

	tc = 'testcase# %s: %s' % ((index + 1), status)
	print(tc)