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
c8 = ("")
c9 = ("")
c10 = ("")
i1 = ("")
i2 = ("")
i3 = ("")
retry = ("")
gameisfinished = False

money = ("59")

print("")
print("")
print(" Hello player! Welcome to my first game. This game is set in the medieval times, so no technology for you!")
print(" In this game you'll be making choices to get different endings. There are 4 Regular endings and 3 Special insanity endings total, try to get them all!")
print("")
plname = input("What is your name? ")
while (plgender.lower() != "m" or plgender.lower() != "f"):
    try:
        plgender = input("Are you a guy or a girl? (M/F) ")
        if (plgender.lower() == "m"):
            plgender = ("sir")
            plgender2 = ("mr.")
            informalgender = ("guy")
            coinholder = ("pouch")
            break
        elif (plgender.lower() == "f"):
            plgender = ("ma'am")
            plgender2 = ("ms.")
            coinholder = ("purse")
            informalgender = ("girl")
            break
        else:
            print("Oops, thats an incorrect input. accepted inputs are m or f")
    except:
        continue

plage = input("How old are you? ")
print("")
if (int(plage) <= 17 and int(plage) > 10):
    print("Lmao imagine being underage")
    print("Anyways")
if (int(plage) >= 70 and int(plage) <= 100):
    print("Jeez, you're old. I suspect all my jokes will fly over your head, but go ahead and play the game anyways")
if (int(plage) == 69):
    print("Nice")
if (int(plage) > 100):
    print("I know you're lying, stop inputing rediculously big numbers")
if (int(plage) < 10 ):
    print("Lmao you're a little baby. Goo goo ga ga")

print("")
print("Now that that's done, lets get into the game")
print("")
print("")
print("You wake up in an uncomfortable bed. As you attempt to stand up you feel your back hurting. 'If i wasnt so goddamn poor i could actually afford a good bed' you think to yourself")
print("You open the door to your small shack. Because you woke up pretty late the milkman has already delivered you the daily milk you always buy from him. There is a note attached 'I noticed you were asleep so i gave you your daily bottle of milk. No worries about the payment, its on the house'")
print("'That guy is awesome' you think to yourself as you take a swig of the milk. Its time to start yet another ordinary day...")
print("")
print("After getting ready to head out you grab your sword and your pickaxe and head to the village. after all, thats where your job is")
print("You walk the path that goes to the village from your lonely shack thinking to yourself about the events that have happened recently but suddenly something catches your eye...")
print("When you look into the woods that surround the path you see something shining in the grass, what could it be?")
print("")
while (c1.lower() != "yes" or c1.lower() != "no"):
    try:
        c1 = str(input("Do you get off the path to investigate? (Yes/No) "))
        print("")
        if (c1.lower() == "yes"):
            print("You decide to try your luck and investigate, what if its something valuable?")
            break
        elif (c1.lower() == "no"):
            print("Its probably nothing anyways, you think. ")
            break
        else:
            print("Oops, thats an incorrect input. accepted inputs are yes or no")
    except:
        continue

if (c1.lower() == "no"):
    print("You continue on the path, ignoring whatever that shiny thing was and make your way to work. After all it would be ineffecient to spend your day doing anything else than working")

if (c1.lower() == "yes"):
    print("You approach the shiny object. you reach out to grab the object. 'Well, its my lucky day' you think as you inspect the coin you just found.")
    print("+1 coin!")
    print("You put the coin in your coin"+ str(coinholder) +" and as you are about to walk back to the path to continue your journey yet another thing catches your eye.")
    print("Out in the distance you see what appears to be a person in the woods. You stand still in shock and then make your decision")
    print("")
    money = ("60")

    while (c2 != "yes" or c2 != "no"):
        try:
            c2 = str(input("Go investigate the person in the woods? (Yes/No) "))
            print("")
            if (c2.lower() == "yes"):
                 print("'Whoever that is, they must be in trouble. these woods are dangerous' you think to yourself")
                 break
            elif (c2.lower() == "no"):
                print("'Nope, not dealing with that, i already got my shiny coin' you think as you quickly get back on the path ")
                print("You make your way to work, you're slightly late due to the detour but it was worth it")
                break
            else:
                print("Oops, thats an incorrect input. accepted inputs are yes or no")
        except:
             continue



if (c2.lower() == "yes"):
    print("You decide to be a hero and save whoever is in distress in these woods")
    print("As you walk closer to the person in the woods you realize its a young girl thats playing with some dolls. 'Thats weird, i guess she must have wandered out too far' you think to yourself")
    print("You're just about to tap her on her shoulder to tell her shes too far in the woods when you feel your vision suddenly fading and your body falling to the ground...")
    print("")
    print("You wake up at the same location that you passed out. Its night now and there's no sight of the girl.'What just happened?' you think to yourself")
    print("You walk back to your little shack, still confused how that could've happened. You reach into your pockets to retrieve the keys to the front door but they're missing")
    print("'What? I swear i didnt forget my keys today, where did they go?' You say as you think out loud to yourself")
    print("Well, this leaves you with only 1 choice. You're going to have to head to the village to get a set of spare keys that you intrusted to your friend Sebastian")
    print("Having no choice you walk the path to the village. 'I hope he's still awake, it does seem to be quite late' you think")
    print("You arrive at the village. You had the strange feeling of being watched whilst traveling through the woods so you're glad to be in familliar territory.")
    print("But one thing is off... Where are all the people? There isn't a soul in sight in the village. It might be night but at this time you should at the very least expect to see a random drunkard wandering...")
    print("For a moment, your instincts kick in")

    while (c4.lower() != "run" or c4.lower() != "stay" ):
        
            c4 = str(input("What do you do? (Run/Stay) "))
            print("")
            if (c4.lower() == "run"):
                 print("Filled with terror due to the strange situation you find yourself in you make a run back to your shack")
                 print("'Its not worth staying here any longer, i'll just kick down the door when i get to my house'")  
                 print("You run and run to your house, but the path feels like it takes way longer to reach your house then usual...")
                 print("But you keep running and running even though you get the feeling that your surroundings arent familliar")
                 print("What happened? Where did you run to when overtaken by panic? I guess nobody will ever know")
                 print("")
                 print("YOU GOT THE INSANITY ENDING: Running maniac!")
                 print("Thanks for playing the game! you got ending 1 out of 7! try to get all the endings")
                 quit()
            elif (c4.lower() == "stay"):
                print("You surpress the urge to run.'no need to panic, its probably nothing unusual' you tell yourself")
                print("You walk to Sebastian's house and knock on the door.'Hey sebastian, you still up?' you call out.")
                print("But before you hear a reply the door suddenly opens by itself...")
                print("'Woah, its unusual for Sebastian to leave his front door unlocked, especially during the night' you think")
                print("You make your way into the house to make sure your friend is alright")
                print("But there isnt a trace of him... 'Well, this is quite awfull' you think as you look around the almost empty house.")
                print("You spot the spare keys to your house. Getting home isn't more important then your friend but its nice to grab the keys so you dont forget later")
                print("As soon as your hand touches the keys you hear the sound of a voice. instinctively you turn around to see who was talking but nobody is around")
                print("'You're in danger' The voice says.'who are you?' you reply. The voice does remind you of Sebastian's voice but the location its coming from is completely empty... something is up... ")
                print("The voice calls out once more: 'A wave of madness will soon hit your world, but you can still be saved. Take the path that goes to Riverdale and you can be saved'")
                print("In confusion you stand there for a moment. 'Riverdale is the big city thats quite a long way from the village' you remember")
                print("'Quickly! Not much time remains!' The voice says whilst fading away.")
                print("Its time for you to choose...")
                print("")

                break
            else:
                print("Oops, thats an incorrect input. accepted inputs are Run or Stay")
        


if (c4.lower() == "stay"):
    while (c5.lower() != "listen" or c5.lower() != "ignore"):

            c5 = str(input("Do you listen to the advice or do you ignore it? (Listen/Ignore) "))
            print("")
            if (c5.lower() == "listen"):
                print("'This isn't any normal situation, if i want to make it out here alive i should listen to his advice'")
                print("You quickly grab your keys on your way out of the house")
                print("You make your way to the path to Riverdale. You never noticed but this path that leads to Riverdale goes right past your house")
                print("As you walk back into the woods this time instead of feeling like you're being watched you feel like a guardian is looking over you, protecting you")
                print("You reach your house, but that isn't your destination. its time to head further into Riverdale")
                print("Although, it would be extremely easy to just get into your home right now. You still have the spare keys from sebastian's house. Your body is exhausted from panicing all day so you could use a rest...")
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
                print("Thanks for playing the game! You got ending 2 out of 7! Try to get all the endings")
                quit()
                break
            else:
                print("Oops, thats an incorrect input. accepted inputs are Run or Stay")


if (c5.lower() == "listen"):
    while (c6.lower() != "home" or c6.lower() != "continue"):
            c6 = str(input("Do you go home or do you continue your journey? (Home/Continue) "))
            print("")
            if (c6.lower() == "home"):
                print("You decide that this has been more than enough stress for one day and that you need to get a good night's rest in order to think right")
                print("You walk up to the door of your shack and hesitate, but then you put the keys into the door. The door unlocks")
                print("'Finally im home safe' you think to yourself")
                print("You take 1 step into your house and then... your foot never touches the floor. The place where the floor of your house is supposed to be is a giant hole")
                print("As you take the step into the infinite abyss you scream in terror. Quickly your entire vision becomes filled with the pure blackness of the void. Out here there's no one to hear your screams...")
                print("")
                print("YOU GOT THE INSANITY ENDING: Unending fall into the abyss!")
                print("Thanks for playing the game! you got ending 3 out of 7! try to get all the endings")
                quit()
            elif (c6.lower() == "continue"):
                print("'No, i didnt get this far just to give up' you think. You continue past your house.")
                print("Soon you reach the river that devides the woods and an open grassy area")
                print("You dont come here often but you're sure that the path leads to a brigde to cross this river")
                print("One problem though: the bridge you remember is nowhere to be seen")
                print("You look around, trying to find a way to cross the bridge")
                print("Whislt you are looking for around for a solution you spot a cave entrance, but something about it is different.")
                print("The outside is decorated with torches that burn a bright green color. You get the feeling that the guardian that protects you wants you to go there")
                print("Seeing no better choice you head into the cave")
                print("The inside of the cave is decorated with skulls and is lit by more torches that burn with green fire.")
                print("even though the place feels strange, you have a weird calm feeling.")
                print("You reach the end of the cave and are met with a huge stone door.")
                print("There is an inscription that reads: 'The "+ str(informalgender) +" that has met the fate of insanity all three times holds the key to unlock safety. Input the correct code to pass")
                print("Underneath inscription there are 4 buttons: up, down, left and right.")
                print("")
                break
            else:
                print("Oops, thats an incorrect input. accepted inputs are Home or Continue")


if (c6.lower() == "continue"):
    while (c7.lower() != "solution" or c7.lower() != "help"):
        try:
            c7 = str(input("Do you want to attempt to put in a solution or call out for help? (Solution/Help) "))
            print("")
            if (c7.lower() == "solution"):
                print("You feel like you know the solution to the puzzle and start to input the code")
                break
            elif (c7.lower() == "help"):
                print("You call out desperately for help one last time, hoping that your guardian responds")
                print("After a couple of seconds of silence you can hear the same voice that you heard in Sebastians's house")
                print("'every time you meet that girl in the forest there will be a path that leads to you going insane. Go down all 3 of those paths and look at the first letter of each ending. R = Right, U = Up, D = down and L = left. Then, put in the code in the same order as the endings are numbered. Only then can you survive this nightmare' ")
                print("Then, the voice fades away one last time")
                print("Thats it then, my only choice is to input the code...")
                print("")
                break
            else:
                print("oops, thats an incorrect input. accepted inputs are Solution or Help")
        except:
             continue

if (c7.lower() == "solution" or c7.lower() == "help"):
    while (i1.lower() != "right" and i2.lower() != "down" and i3.lower() != "up"):

            i1 = str(input("First input (Up/Down/Left/Right)"))
            i2 = str(input("Second input (Up/Down/Left/Right)"))
            i3 = str(input("Third input (Up/Down/Left/Right)"))
            print("")
            if (i1.lower() == "right" and i2.lower() == "down" and i3.lower() == "up"):
                print("You press the correct arrows in a row, not sure how you knew the solution...")
                print("Whatever, its time for you to get inside this cave and into safety")
                print("You look around at the inside of the cave. it appears to be filled with provisions: food and water, as you look around you notice the door has shut behind you")
                print("You find yet another inscription, it reads: 'Welcome "+ str(plname) +" if you're reading this the corruption has begun to spread to our village. This land has held an ancient curse that would be awoken by a wandering demon that disguises herself as a little girl playing with dolls'")
                print("You stop reading for a second to realize the girl you saw in the woods must have been what started all this, still in shock of the situation you continue reading")
                print("'For centuries our village has attempted to disspell the curse to no avail. We were never sure when the corruption would start but if you're here it means i must have lead you here in some way. The only option you have is to hide in this special bunker that can resist the corruption. There's food and water for you to survive. The door opens automatically after the corruption has stopped. best of luck to you' signed - Sebastian")
                print("Wow, unbelievable. I guess your only option is to wait")
                print("")
                print("1 MONTH LATER")
                print("")
                print("Its been a long time. You no longer know if its day or night due to the fact that no sunlight shines outside. One day the loud sound of the door opening is heard through the bunker. You gather your belongings and leave the cave")
                print("You take your first look out of the cave in a long time. All of the plants and trees have died. It almost looks like a wildfire came through here... Its time for you to venture out and find civilization, if there is any left...")
                print("")
                print("YOU GOT THE SECRET ENDING: The true ending!")
                print("Thanks for playing the game! you got ending ? out of 7! This is the secret and final ending. Congratulations on getting here!")
                quit()
            else:
                print("That seems to be the wrong solution...")
                
                while (retry.lower() != "yes" or retry.lower() != "no"):
                
                        retry = str(input("Would you like to try again? (Yes/No) "))
                        print("")
                        if (retry.lower() == "yes"):
                             print("You try to input the code again")
                             break
                        elif (retry.lower() == "no"):
                             print("Confused by the meaning of this puzzle you fall on the ground defeated. Now that you've given up you're sure its not long before the madness consumes you")
                             print("")
                             exit()
                        else:
                             print("Oops, thats an incorrect input. Accepted inputs are Yes or No")
                             continue
            continue                 
            

if (c1.lower() == "no" or c2.lower() == "no"):
    print("You arrive at the local village. You know the inhabbitants quite well since you have lived near their village for quite a while. Usually you start going to work in the mines at this time, but if you felt like it you could do something else...")

    while (c3.lower() != "work" or c3 != "shop"):

            c3 = str(input("Where do you want to go next? (Work/Shop) "))
            print("")
            if (c3.lower() == "work"):
                 print("You head into the mines with your trusty pickaxe")
                 print("")
                 break
            elif (c3.lower() == "shop"):
                print("You enter the local shop, nothing in here truely interests you untill you notice something new... ")
                print("A new pickaxe! It looks very good and you are kinda in need of a new pickaxe...")
                print("")
                break
            else:
                print("Oops, thats an incorrect input. Accepted inputs are Work or Shop")


if (c3.lower() == "shop"):
    print("You decide to ask the shopkeep how expensive this pickaxe is")
    print("'60 coins "+ str(plgender) +", this pickaxe was made by a legendary blacksmith and is extremely effective' he says")
    while (endshop != True):
            c2 = str(print("You look in your coin"+ str(coinholder) + "hoping to have enough to afford the pickaxe"))
            print("")
            if (money == "60"):
                 print("You count up your coins. Exactly 60!'This has to be my luckiest day ever!' You think to yourself in joy")
                 print("'So, you gonna buy it?' the shopkeeper asks.")
                 print("You look 1 last time at your trusty old pickaxe and wish it farewell. You buy the pickaxe from the shopkeeper")
                 print("")
                 upgrade = True
                 endshop = True
                 money = "0"
                 break
            elif (money == "59"):
                print("You count up your coins. Unbelievable! exactly 59 coins... This must be a nightmare...")
                print("You sadly and slowly exit the shop in defeat. The shopkeeper kinda gives you a weird look but he doesnt know the pain of being 1 coin short")
                print("")
                endshop = True
                break


if (c3.lower() == "work" or endshop == True):
    print("Ah, the good ol mines. Not the best job but it sure does put food on the table")
    print("You suddenly remember the rumor that crazy joe found a huge vein of gold in these mines and left our village as a rich man...")
    print("No way thats real though, gold hasnt been found in these mines in decades...")
    print("")
    if (upgrade == True):
        print("So, anyways. You grab out your newly bought pickaxe.'I sure hope that this thing is as good as the shopkeep said it would be' you think")
        print("You start hacking away at the wall of the cave, hoping to find valuables")
        print("As you are digging you notice that your speed is quite a bit faster then your co-workers")
        print("'This thing truely does work!' You think as you efortlesly make your way through the rock")
        print("After a bit of mining you manage to find a valuable power crystal")
        print("'Wow, this is so rare i dont even know what its worth' You think")
        print("You dont give up there, though.  After even more digging you manage to find other small transparent crystals worth aproximately 10 coins")
        print("Its become late in the night so you get out of the mines for the day. As you exit the mines you have a big smile on your face, knowing that you made a lot of money today")
        print("")    

    if (c3.lower() == "work"):
        print("Its just another regular day in the mines. You gather up your strength to make it through another hard day of working")
        print("You mine untill the evening. it was an average day, you manged to find a couple of transparent crystals which are worth aproximately 10 coins")
        print("You head out of the mines quite tired and walk to the shop to sell your transparent crystals")
        print("With your coin"+ str(coinholder) +" 10 coins heavier you start to head home")
        print("")


if (c3.lower() == "work" or endshop == True and upgrade == False):
    print("As you walk in the village on your way to your house you hear a commotion")
    print("A messanger has arrived on horseback from the nearest big city called 'Riverdale'")
    print("The village folk are trying to calm him down as he is trying to tell them a panicked story")
    print("Curious about the commotion you decide to join the crowd and listen to what the messanger has to say")
    print("'A war has broken out between Riverdale and Merringnar, all of Riverdale has feared the possibility of war between the 2 cities and if we dont get reinforcements soon all of the city inhabitants are doomed' He explains")
    print("'The king of Merringnar is an evil tyrant, he killed my mommy and daddy' A kid from the crowd says")
    print("You think for yourself what you should do...")
    print("")

    while (c8.lower() != "join" or c8.lower() != "dont"):

            c8 = str(input("Do you join the cause or do you go on with your day (Join/Dont) "))
            print("")
            if (c8.lower() == "join"):
                print("You raise your sword and loudly proclaim that you will join the war against Merringnar")
                print("Hearing this, multiple strong men and women in the crowd raise their sword and plegde to help Riverdale in their war")
                print("After that, you spend the day gathering your necessities and say goodbye to your friends in the village")
                print("You realize you might not be back for a while so you go to the house of your good friend Sebastian")
                print("He understands your decision and says 'Farewell "+ str(plname) +". My sister and mother live in Riverdale, thank you for helping to protect them")
                print("He hands you a big pouch of coins and says 'here's 100 coins for the journey, stay safe out there'")
                print("You thank him for his support and get your horse named Roach from your stable to make the long journey to Riverdale")
                print("From now on your life will be a whole lot different...")
                print("")
                print("YOU GOT THE REGULAR ENDING: Pledge your allegiance!")
                print("Thanks for playing the game! You got ending 4 out of 7! Try to get all the endings")
                exit()
            elif (c8.lower() == "dont"):
                print("'Im not planning to join some war i dont know anything about' you think to yourself")
                print("You exit the crowd and make your way home")
                print("When you reach your home you eat some bread for dinner")
                print("Its already quite late so you decide to go to sleep for the day")
                print("Lying down on your bed you think to yourself 'What could this day have been?'")
                print("But then you think to yourself 'It doesn't really matter anyways, im always just gonna have a normal boring life'")
                print("")
                print("YOU GOT THE REGULAR ENDING: Just a regular day!")
                print("Thanks for playing the game! You got ending 5 out of 7! Try to get all the endings")
                exit()

            else:
                print("Oops, thats an incorrect input. Accepted inputs are Join or Dont")


if (upgrade == True):
    print("You head into the store to sell your transparent and power crystal")
    print("when you show the shopkeeper what you have he tells you that hell gladly buy the transparent crystals from you but that the power crystal is so rare that you will have to go to the town mage to sell it")
    int(money) + 10
    print("After exiting the store you start to the house of the town mage")
    print("During your walk to the house you spot crazy joe. He has an expensive wizard robe on and is reading a magic scroll")
    print("'So its true, crazy joe DID find gold in the mines, there's no other way he could have clothing that's so expensive!' You think")
    print("You inspect the wizard robes hes wearing and remember that crazy joe always wanted to be a mage but never had the money to do so")
    print("You approach crazy joe curious to find out what his story is")
    print("Greetings "+ str(plgender2) +" "+ str(plname) +" how are you on this fine evening?")
    print("'Wow, you speak quite elegantly crazy joe' you say")
    print("'That is no longer my name. My name is now Joe the wizard' He proclaims")
    print("You're a wizard now? How come?")
    print("'I got extemely wealthy after finding gold in the mines, unfortunately this village is so small that i cant find what i need to progress: a power crystal' he says")
    print("'I do have a power crystal, but would it be worth it to give it up to crazy joe?' you think")
    print("")

    while (c9.lower() != "give" or c9.lower() != "dont"):

            c9 = str(input("Do you give your crystal to him? (Give/Dont) "))
            print("")
            if (c9.lower() == "give"):
                print("You pull the crystal out of your pocket and show it to him")
                print("'Is this what you are looking for?' You ask him")
                print("'Unbelievable, you have a power crystal' he says")
                print("You tell him about how you found it in the mines today and that you were planning to sell it to the town mage")
                print("'Wait, i have a way better deal for you' he says")
                print("'I have more then enough money to buy you all the nessecary stuff to become a mage yourself. We could both use that power crystal and travel the world as mages' he says")
                print("You accept his offer and soon you and Joe the wizzard head out on an adventure to become professional mages...")
                print("")
                print("YOU GOT THE REGULAR ENDING: Mages in arms!")
                print("Thanks for playing the game! You got ending 6 out of 7! Try to get all the endings")
                exit()
                break
            elif (c9.lower() == "dont"):
                print("You wish crazy joe good luck on his quest to find a power crystal and continue to the town mage")
                print("Once you arrive at the mage you explain to him how you found a power crystal")
                print("'A real power crystal? Those are super rare and powerfull, i would be willing to buy it from you for 1000 coins!'")
                print("This is your chance to finally get out of poverty. you sell him the crystal and make it home with more money then you've ever had")
                print("From now on your life will be a whole lot easier...")
                print("")
                print("YOU GOT THE REGULAR ENDING: Filthy rich!")
                print("Thanks for playing the game! You got ending 7 out of 7! Try to get all the endings")
                exit()
                break
            else:
                print("Oops, thats an incorrect input. Accepted inputs are Give or Dont")
