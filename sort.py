#!/usr/bin/python
def last(t):
    return t[-1]
    
def main():
        l=[]
        l=input("Enter list of tuples serparated by space")
        l=l.split(',')
        a=sorted(l, key=last)
        print(a)

if __name__=='__main__':
	main()
    
