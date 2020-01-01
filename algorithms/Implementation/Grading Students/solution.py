import os
import glob
import math

def getNextMultiplier(num, multiplier):
	val = math.ceil(num/multiplier)*multiplier
	return math.ceil(num/multiplier)*num

def solve(grades):
	new_grades = []
	multiplier = 5
	# print(grades)
	for grade in grades:
		# print('multi: ', getNextMultiplier(grade, multiplier))
		if (grade < 38):
			new_grades.append(grade)
		elif ( (getNextMultiplier(grade, multiplier) - grade) < 3):
			new_grades.append(getNextMultiplier(grade, multiplier))
		else:
			new_grades.append(grade)
	return new_grades



grades = [73, 67, 38, 33]
result = solve(grades)
print(result)

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