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

def selsort(a):
    mini = getmin(a)
    swap(a, 0, mini)
    for i in range(0,len(a)-1):
        mini = i + getmin(a[i:])
        swap(a, i-1, mini)
    return a
    

def main():
    a = [13,55,11,22,5,7,32,26,12,526,0]
    c = selsort(a)
    print c
    
if __name__ == '__main__':
    main()