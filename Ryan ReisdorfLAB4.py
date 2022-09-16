#1
for count in range(0,100):
	count+=1
	num=count**2
	a=num%10
	if a==4:
		print(num)	
#2
for value in range(1):
	nmbr=list(map(int,input("Enter 5 positive numbers: ").split()))
	largestNmbr= max(nmbr)
	print(largestNmbr,"is the largest number")
#3	
import random
x=random.randint(5,10)
for i in range(x):
	print("Hello")
#4    
sentence=input("Enter string: ")
vowel='a'+'e'+'o'+'i'+'u'
print(*[i for i in sentence if i in vowel])    
#5    
a=input("Enter string: ")
b='a'
for i in range(len(a)):
    if a[i]  == b:
        print("The letter a can be found at ",i)
#6
a=input('enter string: ')
if a[0].isalpha():
    print('string starts with a letter')
else:
    print('string does not start with a letter')
