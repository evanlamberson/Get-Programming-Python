# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:06:50 2020

@author: Evan
"""
# Lesson 15 Capstone Project: Choose Your Own Adventure

# Import sys for the exit() function to fix multiple game overs as game leaves
# nested conditionals.
import sys

# Screen_line allows for easy transitions after decisions
screen_line = "\n" + ("-" * 100)

# Flags for keeping track of decisions
flag_footprints = False
flag_tire_iron = False
flag_glasses = False
flag_key = False

# Introductory information and how to play
print("Welcome to my survival adventure: THE WOODS")
print("Try to survive and uncover the mysterious secrets of the woods.")
print("Available commands are in CAPITAL letters, and any other command will "
      "exit the program. Have Fun!" + screen_line)

# Begin branching storyline. Only one choice lets users get used to input.
print("You awake, covered in glass and blood, and your head is racked with a "
      "searing pain. You should LOOK around and try to get your bearings."
      + screen_line)
do = input(":: ").upper()
print(screen_line)
if do == "LOOK":
    print("You look over and see a yellow truck, flipped over and burning. "
          "That's when it all hits you.\nYou remember taking a ride with your"
          " friend, Jeannie, out to the woods in her truck. As you came over "
          "the crest of a hill, you saw two strange figures, naked and "
          "covered in blood. Jeannie tried to swerve out of the way but "
          "ended up flipping the truck over a guard rail. \"I sure hope "
          "Jeannie is okay, but I'm worried that those strange figures will "
          "return.\" Should you CHECK THE TRUCK for signs of Jeannie or "
          "VENTURE DEEPER into the woods?" + screen_line)
    do = input(":: ").upper()
    print(screen_line)
    if do == "CHECK THE TRUCK":
        flag_footprints = True
        print("You carefully try lift yourself up out of the position that "
              "you woke up in. Now standing, you hobble your way over to the"
              " flipped truck. You can see where you flew out of the "
              "windshield, but the drivers seat has been all but torn out. "
              "The seatbelt is shredded, and the upholstery is almost "
              "non-existant. There are claw marks covering the door. You "
              "worry that whatever you almost ran into earlier has Jeannie. "
              "As you search the crash site, you notice a trail of small "
              "footprints leaving the truck heading deeper into the woods. "
              "Those could be Jeannie's! Do you follow them and VENTURE "
              "DEEPER or do you KEEP SEARCHING the wreckage?" + screen_line)
        do = input(":: ").upper()
        print(screen_line)
    if do == "KEEP SEARCHING" and flag_footprints == True:
        # checks for flag_footprints to keep players from skipping ahead.
        print("You keep looking around the wreckage of what used to be "
              "Jeannie's truck, and though you don't find anything special "
              "in the cab, you check around the back and find Jeannie's tire "
              "iron. This might come in handy! You decide that there's not "
              "much else of use at the wreck, and it's at risk of exploding, "
              "so you decide not to stick around and VENTURE DEEPER into the "
              "woods." + screen_line)
        flag_tire_iron = True
        do = input(":: ").upper()
        print(screen_line)
    if do == "VENTURE DEEPER":
        if flag_footprints == True and flag_tire_iron == False:
            # if players didn't KEEP SEARCHING, they don't have the tire iron
            # to defend themselves and they die.
            print("The footprints lead you to a small path at an opening in "
                  "the treeline. As you follow it, the vegetation thickens "
                  "until it is up to your chest and you can barely walk "
                  "through it. If only you had some way to cut through all of"
                  "this brush! As you struggle through the weeds, you feel"
                  "a hot breath on the back of your neck. You slowly look "
                  "behind you to face a grotesque being with piercing, pitch-"
                  "black eyes and a primitive machete raised high above it's "
                  "head. It isn't long before you're made the beast's next "
                  "meal." + screen_line)
            print("Y O U   D I E D")
            print("Try again!")
            sys.exit()
        elif flag_footprints == True and flag_tire_iron == True:
            # Players KEEP SEARCHING and find the tire iron to defend 
            # themselves against the beast.
             print("The footprints lead you to a small path at an opening in "
                  "the treeline. As you follow it, the vegetation thickens "
                  "until it is up to your chest and you can barely walk "
                  "through it. If only you had some way to cut through all of"
                  "this brush! As you struggle through the weeds, you feel"
                  "a hot breath on the back of your neck. You slowly look "
                  "behind you to face a grotesque being with piercing, pitch-"
                  "black eyes and a primitive machete raised high above it's "
                  "head. You quickly pull out your tire iron and are faced "
                  "with a split-second decision. Do you STRIKE the monster "
                  "or raise the tire iron and DEFEND yourself?" + screen_line)
             do = input(":: ").upper()
             print(screen_line)
             if do == "STRIKE":
                 print("You swing your tire iron at the beast like a total "
                       "wimp, barely glancing it, so the monster grabs you "
                       "with its free hand and helps itself to a feast of "
                       "your face." + screen_line)
                 print("Y O U   D I E D")
                 print("Try again!")
                 sys.exit()
             elif do == "DEFEND":
                 print("You hold your tire iron up in front of your face as "
                       "the monster swings its machete. Luckily, as the beast"
                       "strikes it's machete gets stuck in your tire iron. "
                       "This gives you a moment to defend yourself. Do you "
                       "PUNCH the monster with your free hand or KICK it "
                       "between the legs?" + screen_line)
                 do = input(":: ").upper()
                 print(screen_line)
                 if do == "PUNCH":
                     print("You try to send the beast a punch with your weak "
                           "hand, but it deftly grabs your fist with its free"
                           " hand and breaks its machete free from the tire "
                           "iron. It isn't long before the monster is "
                           "feasting on your flesh." + screen_line)
                     print("Y O U   D I E D")
                     print("Try again!")
                     sys.exit() 
                 elif do == "KICK":
                     print("You give the monster the strongest kick between "
                           "legs that you can muster up, connecting with a "
                           "satisfying *crack!* The beast whimpers and falls "
                           "to the ground, giving you a chance to break its "
                           "machete free from the tire iron. Seeing you dual-"
                           "wield the two weapons makes the beast flee in "
                           "fear down a path you hadn't noticed before. Do "
                           "you keep following the FOOTPRINT path, newly "
                           "armed with the machete, or do you follow the "
                           "MONSTER?" + screen_line)
                     do = input(":: ").upper()
                     print(screen_line)
                     if do == "FOOTPRINT" and flag_footprints == True:
                         print("Using your newfound machete, you swiftly cut "
                               "through the tall grass and keep following the"
                               " footprint path. It isn't long before the "
                               "footprints swiftly end. It seems like whoever"
                               " left these footprints was just swept up and "
                               "disappeared. Should you LOOK AROUND or RETURN"
                               " to the crossroads?" + screen_line)
                         # Since flag_footprints has already been used for its
                         # original purpose, we can use it again by setting it
                         # back to false.
                         flag_footprints = False
                         do = input(":: ").upper()
                         print(screen_line)
                         if do == "LOOK AROUND":
                             print("You keep looking around where the "
                                   "footprints end. It seems like they just "
                                   "disappeared! When you look above you into"
                                   " the tree branches, you can see a rope "
                                   "hanging down. Whoever this was must have "
                                   "been trapped! You notice a flash of light"
                                   " coming from the base of the tree. You go"
                                   " over to check, and find Jeannie's "
                                   "sunglasses! Someone has her! You should "
                                   "RETURN to the crossroads and try to "
                                   "find out more about Jeannie's captor."
                                   + screen_line)
                             flag_glasses = True
                             do = input(":: ").upper()
                             print(screen_line)
                         if do == "RETURN":
                             print("You return to where you fought that "
                                   "monster. Do you head back down the "
                                   "FOOTPRINT path or follow the MONSTER?"
                                   + screen_line)
                             do = input(":: ").upper()
                             print(screen_line)
                     # Taking care of cases if user returns to footprint path.
                     found_glasses = (flag_footprints == False
                                      and flag_glasses == True)
                     not_found_glasses = (flag_footprints == False
                                          and flag_glasses == False)
                     if do == "FOOTPRINT" and found_glasses:
                         print("You return to where you found Jeannie's "
                               "glasses. There isn't anything left to do. "
                               "RETURN?" + screen_line)
                         do = input(":: ").upper()
                         print(screen_line)
                         if do == "RETURN":
                             print("You return to where you fought that "
                                   "monster. You should follow the MONSTER."
                                   + screen_line)
                             do = input(":: ").upper()
                             print(screen_line)
                     if do == "FOOTPRINT" and not_found_glasses:
                         print("You go back to the end of the footprint trail"
                               ". There might be something else here. You "
                               "should LOOK AROUND." + screen_line)
                         do = input(":: ").upper()
                         print(screen_line)
                         if do == "LOOK AROUND":
                             print("You keep looking around where the "
                                   "footprints end. It seems like they just "
                                   "disappeared! When you look above you into"
                                   " the tree branches, you can see a rope "
                                   "hanging down. Whoever this was must have "
                                   "been trapped! You notice a flash of light"
                                   " coming from the base of the tree. You go"
                                   " over to check, and find Jeannie's "
                                   "sunglasses! Someone has her! You should "
                                   "RETURN to the crossroads and try to "
                                   "find out more about Jeannie's captor."
                                   + screen_line)
                             flag_glasses = True
                             do = input(":: ").upper()
                             print(screen_line)
                             if do == "RETURN":
                                 print("You return to where you fought that "
                                   "monster. You should follow the MONSTER."
                                   + screen_line)
                                 do = input(":: ").upper()
                                 print(screen_line)
                     if do == "MONSTER":
                         print("You start running after the monster, hopeful "
                               "to find answers. After a while, you're "
                               "worried that you've just been running in "
                               "circles until you come upon a camp "
                               "surrounding a strange structure constructed "
                               "out of mud and what seems to be bones. Do you"
                               " go to the FRONT gate or around the SIDE to "
                               "find a different way inside?" + screen_line)
                         do = input(":: ").upper()
                         print(screen_line)
                         if do == "SIDE":
                             print("You carefully make your way around "
                                   "the side of the camp and eventually "
                                   "find a small opening in the wall. "
                                   "You go through it into a small room "
                                   "with a chair and desk sitting in the "
                                   "center of it. On the desk is a small"
                                   " key. You take the key and have to "
                                   "decide. Do you OPEN the door or "
                                   "return to the FRONT entrance?" 
                                   + screen_line)
                             flag_key = True
                             do = input(":: ").upper()
                             print(screen_line)
                         if do == "OPEN" and flag_key == True:
                             print("You carefully open the door and are "
                                   "greeted with the angry faces of a whole "
                                   "camp full of mutant beasts. You are "
                                   "quickly torn to shreds.")
                             print("Y O U   D I E D")
                             print("Try again!")
                             sys.exit()
                         if do == "FRONT":
                             if flag_glasses == True:
                                 print("Before you start walking, you put on"
                                       " Jeannie's sunglasses. When you walk "
                                       "up to the gate, the monsters are "
                                       "unable to distinguish your shades "
                                       "from their own beady, black eyes and "
                                       "recognize you as one of their own. "
                                       "They let you in without any problems."
                                       " The camp seems to have a CENTRAL "
                                       "STRUCTURE with ceremonial markings on"
                                       " its walls, as well as a PRISONER'S "
                                       "QUARTERS sporting menacing spikes and"
                                       " armed guards. Where should you go "
                                       "first?" + screen_line)
                                 do = input(":: ").upper()
                                 print(screen_line)
                                 # Create boolean case in case user is too 
                                 # lazy to use apostrophe.
                                 p_quarters = ("PRISONER'S QUARTERS"
                                               or "PRISONERS QUARTERS")
                                 if do == "CENTRAL STRUCTURE":
                                     print("Feeling extra cool in Jeannie's "
                                           "sunglasses, you stroll, machete "
                                           "in hand, into the central "
                                           "structure of the camp. The "
                                           "building is one large room, "
                                           "decorated with the remains of the"
                                           "monsters' enemies. In the center "
                                           "of the room sits a massive being "
                                           "adorned with decorative jewelry."
                                           " This leader of the monsters sees"
                                           " right through your disguise and "
                                           "before you even have a chance to "
                                           "raise your machete has pinned you"
                                           "to the ground and made a feast "
                                           "out of your face." + screen_line)
                                     print("Y O U   D I E D")
                                     print("Try again!")
                                     sys.exit()
                                 elif do == p_quarters:
                                     if flag_key == True:
                                         print("You carefully move around the"
                                               " camp, avoiding the guards, "
                                               "and make it over to the "
                                               "prisoner's quarters. You "
                                               "carefully open the door and "
                                               "enter. In front of you, in a "
                                               "small cage, is Jeannie!\n"
                                               "\"You're here! Quick! Find "
                                               "the key!\"\nYou pull out the "
                                               "key you found earlier and "
                                               "quickly unlock the cage. You "
                                               "and Jeannie sneak out of the "
                                               "prisoner's quarters and out "
                                               "the hole in the wall that you"
                                               " found earlier. The two of "
                                               "you run back to the road "
                                               "you crashed and wave down a "
                                               "passing van. The van stops "
                                               "and picks you up. The driver,"
                                               " a mysterious man in "
                                               "sunglasses, doesn't speak "
                                               "much. You and Jeannie start "
                                               "to relax, excited that you "
                                               "escaped your captors. The "
                                               "driver peaks in the rearview "
                                               "mirror, bringing down his "
                                               "glasses to reveal his beady, "
                                               "black, eyes." + screen_line)
                                         print("T H E   E N D")
                                         print(screen_line)
                                         print("Thanks for playing!")
                                         sys.exit()
                                     else:
                                         print("You carefully move around the"
                                               " camp, avoiding the guards, "
                                               "and make it over to the "
                                               "prisoner's quarters. You "
                                               "carefully open the door and "
                                               "enter. In front of you, in a "
                                               "small cage, is Jeannie!\n"
                                               "\"You're here! Quick! Find "
                                               "the key!\"\nYou search all "
                                               "over the room, but you can't"
                                               " find the key anywhere. It "
                                               "isn't long before a monster "
                                               "discovers you and strikes you"
                                               " down, so close yet so far."
                                               + screen_line)
                                         print("Y O U   D I E D")
                                         print("Try again!")
                                         sys.exit()
                             else:
                                 print("As you walk up to the front gate, one"
                                       " of the monsters guarding the base "
                                       "snipes you with a bow and arrow."
                                       + screen_line)
                                 print("Y O U   D I E D" + screen_line)
                                 if flag_key == True:
                                     print("~||| YOU FOUND THE KEY THIS TIME,"
                                           " BUT YOU ARE MISSING SOMETHING "
                                           "ELSE. |||~" + screen_line)
                                 print("Try again!")
                                 sys.exit()
                     else:
                         print("You don't do anything and stand there like an"
                               " idiot. The monster comes back and eats you "
                               "for not choosing a command in CAPITAL "
                               "LETTERS." + screen_line)
                         print("Y O U   D I E D")
                         print("Try again!")
                         sys.exit()
                 else:
                     print("Instead of punching or kicking the monster, "
                       "you freeze in fear and don't do anything. It isn't "
                       "long before you're made the beast's next meal. Maybe "
                       "you should try one of the commands in CAPITAL "
                       "LETTERS. " + screen_line)
                     print("Y O U   D I E D")
                     print("Try again!")
                     sys.exit() 
             else:
                 print("Instead of striking or defending from the monster, "
                       "you freeze in fear and don't do anything. It isn't "
                       "long before you're made the beast's next meal. Maybe "
                       "you should try one of the commands in CAPITAL "
                       "LETTERS. " + screen_line)
                 print("Y O U   D I E D")
                 print("Try again!")
                 sys.exit()                 
        else:
            print("You carefully try lift yourself up out of the position "
              "that you woke up in. Now standing, you hobble over to the "
              "treeline. As you peer between the trees, you hear a guttural "
              "roar from behind you. Too afraid too look and see what "
              "monster might be following you, you bolt it into the woods. "
              "While running through the forest, you catch your foot in a "
              "homemade snare and are hoisted up into the trees. It isn't "
              "long before the beasts, a pair of grotesque humanoid figures "
              "sporting gangly limbs, pitch-black eyes, and all too many "
              "teeth help themselves to a feast of your organs."
              + screen_line)
            print("Y O U   D I E D")
            print("Try again!")
            sys.exit()
    else:
        print("G A M E   O V E R")
        print("You can only do the actions shown in capital letters.")
        print("Try again!")
        sys.exit()
else:
    print("G A M E   O V E R")
    print("You can only do the actions shown in capital letters.")
    print("Try again!")
    sys.exit()

