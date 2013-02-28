'''
Created on Aug 19, 2012

@author: czardoz
'''

def swap(a, i ,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def bsort(a):
    while 1:
        swapped = False
        for i in range(0,len(a)-1):
            if a[i] > a[i+1]:
                swap(a,i+1,i)
                swapped = True
        if not swapped:
            break
    return a

def main():
    a = [13,526,11,22,5,7,32,26,12,55,0]
    c = bsort(a)
    print c
     
if __name__ == '__main__':
    main()