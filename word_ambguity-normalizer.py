import sys
import re


#open file using open file mode
fp1 = open(sys.argv[1]) # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


#open file using open file mode
fp2 = open(sys.argv[2]) # Open file on read mode -- input file
words = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file

list_hash = {}
for word in words:
	if(word != ""):
		tt = word.split("\t")
		src = tt[0]
		tgt = tt[1]
		src = src.strip()
		tgt = tgt.strip()
		list_hash[src] = tgt

keys = list_hash.keys()

for key in keys:
	#print(key, list_hash[key])
	i = 0
	for line in lines:
		my_regex = r"(^|[,\"\'\( \/\-\|\t])" + key + r"([ ,\.!\"।\'\/\-)\t]|$)"
		if((re.search(my_regex, line, re.IGNORECASE|re.UNICODE))):
			line = re.sub(my_regex, r"\1" + list_hash[key] +r"\2",line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
			lines[i] = line
		else:
			lines[i] = line
		i = i + 1

for line in lines:
	#to make some characters null
	#line = re.sub(r'\u000C', '', line)
	#line = re.sub(r'\u0003', '', line)
	print(line)