'''
Created on Sep 8, 2012

@author: czardoz
'''

def maxsubarray(a):
    for j in range(0,len(a)):
        netsum = -1000000
        s = 0    
        for i in range(0,len(a)-j):
            s = s + a[i]
            if s > netsum:
                netsum = s
                max_r = i
    return s, max_r

def main():
    a  = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print maxsubarray(a)


if __name__ == '__main__':
    main()