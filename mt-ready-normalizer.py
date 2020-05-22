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

flag = 0
for word in words:
	if(re.search(r'# Anywhere in the text', word, flags=re.IGNORECASE)):
		flag = 0
	elif (re.search(r'# Every begining line only', word, flags=re.IGNORECASE)):
		flag = 1

	if(word != "" and re.search(r'\t', word)):
		tt = word.split("\t")
		src = tt[0]
		tgt = tt[1]
		src = src.strip()
		tgt = tgt.strip()
		if(flag == 0):
			list_hash[src] = tgt + "####0"
		else :
			list_hash[src] = tgt + "####1"

keys = list_hash.keys()

for key in keys:
	#print(key, list_hash[key])
	i = 0
	val = list_hash[key]
	subs = val.split("####")[0]
	f = val.split("####")[1]

	for line in lines:
		if(f == "0"):
			my_regex = r"(^|[,\"\'\( \/\-\|\t])" + key + r"([ ,\.!\"।\'\/\-)\t]|$)"
		elif(f == "1"):
			my_regex = r"^" + key
		#print(my_regex, line, f)
		if((re.search(my_regex, line, flags=re.IGNORECASE|re.UNICODE)) and f == "0"):
			line = re.sub(my_regex, r"\g<1>" + subs +r"\g<2>", line,flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
			lines[i] = line
		elif((re.search(my_regex, line, flags=re.IGNORECASE|re.UNICODE)) and f == "1"):
			line = re.sub(my_regex, subs , line, flags=re.IGNORECASE|re.UNICODE|re.MULTILINE)
			lines[i] = line
		else:
			lines[i] = line
		i = i + 1

for line in lines:
	#to make some characters null
	#line = re.sub(r'\u000C', '', line)
	#line = re.sub(r'\u0003', '', line)
	print(line)