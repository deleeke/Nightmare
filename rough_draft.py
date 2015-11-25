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
                sleep(2)
        pass

#lives = [1,2,3]
#usr = NewUsr('Laura Kraft', 30)

runAway = AIDict()
runAway.importData('usrRun.txt','aiRunresponse.txt')
attack = AIDict()
attack.importData('usrAttack.txt', 'aiAttackresponse.txt')

usrAction = [attack.usrKeywords, runAway.usrKeywords]
aiLines = [attack.aiResponse, runAway.aiResponse]

start = Scene('mainentry.txt','','')
date = Scene('dateEntry.txt', 'quotes.txt','datefail.txt')
job = Scene('','','')
fridge = Scene('','','')


def gameloop(usr, lives):
    for spawn in lives:
        print 'bbbbzzzzzzzzzz\n\n\n'
        start.printslow(start.storytxt,0,-1)
        choice1 = ''
        while choice1 not in ['1', '2', '3']:
            choice1 = str(raw_input("Pick a number 1 to 3\n> "))
        if choice1 == '1':
            date.printslow(date.storytxt, 0,5)
            usrinput = raw_input('what do you do? > ').lower()
            usrinput = usrinput.split(' ')
            keywords = False
            for word in usrinput:
                for i in range(0,len(usrAction)):
                    #print 'in the loop for the %r time' % i
                    if word in usrAction[i]:
                        keywords = True
                        #print 'usrinput in usrAction[%r] True' % i     
                        print aiLines[i][random.randint(0,(len(aiLines[i][:])-1))]
                        #print 'broke out of inner loop'
                        sleep(3)
                        print 'bbbbzzzzzzzzzz\n\n\n'
            if keywords == False:
                print date.printline(date.storytxt, -1)
                sleep(2)
                print date.randline(date.usrtxt)
                sleep(2)
                date.printslow(date.failtxt, 0, -1)
        elif choice1 == '2':
            print 'job scene'
            pass 
        else:
            print 'fridge scene'
            pass

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
age = 0
while int(age) not in range(1, 200):
    age = str(raw_input("Enter your age > "))
    if int(age) < 18:
        print "Sorry this game is not age appropriate."
        sys.exit(0)
lives = 0
while int(lives) not in range(1,11):
    lives = raw_input("""
    On a scale from one to ten,\n
    how terrible would you like this game to be?
    \n (10 being really terrible) > """)
    
lives = range(1, int(lives))
gameloop(name, lives)
