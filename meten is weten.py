print('geef 2 cijfers, daarna rekent de computer uit of het eerste cijfer het kleinste getal is, het grootste of dat ze gelijk zijn')
a = int(input("voer cijfer a in: "))

b = int(input("voer cijfer b in: "))

if (a > b):

    Max = a
    Min = b

    print('a is het grootste getal: '+ str(Max) +'')

    print('het minumum is: '+ str(Min)+'')
    print('het maximum is: '+ str(Max)+'')

elif (a < b):

    Min = a
    Max = b 

    print('a is het kleinste getal: '+ str(Min)+'')

    print('het minumum is: '+ str(Min)+'')
    print('het maximum is: '+ str(Max)+'')
    
else:

    print('a en b zijn even groot')

