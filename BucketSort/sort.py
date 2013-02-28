'''
Created on Aug 20, 2012

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

def busort(a, n):
    buckets = []
    result = []
    bucket_size = 1.0/n
    for i in range(0,n):
        buckets.append([])
    for i in a:
        buckets[int(i/bucket_size)].append(i)
    for bucket in buckets:
        isort(bucket)
    for bucket in buckets:
        for i in bucket:
            result.append(i)
    return result

def main():
    a = [.13,.526,.11,.22,.5,.7,.32,.26,.12,.55,0.42]
    c = busort(a,5)
    print c
    
if __name__ == '__main__':
    main()