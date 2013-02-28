'''
Created on Oct 23, 2012

@author: czardoz
'''
import pprint

def lcs(x ,y):
    m = len(x)
    n = len(y)
    b=[[0]*(n) for i in xrange(m)]
    c=[[0]*(n) for i in xrange(m)]
    for i in range(1,m):
        for j in range(1,n):
            if x[i]==y[j]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 1
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    pprint.pprint(c)
    pprint.pprint(b)
    
def main():
    x = ['z','A','B','C','B','D','A','B']
    y = ['z','B','D','C','A','B','A']
    lcs(x,y)
    
if __name__ == '__main__':
    main()