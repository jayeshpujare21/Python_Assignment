#!/usr/bin/python

def main():
	i=[]
	i=input('Enter input list ')
	i=i.split()
	print(i)
	o=[]
	o=input('Enter new order ')
	o=o.split()
	print(o)
	op=sorted(i, key = lambda word: [o.index(d) for d in word]) 
	for a in op:
		print(a,end=' ')
	

if __name__=='__main__':
	main()
