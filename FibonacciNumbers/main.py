'''
Created on Oct 26, 2012

@author: czardoz
'''

def fib(n):
    f_nos=[]
    f_nos.append(1)
    f_nos.append(1)
    for i in range(2,n+1):
        f_nos.append(f_nos[i-2]+f_nos[i-1])
    return f_nos[-1]

def main():
    n = int(raw_input("Enter Number: "))
    f = fib(n)
    print f

if __name__ == '__main__':
    main()