"""
This program checks if two strings are permutation of each other 
"""
#assuming 256 bit extended ascii character set
LEN = 256


def permutation_checker(String_A, String_B):
	if len(String_A) != len(String_B):
		return False
	letters = [int(0) for arr_temp in range(0,LEN+1)]
	for ch in String_A:
		# ord(x) is inbuilt python function which takes in a character input and returns a integral value of its unicode
		index = ord(ch)
		letters[index] +=1

	for ch in String_B:
		index = ord(ch)
		letters[index] -=1
		if letters[index] < 0:
			return False
	return True


A = input().strip()
B = input().strip()
if permutation_checker(A,B) is False:
	print("Not Permuations")
else:
	print("Permutations")


