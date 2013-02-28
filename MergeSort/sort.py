'''
Created on Aug 19, 2012

@author: czardoz
'''

def merge(a, b):
    result = []
    j = 0
    i = 0
#    swap if lengths not as assumed
#    a is shorter than b
    if len(a) > len(b):
        temp = a
        a = b
        b = temp
    while 1:
        if a[i] < b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
        if j == len(b):
            result.extend(a[i:])
            break
        if i == len(a):
            result.extend(b[j:])
            break
    return result

def msort(a):
    if len(a) <= 1:
        return a
    middle = len(a)/2
    left = msort(a[:middle])
    right = msort(a[middle:])
    result = merge(left, right)
    return result

def main():
    a = [13,526,11,46,1000,22,5,7,32,26,12,55,0,619]
    c = msort(a)
    print c
    
if __name__ == '__main__':
    main()