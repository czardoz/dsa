'''
Created on Aug 19, 2012

@author: czardoz
'''

def bsearch(array, value):
    lower = 0
    upper = len(array)-1
    while lower < upper-1:
        middle = (lower+upper+1)/2
        if value > array[middle]:
            lower = middle
        else:
            upper = middle
    if array[upper] == value:
        return upper
    else:
        return -1

def main():
    array = [10,12,20,23,27,30,31,39,42,44,45,49,57,63,70]
#    array = [1,4,6,8,10,12]
    value = 39
    i = bsearch(array, value)
    print i

if __name__ == '__main__':
    main()