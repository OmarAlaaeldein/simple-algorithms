#I tried implementing most of the functions without resorting to any external libraries or built-in functions
def Avg(a):
    counter,length=0,0#declare a counter to find sum
    try:
        for i in a:#Traverse over the list
            counter,length=counter+i,length+1#Use counter to calculate sum of list
            assert (type(i))==int,"Operand type is incorrect"
        return counter/length
    except (TypeError,ValueError):
        return 'Operand type is incorrect'
#print(Avg([1,2,3])) #outputs a correct answer
#print(Avg([1,2.5,3]))# raises an exception due to float values
#print(Avg([1,'s',3])) #raises an exception due to type error
def Vowels(b):#a,e,i,o,u
    assert type(b)==str,"variable is not str"
    b=b.lower()#convert all letters to lowercase since python distinct between upper and lower case letters
    assert b.isalpha()==True,"Not alphabet"
    counter=0#declare counter to count instances of vowels in our string
    for i in b:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            counter+=1
    return counter
#print(Vowels(['d'])) #list raise assertion error
#print(Vowels(1)) #int or float raise exception
#print(Vowels('Omar2'))# assertion error since 2 is not in alphabet set
#print(Vowels('omar'))#Works just fine
def Swap(a,b):
    try:
        return b,a#tuple swap
    except:
        return 'Not valid inputs'
#print(Swap(3,2)) #works great
#print(Swap(3,None))# also works fine
#to be honest the only case I think which will cause compilation error where there are more or less than 2 positional values
# a,b=Swap(a,b)#typical usage of that function
# we can just use a,b=b,a
def No_odd(N):
    assert type(N)==int,'Input parameter is not integer'
    assert N>0,'Input parameter is less than zero'
    return [i for i in range(1,2*N,2)]#based on the observation that n odd number will occur in 2n numbers
#print(No_odd(-5))#assertion error since N less yhan or equal zero
#print(No_odd('s'))#not integer
def Volume_Sphere(r):
    assert type(r)==int or type(r)==float,'not a real number'#operand type is invalid
    assert r>0,'less than zero'#if r less than zero then error
    return (22/7)*r**3*(4/3)
#print(Volume_Sphere(3))#works great
#print(Volume_Sphere(-3))#error since volume can't be negative
#print(Volume_Sphere('d'))#wrong operand
def GCD(a,b):
    try:
        assert b!=0 and a!=0,'No GCD' #no GCD for zero
        if a<0:     #if any of a or b is less than zero convert to absolute value
            a=abs(a)
        elif b<0:    
            b=abs(b)
        while min(a,b)!=0:# aplies euclidean algorithm
            if a>=b:
                a=a%b
            elif b>=a:
                b=b%a
        return max(a,b) #when any or a or b becomes zero break loop and return other value
    except(ValueError,TypeError):
        return 'Operand type not valid'
#print(GCD(10,35))#works well
#print(GCD('s',35))#not valid
#(GCD(0,35))#raise assertion error
print(GCD(10,-35))#works great
#Done!