###############################################################################
# Macbeth Adventure by Adam King, Spring 2017                                 #
# A short text adventure game based on Macbeth, a famous play by Shakespeare. #
# Last updated: 5/5/2021                                                      #
###############################################################################

import sys


class Adventure(object):
    def __init__(self):
        self.currentRoom = 1
        self.compass = ['NORTH', 'SOUTH', 'EAST', 'WEST']

        self.visitedRoom1 = 0
        self.visitedRoom2 = 0
        self.visitedRoom3 = 0
        self.visitedRoom4 = 0
        self.visitedRoom5 = 0
        self.visitedRoom6 = 0
        self.visitedRoom7 = 0
        self.visitedRoom8 = 0
        self.visitedRoom9 = 0
        self.visitedRoom10 = 0

        self.visited = {
            1: self.visitedRoom1,
            2: self.visitedRoom2,
            3: self.visitedRoom3,
            4: self.visitedRoom4,
            5: self.visitedRoom5,
            6: self.visitedRoom6,
            7: self.visitedRoom7,
            8: self.visitedRoom8,
            9: self.visitedRoom9,
            10: self.visitedRoom10}

        self.playerInventory = []
        self.room1Inventory = []
        self.room2Inventory = ['EYE']
        self.room3Inventory = []
        self.room4Inventory = ['LEG']
        self.room5Inventory = []
        self.room6Inventory = []
        self.room7Inventory = ['FROG TOE']
        self.room8Inventory = ['WING']
        self.room9Inventory = []
        self.room10Inventory = ['HAIR']

        self.roomInventories = {
            1: self.room1Inventory,
            2: self.room2Inventory,
            3: self.room3Inventory,
            4: self.room4Inventory,
            5: self.room5Inventory,
            6: self.room6Inventory,
            7: self.room7Inventory,
            8: self.room8Inventory,
            9: self.room9Inventory,
            10: self.room10Inventory}

        self.itemScore = 0
        self.roomScore = 0
        self.score = 0

        self.rooms = {
            1: {'name': 'Witch Cave',
                'NORTH': 3,
                'SOUTH': 8,
                'EAST': 6,
                'WEST': 5,
                'description': '''\nYou are in a dark cave. In the middle, there is a cauldron boiling. With a clasp
of thunder, three witches suddenly appear before you.''',
                'task': '''The witches speak in unison:
Mortal, we have summoned thee, make haste!
And go forth into the farrow'd waste.
Find eye of newt, and toe of frog,
And deliver thus to this Scottish bog.
Lizard's leg, and owlet's wing,
And hair of cat that used to sing.
These things we need t' brew our charm;
Bring them forth -and suffer no 'arm.
Leave us and go!
'Tis no more to be said,
Save if you fail, then thou be stricken, dead."\n''',
                'visited': 'The witches stand before you, glaring; they seem to be expecting something from you.\n'},
            2: {'name': 'state of Georgia',
                'SOUTH': 2,
                'EAST': 3,
                'WEST': 2,
                'description': '''\nYou're transported back in time… you find yourself in Georgia during the midst
of a congressional campaign.''',
                'preAction': '''There is a campaign poster of Newt Gingrich, the Speaker of the House of
Representatives, on the wall, with his large eyes looking right at you.\n''',
                'postAction': 'There is a defaced poster of Newt Gingrich on the wall.\n'},
            3: {'name': 'Room 3',
                'SOUTH': 1,
                'EAST': 4,
                'WEST': 2,
                'description': '''\nYou arrive at a quaint looking town. The aesthetic seems very 11th century. The 
people seem busy tending to their farms. There's not much to see here.\n'''},
            4: {'name': 'Room 4',
                'SOUTH': 6,
                'EAST': 6,
                'description': '''\nAs you walk through the forest, you notice many small lizards sunbathing on the
rocks near a pond. A hawk soars above with what appears to be a lizard in its talons.''',
                'preAction': '''There is a lizard's leg lying on the ground, it presumably came from that hawk's
soon-to-be dinner.\n''',
                'postAction': 'Nothing much to see here.'},
            5: {'name': 'Room 5',
                'EAST': 1,
                'WEST': 7,
                'description': '''\nThe scenery here seems very wrong. Everything seems wrong. A sense of horror and 
dread washes over you.\n'''},
            6: {'name': 'Room 6',
                'NORTH': 4,
                'SOUTH': 8,
                'EAST': 9,
                'WEST': 1,
                'description': '''\nThis place looks like a crossroads that leads in many directions, with many
signs pointing to different places you've never heard of. You wonder which path
will lead you to the next item in your quest.\n'''},
            7: {'name': "Monty Python's Flying Circus scene",
                'NORTH': 2,
                'WEST': 5,
                'description': '\nWhy does this place look like the set of a Monty Python sketch?',
                'preAction': '''You find yourself walking into a scene where the cast of Monty Python's Flying
Circus is performing the "Crunchy Frog" sketch. You see the confectioner as he replies, "If we took the bones
out it wouldn't be crunchy now, would it?" You see a box of "Crunchy Frog" chocolates, the contents of which
contains a dozen nicely cleaned whole frogs that have been carefully hand-dipped in the finest chocolate.\n''',
                'postAction': 'You see a box of "Crunchy Frog" chocolates, the contents of which have been pilfered.\n'},
            8: {'name': 'Room 8',
                'EAST': 6,
                'description': '''\nOn your travels, you meet an apothecary.''',
                'preAction': '''The apothecary tells you that he has had a hard time selling his collection of
owlet wings. He offers to give you one for free, saying "Here, just take it. I have
too many of these damned things as it is. I just need them gone." You would ask why
he happens to own so many, but he seems a bit too perturbed to talk about it.\n''',
                'postAction': 'He has nothing to give you.\n'},
            9: {'name': 'area outside the door of a dormitory kitchen',
                'NORTH': 6,
                'WEST': 10,
                'description': '''\nAs you step through the time portal, your head begins to spin. You're
disoriented and then awaken. You find yourself at the outside door of a dormitory
kitchen. Listening, you hear the Chef yelling, "Stop! Stop!" while several cats
inside are singing a serenade of the "Meow Mix" commercial theme. Suddenly, the
repeated thump of a cleaver puts an abrupt end to the music.\n'''},
            10: {'name': 'dormitory kitchen',
                 'EAST': 9,
                 'description': '''\nYou enter the dormitory kitchen. That time portal from earlier appears
behind the kitchen door, but nobody else seems to notice for some reason.''',
                 'preAction': '''You are in the kitchen. Looking out into the
cafeteria, you see students reaching for Pepto-Bismol while trying to stomach
the latest version of the Chef's Surprise. You see the Chef as he finishes dumping
fresh meat into his 50-quart stewing pot. There are clumps of cat hair on the
butcher's block. You hear the Chef muttering to himself, "Prepared properly, cat
tastes much like chicken...\n"''',
                 'postAction': '''You have been transported back to the moment directly after you took the cat
hair. You should probably leave before that crazy chef spots you and decides to put
YOU in the stew.\n'''}}

    def actions(self):
        while True:
            action = input('Enter an action: ').upper().split()
            try:
                if action[0] == 'GO' or action[0] == 'MOVE':
                    if action[1] in self.rooms[self.currentRoom]:
                        self.currentRoom = self.rooms[self.currentRoom][action[1]]
                        print(self.rooms[self.currentRoom]['description'])
                        self.visited[self.currentRoom] = 1
                        self.action_descriptions()
                    else:
                        print('You cannot go that direction.')
                elif action[0] in self.compass:
                    if action[0] in self.rooms[self.currentRoom]:
                        self.currentRoom = self.rooms[self.currentRoom][action[0]]
                        print(self.rooms[self.currentRoom]['description'])
                        self.visited[self.currentRoom] = 1
                        self.action_descriptions()
                    else:
                        print('You cannot go that direction.')
                elif action[0] == 'TAKE':
                    if action[1] == 'TOE' or action[1] == 'FROG':
                        if 'FROG TOE' in self.roomInventories[self.currentRoom]:
                            self.roomInventories[self.currentRoom].remove('FROG TOE')
                            self.playerInventory.append('FROG TOE')
                            print('You got the FROG TOE.')
                    if action[1] in self.roomInventories[self.currentRoom]:
                        self.roomInventories[self.currentRoom].remove(action[1])
                        self.playerInventory.append(action[1])
                        print('You got the ' + action[1] + '.')
                    else:
                        if action[1] == 'TOE' or action[1] == 'FROG':
                            pass
                        else:
                            print('You cannot take ' + ' '.join(action[1:]) + '!')
                elif action[0] == 'DROP':
                    if action[1] == 'TOE' or action[1] == 'FROG':
                        if 'FROG TOE' in self.playerInventory:
                            self.roomInventories[self.currentRoom].append('FROG TOE')
                            self.playerInventory.remove('FROG TOE')
                            print('You dropped the FROG TOE.')
                    if action[1] in self.playerInventory:
                        self.roomInventories[self.currentRoom].append(action[1])
                        self.playerInventory.remove(action[1])
                        print('You dropped the ' + action[1] + '.')
                    else:
                        print('You cannot drop ' + ' '.join(action[1:]) + '!')
                elif action[0] == 'LOOK':
                    print(self.rooms[self.currentRoom]['description'])
                    if self.visitedRoom1 == 0:
                        print(self.rooms[1]['task'])
                        self.visitedRoom1 = 1
                    else:
                        self.action_descriptions()
                elif action[0] == 'INVENTORY':
                    print('Your inventory: ' + ', '.join(self.playerInventory))
                elif action[0] == 'SCORE':
                    self.player_score()
                elif action[0] == 'HELP':
                    self.instructions()
                elif action[0] == 'QUIT':
                    sys.exit()
                else:
                    print("You can't " + ' '.join(action) + '!')
                if len(self.room1Inventory) >= 5:
                    print('''The witches look at your items with suspicion, but decide to go through with the 
                    incantation of the spell: "Take lizard's leg and owlet's wing, And hair of cat that used to sing. 
                    In the cauldron they all shall go; Stirring briskly, to and fro. When the color is of a hog, 
                    Add eye of newt and toe of frog. Bubble all i' the charmed pot; Bubble all 'til good and hot. 
                    Pour the broth into a cup of stone, And stir it well with a mummy's bone." You take the resulting 
                    broth offered to you and drink... As the fog clears, you find yourself at a computer terminal; 
                    your adventure is at an end.''')
                    print('Congratulations! You have won the game. Enter the QUIT command to exit the program.')
            except IndexError:
                pass

    def pre_action(self):
        if self.currentRoom == 2 and 'EYE' in self.room2Inventory:
            print(self.rooms[2]['preAction'])
        elif self.currentRoom == 4 and 'LEG' in self.room4Inventory:
            print(self.rooms[4]['preAction'])
        elif self.currentRoom == 7 and 'FROG TOE' in self.room7Inventory:
            print(self.rooms[7]['preAction'])
        elif self.currentRoom == 8 and 'WING' in self.room8Inventory:
            print(self.rooms[8]['preAction'])
        elif self.currentRoom == 10 and 'HAIR' in self.room10Inventory:
            print(self.rooms[10]['preAction'])
        else:
            pass

    def post_action(self):
        if self.currentRoom == 2 and 'EYE' not in self.room2Inventory:
            print(self.rooms[2]['postAction'])
        elif self.currentRoom == 4 and 'LEG' not in self.room4Inventory:
            print(self.rooms[4]['postAction'])
        elif self.currentRoom == 7 and 'FROG TOE' not in self.room7Inventory:
            print(self.rooms[7]['postAction'])
        elif self.currentRoom == 8 and 'WING' not in self.room8Inventory:
            print(self.rooms[8]['postAction'])
        elif self.currentRoom == 10 and 'HAIR' not in self.room10Inventory:
            print(self.rooms[10]['postAction'])
        else:
            pass

    def room_1_visit(self):
        if self.currentRoom == 1 and self.visitedRoom1 == 1:
            print(self.rooms[1]['visited'])
        else:
            pass

    def action_descriptions(self):
        self.room_1_visit()
        self.pre_action()
        self.post_action()

    def player_score(self):
        self.itemScore = len(self.room1Inventory)
        self.roomScore = (
                self.visited[1] + self.visited[2] + self.visited[3] + self.visited[4] + self.visited[5] +
                self.visited[6] + self.visited[7] + self.visited[8] + self.visited[9] + self.visited[10])
        self.score = self.roomScore + self.itemScore
        print('Your current score: ' + str(self.score))

    @staticmethod
    def instructions():
        print('\n')
        print('-------------------------------------------------------------------------------')
        print('Instructions:')
        print("To return back from whence you came, fetch all the items for the witchs' brew.")
        print("All items must be dropped at the witchs' cave in order to win.")
        print('-------------------------------------------------------------------------------')
        print('Commands:')
        print('-------------------------------------------------------------------------------')
        print('''NORTH or GO NORTH or MOVE NORTH: Head north from your current position.
SOUTH or GO SOUTH or MOVE SOUTH: Head south from your current position.
EAST or GO EAST or MOVE EAST: Head east from your current position.
WEST or GO WEST or MOVE WEST: Head west from your current position.
TAKE (item): add item to your inventory. Ex: TAKE EYE
DROP (item): remove item from your inventory. EX: DROP EYE
    Items:
    EYE
    LEG
    FROG or TOE
    WING
    HAIR
INVENTORY: display your inventory.
LOOK: displays a description of your current surroundings.
SCORE: displays your current score.
HELP: display these instructions.
QUIT: exit the program.''')
        print('-------------------------------------------------------------------------------')
        print('\n')


def main():
    a = Adventure()
    print('Welcome to the Macbeth Adventure Game!')
    a.instructions()
    print('To embark on this perilous fetch quest:')
    print('Enter the LOOK command to start the game.\n')
    a.actions()


if __name__ == '__main__':
    main()
