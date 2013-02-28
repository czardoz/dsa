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
    
def main():
    a = [1,3,5,7,9,11,13,55]
    b = [2,4,44]
    c = merge(a, b)
    print c
    
if __name__ == '__main__':
    main()