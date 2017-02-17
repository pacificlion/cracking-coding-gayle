'''
This program depends upon bitwise operator i.e
1 is bitwise left shifted by each character in its integer form
Example - 343 , checker = 0
1 <<3 , then this res is bitwise added to checker, if its zero , then the character is not yet occurred so checker is added to its value
checker = 1000, for 4,  1000 & (1 <<4) = 0, so checker is summed with 1<<4
checker = 11000, for 3, 11000 & (1<<3) = 01000 not equal to zero hence character is repeated
'''
LEN = 256
MIN_CHARACTER =chr(0)

string1 = input()

checker = 0
flag =0
for ch in string1:
	arr_temp = ord(ch) - ord(MIN_CHARACTER)
	if checker & (1 << arr_temp) is 0:
		checker += (1 << arr_temp)
	else:
		flag = -1
if flag is -1:
	print("Not Unique")
else:
	print("Unique")