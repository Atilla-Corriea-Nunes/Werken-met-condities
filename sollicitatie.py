failbool = False
print("Solicitatie Circusdirecteur voor Circus HotelDeBotel")
print("u zal wat vragen krijgen om te constanteren of u deze positie kan nemen")
print(" ")
q1 = input("hoeveel jaren heeft u praktijk ervaring met dieren-dressuur? ")
r4 = input("heeft u ooit een donatie gedaan aan een goed doel? ")
q12 = input("hoeveel jaar heeft u ervaring met jongleren? ")
r1 = input("heeft u een iq level die hoger is dan 2? ")
q13 = input("hoeveel jaar heeft u praktijkervaring met acrobatiek? ")
q2 = input("bent u in bezit van een MBO-4 ondernemen diploma? (Ja/Nee) ")
r2 = input("Vind u kwark meer lekker dan vla? (Ja/Nee) ")
q3 = input("bent u in bezit van een geldig vrachtwagen rijbewijs? (Ja/Nee) ")
q4 = input("bent u in bezit van een hoge hoed? (Ja/Nee) ")
r3 = input("hoe lang kan uw adem houden onderwater? ")
q5 = input("bent u een man of een vrouw? (M/V) ")
if (q5.lower() == "m"):
    q52 = 21
    q51 = input("heeft u een snor en zo ja wat is de breedte in cm? (als u geen snor heeft vul 'geen' in) ")
    if (q51.lower() == "geen"):
        failbool = True
        q51 = 9

elif (q5.lower() == "v"):
    q51 = 11
    q52 = input("draag je rood krulhaar en zo ja wat is de lengte in cm? (als u geen rood krulhaar heeft vul 'geen' in ")
    if (q52.lower() == "geen"):
        failbool = True
        q52 = 19
else:
    print('verkeerde input, probeer nog een keer')
    exit()    

q6 = input("wat is uw lengte in centimeters? ")
q7 = input("hoeveel weegt u in kilos? ")
q8 = input('heeft u het certificaat “Overleven met gevaarlijk personeel”? (Ja/Nee) ')

if (int(q1) < 4 or int(q12) < 5  or int(q13) < 3, q2.lower() == "ja", q3.lower() == "ja", q4.lower() == "ja", int(q51) < 10, int(q52) < 20, int(q6) < 149, int(q7) < 89 , q8.lower() == "ja", failbool == False):
    print(" ")
    print("Goed nieuws: u bent aangenomen!")

else:
    print(" ")
    print("sorry, u bent niet geaccepteerd..")
