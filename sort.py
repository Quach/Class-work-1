# -*- coding: utf-8 -*-
"class practice work"

def sort(src_array):
    "gnome sorting"
    i = 1
    while i < len(src_array):
        if src_array[i - 1] <= src_array[i]:
            i += 1
        else:
            src_array[i - 1], src_array[i] = src_array[i], src_array[i - 1]
            i = i if i == 1 else i - 1
    return src_array

def main():
    "main"

    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert sort([1, 2, 3, 3, 3, 4]) == [1, 2, 3, 3, 3, 4]
    assert sort([4, 3, 3, 3, 3, 2, 2, 2, 2, 1])\
        == [1, 2, 2, 2, 2, 3, 3, 3, 3, 4]
    assert sort([1, 3, 4, 2, 5, 7, 9, 8]) == [1, 2, 3, 4, 5, 7, 8, 9]
    #some more tests
    assert sort([]) == []
    assert sort([]) == []
    assert sort([]) == []
    assert sort([]) == []
    assert sort([]) == []
    assert sort([]) == []
    assert sort([]) == []

    print "OK!"
    raw_input()
    return 0

if __name__ == "__main__":    
    exit(main())
