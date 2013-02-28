'''
Created on Aug 19, 2012

@author: czardoz
'''

def getmin(a):
    mini = 0
    for i in range(0,len(a)):
        if a[i] < a[mini]:
            mini = i
    return mini

def swap(a, i ,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def isort(a):
    if len(a) <= 1:
        return a
    mini = getmin(a)
    swap(a,0,mini)
    for i in range(2,len(a)):
        key = a[i]
        j = i-1
        while(a[j] > key):
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
    return a

def main():
    a = [13,526,11,22,5,7,32,26,12,55,0]
    c = isort(a)
    print c
    
if __name__ == '__main__':
    main()