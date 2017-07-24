import os
import glob

def getDiagnolDiff(n):
	start_ind = 0
	end_ind = n - 1
	r_d_sum = 0
	l_d_sum = 0

	for a_i in range(n):
	    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
	    r_d_sum += a_t[start_ind]
	    l_d_sum += a_t[end_ind]
	    
	    start_ind += 1
	    end_ind -= 1

	return(abs(r_d_sum - l_d_sum))

# execute all test cases
outputs = [];
inp_path = './testcases/input/*'
out_path = './testcases/output/*'

for file in glob.glob(inp_path):
	inpfile = open(file, 'r')
	
	# take the inputs from file
	n = int(inpfile.readline().strip())
	res = getDiagnolDiff(n)

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