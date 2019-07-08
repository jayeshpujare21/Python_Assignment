#!/usr/bin/python

def main():
	n=int(input("Enter number of pairs: "))
	el = []
	op = []
	for x in range(n):
		s = input("Enter the names of employees: ")
		el.append(set(s.split()))
	for i in el:
		for j in el:
			if i != j and not i.isdisjoint(j):
				el.append(i | j)
				el.remove(i)
				el.remove(j)
				break

	print("The list is: " + str(el))

	s2=input("Enter the pair: ")
	op = s2.split()
	f=0
	for i in el:
		if (op[1]) in i and (op[0]) in i:
			f=1
		else:
			f=0
	if f==1:
		print('Employees are connected')
	else:
		print('Employees are NOT connected')
if __name__=='__main__':
	main()
