# -*- coding: utf-8 -*-
"class practice work"

def factorization(number):
	"factorization"

	res = []
	for division in xrange(2, int(number**0.5)):
			while number % division == 0:
				number /= division
				res.append(division)
				if (number == 1):
					break
	if(number != 1):
		res.append(number)

	return res

def main():
    "main"
    assert factorization(1) == []
    assert factorization(20) == [2, 2, 5]
    assert factorization(2 * 5 * 179) == [2, 5, 179]
    print "OK!"
    raw_input()
    return 0

if __name__ == "__main__":    
	exit(main())