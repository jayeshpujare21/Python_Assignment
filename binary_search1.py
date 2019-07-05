#!/usr/bin/python
def binary_search(list,l,r,n):
    try:
        mid=int(l+(r-l)/2)
        print(mid)
        print(list[l:mid])
        print(list[mid:r])
        if n == list[mid]:
            print("Index of element ", n ," is ",mid)
        elif n < list[mid]:
            binary_search(list,l,mid,n)
        else:
            binary_search(list,mid,r,n)     
    except:
        print("Element Not Found")

    
def main():
        l=[]
        l=input("Enter elements of list serparated by space")
        list=l.split()
        print(list)
        n=input("Enter element to be search ")
        binary_search(list,0,len(list),n)

if __name__=='__main__':
	main()
    
