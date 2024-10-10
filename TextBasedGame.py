# Ambrose Hawkins

# use to separate text
def print_break():
    print('~ ' * 11)


def print_intro():
    print('The Secret of Everhill Manor')
    print_break()
    char_name = input('Enter your name: ')
    print(
        """        Before the Great Blight, Everhill was a bright, bustling town. Home to 
        the finest artisans and merchants, nobles from far away would flock to 
        Everhill to find solace from the busy cities – while curating fine 
        collections of souvenirs to amaze their peers. As you walk down the 
        main road, dark and empty, you can almost imagine the splendor that 
        this town might have seen in its heyday. Little rows of darling shops 
        and cottages dot the verdant landscape leading up to the large hill in 
        the distance, their inhabitants nowhere to be seen, dead or hiding from 
        their lord. Lord Enret, resident of the large Everhill Manor on the hill, 
        once hosted lavish banquets and frequent parties at the esteemed estate. 
        However, it is rumored that Lord Enret has since taken up the deplorable 
        art of Necromancy, and as such, the remaining residents of Everhill fear 
        that he will soon unleash upon them a new plague – one that will finish 
        them off for good. You, {}, must confront Lord Enret and stop him from 
        completing his dark ritual so that the town of Everhill might rebuild 
        and be able to flourish once again. Good luck.""".format(char_name)
    )
    print_break()


def print_instructions():
    print('You will begin the game in the Entry Hall of Everhill Manor.')
    print('To move, type "go East", "go West", "go North", or "go South".')
    print('To get an item, type "get [Item Name]".')
    print('Available items will be capitalized in the room description.')
    print('To exit the game at any time, type "exit".')
    print('If you need to see these instructions again, type "help".')
    print_break()


def end_game(ending):
    if ending == 0:  # took ring of necromot
        print('''        You steel yourself and open the doors at the end of the hallway to reveal a grand study. Lord Enret 
        notices you immediately from his crowded workspace and throws something in your direction. You look down at the 
        ground where it landed. The projectile looks vile, and dirty brown vapors rise from it. Whatever effect it was 
        meant to have on you doesn’t seem to be working, so you turn back to Enret, who seems to be growing increasingly 
        concerned. “That should have killed you!” Enret exclaims, backing away. Seizing your chance, you pull out the 
        only weapon you brought with you – a small knife – and close the distance between you and the necromancer, 
        swiftly slashing through his jugular vein. Lord Enret falls backwards, incapacitated, and it is clear that no 
        one will be completing his dangerous ritual.''')
        print_break()
        print('Congratulations, you won the game. Thank you for playing.')

    if ending == 1:  # no ring
        print('''        You steel yourself and open the doors at the end of the hallway to reveal a grand study. Lord Enret 
        notices you immediately from his crowded workspace and throws something in your direction. You look down at the 
        ground where it landed. The projectile looks vile, and dirty brown vapors rise from it. Suddenly, you are 
        overcome with nausea, and your fingers begin to turn black. Lord Enret rises from his chair and chuckles, “No 
        one will stop me from achieving my goal.” You weakly grope for the small knife at your waist in a last effort 
        to defend yourself, but your intentions are futile. Lord Enret’s smug face is the last thing you see before you 
        lose all feeling and everything fades to black.''')
        print_break()
        print('A dark plague has been released upon Everhill. You lose. Thank you for playing.')

    if ending == 2:  # took ring of levitas, no passage
        print('''        As you reach for the door, you hear an explosion and someone yell, “NOOOOO!!!!” A loud crash sounds 
        throughout the manor, as if somewhere a window has broken. You rush to the hearth window to see a corpse, 
        rotting and putrid, sprinting toward the town. You try to find a way to open the window so that you can 
        intercept the corpse before it can infect anyone else, but it seems stuck. You watch helplessly as it reaches 
        the town square and tumbles into the well.''')
        print_break()
        print('A dark plague has been released upon Everhill. You lose. Thank you for playing.')

    if ending == 3:  # took ring of levitas, passage
        print('''        You look up and see a hatch in the ceiling, but there doesn’t seem to be a way to get up there. 
        Suddenly, as if prompted by your thoughts, the Ring of Levitas on your finger begins to glow. You slowly rise 
        off the floor and up to the ceiling. After undoing the hatch, you push your body through it to find yourself in 
        a long passage. You crawl through it, eventually coming to a vent cover, through which you see none other than 
        Lord Enret himself! He stands at a workstation within a few feet of you and seems to be busy at work – flipping 
        through dusty-looking old books and setting items around the ritual circle in front of him. You need to work 
        fast! You ready your small knife in your hand, push the cover off the vent, and jump onto Lord Enret from 
        behind. Before Enret can react, you swiftly slash your knife across his jugular vein, and he drops to the 
        floor. Now the town is safe from Enret’s dastardly plan, and you destroy the ritual circle for good measure.''')
        print_break()
        print('Congratulations, you won the game. Thank you for playing.')

    if ending == 4:  # took chalice of the undead
        print('''        Upon touching the Chalice, you are immediately transported to a large study. Lord Enret looks up, 
        startled, from his workspace and readies himself to attack. Suddenly, however, he stops, his eyes lingering on 
        the Chalice in your hands. “Is – is that the Chalice of the Undead?” His voice is raspy and quiet, as if it had 
        not been used in a long time. You answer in the affirmative, and Lord Enret raises his arms to the ceiling. “At 
        last, I have the means to bring back my beloved Lady!” He takes the Chalice from your hands, and places it in 
        the middle of the ritual circle.''')
        print_break()
        print('Congratulations, you won the game. Thank you for playing.')


def main():
    # The dictionary links a room to other rooms.
    rooms = {
        'Entry Hall': {
            'North': 'Dining Room',
            'South': 'Dark Closet',
            'East': 'Hallway',
            'West': 'Patio',
            'item': 'Silver Key',
            'description': '''            You stand in the Entry Hall of Everhill Manor. In front of you stands a long table, and 
            resting atop it sits a large crystal chest, containing a Silver Key. You try to open it but are 
            unsuccessful. However, there are six empty settings within the crystal. Perhaps if you find the objects 
            that fit in the settings, you’ll be able to open the chest.''',
            'has item': False
        },
        'Dining Room': {
            'South': 'Entry Hall',
            'East': 'Kitchen',
            'item': 'Starving Rotted Eye',
            'description': '''            You open the door to a modestly-sized Dining Room. It seems this was where the family ate 
            their meals, reserving the enormous Entry Hall for large banquets. On the Dining Room table sits a solitary 
            dinner plate. It holds no food – only a Starving Rotted Eye.''',
            'has item': False
        },
        'Dark Closet': {
            'North': 'Entry Hall',
            'East': "Lady's Bedchamber",
            'item': 'Sickly Rotted Eye',
            'description': '''            You find yourself staring into a dark, cramped closet. Something about this closet gives 
            you the creeps, but you can’t quite put your finger on why. Then, a Sickly Rotted Eye rolls toward you from 
            a pile of clothes on the floor and lightly bumps against your shoe.''',
            'has item': False
        },
        'Hallway': {
            'East': "Necromancer's Study",
            'West': 'Entry Hall',
            'item': ('Ring of Necromot', 'Ring of Levitas'),
            'description': '''            The silver Key fits in the lock on the door. Opening it, you find yourself in a long 
            hallway. At the end, there is a small shelf next to another door. On the shelf, you find two rings. One is 
            a deep matte black, set with a large fire opal, labeled “Ring of Necromot.” The other is inlaid with a 
            square-cut blue sapphire. Its silver band is carved with a swirling pattern and has “Ring of Levitas” 
            inscribed on the inside.''',
            'has item': False
        },
        'Patio': {
            'East': 'Entry Hall',
            'item': 'Bleached Rotted Eye',
            'description': '''            You open the grand double doors to look back out onto the Patio. It’s very untidy, with 
            leaves and spiderwebs everywhere. Next to the doors is an old chair; its white paint is brittle and 
            peeling. On the seat lies a Bleached Rotted Eye.''',
            'has item': False
        },
        'Kitchen': {
            'East': 'Hearth',
            'West': 'Dining Room',
            'item': 'Fermented Rotted Eye',
            'description': '''            Moving into the Kitchen, you quickly spot your next eye. A jar containing a green orb 
            sits on the counter. The label reads “Fermented Rotted Eye”.''',
            'has item': False
        },
        "Lady's Bedchamber": {
            'West': 'Dark Closet',
            'item': 'Chalice of the Undead',
            'description': '''            Although it is dark, you notice that there is a patch of ripped wallpaper on the east 
            wall of the closet. You place your hand on the wall, and it gives slightly under your touch. The entire 
            wall swings back to reveal a dimly lit bedroom. It is gaudily decorated with trinkets of gold and silver 
            lining the vanity and the fireplace. The bed itself is large, with long, red satin curtains obstructing 
            your view of what may be laying inside. Pulling one of the curtains aside, you are immediately repulsed by 
            the stench coming from inside the bed. Neatly tucked into the bedcovers lies a horrid corpse. “She was very 
            lovely once.” You turn around to see a tall figure in a black veil sitting at the bench in the window. “I 
            am Achlys, goddess of Death. Your Lord Enret is foolish. He thinks that he has the power to bring back his 
            fair Lady, but he will not succeed. There is only one way to escape Death.” The goddess holds a silver 
            chalice up to you, as if to offer it. “This is the Chalice of the Undead. If you bring this cup to Lord 
            Enret, you may avoid further calamity.”''',
            'has item': False
        },
        "Necromancer's Study": {  # villain
            'West': 'Hallway',
            'description': '',
            'has item': False
        },
        'Hearth': {
            'East': 'Library',
            'West': 'Kitchen',
            'item': 'Charred Rotted Eye',
            'description': '''            You open the door to the Hearth, where you are greeted by bright sunlight streaming 
            through the windows on either side of the large fireplace. Upon closer inspection of the fireplace, you 
            find a Charred Rotted Eye nestled between what’s left of the wood logs.''',
            'has item': False
        },
        'Library': {
            'West': 'Hearth',
            'Up': 'Secret Passage',
            'item': 'Great Rotted Eye',
            'description': '''            In the Library, you are surrounded by towering shelves of books. You pull your coat 
            around you a little tighter; there seems to be a draft in here. Sitting on a lectern in the middle of the 
            room is a Great Rotted Eye.''',
            'has item': False
        },
        'Secret Passage': {  # villain
            'Down': 'Library',
            'description': '',
            'has item': False
        }
    }

    # starting conditions
    current_room = 'Entry Hall'
    inventory = []
    i = 0

    # print game instructions
    print_intro()
    print_instructions()

    while i == 0:  # loops until break statement is reached or game ends

        # show status
        print('You are in the', current_room)
        print('Inventory:', inventory)

        # only show description when needs to see the name of the item
        if not rooms[current_room]['has item']:
            print(rooms[current_room]['description'])

        print_break()

        # get move from player
        user_input = input('Enter your move: ')

        # check for exit command
        if user_input == 'exit':
            print('Thank you for playing the game.')
            break

        # check for help command
        if user_input == 'help':
            print_instructions()

        # can't put one word inputs through split method
        elif ' ' not in user_input:
            print('Invalid move')
            print_break()

        else:
            # split user input into two strings
            user_string1, user_string2 = user_input.split(' ', 1)

            if (user_string1 != 'go') and (user_string1 != 'get'):
                print('Invalid move')
                print_break()

            # move rooms
            elif user_string1 == 'go':
                if user_string2 not in rooms[current_room]:
                    print("You can't go that way!")
                    print_break()

                else:
                    if (user_string2 == 'East') and (current_room == 'Entry Hall'):
                        if rooms['Entry Hall']['has item']:
                            current_room = rooms['Entry Hall']['East']

                        else:
                            print('The door is locked.')
                            print_break()

                    elif (current_room == 'Hearth') and (rooms['Hallway']['item'][1] in inventory):
                        end_game(2)
                        input('Press "Enter" to end the game.')
                        i = 1

                    elif (user_string2 == 'East') and (current_room == 'Hallway'):
                        if rooms['Hallway']['item'][0] in inventory:
                            end_game(0)
                            input('Press "Enter" to end the game.')
                            i = 1

                        else:
                            end_game(1)
                            input('Press "Enter" to end the game.')
                            i = 1

                    elif (user_string2 == 'Up') and (current_room == 'Library'):
                        if rooms['Hallway']['item'][1] in inventory:
                            current_room = 'Secret Passage'
                            end_game(3)
                            input('Press "Enter" to end the game.')
                            i = 1

                        else:
                            print('There seems to be a hatch in the ceiling, but you have no way of getting up there.')
                            print_break()

                    else:
                        # assign new value to current room from rooms dictionary
                        current_room = rooms[current_room][user_string2]

            # get items
            else:
                if rooms[current_room]['has item']:
                    print('You already have the item in this room.')
                    print_break()

                elif current_room == 'Hallway':
                    if (user_string2 == rooms['Hallway']['item'][0]) or (user_string2 == rooms['Hallway']['item'][1]):
                        inventory.append(user_string2)
                        rooms['Hallway']['has item'] = True

                        if rooms['Hallway']['item'][1] in inventory:
                            current_room = 'Library'
                            print('''                            You feel a wave of nausea come over you and everything goes dark before waking up 
                            on the floor of the Library. You have to find a way back to that hallway before Lord Enret 
                            finishes his ritual!''')

                    else:
                        print('There is no {} in this room.'.format(user_string2))
                        print_break()

                elif current_room == 'Entry Hall':
                    if user_string2 == rooms['Entry Hall']['item']:
                        if (rooms['Dining Room']['has item']) and (rooms['Dark Closet']['has item']) and \
                                (rooms['Patio']['has item']) and (rooms['Kitchen']['has item']) and \
                                (rooms['Hearth']['has item']) and (rooms['Library']['has item']):
                            print('Each of the eyes fit nicely into the grooves on the chest. It opens.')
                            print_break()
                            inventory.append(user_string2)
                            rooms['Entry Hall']['has item'] = True

                        else:
                            print('You must first collect all 6 Rotted Eyes from the other rooms.')
                            print_break()

                    else:
                        print('There is no {} in this room.'.format(user_string2))
                        print_break()

                else:
                    if user_string2 == rooms[current_room]['item']:
                        inventory.append(user_string2)
                        rooms[current_room]['has item'] = True

                        if user_string2 == rooms["Lady's Bedchamber"]['item']:
                            end_game(4)
                            input('Press "Enter" to end the game.')
                            i = 1

                    else:
                        print('There is no {} in this room.'.format(user_string2))
                        print_break()


if __name__ == '__main__':
    main()
