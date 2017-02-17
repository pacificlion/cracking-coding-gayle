LEN = 256
MIN_CHARACTER =chr(0)

string1 = input()

#This array stores the count of characters
arr = [int(0) for i in range (0, LEN +1)]

flag = 0
for ch in string1:
	arr_temp = ord(ch) - ord(MIN_CHARACTER)
	if arr[arr_temp]  is 1:
	    flag = -1
	    break 
	arr[arr_temp] = 1
if flag is -1:
	print("Not Unique")
else:
	print("Unique")