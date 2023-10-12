#create a function that returns your full name and your age as functions 
def my_name_and_age(name,age):
    print(f"my name is {name} and i am {age}years old")
my_name_and_age("Edna",27)

# A function that reverses a string
def reversedString():
    text='1,2,3,4,a,b,c,d'
    newstring=text[::-1]
    print(f'This is reverserd string: {newstring}')
reversedString()
# mtd2
def reversedStr():
    text='1,2,3,4,a,b,c,d'
    newstring=list(text)
    newstring.reverse()
    
    n=''.join(newstring)
    print(type(n))
    print(f'This is reverserd string: {n}')
reversedStr()
# function to sum all evennumbers in alist [8,2,3,0,7]
def sumOfEvenNumbers():
    listOfNumbers=[8,2,3,-1,7]
    sum1=0
    for x in listOfNumbers:
       sum1*=x
    print(f'Sum of even numbers= {sum1}')
sumOfEvenNumbers()

# function to multiply all numbers in alist [8,2,3,3,-1,7]
def product():
    listOfNumbers=[8,2,3,-1,7]
    pdt=1
    for x in listOfNumbers:
        pdt*=x
    print(f'Product ={pdt}')
product()
# function to print even numbers in a list
def evenNumber():
    numbers=(1,2,3,4,5,6,7,8,9)
    mylist=[]
    for x in numbers:
        if x%2==0:
         mylist.append(x)
    print(f'EvenNumbers={mylist}')
evenNumber()         

