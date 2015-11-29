import os.path
import sys
import random
from time import sleep

class NewUsr(object):
    
    def __init__(self, name, age, lives):
        self.name = name
        self.age = age
        self.lives = range(1,int(lives))

    def UsrData(self, datafile):
        self.usrdata = datafile
        pass

class AIDict(object):
   def importData(self, filename1, filename2):
       usrtxt = open(filename1)
       usrtxt = usrtxt.read()
       self.usrKeywords = usrtxt.split('\n')
       del(self.usrKeywords[-1])
       aitxt= open(filename2)
       aitxt = aitxt.read()
       self.aiResponse = aitxt.split('\n')
       del(self.aiResponse[-1])

class Scene(object):
    def __init__(self, storytxt, usrtxt, failtxt):
        self.storytxt = storytxt
        self.usrtxt = usrtxt
        self.failtxt = failtxt
    
    def printline(self, textfile, x):
        txt = open(textfile)
        txt = txt.read()
        txt = txt.split('-')
        self.txt = txt
        return self.txt[x]

    def randline(self, textfile):
        lines = open(textfile)
        lines = lines.read()
        lines = lines.split('-')
        line = lines[random.randint(0,len(lines))]
        return line

    def printslow(self, textfile, x, y):
        txt = open(textfile)
        txt = txt.read()
        txt = txt.split('-')
        self.txt = txt
        i = x
        for line in self.txt[x:y]:
            if self.txt[i] != None:
                print self.txt[i]
                i += 1
                sleep(4)
        pass

def ExeScene(scenename):
    scenename.printslow(scenename.storytxt, 0,5)
    usrinput = raw_input('what do you do? > ').lower()
    usrinput = usrinput.split(' ')
    keywords = False
    for word in usrinput:
        for i in range(0,len(usrAction)):
            if word in usrAction[i]:
                keywords = True
                print aiLines[i][random.randint(0,(len(aiLines[i][:])-1))]
                sleep(3)
                print BUZZER
        if keywords == False:
            print scenename.printline(scenename.storytxt, -1)
            sleep(2)
            print scenename.randline(scenename.usrtxt)
            sleep(2)
            scenename.printslow(scenename.failtxt, 0, -1)

runAway = AIDict()
runAway.importData('usrRun.txt','aiRunresponse.txt')
attack = AIDict()
attack.importData('usrAttack.txt', 'aiAttackresponse.txt')
love = AIDict()
love.importData('usrLove.txt', 'aiLoveResponse.txt')

usrAction = [attack.usrKeywords, runAway.usrKeywords, love.usrKeywords]
aiLines = [attack.aiResponse, runAway.aiResponse, love.aiResponse]

start = Scene('mainentry.txt','','')
date = Scene('dateEntry.txt', 'quotes.txt','datefail.txt')
job = Scene('','','')
fridge = Scene('','','')

BUZZER = '\n\n*******bbbbzzzzzzzzzz*******\n\n'

def gameloop(usr, lives):
    for spawn in lives:
        print BUZZER
        start.printslow(start.storytxt,0,-1)
        choice = ''
        while choice not in ['1', '2', '3']:
            choice = str(raw_input("Pick a number 1 to 3\n> "))
        if choice == '1':
            ExeScene(date)
        elif choice == '2':
            ExeScene(job)
        else:
            ExeScene(fridge)

    print """
    You soar into a seething maelstrom of particles...
    hit a wall of fire...
    your legs get stretched out like a mile of spaggetti...
    your shoulders crush your chest as they are forced inwards...
    and you are burned to a crisp in an instant.
    Ouch.
    """
# game start
print """
Welcome to NIGHTMARE()
It will be unpleasant...
"""
name = str(raw_input("Enter Usr Name > "))
age = '0'
while int(age) not in range(1, 200):
    age = str(raw_input("Enter your age > "))
    if int(age) < 18:
        print "Sorry this game is not age appropriate."
        sys.exit(0)
lives = '0'
DIGITS = range(1,11)
while int(lives) not in DIGITS:
    lives = str(raw_input("""
    On a scale from one to ten,\n
    how terrible would you like this game to be?
    \n (10 being really terrible) > """))
    
lives = range(1, int(lives))
gameloop(name, lives)
