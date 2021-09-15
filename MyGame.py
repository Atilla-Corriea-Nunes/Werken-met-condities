#This game was made by Atilla Correia Nunes :D

plgender = ("")
upgrade = False
endshop = False
c1 = ("")
c2 = ("")
c3 = ("")
c4 = ("")
c5 = ("")
c6 = ("")
c7 = ("")

money = ("none")

print("")
print("")
print(" Hello player! Welcome to my first game. This game is set in the medieval times, so no technology for you! In this game you'll be making choices to get different endings. there are ___ endings in total, try to get them all!")
print("")
plname = input("What is your name? ")
while (plgender != "m" or plgender != "f"):
    try:
        plgender = input("Are you a guy or a girl? (M/F) ")
        if (plgender.lower() == "m"):
            plgender = ("sir")
            coinholder = ("pouch")
            break
        elif (plgender.lower() == "f"):
            plgender = ("ma'am")
            coinholder = ("purse")
            break
        else:
            print("oops, thats an incorrect input. accepted inputs are m or f")
    except:
        continue

plage = input("How old are you? ")
print("")
if (int(plage) <= 17):
    print("lmao imagine being underage")
    print("anyways")
if (int(plage) >= 70):
    print("Jeez, you're old. i suspect all my jokes will fly over your head, but go ahead and play the game anyways")
if (int(plage) == 69):
    print("Nice")
if (int(plage) > 100):
    print("i know you're lying, stop inputing rediculously big numbers")
print("")
print("Now that that's done, lets get into the game")
print("")
print("")
print("You wake up in an uncomfortable bed. As you attempt to stand up you feel your back hurting. 'If i wasnt so goddamn poor i could actually afford a good bed' you think to yourself")
print("You open the door to your small shack. because you woke up pretty late the milkman has already delivered you the daily milk you always buy from him. there is a note attached 'i noticed you were asleep so i gave you your daily bottle of milk. no worries about the payment, its on the house'")
print("'That guy is awesome' you think to yourself as you take a swig of the milk. Its time to start yet another ordinary day...")
print("")
print("After getting ready to head out you grab your sword and your pickaxe and head to the village, after all thats where your job is")
print("You walk the path that goes to the village from your lonely shack thinking to yourself about the events that have happened recently but suddenly something catches your eye...")
print("When you look into the woods that surround the path you see something shining in the grass, what could it be?")
print("")
while (c1 != "yes" or c1 != "no"):
    try:
        c1 = str(input("Do you get off the path to investigate? (Yes/No) "))

        if (c1.lower() == "yes"):
            print("you decide to try your luck and investigate, what if its something valuable?")
            break
        elif (c1.lower() == "no"):
            print("Its probably nothing anyways, you think. ")
            break
        else:
            print("oops, thats an incorrect input. accepted inputs are yes or no")
    except:
        continue

if (c1.lower() == "no"):
    print("you continue on the path, ignoring whatever that shiny thing was and make your way to work. After all it would be ineffecient to spend your day doing anything else than working")

if (c1.lower() == "yes"):
    print("You approach the shiny object. you reach out to grab the object. 'Well, its my lucky day' you think as you inspect the coin you just found.")
    print("+1 coin!")
    print("You put the coin in your coin"+ str(coinholder) +" and as you are about to walk back to the path to continue your journey yet another thing catches your eye.")
    print("out in the distance you see what appears to be a person in the woods. You stand still in shock and then make your decision")

    while (c2 != "yes" or c2 != "no"):
        try:
            c2 = str(input("Go investigate the person in the woods? (Yes/No) "))

            if (c2.lower() == "yes"):
                 print("'Whoever that is, they must be in trouble. these woods are dangerous' you think to yourself")
                 break
            elif (c2.lower() == "no"):
                print("'Nope, not dealing with that, i already got my shiny coin' you think as you quickly get back on the path ")
                print("You make your way to work, you're slightly late due to the detour but it was worth it")
                money = ("low")
                break
            else:
                print("oops, thats an incorrect input. accepted inputs are yes or no")
        except:
             continue



if (c2.lower() == "yes"):
    print("You decide to be a hero and save whoever is in distress in these woods")
    print("as you walk closer to the person in the woods you realize its a young girl thats playing with some dolls. 'thats weird, i guess she must have wandered out too far' you think to yourself")
    print("You're just about to tap her on her shoulder to tell her shes too far in the woods when you feel your vision suddenly fading and your body falling to the ground...")
    print("")
    print("You wake up at the same location that you passed out. Its night now and there's no sight of the girl.'What just happened?' you think to yourself")
    print("You walk back to your little shack, still confused how that could've happened. You reach into your pockets to retrieve the keys to the front door but they're missing")
    print("'What? I swear i didnt forget my keys today, where did they go?' You say as you think out loud to yourself")
    print("Well, this leaves you with only 1 choice. You're going to have to head to the village to get a set of spare keys that you intrusted to your friend Sebastian")
    print("Having no choice you walk the path to the village. 'I hope he's still awake, it does seem to be quite late' you think")
    print("You arrive at the village. You had the strange feeling of being watched whilst traveling through the woods so you're glad to be in familliar territory.")
    print("But one thing is off... Where are all the people? there isn't a soul in sight in the village. it might be night but at this time you should at the very least expect to see a random drunkard wandering...")
    print("For a moment, your instincts kick in")

    while (c4.lower() != "run" or c4 != "stay"):
        try:
            c4 = str(input("What do you do? (Run/Stay) "))

            if (c4.lower() == "run"):
                 print("Filled with terror due to the strange situation you find yourself in you make a run back to your shack")
                 print("'its not worth staying here any longer, i'll just kick down the door when i get to my house'")
                 print("You run and run to your house, but the path feels like it takes way longer to reach your house then usual...")
                 print("But you keep running and running even though you get the feeling that your surroundings arent familliar")
                 print("What happened? Where did you run to when overtaken by panic? I guess nobody will ever know")
                 print("")
                 print("YOU GOT THE INSANITY ENDING: Running maniac!")
                 print("Thanks for playing the game! you got ending 1 out of ?! try to get all the endings")
                 exit()
            elif (c4.lower() == "stay"):
                print("You surpress the urge to run.'no need to panic, its probably nothing unusual' you tell yourself")
                print("You walk to Sebastian's house and knock on the door.'Hey sebastian, you still up?' you call out.")
                print("But before you hear a reply the door suddenly opens by itself...")
                print("'Woah, its unusual for Sebastian to leave his front door unlocked, especially during the night' you think")
                print("You make your way into the house to make sure your friend is alright")
                print("But there isnt a trace of him... 'Well, this is quite awfull' you think as you look around the almost empty house.")
                print("You spot the spare keys to your house. Getting home isn't more important then your friend but its nice to grab the keys so you dont forget later")
                print("As soon as your hand touches the keys you hear the sound of a voice. instinctively you turn around to see who was talking but nobody is around")
                print("'You're in danger' The voice says.'who are you?' you reply. the voice does remind you of Sebastian's voice but the location its coming from is completely empty... something is up... ")
                print("The voice calls out once more: 'A wave of madness will soon hit your world, but you can still be saved. take the path that goes to Riverdale and you can be saved'")
                print("in confusion you stand there for a moment. 'Riverdale is the big city thats quite a long way from the village' you remember")
                print("'Quickly! Not much time remains!' The voice says whilst fading away.")
                print("Its time for you to choose...")
                print("")

                break
            else:
                print("oops, thats an incorrect input. accepted inputs are Run or Stay")
        except:
             continue


if (c4.lower() == "Stay"):
    while (c5.lower() != "listen" or c5 != "ignore"):
        try:
            c5 = str(input("Do you listen to the advice or do you ignore it? (Listen/Ignore) "))

            if (c5.lower() == "listen"):
                print("")
                break
            elif (c5.lower() == "ignore"):
                print("There's no reason for you to trust this voice, you must find an actual person to talk to and quickly. This situation is extremely unsettling")
                print("You quickly grab your keys and stuff them in your pockets. You run out of the house in search of a living soul that could tell you what is happening ")
                print("Running around the village in distress you cant see anyone. All of the lights in the houses are off.")
                print("Finally you make it to the village church. The inside is lit! Great, there must be people in there")
                print("You open the doors to the church. As you look inside you hear loud chanting in a language you dont understand. The church is filled completely, every seat it taken by someone and theres a bunch of villagers chanting something at the very end")
                print("All of the villagers are wearing black robes with hoods and ignore your presense as you walk into the church 'What is happening? this must be the entire population of the village in here at the same time!' you think")
                print("You quickly look at the almost unrecognisable group of people that is chanting something hoping to recognize Sebastian")
                print("Thankfully you spot what looks to be Sebastian. You hurriedly get to him and tap him on his shoulder 'Sebastian, whats happening? Why is the entire village here? I need your help'")
                print("'Ah, "+ str(plname) +",you finally came. We were expecting you. Come join us now!' He says. The voice does not sound like Sebastian's")
                print("The hooded figure turns around to meet your eyes. When you look into his eyes you make the terrifying discovery that his eyes are completely blood red")
                print("You feel your body hitting the ground from pure shock as you lose conciousness...")
                print("")
                print("YOU GOT THE INSANITY ENDING: Doomed by the cult!")
                print("Thanks for playing the game! you got ending 2 out of ?! try to get all the endings")
                break
            else:
                print("oops, thats an incorrect input. accepted inputs are Run or Stay")
        except:
             continue



if (c1.lower() == "no" or c2.lower() == "no"):
    print("You arrive at the local village. You know the inhabbitants quite well since you have lived near their village for quite a while. Usually you start going to work in the mines at this time, but if you felt like it you could do something else...")

    while (c3.lower() != "work" or c3 != "shop"):
        try:
            c3 = str(input("Where do you want to go next? (Work/Shop) "))

            if (c3.lower() == "work"):
                 print("You head into the mines with your trusty pickaxe")
                 break
            elif (c3.lower() == "shop"):
                print("You enter the local shop, nothing in here truely interests you untill you notice something new... ")
                print("A new pickaxe! it looks very good and you are kinda in need of a new pickaxe...")
                break
            else:
                print("oops, thats an incorrect input. accepted inputs are Work or Shop")
        except:
             continue

if (c3.lower() == "shop"):
    print("you decide to ask the shopkeep how expensive this pickaxe is")
    print("'60 coins "+ str(plgender) +", this pickaxe was made by a legendary blacksmith and is extremely effective' he says")
    while (endshop != True):
        try:
            c2 = str(print("You look in your coin"+ str(coinholder) + "hoping to have enough to afford the pickaxe"))

            if (money == "low"):
                 print("You count up your coins. Exactly 60!'This has to be my luckiest day ever!' you think to yourself in joy")
                 print("'So, you gonna buy it?' the shopkeeper asks.")
                 print("You look 1 last time at your trusty old pickaxe and wish it farewell. You buy the pickaxe from the shopkeeper")
                 print("")
                 upgrade = True
                 endshop = True
                 money = "none"
                 break
            elif (money == "none"):
                print("You count up your coins. Unbelievable! exactly 59 coins... This must be a nightmare...")
                print("you sadly and slowly exit the shop in defeat. the shopkeeper kinda gives you a weird look but he doesnt know the pain of being 1 coin short")
                print("")
                endshop = True
                break
        except:
             continue

if (c3.lower() == "work" or upgrade == True):
    print("Ah, the good ol mines. Not the best job but it sure does put food on the table")
    print("You suddenly remember the rumor that crazy joe found a huge vein of gold in these mines and left our village as a rich man...")
    print("No way thats real though, gold hasnt been found in these mines in decades...")
    print("")
    if (upgrade == True):
        print("So, anyways. You grab out your newly bought pickaxe.'I sure hope that this thing is as good as the shopkeep said it would be' you think")
        print("You start hacking away at the wall of the cave, hoping to find valuables")
        print("As you are digging you notice that your s")


