#code for the milestone challenge adventure game
import time
import sys

def twosecsleep():
    time.sleep(2)

b=0.1
c=0.05
print("\n")
print("Welcome to Cool Beans!")
twosecsleep()
print()
print("A choice based adventure game written in Python.")
twosecsleep()
print("\n")

start = input("Do you want to start the game? (y/n) ")

if start == "n" or start == "N" or start == "no" or start == "No" or start == "NO":
    twosecsleep()
    twosecsleep()
    print("\n")
    print("Cool beans, see you later!")
elif start == "y" or start == "Y" or start == "yes" or start == "Yes" or start == "YES": 
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    twosecsleep()
    s ="Whe... Where am I?"
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print("\n")
    twosecsleep()
    s2 = "Ugh, my head is killing me... I shouldn't have eaten all those rum truffles..."
    for char in s2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    twosecsleep()
    twosecsleep()
    print("\n")
    s3 = "It's so dark in here... I can't see anything"
    for char in s3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)    
    twosecsleep()
    print()
    print("\n")
    print("What do you want to do?")
    twosecsleep()
    print("\n")
    print("1. Yell for help")
    twosecsleep()
    print("2. Crawl around and try to find a way out")
    twosecsleep()
    print("3. Search your pockets")
    twosecsleep()
    print("\n")
    choice = input("Choose 1, 2, or 3: ")
    if choice == "1":
        sleep()
        twosecsleep()
        print("AAAAAAAAAAAAA HEEEEEEELLPP")
        twosecsleep()
        print("\n")
        twosecsleep()
        print("...")
        print("\n")
        twosecsleep()
        print("You hear the echo of your voice in the distance")
        print("\n")
        twosecsleep()
        print("Then you hear a rustle close to you...")
        print("\n")
        twosecsleep()
        s ="Hello?"
        for char in s:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(b)
        print("\n")
        twosecsleep()
        print("Anyone there?")
        print("\n")
        print("...")
        twosecsleep()
        print("\n")
    
        s2 ="hello?"
        for char in s2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(b)       
        print("\n")
        twosecsleep()
        print("A bear is there.")
        print("\n")
        twosecsleep()
        print("GAME OVER")
        print()
    if choice == "2":
        twosecsleep()
        print("You crawl around trying to find a way out")
        print("\n")
        twosecsleep()
        print("The ground is wet and slippery")
        print("\n")
        twosecsleep()
        print("You are making your way through the cave when you stuble upon something")
        print("\n")
        twosecsleep()
        print("It's hairy and it's snoring")
        print("\n")
        s ="IT'S A BEAR!"
        for char in s:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(b)
        twosecsleep()
        print("\n")
        twosecsleep()
        print("And you just woke it up.")
        print("\n")
        twosecsleep()
        print("GAME OVER")
        print()
    if choice == "3":
        twosecsleep()
        print("\n")
        print("You search your pockets...")
        print("\n")
        twosecsleep()
        print("You found a lighter, a phone and some pocket sand.")
        print("\n")
        twosecsleep()
        print("You spark the lighter.")
        print("\n")
        twosecsleep()
        s = "I can see a way out... "
        for char in s:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(b)
        print("\n")
        twosecsleep()
        print("You pick up the pace and make it out of the cave.")
        print("\n")
        twosecsleep()
        print("The cave entrance is surrounded by woods.")
        print("\n")
        twosecsleep()
        print("There's a path through the forest leading into the cave.")
        print("\n")
        twosecsleep()
        on_off_path = input("Do you follow the path? (y/n) ")
        twosecsleep()
        if on_off_path == "n" or on_off_path == "N" or on_off_path == "no" or on_off_path == "No" or on_off_path == "NO":
            twosecsleep()
            print("\n")
            print("You decided you won't follow the path.")
            print("\n")
            twosecsleep()
            print("You start walking through the woods.")
            print("\n")
            twosecsleep()
            print("Some time after, you're walking... ")
            print("\n")
            twosecsleep()
            print("SNAP! You look down, and you see your leg caught in a bear trap.")
            print("\n")
            twosecsleep()
            print("GAME OVER")
            twosecsleep()
        if on_off_path == "y" or on_off_path == "Y" or on_off_path == "yes" or on_off_path == "Yes" or on_off_path == "YES":
            twosecsleep()
            print("\n")
            print("You follow the path...")
            twosecsleep()
            print("\n")
            twosecsleep()
            print("Maybe an hour passed, but you finally see the forest clearing")
            print("\n")
            twosecsleep()
            s ="I see a dirt road, I should be able to find someone to help me if I follow it!"
            for char in s:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            twosecsleep()
            print("\n")
            print("You keep walking down the road...")
            twosecsleep()
            print("\n")
            s2 ="I've been walking for hours and I haven't seen anyone..."
            for char in s2:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            print("\n")
            twosecsleep()
            s3 = "I'm so tired..."
            for char in s3:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)                
            print("\n")
            twosecsleep()
            s4 = "I should check if I can call someone..."
            for char in s4:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            print("\n")
            twosecsleep()
            print("You take out your phone, and press the power button.")
            print("\n")
            twosecsleep()
            print("The phone boots up but barely has any battery life.")
            print("\n")
            twosecsleep()
            print("RING RING RING")
            print("RING RING RING")
            print("RING RING RING")
            print("\n")
            twosecsleep()
            s5 = "Hello?! Please send help, I'm lost in.."
            for char in s5:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
        
            print("\n")
            s6 = "We're trying to reach you concerning your vehicle's extended warranty."
            for char in s6:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(c)
            print("\n")
            s7 = "You should've received a notice in the mail about your car's..."
            for char in s7:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(c)

            print("\n")

            print("The phone dies...")
            twosecsleep()
            print("\n")
            twosecsleep()
            print("F@#$%!!")
            print("\n")
            twosecsleep()
            print("You angrily continue walking...")
            print("\n")
            twosecsleep()
            print("After a few more minutes, you see a man sitting next to the road.")
            twosecsleep()
            print("\n")
            s8 = "Heeey! Hello!!"
            for char in s8:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            twosecsleep()           
            print("\n") 
            print("You pick up the pace and get closer to the man.")
            print("\n")
            twosecsleep()
            print("He's tall, wearing odd clothing and a funny looking hat.")
            print("\n")
            twosecsleep()
            s9 = "I'm lost... My phone is dead, can I borrow your phone?"
            for char in s9:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)            
            print("\n")
            twosecsleep()
            s10 = "Many people get lost in these woods, says the man."
            for char in s10:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)            
            twosecsleep()
            s11 = "My name is Py, I'll help you find your way home."
            for char in s11:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)            
            print("\n")
            twosecsleep()
            s12 = "Py: What's the last thing you remember?"
            print("\n")
            for char in s12:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            print("\n")
            twosecsleep()
            s13 = "I was on a camping trip..."
            for char in s13:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s14 = "We were hiking in the woods and we found a cave."
            for char in s14:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s15 = "I think I walked into the cave..."
            for char in s15:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s16 = "I can't remember anything after..."
            for char in s16:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s17 = "Py: You see, the cave you walked into is not in the same woods as the one you were hiking in"
            for char in s17:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(c)

            print("\n")
            twosecsleep()
            s18 = "I'm not sure what do you mean..."
            for char in s18:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s19 ="Py: You have travelled to a pararel universe."
            for char in s19:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(c)

            print("\n")
            twosecsleep()
            s20 = "Py: The only way to go back to your universe is to find and eat the secret beans."
            for char in s20:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(c)

            print("\n")
            twosecsleep()
            s21 = "Beans? What are you talking about?"
            for char in s21:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s22 = "Py: You need to go to the tavern down the road."
            for char in s22:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)


            print("\n")
            twosecsleep()
            s23 = "Py: The barkeep is called Mikael."
            for char in s23:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s24 ="Py: Ask him to give you the beans."
            for char in s24:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            print("\n")
            twosecsleep()
            s25 = "Py: The beans will take you back home."
            for char in s25:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s26 = "Ok, thank you Py!"
            for char in s26:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            print("\n") 
            twosecsleep()
            print("You walk down the road as the sun is setting...")
            print("\n") 
            twosecsleep()
            print("You see the tavern!")
            print("\n")
            twosecsleep()
            print("You walk in, it's a nice tavern with a large bar and a fireplace")
            print("\n")
            twosecsleep()
            s27 = "Welcome to Apple Pie Tavern"
            print("\n")
            twosecsleep()
            print("You walk up to the bar and ask ...")
            print("\n")
            twosecsleep()
            s28 = "Hi, are you Mikael?"
            for char in s28:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s29 = "Mikael: Yes, I am."
            for char in s29:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            s30 = "Py sent me here, he said you can help me. I need the secret beans."
            for char in s30:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(c)

            print("\n")
            twosecsleep()
            s30 =  "Mikael: I have them."
            for char in s30:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)
            print("\n")
            s31 = "I'll give you the beans if you can guess their price"
            for char in s31:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(c)

            print("\n")
            s32 = "You only have one guess..."
            for char in s32:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            s33 = "Mikael: What's the price?"
            for char in s33:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(b)

            print("\n")
            twosecsleep()
            print("1) 2 silver coins and 5 bronze coins")
            twosecsleep()
            print("2) 4 silver coins and a gold coin")
            twosecsleep()
            print("3) 3 gold coins and 14 silver coins")
            twosecsleep()
            print("/n")
            guess = input("What do you think the price is? (1/2/3) ")
            if guess == "1":
                s1 = "Mikael: Sorry, that's not correct"
                for char in s1:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)

                print("\n")
                twosecsleep()
                print("You get kicked out of the tavern")
                print("\n")
                twosecsleep()
                print("GAME OVER")
            if guess == "2":
                s1 = "Mikael: Sorry, that's not correct"
                for char in s1:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)


                print("\n")
                twosecsleep()
                print("You get kicked out of the tavern")
                print("\n")
                twosecsleep()
                print("GAME OVER")
            if guess == "3":
                s = "Mikael: You're right!"
                for char in s:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)
                print("\n")
                s2 = "Mikael: Let me get the beans for you."
                for char in s2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)
                print("\n")
                s3 = "Mikael: Here you go!"
                for char in s3:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)
                print("\n")
                s4 = "These are just regular beans"
                for char in s4:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)
                print("\n")
        
                s5 = "Mikael: Yes but I keep them refrigerated"
                for char in s5:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)
                
                print("\n")
                twosecsleep()
                print("You swallow the beans and feel a rush of energy")
                print("\n")
                twosecsleep()
                print("You wake up back in your tent...")
                print("\n")
                twosecsleep()
                s6 = "Well that was a wierd dream..."
                for char in s6:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)
                print("\n")
                twosecsleep()
                print("\n")
                s7 = "Congrats, you finished the game!"
                for char in s7:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(b)
                print("\n")


