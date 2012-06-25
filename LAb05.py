#archibold_acheampong
print 'Problem 2:','\n'

def factorial(integer):
    if integer==0:
        return 1
    else:
        return integer*factorial(integer-1)
number=int(raw_input('Please enter any integer :'))
print factorial(number)


print 'Problem 3:','\n'

def fibonacci(integer):
    if integer==0:
        return 0
    elif integer==1:
        return 1
    else:
        return fibonacci(integer-1)+fibonacci(integer-2)
number=int(raw_input('Please enter any integer :'))
#print fibonacci(number)
for x in range(1,number+1):
    print fibonacci(x),


print 'Problem 4:','\n'

def prime(integer):
    count=0
    for x in range(1,integer+1):
        if integer%x==0:
            count+=1
    if count==2:
        return 'True'
    else:
        return False 
    #return True
number=int(raw_input('Please enter any integer :'))
print prime(number)


print 'Challenge Problems:','\n'
print 'Problem 4:','\n'


def isPalindrome(string):
    count=0
    for x in range(0,int(len(string)/2)):
        print string[x],string[-(x+1)]
        if string[x]==string[-(x+1)]:
            count+=1
            #x+=1
    print count
    if count==int(len(string)/2):
        print 'is a palindrome'
    else:
        print 'is not a palindrome'
    #palindrome_test
string=raw_input('Please enter any string :')
print isPalindrome(string)


print 'Problem 5:','\n'

def isSubstring(string1,string2):

string1=raw_input('Please enter the first string :')
string2=raw_input('Please enter the second string :')
