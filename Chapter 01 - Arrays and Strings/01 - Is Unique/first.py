#assuming 256 bit extended ascii character set
LEN = 256
#chr(i) is inbuilt python function that returns unicode character representing the integer i 
MIN_CHARACTER =chr(0)


def is_unique(string_A):
	#This array stores the count of characters
	arr = [int(0) for i in range (0, LEN +1)]
	for ch in string_A:
		arr_temp = ord(ch) - ord(MIN_CHARACTER)
		if arr[arr_temp]  is 1:
		    return False
		arr[arr_temp] = 1
	return True


A = input().strip()
if is_unique(A) is False:
	print("Not Unique")
else:
	print("Unique")