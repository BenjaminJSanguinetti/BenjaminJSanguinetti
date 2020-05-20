##This is the Final Pi prjoect
##By: Benamin Sanguinetti
from Tkinter import *
import time
import random
import math

class Application(Frame):
    
    def createWidgets(self):
        
        self.Welcome = Label(self)
        self.Welcome["text"] = "Welcom to Project Reflex, an interface desgined to test and improve cognative function.\n Each game will open in the py Shell"

        self.Img = PhotoImage(file="Brain.gif")
        self.Brain = Label(self)
        self.Brain["image"] = self.Img
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.Intro1 = Label(self)
        self.Intro1["text"] = "The number memory test evaluates \nhow many numbers you can hold in short term memory"

        self.Intro2 = Label(self)
        self.Intro2["text"] = "The word memory test evaluates \nhow many words you can hold in short term memory"

        self.Intro3 = Label(self)
        self.Intro3["text"] = "The number memory test evaluates \nhow many numbers you can hold in short term memory"

        self.Vis = Button(self)
        self.Vis["text"] = "Visual Memory test"
        self.Vis["command"] = self.visualMem
        
        
        self.Num = Button(self)
        self.Num["text"] = "Number Memory test"
        self.Num["command"] = self.numMem
        
        self.Reaction = Button(self)
        self.Reaction["text"] = "Reaction test"
        self.Reaction["command"] = self.reaction

        self.QUIT.grid(row=0, column = 0)
        self.Welcome.grid(row=0, column=1)
        self.Brain.grid(row=0, column=2)
        self.Intro1.grid(row=1, column=0)
        self.Intro2.grid(row=1, column=1)
        self.Intro3.grid(row=1, column=2)
        self.Num.grid(row=2, column=0)
        self.Vis.grid(row=2, column=1)
        self.Reaction.grid(row=2, column=2)
        
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def visualMem(self):
        wordBank=["kick","unit","public","little","consider","bird","sable","stay","alert","yoke","scintillating","whimsical","tick","volatile","cry","field","cold","ruthless","thumb","spiffy","mature","turn","grape","abnormal","belong","unarmed","program","cloth","cloistered","spy","lavish","trick","gray","pretty","likeable","crawl","southwest","background","grasshopper","keyway","washroom","jellybean","grassland","keystone","moonlight","grandnephew","lifelong","hometown"]
        used=[]
        level=1
        
        print "In this test you will be given a word you must answer 'new' if you have not seen that word has shown up before and 'old' if it has not been shown to you yet."
        print ""
        
        ready = raw_input("Do you want to play? (yes/no) ")
        
        if ready == "yes":
            game=True
            
            while game:

                if level == 1:
                    i=random.randint(0,len(wordBank)-1)
                    random.shuffle(wordBank)
                    print wordBank[i]
                    used.append(wordBank[i])
                    wordBank.remove(wordBank[i])
                    answer = raw_input("new or old? ")
                    print "This is the first one of course its new."
                    level += 1
                    time.sleep(3)
                    for x in range(100):
                        print " "
                        
                elif level > 1:
                    new=random.randint(0,100)
                    if new < 75:
                        i=random.randint(0,len(wordBank)-1)
                        random.shuffle(wordBank)
                        print wordBank[i]
                        used.append(wordBank[i])
                        wordBank.remove(wordBank[i])
                        answer = raw_input("new or old? ")
                        
                        if answer=="old":
                            print ""
                            print "This word is actually new."
                            time.sleep(3)
                            for x in range(100):
                                print " "
                            game=False
                            
                            
                        elif answer =="new":
                            print ""
                            print "Correct"
                            level += 1
                            time.sleep(3)
                            for x in range(100):
                                print " "
                                
                    if new >= 75:
                        random.shuffle(used)
                        i=random.randint(0,len(used)-1)
                        print used[i]
                        answer = raw_input("new or old? ")
                        if answer=="new":
                            print ""
                            print "This word is actually old."
                            time.sleep(3)
                            for x in range(100):
                                print " "
                            game=False
                            
                        elif answer =="old":
                            print ""
                            print "Correct"
                            level += 1
                            time.sleep(3)
                            for x in range(100):
                                print " "
                                
            self.visualMem()
              
    def numMem(self):
        print "In this test you will be given a number that you need to replicate after a short period."
        print ""
        game=False
        level = 3
        ready = raw_input("Do you want to play? (yes/no) ")
        if ready == "yes":
            game=True
        while game:
            goal = random.randint(10**(level - 1), (10**level) - 1)
            print goal
            time.sleep(7)
            for x in range(100):
                print " "
            tic = time.time()

            answer = input("What was the number? ")
            toc = time.time()
            passed =  toc-tic

            if passed > 7:
                print "You took too long!"
                print "You got to level" + str(level - 2)
                print " "
                game=False
                self.numMem()
            elif answer == goal:
                print "Correct"
                print " "
                level += 1
            elif answer != goal:
                print "That is wrong D;"
                print "You got to level " + str(level - 2)
                print " "
                game=False
                self.numMem()

        

        
    def reaction(self):
        print " "
        print "Wait until the prompt tells you then press enter as fast as possible."
        raw_input("press enter to start")
        
        sleeptime = random.randint(5,10)
        time.sleep(sleeptime)

        global tic
        tic = time.time()

        raw_input("PRESS ENTER")

        toc = time.time()
        passed =  toc-tic
        print "That took " + str(passed) + " seconds"
        again = input("Again? (1=yes 0=no) ")
        print " "
        if again == 1:
            self.reaction()
        else:
            return
            
                          
        

        
        




global app
root = Tk()
root.title("Project Reflex")
#root.attributes('-fullscreen', True)
app = Application(master=root)

app.mainloop()
root.destroy()
