# -*- coding: utf-8 -*-
"class practice work"

def str_func(str_source):
	res = ""
	written = False
	find_sharp = False
	main_symbol = ''
	for temp_symbol in str_source:
		if (temp_symbol == '#'):
			if find_sharp == True:
				if written != True:
					written = True
					res += res[-1]
			else:
				written = False
				find_sharp = True
			continue
		if (temp_symbol == main_symbol):
			if written != True:
				res += main_symbol
				written = True
		else:
			written = False
			find_sharp =False
			main_symbol = temp_symbol

	return res

def main():    
	"main"

	str_func("###") == ""
	assert str_func("1") == ""
	assert str_func("11") == "1"
	assert str_func("111111") == "1"
	assert str_func("11#") == "1"
	assert str_func("11##") == "11"
	assert str_func("11122234###55") == "1225"

	print "OK!"
	return 0

if __name__ == "__main__":    
	exit(main())