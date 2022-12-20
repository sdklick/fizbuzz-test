'''
write a program that prints from 1 to 30 but for multiple of three
print 'fizz' instead of number and for the multiple of the five print
'buzz' for number which are both multiple three and five print 'fizbuzz'
this is famously known as fizbuzz test

'''
lownum=int(input('Enter Start number : '))
highnum=int(input('Enter Ending number : '))

for x in range(lownum, highnum+1):
    if (x % 3 == 0) and (x % 5 == 0):
        print('fizbuzz')
    elif x % 5 == 0:
        print('buzz')
    elif x % 3 == 0:
        print("fizz")
    else:
        print(x)    
