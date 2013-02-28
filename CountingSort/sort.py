'''
Created on Aug 20, 2012

@author: czardoz
'''

def getmax(a):
    maxi = 0
    for i in range(0,len(a)):
        if a[i] > a[maxi]:
            maxi = i
    return maxi

def csort(a):
    maxn = a[getmax(a)]
    counts = []
    for i in range(0,maxn+1):
        counts.append(0)
    for i in a:
        counts[i-1]+=1
    for i in range(1,maxn+1):
        counts[i-1]+=counts[i-2]
    print a
    print counts
    return []

def main():
    a = [5,8,2,7,3,4]
    c = csort(a)
    print c
    
if __name__ == '__main__':
    main()