import sys
import re


#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


for line in lines:
	line = re.sub(r'\u000C', '', line)
	line = re.sub(r'\u0003', '', line)
	line = re.sub(r' +', ' ', line)
	line = re.sub(r'^ ', '', line)
	line = re.sub(r' $', '', line)
	if(line != ''):
		print(line, end=' ')