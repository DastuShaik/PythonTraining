"""
Python Program to count even numbers in a list assuming '0' as even 

"""

#print('Enter the numbers in the list:')
c=0
#lst=list(map(int,input().split()))
lst=[2,4,4,5,2,55,0,54,45,12]
for i in range(len(lst)):
	if lst[i]%2==0: c+=1
print(c)
