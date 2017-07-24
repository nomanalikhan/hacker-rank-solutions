import os
import glob
import sys


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    alice_points = 0
    bob_points = 0
    
    if (a0 > b0 and a0 != b0):
        alice_points += 1
    elif (a0 < b0 and a0 != b0):
        bob_points += 1
        
    if (a1 > b1 and a1 != b1):
        alice_points += 1
    elif (a1 < b1 and a1 != b1):
        bob_points += 1
        
    if (a2 > b2 and a2 != b2):
        alice_points += 1
    elif (a2 < b2 and a2 != b2):
        bob_points += 1
        
    return ([alice_points, bob_points])


# execute all test cases
outputs = [];
inp_path = './testcases/input/*'
out_path = './testcases/output/*'

for file in glob.glob(inp_path):
	inpfile = open(file, 'r')
	
	# take the inputs from files
	a0, a1, a2 = inpfile.readline().strip().split(' ')
	a0, a1, a2 = [int(a0), int(a1), int(a2)]
	b0, b1, b2 = inpfile.readline().strip().split(' ')
	b0, b1, b2 = [int(b0), int(b1), int(b2)]
	result = solve(a0, a1, a2, b0, b1, b2)

	# push the output to array to check with output file later on
	outputs.append(" ".join(map(str, result)))

for index, file in enumerate(glob.glob(out_path)):
	inpfile = open(file, 'r')
	
	# take the inputs from first file
	expected_out = int(inpfile.readline())

	status = 'failed'
	if(expected_out == outputs[index]):
		status = 'passed'

	tc = 'testcase# %s: %s' % ((index + 1), status)
	print(tc)


# res = '%s %s' % (alice_points, bob_points)
# print(res)
# return res
# 
# 
# 
# 
# 
print (" ".join(map(str, result)))