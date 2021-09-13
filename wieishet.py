q1 = input('is de kaas geel? (Ja/Nee) ')

if (q1.lower() == "ja"):

    q2 = input('Zitten er gaten in? (Ja/Nee) ')

    if (q2.lower() == "ja"):

        q3 = input('is de kaas belachelijk duur? (Ja/Nee) ')

        if (q3.lower() == "ja"):
            print('Uw kaas is emmenthaler')
        
        else:
            print('Uw kaas is leerdammer')

    else:

        q6 = input('is de kaas hard als steen? (Ja/Nee) ')

        if (q6.lower() == "ja"):
            print('uw kaas is pammigiano reggiano')

        else:
            print('uw kaas is goudse kaas')


else:

    q4 = ('heeft de kaas blauwe schimmel? (Ja/Nee) ')

    if (q4.lower() == "ja"):
        q5 = input('heeft de kaas een korst? (Ja/Nee) ')

        if (q5.lower() == "ja"):

            print('uw kaas is Blue de Rochbaron')

        else:
            print("uw kaas is fourme d'Ambert")

    else:

        q7 = input('Heeft de kaas een korst? (Ja/Nee) ')

        if (q7.lower() == "ja"):

            print('uw kaas is camembert')
        
        else:

            print('uw kaas is mozzerella')

