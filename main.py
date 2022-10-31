import random
import math
import pickle
from colored import fore, back, style, fg, bg, attr
import string
import sys, termios, tty, os, time
 
def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, oglold_settings)
  return ch

class Player:
  def __init__(self,Name,Tag,colo):
    self.Name = Name 
    self.Health = 100
    self.Level = 6
    self.gold = 1000
    self.storelist = []
    self.team = []
    self.teamC = []
    self.deadteam = []
    self.backteam = []
    self.teamS = []
    self.deadteamS= []
    self.backteamS = []
    self.front = []
    self.center = []
    self.back = []
    self.teamID = []
    self.Tag = Tag
    self.colo = fg(colo)
    self.ben = 0
    self.bla = 0
    self.col = 0
    self.dom = 0
    self.ind = 0
    self.iri = 0
    self.kor = 0
    self.mex = 0
    self.pal = 0
    self.per = 0
    self.fil = 0
    self.pue = 0
    self.syr = 0
    self.tun = 0
    self.tur = 0
    self.uru = 0
    self.whi = 0
    self.chi = 0
    self.emo = 0
    self.fre = 0
    self.gam = 0
    self.gay = 0
    self.int = 0
    self.lea = 0
    self.mus = 0
    self.nai = 0
    self.pur = 0
    self.shy = 0
    self.soy = 0
    self.str = 0
    self.vul = 0
    self.vultarg = []
    self.wee = 0
    self.walui = ""

  def carouselAI(self,stage):
    pick = random.choice(carousellist)
    if len(self.team) < self.Level:
      self.team.append(pick)
    elif len(self.backteam) < 9:
      self.backteam.append(pick)
    elif (len(self.team) == self.Level and len(self.backteam) == 9):
      None
    carousellist.remove(pick)
    print("\n"+self.Name,"picks",pick.NAME+"!")
    if self.Name == "Waluigi" and stage == 1:
      self.walui = pick.NAME

  def teamset(self,types,pl1="",pl2=""):
    for x in self.deadteam:
      x.cHP = x.HP
      x.fcMP = x.cMP
      x.purge("Death",pl1,pl2)
      self.team.append(x)
    self.deadteam = []
    self.deadteamS = []
    if types == "Team":
      self.teamS = []
      for x in self.team:
        self.teamS.append(x.NAME)
    elif types == "Reserve":
      self.backteamS = []
      for x in self.backteam:
        self.backteamS.append(x.NAME)
  
  def synergy(self,check=False):
    self.ben = 0
    self.bla = 0
    self.col = 0
    self.dom = 0
    self.ind = 0
    self.iri = 0
    self.kor = 0
    self.mex = 0
    self.pal = 0
    self.per = 0
    self.fil = 0
    self.pue = 0
    self.syr = 0
    self.tun = 0
    self.tur = 0
    self.uru = 0
    self.whi = 0
    self.chi = 0
    self.emo = 0
    self.fre = 0
    self.gam = 0
    self.gay = 0
    self.int = 0
    self.lea = 0
    self.mus = 0
    self.nai = 0
    self.pur = 0
    self.shy = 0
    self.soy = 0
    self.str = 0
    self.vul = 0
    self.wee = 0
    for x in self.team:
      if "Bengali" in x.SYN:
        self.ben = self.ben + 1
      if "Black" in x.SYN:
        self.bla = self.bla + 1
      if "Colombian" in x.SYN:
        self.col = self.col + 1
      if "Dominican" in x.SYN:
        self.dom = self.dom + 1
      if "Indian" in x.SYN:
        self.ind = self.ind + 1
      if "Irish" in x.SYN:
        self.iri = self.iri + 1
      if "Korean" in x.SYN:
        self.kor = self.kor + 1
      if "Mexican" in x.SYN:
        self.mex = self.mex + 1
      if "Palestinian" in x.SYN:
        self.pal = self.pal + 1
      if "Peruvian" in x.SYN:
        self.per = self.per + 1
      if "Filipino" in x.SYN:
        self.fil = self.fil + 1
      if "Puerto Rican" in x.SYN:
        self.pue = self.pue + 1
      if "Syrian" in x.SYN:
        self.syr = self.syr + 1
      if "Tunisian" in x.SYN:
        self.tun = self.tun + 1
      if "Turkish" in x.SYN:
        self.tur = self.tur + 1
      if "Uruguayan" in x.SYN:
        self.uru = self.uru + 1
      if "White" in x.SYN:
        self.whi = self.whi + 1
      if "Chill" in x.SYN:
        self.chi = self.chi + 1
      if "Emo" in x.SYN:
        self.emo = self.emo + 1
      if "Free Spirit" in x.SYN:
        self.fre = self.fre + 1
      if "Gamer" in x.SYN:
        self.gam = self.gam + 1
      if "Gay" in x.SYN:
        self.gay = self.gay + 1
      if "Intellectual" in x.SYN:
        self.int = self.int + 1
      if "Leader" in x.SYN:
        self.lea = self.lea + 1
      if "Musclehead" in x.SYN:
        self.mus = self.mus + 1
      if "Naive" in x.SYN:
        self.nai = self.nai + 1 
      if "Pure" in x.SYN:
        self.pur = self.pur + 1
      if "Shy" in x.SYN:
        self.shy = self.shy + 1
      if "Soy" in x.SYN:
        self.soy = self.soy + 1
      if "Stressed" in x.SYN:
        self.str = self.str + 1      
      if "Vulgar" in x.SYN:
        self.vul = self.vul + 1
      if "Weeb" in x.SYN:
        self.wee = self.wee + 1
    if check == True:
      print("")
      if self.ben > 0:
        print("Bengali:",self.ben)
      if self.bla > 0:
        print("Black:",self.bla)
      if self.col > 0 :
        print("Colombian:",self.col)
      if self.dom > 0:
        print("Dominican:",self.dom)
      if self.ind > 0:
        print("Indian:",self.ind)
      if self.iri > 0:
        print("Irish:",self.iri)
      if self.kor > 0:
        print("Korean:",self.kor)
      if self.mex > 0:
        print("Mexian:",self.mex)
      if self.pal > 0:
        print("Palestinian:",self.pal)
      if self.per > 0:
        print("Peruvian:",self.per)
      if self.fil > 0:
        print("Filipino:",self.fil)     
      if self.pue > 0:
        print("Puerto Rican:",self.pue)
      if self.syr > 0:
        print("Syrian:",self.syr)
      if self.tun > 0:
        print("Tunisian:",self.tun)
      if self.tur > 0:
        print("Turkish:",self.tur)
      if self.uru > 0:
        print("Uruguayan:",self.uru)
      if self.whi > 0:
        print("White:",self.whi)
      if self.chi > 0:
        print("Chill:",self.chi)
      if self.emo > 0:
        print("Emo:",self.emo)
      if self.fre > 0:
        print("Free Spirit:",self.fre)
      if self.gam > 0:
        print("Gamer:",self.gam)
      if self.gay > 0:
        print("Gay:",self.gay)
      if self.int > 0:
        print("Intellectual:",self.int)
      if self.lea > 0:
        print("Leader:",self.lea) 
      if self.mus > 0:
        print("Musclehead:",self.mus)
      if self.nai > 0:
        print("Naive:",self.nai)
      if self.pur > 0:
        print("Pure:",self.pur)
      if self.shy > 0:
        print("Shy:",self.shy)
      if self.soy > 0:
        print("Soy:",self.soy)
      if self.str > 0:
        print("Stressed:",self.str)
      if self.vul > 0:
        print("Vulgar:",self.vul)
      if self.wee > 0:
        print("Weeb",self.wee)

  def AIprep(self):
    storelevel(self.Level) 

    if self.Name == "Wakim":
      if self.Level < 6:
        self.store(self.Name)
      elif self.Level >=6:
        bruh = 0
        while bruh == 0:
          self.store(self.Name)   
          if self.gold > 2:    
            storelevel(self.Level)
            self.gold = self.gold - 2
          elif self.gold <= 2:
            bruh = 1

    elif self.Name == "Waluigi":
      cnt = 0
      for x in self.backteam:
        if x.RAR == 4:
          yikes = []
          for y in self.team:
            if y.RAR != 4:
              yikes.append(y)
          selling = random.choice(yikes)
          self.aisell(selling)
          self.team.append(x)
          self.teamset("Team")
          self.teamset("Reserve")
      if self.Level < 8:
        self.store(self.Name)
        if self.gold > 2:    
          storelevel(self.Level)
          self.gold = self.gold - 2
          self.store(self.Name)
      elif self.Level == 8:
        cnt = 0
        self.store(self.Name)
        while cnt < 6:
          cnt = cnt + 1
          if self.gold > 2:    
            storelevel(self.Level)
            self.gold = self.gold - 2
            self.store(self.Name)
          elif self.gold <= 2:
            break
      elif self.Level == 9:
        bruh = 0
        while bruh == 0:
          self.store(self.Name)   
          if self.gold > 2:    
            storelevel(self.Level)
            self.gold = self.gold - 2
          elif self.gold <= 2:
            bruh = 1

    elif self.Name == "Xehanort":
      None

    elif self.Name == "Himekawa":
      if self.Level < 9:
        self.store(self.Name)
      elif self.Level == 9:
        bruh = 0
        while bruh == 0:
          self.store(self.Name)   
          if self.gold > 2:    
            storelevel(self.Level)
            self.gold = self.gold - 2
          elif self.gold <= 2:
            bruh = 1

    elif self.Name == "Belle Delphine":
      None
    
    elif self.Name == "Aizawa":
      None
    
    elif self.Name == "Espinoza":
      None
    
    elif self.Name == "Eldesouky":
      None
    
    elif self.Name == "RJ":
      None
    
    elif self.Name == "Salem":
      None
    
    elif self.Name == "Josh":
      None
    
    elif self.Name == "Flabby":
      None

    elif self.Name == "Ling Ling":
      None

    elif self.Name == "Patrick":
      None


  def prep(self,types="",skip=""):
    global elapsed
    global start
    global ghost
    start = time.time()        
    elapsed = 0   
    self.storelevel() 
    print("""\nPress the "S" key to skip the round timer""")           
    while elapsed < 60:
      for x in self.team:
        print(x.NAME,x.items)          
      print("\nRound",rnd,"\nLv:",self.Level,"Gold:",self.gold,"Time:",round(60-elapsed),"seconds left.")
      print(fore.GREY_100 +"(1) Buy Units  (2) Row Order  (3) Arrange Units\n(4) Sell Units  (5) Information\nAction: "+ style.RESET)
      char = getch()
      elapsed = time.time() - start
      if elapsed > 60:      
        break
      if char == "1":
        self.store("Player")
      elif char == "2":
        row("Player")
      elif char == "3":
        arrange("Player")
      elif char == "4":
        self.sell("Player")
      elif char == "5":
        info("Player")
      elif char.lower() == "s":
        print("\nRound skipped")
        break
    time.sleep(1)
    if types == "PvP":
      for x in opponents:
        x.AIprep()
      bruh = []
      ghost = 0
      for x in play:
        bruh.append(x)
      while len(bruh) > 0:
        ghost = 0
        red = random.choice(bruh)
        bruh.remove(red)
        if len(bruh) != 0 :
          blue = random.choice(bruh)
          bruh.remove(blue)
        else:
          blue = random.choice(play)
          ghost = 1
        if (p1 == red or p1 == blue) and ghost != 1:
          battle(red,blue,False)
        elif p1 == red and ghost == 1:
          battle(red,blue,False)
        else:
          battle(red,blue,True)

  def storelevel(self):
    if self.Level == 1 or self.Level == 2:
      ran = []
      ran.append(random.choice(tier1))
      giveitem(ran)
      un1 = ran
      ran = []
      ran.append(random.choice(tier1))
      giveitem(ran)
      un2 = ran
      ran = []
      ran.append(random.choice(tier1))
      giveitem(ran)
      un3 = ran
      ran = []
      ran.append(random.choice(tier1))
      giveitem(ran)
      un4 = ran
      ran = []
      ran.append(random.choice(tier1))
      giveitem(ran)
      un5 = ran
    elif self.Level == 3:
      champs = []
      for x in range(60):
        ran = []
        ran.append(random.choice(tier1))
        giveitem(ran)
        champs.append(ran)
      for x in range(30):
        ran = []
        ran.append(random.choice(tier2))
        giveitem(ran)
        champs.append(ran)
      for x in range(10):
        ran = []
        ran.append(random.choice(tier3))
        giveitem(ran)
        champs.append(ran)
      un1 = random.choice(champs)
      un2 = random.choice(champs)
      un3 = random.choice(champs)
      un4 = random.choice(champs)
      un5 = random.choice(champs)
    elif self.Level == 4:
      champs = []
      for x in range(50):
        ran = []
        ran.append(random.choice(tier1))
        giveitem(ran)
        champs.append(ran)
      for x in range(30):
        ran = []
        ran.append(random.choice(tier2))
        giveitem(ran)
        champs.append(ran)
      for x in range(15):
        ran = []
        ran.append(random.choice(tier3))
        giveitem(ran)
        champs.append(ran)
      for x in range(5):
        ran = []
        ran.append(random.choice(tier4))
        giveitem(ran)
        champs.append(ran)
      un1 = random.choice(champs)
      un2 = random.choice(champs)
      un3 = random.choice(champs)
      un4 = random.choice(champs)
      un5 = random.choice(champs)
    elif self.Level == 5:
      champs = []
      for x in range(38):
        ran = []
        ran.append(random.choice(tier1))
        giveitem(ran)
        champs.append(ran)
      for x in range(35):
        ran = []
        ran.append(random.choice(tier2))
        giveitem(ran)
        champs.append(ran)
      for x in range(20):
        ran = []
        ran.append(random.choice(tier3))
        giveitem(ran)
        champs.append(ran)
      for x in range(6):
        ran = []
        ran.append(random.choice(tier4))
        giveitem(ran)
        champs.append(ran)
      for x in range(1):
        ran = []
        ran.append(random.choice(tier5))
        giveitem(ran)
        champs.append(ran)
      un1 = random.choice(champs)
      un2 = random.choice(champs)
      un3 = random.choice(champs)
      un4 = random.choice(champs)
      un5 = random.choice(champs)
    elif self.Level == 6:
      champs = []
      for x in range(25):
        ran = []
        ran.append(random.choice(tier1))
        giveitem(ran)
        champs.append(ran)
      for x in range(35):
        ran = []
        ran.append(random.choice(tier2))
        giveitem(ran)
        champs.append(ran)
      for x in range(25):
        ran = []
        ran.append(random.choice(tier3))
        giveitem(ran)
        champs.append(ran)
      for x in range(10):
        ran = []
        ran.append(random.choice(tier4))
        giveitem(ran)
        champs.append(ran)
      for x in range(5):
        ran = []
        ran.append(random.choice(tier5))
        giveitem(ran)
        champs.append(ran)
      un1 = random.choice(champs)
      un2 = random.choice(champs)
      un3 = random.choice(champs)
      un4 = random.choice(champs)
      un5 = random.choice(champs)
    elif self.Level == 7:
      champs = []
      for x in range(15):
        ran = []
        ran.append(random.choice(tier1))
        giveitem(ran)
        champs.append(ran)
      for x in range(29):
        ran = []
        ran.append(random.choice(tier2))
        giveitem(ran)
        champs.append(ran)
      for x in range(30):
        ran = []
        ran.append(random.choice(tier3))
        giveitem(ran)
        champs.append(ran)
      for x in range(15):
        ran = []
        ran.append(random.choice(tier4))
        giveitem(ran)
        champs.append(ran)
      for x in range(10):
        ran = []
        ran.append(random.choice(tier5))
        giveitem(ran)
        champs.append(ran)
      for x in range(1):
        ran = []
        ran.append(random.choice(tier6))
        giveitem(ran)
        champs.append(ran)
      un1 = random.choice(champs)
      un2 = random.choice(champs)
      un3 = random.choice(champs)
      un4 = random.choice(champs)
      un5 = random.choice(champs)
    elif self.Level == 8:
      champs = []
      for x in range(10):
        ran = []
        ran.append(random.choice(tier1))
        giveitem(ran)
        champs.append(ran)
      for x in range(20):
        ran = []
        ran.append(random.choice(tier2))
        giveitem(ran)
        champs.append(ran)
      for x in range(30):
        ran = []
        ran.append(random.choice(tier3))
        giveitem(ran)
        champs.append(ran)
      for x in range(23):
        ran = []
        ran.append(random.choice(tier4))
        giveitem(ran)
        champs.append(ran)
      for x in range(15):
        ran = []
        ran.append(random.choice(tier5))
        giveitem(ran)
        champs.append(ran)
      for x in range(2):
        ran = []
        ran.append(random.choice(tier6))
        giveitem(ran)
        champs.append(ran)
      un1 = random.choice(champs)
      un2 = random.choice(champs)
      un3 = random.choice(champs)
      un4 = random.choice(champs)
      un5 = random.choice(champs)
    elif self.Level == 9:
      champs = []
      for x in range(5):
        ran = []
        ran.append(random.choice(tier1))
        giveitem(ran)
        champs.append(ran)
      for x in range(10):
        ran = []
        ran.append(random.choice(tier2))
        giveitem(ran)
        champs.append(ran)
      for x in range(20):
        ran = []
        ran.append(random.choice(tier3))
        giveitem(ran)
        champs.append(ran)
      for x in range(35):
        ran = []
        ran.append(random.choice(tier4))
        giveitem(ran)
        champs.append(ran)
      for x in range(25):
        ran = []
        ran.append(random.choice(tier5))
        giveitem(ran)
        champs.append(ran)
      for x in range(5):
        ran = []
        ran.append(random.choice(tier6))
        giveitem(ran)
        champs.append(ran)
      un1 = random.choice(champs)
      un2 = random.choice(champs)
      un3 = random.choice(champs)
      un4 = random.choice(champs)
      un5 = random.choice(champs)
    self.storelist = [un1,un2,un3,un4,un5]
    print(self.storelist)

  def store(self,types,skip=""):
    global elapsed
    global start
    global check
    bruh = 1
    if types == "Player":
      while elapsed < 60:
        print("")          
        for x in self.storelist:
          if x == "EMPTY":
            print("("+str(bruh)+")",x)
          if x[0] in tier1:
            print("("+str(bruh)+")",x[0],"["+x[1]+"]")
          if x[0] in tier2:
            print("("+str(bruh)+")",fore.GREEN_1+x[0]+style.RESET,"["+x[1]+"]")
          if x[0] in tier3:
            print("("+str(bruh)+")",fore.DODGER_BLUE_2+x[0]+style.RESET,"["+x[1]+"]")
          if x[0] in tier4:
            print("("+str(bruh)+")",fore.PURPLE_1B+x[0]+style.RESET,"["+x[1]+"]")
          if x[0] in tier5:
            print("("+str(bruh)+")",fore.DARK_ORANGE+x[0]+style.RESET,"["+x[1]+"]")
          if x[0] in tier6:
            print("("+str(bruh)+")",fore.CYAN_1+x[0]+style.RESET,"["+x[1]+"]")
          bruh = bruh + 1
        bruh = 1
        print("\nGold:",p1.gold,"Time:",round(60-elapsed),"seconds left.\n(1-5) Buy Champion  (R) Reroll  (Enter) Exit\nAction: ")
        char = getch()
        elapsed = time.time() - start
        if elapsed > 60:      
          break  
        if char == "\r":
          break
        if char.lower() == "r":
          if self.gold >=2:
            self.gold = self.gold - 2
            self.storelevel()
          else:
            print("\nYou do not have enough gold to reroll!")
        if char == "1" or char == "2" or char == "3" or char == "4" or char == "5":
          pers = self.storelist[int(char)-1]
          if pers[0] in tier1:
            self.storesimp(pers,1,int(char)-1)
          elif pers[0] in tier2:
            self.storesimp(pers,2,int(char)-1)
          elif pers[0] in tier3:
            self.storesimp(pers,3,int(char)-1)
          elif pers[0] in tier4:
            self.storesimp(pers,4,int(char)-1)
          elif pers[0] in tier5:
            self.storesimp(pers,5,int(char)-1)
          elif pers[0] in tier6:
            self.storesimp(pers,6,int(char)-1)
    elif types == "Wakim":
      for x in storelist:
        if x[0] == "Norman" or x[0] == "Lascelles" or x[0] == "Tyasia" or x[0] == "David" or x[0] == "Edmond" or x[0] == "Jahir" or x[0] == "Shannae" or x[0] == "Kylie":
          if x[0] in tier1:
            self.storesimp(x,1,storelist.index(x),"Skip")
          elif x[0] in tier2:
            self.storesimp(x,2,storelist.index(x),"Skip")
          elif x[0] in tier3:
            self.storesimp(x,3,storelist.index(x),"Skip")
          elif x[0] in tier4:
            self.storesimp(x,4,storelist.index(x),"Skip")
          elif x[0] in tier5:
            self.storesimp(x,5,storelist.index(x),"Skip")
          elif x[0] in tier6:
            self.storesimp(x,6,storelist.index(x),"Skip")
        elif len(self.team) < self.Level:
          if x[0] in tier1:
            self.storesimp(x,1,storelist.index(x),"Skip")
          elif x[0] in tier2:
            self.storesimp(x,2,storelist.index(x),"Skip")
          elif x[0] in tier3:
            self.storesimp(x,3,storelist.index(x),"Skip")
          elif x[0] in tier4:
            self.storesimp(x,4,storelist.index(x),"Skip")
          elif x[0] in tier5:
            self.storesimp(x,5,storelist.index(x),"Skip")
          elif x[0] in tier6:
            self.storesimp(x,6,storelist.index(x),"Skip")
    elif types == "Waluigi":
      for x in storelist:
        if x[0] in tier4:
          self.storesimp(x,4,storelist.index(x),"Skip")
        elif x[0] == self.walui:
          if x[0] in tier1:
            self.storesimp(x,1,storelist.index(x),"Skip")
          elif x[0] in tier2:
            self.storesimp(x,2,storelist.index(x),"Skip")
          elif x[0] in tier3:
            self.storesimp(x,3,storelist.index(x),"Skip")
          elif x[0] in tier4:
            self.storesimp(x,4,storelist.index(x),"Skip")
          elif x[0] in tier5:
            self.storesimp(x,5,storelist.index(x),"Skip")
          elif x[0] in tier6:
            self.storesimp(x,6,storelist.index(x),"Skip")
        elif len(self.team) < self.Level:
          if x[0] in tier1:
            self.storesimp(x,1,storelist.index(x),"Skip")
          elif x[0] in tier2:
            self.storesimp(x,2,storelist.index(x),"Skip")
          elif x[0] in tier3:
            self.storesimp(x,3,storelist.index(x),"Skip")
          elif x[0] in tier4:
            self.storesimp(x,4,storelist.index(x),"Skip")
          elif x[0] in tier5:
            self.storesimp(x,5,storelist.index(x),"Skip")
          elif x[0] in tier6:
            self.storesimp(x,6,storelist.index(x),"Skip")
    elif types == "Himekawa":
      upg = []
      for x in self.team:
        if x.RAR < 5:
          upg.append(x.NAME)
      for x in storelist:
        if x[0] in tier5 or x[0] in tier6:
          if x[0] in tier5:
            self.storesimp(x,5,storelist.index(x),"Skip")
          elif x[0] in tier6:
            self.storesimp(x,6,storelist.index(x),"Skip")
        elif x[0] in upg:
          if x[0] in tier1:
            self.storesimp(x,1,storelist.index(x),"Skip")
          elif x[0] in tier2:
            self.storesimp(x,2,storelist.index(x),"Skip")
          elif x[0] in tier3:
            self.storesimp(x,3,storelist.index(x),"Skip")
          elif x[0] in tier4:
            self.storesimp(x,4,storelist.index(x),"Skip")
          elif x[0] in tier5:
            self.storesimp(x,5,storelist.index(x),"Skip")
          elif x[0] in tier6:
            self.storesimp(x,6,storelist.index(x),"Skip")
        elif len(self.team) < self.Level:
          if x[0] in tier1:
            self.storesimp(x,1,storelist.index(x),"Skip")
          elif x[0] in tier2:
            self.storesimp(x,2,storelist.index(x),"Skip")
          elif x[0] in tier3:
            self.storesimp(x,3,storelist.index(x),"Skip")
          elif x[0] in tier4:
            self.storesimp(x,4,storelist.index(x),"Skip")
          elif x[0] in tier5:
            self.storesimp(x,5,storelist.index(x),"Skip")
          elif x[0] in tier6:
            self.storesimp(x,6,storelist.index(x),"Skip")
    else:
      upg = []
      for x in self.team:
        upg.append(x.NAME)
          

  def storesimp(self,unit,cos,pos,skip=""):
    global storelist
    global check
    check = 0
    if unit[0] in self.teamS or unit[0] in self.backteamS:
      if skip != "":
        self.dupe(unit,cos,"Skip")
      else:
        self.dupe(unit,cos)
      if check == 1:
        storelist.pop(pos)
        storelist.insert(pos,"EMPTY")
    elif unit[0] not in self.teamS and unit[0] not in self.backteamS:
      if skip != "":
        self.purchase(unit,cos,skip="Skip")
      else:
        self.purchase(unit,cos)
      if check == 1:
        storelist.pop(pos)
        storelist.insert(pos,"EMPTY")

  def dupe(self,unit,rarity,skip=""):
    global check 
    if self.gold < rarity:
      if skip != "Skip":
        print("\nYou do not have enough gold to purchase this unit!")
        time.sleep(0.5)
    elif (len(self.backteam) >=9 and (len(self.team) >= self.Level)):
      if skip != "Skip":
        print("\nYou do not have space to purchase this unit!")
        time.sleep(0.5)
    elif ((self.gold >= rarity) and (len(self.backteam) <9 or (len(self.team) < self.Level))):
      pers = ""
      for x in self.team:
        if x.NAME == unit[0]:
          pers = x
      for x in self.backteam:
        if x.NAME == unit[0]:
          pers = x
      if pers.LV == 8:
        if skip != "Skip":
          print("\nThis unit is already max level!")
          time.sleep(0.5)
      else:
        pers.setlevel(pers.LV+1)
        if unit != "Amira":
          pers.mixitem(unit[1])
        elif unit == "Amira":
          pers.items.append(unit[1])
        if skip != "Skip":
          print("\nYou purchased an upgrade for",pers.NAME+"!")
          if pers.RAR == 1:
            print(fore.YELLOW_1 +"LV:",str(pers.LV+1)+style.RESET,"-",pers.NAME,"-",pers.items)
          elif pers.RAR == 2:
            print(fore.YELLOW_1 +"LV:",str(pers.LV+1)+style.RESET,"-",fore.GREEN_1+pers.NAME+style.RESET,"-",pers.items)
          elif pers.RAR == 3:
            print(fore.YELLOW_1 +"LV:",str(pers.LV+1)+style.RESET,"-",fore.DODGER_BLUE_2+pers.NAME+style.RESET,"-",pers.items)
          elif pers.RAR == 4:
            print(fore.YELLOW_1 +"LV:",str(pers.LV+1)+style.RESET,"-",fore.PURPLE_1B+pers.NAME+style.RESET,"-",pers.items)
          elif pers.RAR == 5:
            print(fore.YELLOW_1 +"LV:",str(pers.LV+1)+style.RESET,"-",fore.DARK_ORANGE+pers.NAME+style.RESET,"-",pers.items)
          pers.itemcatalog()
        self.gold = self.gold - rarity
        check = 1

  def sell(self):
    print("")

  def aisell(unit):
    retur = 0
    if unit in tier1:
      retur = 1
    if unit in tier2:
      retur = 2
    if unit in tier3:
      retur = 3
    if unit in tier4:
      retur = 4
    if unit in tier5:
      retur = 5
    if unit in tier6:
      retur = 6
    self.gold = self.gold + round((retur*unit.LV)/2)
    self.team.remove(unit)


  def purchase(self,unit,rarity,caro=False,back=False,skip=""):
    global ID
    global check
    if ((self.gold < rarity) and (caro != True)) and back == False:
      if skip != "Skip":
        print("\nYou do not have enough gold to purchase this unit!")
        time.sleep(0.5)
    elif (len(self.backteam) >=9 and (len(self.team) >= self.Level) and caro != True) and back == False:
      if skip != "Skip":
        print("\nYou do not have space to purchase this unit!")
        time.sleep(0.5)
    elif ((self.gold >= rarity) and (len(self.backteam) <9 or (len(self.team) < self.Level))) or caro == True or back == True:
      ID = ID + 1 
      if isinstance(unit, str) == True:
        unit = [unit]
      if unit[0] == "Mohammad":
        gHP = 550
        gcMP = 0
        gMP = 175
        gAT = 40
        gDF = 20
        gMAT = 1
        gMDF = 40
        gSP = 35
        gAC = 100
        gEV = 120
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["Palestinian","Free Spirit","Gamer"]
      if unit[0] == "Ishraq":
        gHP = 950
        gcMP = 0
        gMP = 65
        gAT = 60
        gDF = 35
        gMAT = 1
        gMDF = 20
        gSP = 30
        gAC = 100
        gEV = 120
        gCT = 35
        gAPN = 0
        gMPN = 0
        gMRG = 15
        gGEN = "Male"
        gSYN = ["Bengali","Free Spirit"]
      if unit[0] == "James":
        gHP = 550
        gcMP = 0
        gMP = 100
        gAT = 40
        gDF = 25
        gMAT = 1
        gMDF = 20
        gSP = 35
        gAC = 100
        gEV = 110
        gCT = 20
        gAPN = 0
        gMPN = 0
        gMRG = 25
        gGEN = "Male"
        gSYN = ["Syrian","Shy"]
      if unit[0] == "Jeremy":
        gHP = 700
        gcMP = 25
        gMP = 100
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 15
        gSP = 30
        gAC = 110
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Male"
        gSYN = ["Peruvian","Shy"]
      if unit[0] == "Arwyn":
        gHP = 700
        gcMP = 0
        gMP = 100
        gAT = 45
        gDF = 30
        gMAT = 1
        gMDF = 40
        gSP = 30
        gAC = 110
        gEV = 110
        gCT = 35
        gAPN = 0
        gMPN = 0
        gMRG = 14
        gGEN = "Male"
        gSYN = ["Filipino","Weeb","Emo"]
      if unit[0] == "Brian":
        gHP = 850
        gcMP = 0
        gMP = 100
        gAT = 50
        gDF = 35
        gMAT = 1
        gMDF = 20
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Mexican","Emo"]
      if unit[0] == "Dereck":
        gHP = 450
        gcMP = 0
        gMP = 75
        gAT = 40
        gDF = 20
        gMAT = 1
        gMDF = 20
        gSP = 20
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Filipino","Weeb"]
      if unit[0] == "Octavio":
        gHP = 550
        gcMP = 0
        gMP = 75
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 20
        gSP = 30
        gAC = 110
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["Dominican","Gamer"]
      if unit[0] == "Blandino":
        gHP = 550
        gcMP = 25
        gMP = 100
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 20
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["Dominican","Free Spirit"]
      if unit[0] == "Richard":
        gHP = 1100
        gcMP = 25
        gMP = 100
        gAT = 75
        gDF = 35
        gMAT = 1
        gMDF = 10
        gSP = 20
        gAC = 100
        gEV = 100
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["White","Musclehead"]
      if unit[0] == "Najely":
        gHP = 700
        gcMP = 25
        gMP = 100
        gAT = 40
        gDF = 30
        gMAT = 1
        gMDF = 20
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Female"
        gSYN = ["Mexican","Gamer"]
      if unit[0] == "Kelly":
        gHP = 600
        gcMP = 50
        gMP = 125
        gAT = 45
        gDF = 25
        gMAT = 1
        gMDF = 50
        gSP = 30
        gAC = 120
        gEV = 120
        gCT = 40
        gAPN = 0
        gMPN = 0
        gMRG = 14
        gGEN = "Female"
        gSYN = ["Korean","Intellectual","Leader"]
      if unit[0] == "Hassan":
        gHP = 800
        gcMP = 25
        gMP = 100
        gAT = 55
        gDF = 30
        gMAT = 1
        gMDF = 25
        gSP = 30
        gAC = 110
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Tunisian","Free Spirit"]
      if unit[0] == "Tahsin":
        gHP = 400
        gcMP = 50
        gMP = 100
        gAT = 45
        gDF = 20
        gMAT = 1
        gMDF = 20
        gSP = 25
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Female"
        gSYN = ["Bengali","Shy"]
      if unit[0] == "Zaid":
        gHP = 900
        gcMP = 50
        gMP = 100
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Palestinian","Soy"]
      if unit[0] == "Amira":
        gHP = 1000
        gcMP = 0
        gMP = 50
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 45
        gAPN = 0
        gMPN = 0
        gMRG = 15
        gGEN = "Female"
        gSYN = ["Egyptian","Stressed","Leader"]
      if unit[0] == "Khalil":
        gHP = 750
        gcMP = 0
        gMP = 60
        gAT = 60
        gDF = 30
        gMAT = 1
        gMDF = 25
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Palestinian","Emo","Weeb"]
      if unit[0] == "Kylie":
        gHP = 900
        gcMP = 0
        gMP = 75
        gAT = 55
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 30
        gAC = 120
        gEV = 100
        gCT = 35
        gAPN = 0
        gMPN = 0
        gMRG = 15
        gGEN = "Female"
        gSYN = ["Puerto Rican","Irish","Chill"]
      if unit[0] == "Alvaro":
        gHP = 800
        gcMP = 0
        gMP = 100
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["Peruvian","Gamer"]
      if unit[0] == "Edmond":
        gHP = 800
        gcMP = 0
        gMP = 100
        gAT = 60
        gDF = 30
        gMAT = 1
        gMDF = 15
        gSP = 35
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Male"
        gSYN = ["Black","Chill"]
      if unit[0] == "Jahir":
        gHP = 450
        gcMP = 25
        gMP = 100
        gAT = 45
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["Black",'Chill']
      if unit[0] == "Reema":
        gHP = 550
        gcMP = 25
        gMP = 50
        gAT = 40
        gDF = 20
        gMAT = 1
        gMDF = 35
        gSP = 30
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Female"
        gSYN = ["Indian","Stressed"]
      if unit[0] == "Kenny":
        gHP = 850
        gcMP = 0
        gMP = 125
        gAT = 40
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Male"
        gSYN = ["Peruvian","Shy"]
      if unit[0] == "Brandon":
        gHP = 950
        gcMP = 25
        gMP = 125
        gAT = 60
        gDF = 35
        gMAT = 1
        gMDF = 20
        gSP = 35
        gAC = 110
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["Puerto Rican","Chill"]
      if unit[0] == "Tim":
        gHP = 900
        gcMP = 0
        gMP = 20
        gAT = 50
        gDF = 25
        gMAT = 1
        gMDF = 35
        gSP = 30
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 14
        gGEN = "Male"
        gSYN = ["White","Free Spirit","Intellectual"]
      if unit[0] == "Daniel":
        gHP = 900
        gcMP = 0
        gMP = 100
        gAT = 45
        gDF = 35
        gMAT = 1
        gMDF = 35
        gSP = 25
        gAC = 120
        gEV = 100
        gCT = 35
        gAPN = 0
        gMPN = 0
        gMRG = 14
        gGEN = "Male"
        gSYN = ["Dominican","Peruvian","Intellectual","Gay"]
      if unit[0] == "Jaidah":
        gHP = 800
        gcMP = 0
        gMP = 125
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 35
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Female"
        gSYN = ["Dominican","Intellectual","Leader"]
      if unit[0] == "Lascelles":
        gHP = 800
        gcMP = 50
        gMP = 125
        gAT = 40
        gDF = 30
        gMAT = 1
        gMDF = 35
        gSP = 25
        gAC = 100
        gEV = 110
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["Black","Weeb","Pure"]
      if unit[0] == "Tyasia":
        gHP = 700
        gcMP = 0
        gMP = 75
        gAT = 55
        gDF = 25
        gMAT = 1
        gMDF = 25
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Female"
        gSYN = ["Black","Stressed"]
      if unit[0] == "Julius":
        gHP = 1150
        gcMP = 25
        gMP = 75
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 25
        gSP = 30
        gAC = 110
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["Uruguayan","Free Spirit","Vulgar"]
      if unit[0] == "Matvey":
        gHP = 600
        gcMP = 75
        gMP = 100
        gAT = 45
        gDF = 25
        gMAT = 1
        gMDF = 25
        gSP = 30
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Male"
        gSYN = ["Filipino","Shy"]
      if unit[0] == "Jackie":
        gHP = 600
        gcMP = 0
        gMP = 60
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 35
        gAC = 100
        gEV = 120
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Female"
        gSYN = ["White","Gay","Free Spirit"]
      if unit[0] == "Andrew":
        gHP = 400
        gcMP = 0
        gMP = 50
        gAT = 45
        gDF = 25
        gMAT = 1
        gMDF = 20
        gSP = 25
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Indian","Vulgar"]
      if unit[0] == "Nicole":
        gHP = 800
        gcMP = 25
        gMP = 100
        gAT = 45
        gDF = 20
        gMAT = 1
        gMDF = 35
        gSP = 30
        gAC = 100
        gEV = 110
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Female"
        gSYN = ["Colombian","Stressed","Leader"]
      if unit[0] == "Abby":
        gHP = 1100
        gcMP = 0
        gMP = 150
        gAT = 50
        gDF = 35
        gMAT = 1
        gMDF = 35
        gSP = 25
        gAC = 120
        gEV = 100
        gCT = 35
        gAPN = 0
        gMPN = 0
        gMRG = 15
        gGEN = "Female"
        gSYN = ["White","Naive"]
      if unit[0] == "Olivia":
        gHP = 900
        gcMP = 75
        gMP = 75
        gAT = 45
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Female"
        gSYN = ["Filipino","Chill"]
      if unit[0] == "Basel":
        gHP = 600
        gcMP = 0
        gMP = 75
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 10
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["Palestinian","Musclehead"]
      if unit[0] == "Handell":
        gHP = 650
        gcMP = 0
        gMP = 60
        gAT = 45
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["Dominican","Soy"]
      if unit[0] == "Shah":
        gHP = 650
        gcMP = 30
        gMP = 60
        gAT = 60
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Bengali","Musclehead"]
      if unit[0] == "Kholilur":
        gHP = 600
        gcMP = 0
        gMP = 100
        gAT = 60
        gDF = 30
        gMAT = 1
        gMDF = 20
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Bengali","Musclehead"]
      if unit[0] == "Ramirez":
        gHP = 450
        gcMP = 0
        gMP = 50
        gAT = 45
        gDF = 20
        gMAT = 1
        gMDF = 25
        gSP = 25
        gAC = 110
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Mexican","Weeb"]
      if unit[0] == "Keyur":
        gHP = 750
        gcMP = 25
        gMP = 100
        gAT = 40
        gDF = 25
        gMAT = 1
        gMDF = 35
        gSP = 30
        gAC = 100
        gEV = 110
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["Indian","Soy","Gamer"]
      if unit[0] == "Siddarth":
        gHP = 400
        gcMP = 0
        gMP = 50
        gAT = 40
        gDF = 20
        gMAT = 1
        gMDF = 25
        gSP = 100
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["Indian","Soy"]
      if unit[0] == "Amber":
        gHP = 500
        gcMP = 50
        gMP = 125
        gAT = 45
        gDF = 25
        gMAT = 1
        gMDF = 20
        gSP = 20
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Female"
        gSYN = ["Pakistani","Chill"]
      if unit[0] == "John":
        gHP = 900
        gcMP = 0
        gMP = 100
        gAT = 45
        gDF = 30
        gMAT = 1
        gMDF = 35
        gSP = 20
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Male"
        gSYN = ["White","Shy"]
      if unit[0] == "Metin":
        gHP = 1050
        gcMP = 0
        gMP = 100
        gAT = 70
        gDF = 40
        gMAT = 1
        gMDF = 5
        gSP = 20
        gAC = 100
        gEV = 80
        gCT = 20
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Male"
        gSYN = ["Turkish","Gamer"]
      if unit[0] == "Abida":
        gHP = 700
        gcMP = 0
        gMP = 75
        gAT = 50
        gDF = 25
        gMAT = 1
        gMDF = 20
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 13
        gGEN = "Female"
        gSYN = ["Bengali","Vulgar"]
      if unit[0] == "Taylor":
        gHP = 950
        gcMP = 0
        gMP = 100
        gAT = 60
        gDF = 30
        gMAT = 1
        gMDF = 30
        gSP = 20
        gAC = 100
        gEV = 90
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Female"
        gSYN = ["White","Gay","Gamer"]
      if unit[0] == "David":
        gHP = 900
        gcMP = 0
        gMP = 100
        gAT = 60
        gDF = 30
        gMAT = 1
        gMDF = 10
        gSP = 35
        gAC = 100
        gEV = 110
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Male"
        gSYN = ["Black","Chill","Musclehead"]
      if unit[0] == "Noah":
        gHP = 600
        gcMP = 0
        gMP = 75
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 25
        gSP = 30
        gAC = 110
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Male"
        gSYN = ["Puerto Rican","Free Spirit"]
      if unit[0] == "Dylan":
        gHP = 550
        gcMP = 0
        gMP = 100
        gAT = 50
        gDF = 30
        gMAT = 1
        gMDF = 20
        gSP = 30
        gAC = 100
        gEV = 110
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["White","Shy"]
      if unit[0] == "Erick":
        gHP = 600
        gcMP = 0
        gMP = 100
        gAT = 50
        gDF = 25
        gMAT = 1
        gMDF = 20
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 10
        gGEN = "Male"
        gSYN = ["Uruguayan","Gay"]
      if unit[0] == "Anthony":
        gHP = 600
        gcMP = 0
        gMP = 100
        gAT = 45
        gDF = 30
        gMAT = 1
        gMDF = 25
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 11
        gGEN = "Male"
        gSYN = ["Mexican","Gay"]
      if unit[0] == "Alberlyn":
        gHP = 500
        gcMP = 25
        gMP = 100
        gAT = 45
        gDF = 25
        gMAT = 1
        gMDF = 30
        gSP = 25
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Female"
        gSYN = ["Dominican","Free Spirit"]
      if unit[0] == "Shannae":
        gHP = 650
        gcMP = 0
        gMP = 60
        gAT = 50
        gDF = 25
        gMAT = 1
        gMDF = 20
        gSP = 30
        gAC = 100
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 12
        gGEN = "Female"
        gSYN = ["Black","Shy"]
      if unit[0] == "Ian":
        gHP = 1000
        gcMP = 25
        gMP = 80
        gAT = 65
        gDF = 35
        gMAT = 1
        gMDF = 30
        gSP = 40
        gAC = 110
        gEV = 100
        gCT = 25
        gAPN = 0
        gMPN = 0
        gMRG = 14
        gGEN = "Male"
        gSYN = ["White","Filipino","Musclehead"]
      if unit[0] == "Norman":
        gHP = 700
        gcMP = 0
        gMP = 125
        gAT = 40
        gDF = 30
        gMAT = 1
        gMDF = 40
        gSP = 30
        gAC = 110
        gEV = 110
        gCT = 35
        gAPN = 0
        gMPN = 0
        gMRG = 15
        gGEN = "Male"
        gSYN = ["Black","Soy","Weeb"]
      if unit[0] == "Alice":
        gHP = 650
        gcMP = 0
        gMP = 100
        gAT = 45
        gDF = 20
        gMAT = 1
        gMDF = 45
        gSP = 30
        gAC = 110
        gEV = 110
        gCT = 30
        gAPN = 0
        gMPN = 0
        gMRG = 14
        gGEN = "Female"
        gSYN = ["Chinese","Free Spirit"]      
      if ((len(self.team) < self.Level) and caro != True) and back == False:
        pepe = Entity(unit[0],gHP,gcMP,gMP,gAT,gDF,gMAT,gMDF,gSP,gAC,gEV,gCT,gAPN,gMPN,gMRG,str(ID),gGEN,gSYN,rarity)
        if unit[1] != "":
          pepe.items.append(unit[1])
        self.team.append(pepe)
        if skip != "Skip":
          print("\nYou purchased",unit[0]+"!")
        self.teamset("Team")
      elif ((len(self.team) == self.Level and caro != True)) and back == False:
        pepe = Entity(unit[0],gHP,gcMP,gMP,gAT,gDF,gMAT,gMDF,gSP,gAC,gEV,gCT,gAPN,gMPN,gMRG,str(ID),gGEN,gSYN,rarity)
        if unit[1] != "":
          pepe.items.append(unit[1])
        self.backteam.append(pepe)
        if skip != "Skip":
          print("\nYou purchased",unit[0]+"! They are moved to the reserve team!")
        self.teamset("Reserve")
      elif caro == True:
        pepe = Entity(unit[0],gHP,gcMP,gMP,gAT,gDF,gMAT,gMDF,gSP,gAC,gEV,gCT,gAPN,gMPN,gMRG,str(ID),gGEN,gSYN,rarity)
        if unit[1] != "":
          pepe.items.append(unit[1])
        carousellist.append(pepe)
      if back == True:
        self.team.append(Entity(unit[0],gHP,gcMP,gMP,gAT,gDF,gMAT,gMDF,gSP,gAC,gEV,gCT,gAPN,gMPN,gMRG,str(ID),gGEN,gSYN,rarity))
      if caro != True and back == False:
        self.gold = self.gold - rarity
        check = 1

class Entity:
  def __init__(self,NAME,HP,cMP,MP,AT,DF,MAT,MDF,SP,AC,EV,CT,APN,MPN,MRG,ID,GEN,SYN,RAR):
    self.SYN = SYN
    self.RAR = RAR
    self.NAME = NAME        #Variables that every fighting entity share 
    self.HP = HP            #Health - Allows you to fight when > 0 
    self.bHP = HP
    self.cMP = cMP
    self.bcMP = cMP
    self.MP = MP            #Mana - For casting skills"
    self.AT = AT            #Attack - Physical Damage
    self.bAT = AT
    self.DF = DF            #Defense - %cut of Physical damage based on rational function AT*(x/x+100)
    self.MAT = MAT          #Magic Attack - Magical Attack
    self.MDF = MDF          #Magic Defense - %cut of Magical damage based on rational function AT*(x/x+100)
    self.SP = SP            #Speed - Probability of going                                 
    self.AC = AC            #Accuracy - Chance of hitting
    self.EV = EV            #Evasion - Chance of dodgeing
    self.CT = CT            #Critical Chance - Chance of dealing bonus damage
    self.APN = APN          #Armor Penetration - Minuses Defense
    self.MPN = MPN          #Magic Penetration - Minuses Magic Defense
    self.MRG = MRG          #Mana Regeneration - Regens Mana on normal attacks
    self.cHP = HP
    self.cAT = AT
    self.cDF = DF
    self.cMAT = MAT
    self.cMDF = MDF
    self.cSP = SP
    self.cAC = AC
    self.cEV = EV
    self.cCT = CT
    self.CTdmg = 1.5
    self.cAPN = APN
    self.cMPN = MPN
    self.cMRG = MRG
    self.dmgreduct = 1
    self.ID = ID
    self.LV = 0
    self.cLV = self.LV
    self.GEN = GEN
    self.fHP = self.HP
    self.fMP = self.MP
    self.fcMP = self.cMP
    self.fAT = self.AT             
    self.fDF = self.DF
    self.fMAT = self.MAT
    self.fMDF = self.MDF
    self.fSP = self.SP
    self.fAC = self.AC
    self.fEV = self.EV
    self.fCT = self.CT
    self.fAPN = self.APN
    self.fMPN = self.MPN
    self.fMRG = self.MRG
    self.pAT = 1.00
    self.pDF = 1.00
    self.pMAT = 1.00
    self.pMDF = 1.00
    self.pSP = 1.00
    self.pAC = 1.00
    self.pEV = 1.00
    self.pCT = 1.00
    self.pAPN = 1.00
    self.pMPN = 1.00
    self.pMRG = 1.00       
    self.items = []
    self.color = ""
    self.lifesteal = 0 #Positive Effects $
    self.healmod = 1
    self.dmgstore = 0
    self.hitcount = 0
    self.totaldamage = 0
    self.immortal = 0
    self.ktogg = False
    self.dabstack = 0
    self.invis = 0
    self.trig = 0
    self.critflow = 0
    self.runhigh = 0
    self.thehut = False
    self.jabbaroll = 0
    self.tension = 0
    self.rallied = [0]
    self.simping = 0
    self.simped = [0]
    self.giant = False
    self.confection = [0]
    self.eagle = [0]
    self.sexy = 0
    self.teamed = [0]
    self.sitting = [0]
    self.hiding = 0
    self.swift = 0
    self.organ = False
    self.organized = 0
    self.hogrider = 0
    self.hogg = 0
    self.anime = [0]
    self.jutsu = False
    self.graced = [0]
    self.ego = []
    self.weebHP = 0
    self.mferv = 0
    self.fferv = 0
    self.destiny = 0
    self.knowledge = 0
    self.trying = 0
    self.cross = 0
    self.kahoot = 0
    self.javelin = 0
    self.syria = 0
    self.tunis = 0
    self.chin = 0
    self.urug = False
    self.emohit = 0
    self.graham = [0,0,0,0,0,0,0,0,0,0,0]
    self.fear = [0,0]      #Negative Effects
    self.charmed = 0
    self.poisond = 0
    self.poisont = 0
    self.bleedd = 0
    self.bleedt = 0
    self.burnd = 0
    self.burnt = 0
    self.decayd = 0
    self.decayt = 0
    self.silenced = 0
    self.disarmed = 0
    self.tremsl = 0
    self.greased = [0]
    self.blind = 0
    self.named = [0]
    self.crips = [0]
    self.touched = [0]
    self.chilled = [0]
    self.deathmark = 0
    self.sad = [0]
    self.drift = [0]
    self.chilly = 0
    self.burning = 0
    self.grievous = 0
    self.tethered = [0]
    self.hater = 0
    self.hatelis = []
    self.delled = 0
    self.scanned = 0
    self.deturn = 0
    #Stuns
    self.stunned = False
    self.stunimmune = False
    self.tremstun = 0
    self.dance = 0
    self.rooted = 0
    self.taunted = [0]
    self.frozen = 0
    self.paralyzed = 0
    self.confused = 0
    self.crushed = False
    #Mob Essentials
    self.setHP = 0

  def setlevel(self,Lev):
    diff = Lev-self.LV
    for x in range(diff):
      self.HP = self.HP + round(self.bHP*0.2)
      self.AT = self.AT + round(self.bAT*0.2)
      self.cHP = self.HP
      self.fHP = self.HP
      self.LV = self.LV + 1
      self.cLV = self.LV

  def itemcatalog(self):
    for x in self.items:
      if x == "Bloodrazor":
        print(fore.YELLOW_1+style.BOLD+"Bloodrazor"+style.RESET+fore.YELLOW_1,"(Attack + Attack):"+style.RESET,"Attacks apply a bleed for 1.5% of an enemy’s max health(HP) for 5 turns.")
      if x == "Zulfiqar":
        print(fore.YELLOW_1+style.BOLD+"Zulfiqar"+style.RESET+fore.YELLOW_1,"(Attack + Defense):"+style.RESET,"Dodging an attack disarms the attacker for 1 turn.")
      if x == "Anatomy of Hearts":
        print(fore.YELLOW_1+style.BOLD+"Anatomy of Hearts"+style.RESET+fore.YELLOW_1,"(Attack + Health):"+style.RESET,"Send out a pulse that deals 7.5% of an enemy’s current health as magic damage to 3 random enemies. This pulse ignores barriers, accuracy(AC) check, and cannot kill an enemy. Only procs if the user lives on their turn.")
      if x == "Flow of Wind":
        print(fore.YELLOW_1+style.BOLD+"Flow of Wind"+style.RESET+fore.YELLOW_1,"(Attack + Mana):"+style.RESET,"Increases mana regeneration(MRG) by 4.")
      if x == "Duality":
        print(fore.YELLOW_1+style.BOLD+"Duality"+style.RESET+fore.YELLOW_1,"(Attack + Magic Attack):"+style.RESET,"The user’s attack(AT) is increased by 35% of the user’s magic attack(MAT) above 100%.")
      if x == "Thotslayer":
        print(fore.YELLOW_1+style.BOLD+"Thotslayer"+style.RESET+fore.YELLOW_1,"(Attack + Magic Defense):"+style.RESET,"Deal 20% more damage to Females.")
      if x == "Rally Banner":
        print(fore.YELLOW_1+style.BOLD+"Rally Banner"+style.RESET+fore.YELLOW_1,"(Attack + Speed):"+style.RESET,"Increases all ally’s speed(SP) in the unit’s combat row by 2.")
      if x == "Honjo Masamune":
        print(fore.YELLOW_1+style.BOLD+"Honjo Masamune"+style.RESET+fore.YELLOW_1,"(Attack + Critical):"+style.RESET,"Increases armor penetration(APN) by +35 when the user's health(HP) is above 50%.")
      if x == "Thornmail":
        print(fore.YELLOW_1+style.BOLD+"Thornmail"+style.RESET+fore.YELLOW_1,"(Defense + Defense):"+style.RESET,"Reflect 20% of raw melee damage taken back to enemy as magic damage. This damage cannot miss, does not proc barriers, and cannot kill an enemy. This does not proc if the user dies from the enemy attack.")
      if x == "Flaming Cinders":
        print(fore.YELLOW_1+style.BOLD+"Flaming Cinders"+style.RESET+fore.YELLOW_1,"(Defense + Health):"+style.RESET,"Anyone who attacks the user has their healing reduced by 50% for 3 turns. This does not proc if the user dies, and does not stack with Grand.")
      if x == "The Gambit":
        print(fore.YELLOW_1+style.BOLD+"The Gambit"+style.RESET+fore.YELLOW_1,"(Defense + Mana):"+style.RESET,"Increases mana(MP) gained by being attacked by 70%.")
      if x == "Feminism":
        print(fore.YELLOW_1+style.BOLD+"Feminism"+style.RESET+fore.YELLOW_1,"(Defense + Magic Attack):"+style.RESET,"Deal 20% more damage to Males.")
      if x == "Obscene Wear":
        print(fore.YELLOW_1+style.BOLD+"Obscene Wear"+style.RESET+fore.YELLOW_1,"(Defense + Magic Defense):"+style.RESET,"Taunt all enemies at the beginning of battle for 1 turn.")
      if x == "Miller's Hearing Aid":
        print(fore.YELLOW_1+style.BOLD+"Miller's Hearing Aid"+style.RESET+fore.YELLOW_1,"(Defense + Speed):"+style.RESET,"Gain +100% evasion(EV) on every 5th attack the user is hit.")
      if x == "Critical Measure":
        print(fore.YELLOW_1+style.BOLD+"Critical Measure"+style.RESET+fore.YELLOW_1,"(Defense + Critical):"+style.RESET,"When the user is under 25% max health(HP), gain +75% critical chance(CT).")
      if x == "Eternal":
        print(fore.YELLOW_1+style.BOLD+"Eternal"+style.RESET+fore.YELLOW_1,"(Health + Health):"+style.RESET,"Increase your health(HP) by a further +300. (+600 HP in total)")
      if x == "Care Package":
        print(fore.YELLOW_1+style.BOLD+"Care Package"+style.RESET+fore.YELLOW_1,"(Health + Mana):"+style.RESET,"Randomly heal an ally for 10% of their missing health(HP) per turn. Only procs if the user lives on their turn.")
      if x == "Grand":
        print(fore.YELLOW_1+style.BOLD+"Grand"+style.RESET+fore.YELLOW_1,"(Health + Magic Attack):"+style.RESET,"The user’s ability damage lowers the healing of any enemy hit by 50% for 10 turns. This does not stack with Flaming Cinders.")
      if x == "Devourer":
        print(fore.YELLOW_1+style.BOLD+"Devourer"+style.RESET+fore.YELLOW_1,"(Health + Magic Defense):"+style.RESET,"Heal for 20% of missing health(HP) every time any enemy is defeated.")
      if x == "Cleats":
        print(fore.YELLOW_1+style.BOLD+"Cleats"+style.RESET+fore.YELLOW_1,"(Health + Speed):"+style.RESET,"Regenerate the user for 2.5% of their maximum health(HP) per turn.")
      if x == "Pearson Textbook":
        print(fore.YELLOW_1+style.BOLD+"Pearson Textbook"+style.RESET+fore.YELLOW_1,"(Health + Critical):"+style.RESET,"Revives a user upon death with 75% of their health(HP). The user is cleansed upon revival.")
      if x == "Endiness":
        print(fore.YELLOW_1+style.BOLD+"Endiness"+style.RESET+fore.YELLOW_1,"(Mana + Mana):"+style.RESET,"After casting an ability, recover 20 mana(MP).")
      if x == "Tryhard":
        print(fore.YELLOW_1+style.BOLD+"Tryhard"+style.RESET+fore.YELLOW_1,"(Mana + Magic Attack):"+style.RESET,"Gain magic attack(MAT) equivalent to 25% of the user’s base mana(MP) required after they cast the skill. This can total to 100% of the user's base mana(MP), or 4 total casts.")
      if x == "Rulebook":
        print(fore.YELLOW_1+style.BOLD+"Rulebook"+style.RESET+fore.YELLOW_1,"(Mana + Magic Defense):"+style.RESET,"All allies in the same row as this unit have +30 magic attack(MAT) split among all allies.")
      if x == "Resource Catalyst":
        print(fore.YELLOW_1+style.BOLD+"Resource Catalyst"+style.RESET+fore.YELLOW_1,"(Mana + Speed):"+style.RESET,"Gain bonus speed(SP) equal to the user’s base mana regeneration(MRG).")
      if x == "Giancoli Textbook":
        print(fore.YELLOW_1+style.BOLD+"Giancoli Textbook"+style.RESET+fore.YELLOW_1,"(Mana + Critical):"+style.RESET,"Revives a user upon death with 20% of their health(HP) and 80% of their mana(MP) full. The user is cleansed upon revival.")
      if x == "Last Say":
        print(fore.YELLOW_1+style.BOLD+"Last Say"+style.RESET+fore.YELLOW_1,"(Magic Attack + Magic Attack):"+style.RESET,"Gain 50% magic penetration(MPN).")
      if x == "Cross":
        print(fore.YELLOW_1+style.BOLD+"Cross"+style.RESET+fore.YELLOW_1,"(Magic Attack + Magic Defense):"+style.RESET,"Have a magic damage barrier up at the start of battle for 1 instance of magic damage.")
      if x == "Kahoot":
        print(fore.YELLOW_1+style.BOLD+"Kahoot"+style.RESET+fore.YELLOW_1,"(Magic Attack + Speed):"+style.RESET,"Gain 2.5% magic attack(MAT) every of the user’s turn, up to a maximum of 100%.")
      if x == "God's Javelin":
        print(fore.YELLOW_1+style.BOLD+"God's Javelin"+style.RESET+fore.YELLOW_1,"(Magic Attack + Critical):"+style.RESET,"Increase critical chance(CT) and critical damage by 15% every time the user casts their ability.")
      if x == "Bible":
        print(fore.YELLOW_1+style.BOLD+"Bible"+style.RESET+fore.YELLOW_1,"(Magic Defense + Magic Defense):"+style.RESET,"Gain +60 magic defense(MDF). (+100 MDF in total)")
      if x == "Hater Guard":
        print(fore.YELLOW_1+style.BOLD+"Hater Guard"+style.RESET+fore.YELLOW_1,"(Magic Defense + Speed):"+style.RESET,"Gain +10 magic defense(MDF) and +10% evasion(EV) for every enemy that tries to hit the unit in the last 3 turns.")
      if x == "Physics Equation Sheet":
        print(fore.YELLOW_1+style.BOLD+"Physics Equation Sheet"+style.RESET+fore.YELLOW_1,"(Magic Defense + Critical):"+style.RESET,"Upon getting hit by a critical strike, reduce the enemy’s critical strike chance to 0% for 3 turns. This only procs if the holder is alive.")
      if x == "Vengeance":
        print(fore.YELLOW_1+style.BOLD+"Vengeance"+style.RESET+fore.YELLOW_1,"(Speed + Speed):"+style.RESET,"Gain +200% accuracy(AC).")
      if x == "Sacred Scythe":
        print(fore.YELLOW_1+style.BOLD+"Sacred Scythe"+style.RESET+fore.YELLOW_1,"(Speed + Critical):"+style.RESET,"Gain 50% crit strike damage.")
      if x == "Graham's Report":
        print(fore.YELLOW_1+style.BOLD+"Graham's Report"+style.RESET+fore.YELLOW_1,"(Critical + Critical):"+style.RESET,"Gain 2% of a random stat on your turn, excluding health(HP). The crit strike(CT) bonuses are 10% instead of 2%.")
      if x == "Attack":
        print(fore.YELLOW_1+"Attack:"+style.RESET,"Gain +10 attack(AT).")
      if x == "Defense":
        print(fore.YELLOW_1+"Defense:"+style.RESET,"Gain +20 defense(DF).")
      if x == "Health":
        print(fore.YELLOW_1+"Health:"+style.RESET,"Gain +150 health(HP).")
      if x == "Mana":
        print(fore.YELLOW_1+"Mana:"+style.RESET,"Gain +15 starting mana(MP).")
      if x == "Magic Attack":
        print(fore.YELLOW_1+"Magic Attack:"+style.RESET,"Gain +10% magic attack(MAT).")
      if x == "Magic Defense":
        print(fore.YELLOW_1+"Magic Defense:"+style.RESET,"Gain +20 magic defense(MDF).")
      if x == "Speed":
        print(fore.YELLOW_1+"Speed:"+style.RESET,"Gain +5 speed(SP).")
      if x == "Critical":
        print(fore.YELLOW_1+"Defense:"+style.RESET,"Gain +5% critical chance(CT).")

  
  def mixitem(self,item):
    mixer = self.items[len(self.items)-1]
    if mixer == "Attack" or mixer == "Defense" or mixer == "Health" or mixer == "Mana" or mixer == "Magic Attack" or mixer == "Magic Defense" or mixer == "Speed" or mixer == "Critical":    
      self.items.remove(mixer)
      mix = [item,mixer]
      if mix[0] == "Attack" and mix[1] == "Attack":
        self.items.append("Bloodrazor")
      if "Attack" in mix and "Defense" in mix:
        self.items.append("Zulfiqar")
      if "Attack" in mix and "Health" in mix:
        self.items.append("Anatomy of Hearts")
      if "Attack" in mix and "Mana" in mix:
        self.items.append("Flow of Wind")
      if "Attack" in mix and "Magic Attack" in mix:
        self.items.append("Duality")
      if "Attack" in mix and "Magic Defense" in mix:
        self.items.append("Thotslayer")
      if "Attack" in mix and "Speed" in mix:
        self.items.append("Rally Banner")
      if "Attack" in mix and "Critical" in mix:
        self.items.append("Honjo Masamune")
      if mix[0] == "Defense" and mix[1] == "Defense":
        self.items.append("Thornmail")
      if "Defense" in mix and "Health" in mix:
        self.items.append("Flaming Cinders")
      if "Defense" in mix and "Mana" in mix:
        self.items.append("The Gambit")
      if "Defense" in mix and "Magic Attack" in mix:
        self.items.append("Feminism")
      if "Defense" in mix and "Magic Defense" in mix:
        self.items.append("Obscene Wear")
      if "Defense" in mix and "Speed" in mix:
        self.items.append("Miller's Hearing Aid")
      if "Defense" in mix and "Critical" in mix:
        self.items.append("Critical Measure")
      if mix[0] == "Health" and mix[1] == "Health":
        self.items.append("Eternal")
      if "Health" in mix and "Mana" in mix:
        self.items.append("Care Package")
      if "Health" in mix and "Magic Attack" in mix:
        self.items.append("Grand")
      if "Health" in mix and "Magic Defense" in mix:
        self.items.append("Devourer")
      if "Health" in mix and "Speed" in mix:
        self.items.append("Cleats")
      if "Health" in mix and "Critical" in mix:
        self.items.append("Pearson Textbook")
      if mix[0] == "Mana" and mix[1] == "Mana":
        self.items.append("Endiness")
      if "Mana" in mix and "Magic Attack" in mix:
        self.items.append("Tryhard")
      if "Mana" in mix and "Magic Defense" in mix:
        self.items.append("Rulebook")
      if "Mana" in mix and "Speed" in mix:
        self.items.append("Resource Catalyst")
      if "Mana" in mix and "Critical" in mix:
        self.items.append("Giancoli Textbook")
      if mix[0] == "Magic Attack" and mix[1] == "Magic Attack":
        self.items.append("Last Say")
      if "Magic Attack" in mix and "Magic Defense" in mix:
        self.items.append("Cross")
      if "Magic Attack" in mix and "Speed" in mix:
        self.items.append("Kahoot")
      if "Magic Attack" in mix and "Critical" in mix:
        self.items.append("God's Javelin")
      if mix[0] == "Magic Defense" and mix[1] == "Magic Defense":
        self.items.append("Bible")
      if "Magic Defense" in mix and "Speed" in mix:
        self.items.append("Hater Guard")
      if "Magic Defense" in mix and "Critical" in mix:
        self.items.append("Physics Equation Sheet")
      if mix[0] == "Speed" and mix[1] == "Speed":
        self.items.append("Vengeance")
      if "Speed" in mix and "Critical" in mix:
        self.items.append("Sacred Scythe")
      if mix[0] == "Critical" and mix[1] == "Critical":
        self.items.append("Graham's Report")
    else:
      if len(self.items) < 3:
        self.items.append(item)


  def effects(self,ally,enemy): #Non-Global effects(so no timer here for onhit or onturn)

    global turncount

    #if self.NAME == "Abby": #~
      #self.stunimmune = True

    #Synergy

    if self.mferv > 0:
      if ally.ben >= 2 and ally.ben < 4:
        self.pAT = self.pAT * (1+(0.075*self.mferv))
      elif ally.ben >= 4:
        self.pAT = self.pAT * (1+(0.1*self.mferv))

    if self.fferv > 0:
      if ally.ben >= 2 and ally.ben < 4:
        self.pMAT = self.pMAT * (1+(0.075*self.fferv))
      elif ally.ben >= 4:
        self.pMAT = self.pMAT * (1+(0.1*self.fferv))

    if self.chilly > 0:
      if self.runhigh <= 0:
        self.pSP = self.pSP * 0.6
    
    if ally.mex >= 2:
      if ally.mex >=2 and ally.mex < 4 and "Mexican" in self.SYN:
        self.fDF = self.fDF + 30
      elif ally.mex >= 4:
        self.fDF = self.fDF + 80

    if "Black" in self.SYN:
      if ally.bla >= 2 and ally.bla < 4:
        self.pSP = self.pSP * 1.1
      elif ally.bla >= 4 and ally.bla < 6:
        self.pSP = self.pSP * 1.2
      elif ally.bla >= 6 and ally.bla < 8:
        self.pSP = self.pSP * 1.5
      elif ally.bla >= 8:
        self.pSP = self.pSP * 2
    
    if "Peruvian" in self.SYN:
      if ally.per >= 2 and ally.per < 5:
        self.lifesteal = self.lifesteal + 0.2
      elif ally.per >= 5:
        self.lifesteal = self.lifesteal + 0.5

    if ally.fil >= 2:
      if ally.fil >= 2 and ally.fil < 4 and "Filipino" in self.SYN:
        self.pMRG = self.pMRG * 1.5
      elif ally.fil >= 4:
        self.pMRG = self.pMRG * 1.5

    if ally.pue > 0:
      if ally.pue == 1 and "Puerto Rican" in self.SYN:
        self.fAC = self.fAC + 30
      if ally.pue >= 2:
        self.fAC = self.fAC + 60

    if self.syria > 0:
      self.fEV = self.fEV + (20*self.syria)

    if "Uruguayan" in self.SYN:
      if self.urug == True:
        if ally.uru == 1:
          self.fDF = self.fDF + 100
          self.fMDF = self.fMDF + 100
        elif ally.uru >= 2:
          self.fDF = self.fDF + 200
          self.fMDF = self.fMDF + 200

    if ally.whi >= 2:
      if ally.whi >=2 and ally.whi < 4 and "White" in self.SYN:
        self.fMAT = self.fMAT + 0.25
      elif ally.whi >= 4 and ally.whi < 6 and "White" in self.SYN:
        self.fMAT = self.fMAT + 0.5
      elif ally.whi >= 6 and ally.whi < 8:
        self.fMAT = self.fMAT + 0.75
      elif ally.whi >= 8:
        self.fMAT = self.fMAT + 1

    if "Intellectual" in self.SYN:
      if self.cHP < round(0.5*self.fHP):
        self.pMRG = self.pMRG * 2
      if ally.int >= 3:
        self.fMPN = self.fMPN + 50
        self.fAC = self.fAC + 20
        self.fEV = self.fEV + 20

    if ally.mus >= 2:
      if ally.mus >= 3 and ally.mus < 5:
        self.pAT = self.pAT * 1.2
        if "Musclehead" in self.SYN:
          self.fDF = self.fDF + 30
          self.fSP = self.fSP + 5
      elif ally.mus >= 5:
        self.pAT = self.pAT * 1.75
        if "Musclehead" in self.SYN:
          self.fDF = self.fDF + 100
          self.fSP = self.fSP + 20

    if ally.lea >= 1:
      if ally.lea > 1:
        if "Leader" in self.SYN:
          self.pAT = self.pAT * 0.5
          self.pMAT = self.pMAT * 0.5
      elif ally.lea == 1:
        if "Leader" in self.SYN:
          self.pMRG = self.pMRG * (1+(0.05*ally.soy))
          self.pAT = self.pAT * (1+(0.05*ally.soy))
          self.pMAT = self.pMAT * (1+(0.05*ally.soy))
          self.pDF = self.pDF * (1+(0.05*ally.soy))
          self.pMDF = self.pMDF * (1+(0.05*ally.soy))
          self.pSP = self.pSP * (1+(0.05*ally.soy))
          self.pAC = self.pAC * (1+(0.05*ally.soy))
          self.pEV = self.pEV * (1+(0.05*ally.soy))
          self.pCT = self.pCT * (1+(0.05*ally.soy))
          self.pAPN = self.pAPN * (1+(0.05*ally.soy))
          self.pMPN = self.pMPN * (1+(0.05*ally.soy))
        self.fSP = self.fSP + 10

    if "Pure" in self.SYN:
      taken = self.hitcount
      if taken > 10:
        taken = 10
      self.pAT = self.pAT * (2-(0.1*taken))
      self.pMAT = self.pMAT * (2-(0.1*taken))
      self.pDF = self.pDF * (2-(0.1*taken))
      self.pMDF = self.pMDF * (2-(0.1*taken))

    if "Stressed" in self.SYN:
      if ally.str >= 1 and ally.str < 3:
        if self.cHP < round(0.25*self.fHP):
          self.fCT = self.fCT + 50
          self.pAT = self.pAT * 1.5
          self.pMAT = self.pMAT * 1.5
          self.pSP = self.pSP * 1.5
      elif ally.str >= 3:
        if self.cHP < round(0.25*self.fHP):
          self.fCT = self.fCT + 100
          self.pAT = self.pAT * 2
          self.pMAT = self.pMAT * 2
          self.pSP = self.pSP * 2

    if "Weeb" in self.SYN and ally.wee >= 3:
      self.fHP = self.weebHP

    #Items
    if "Critical Measure" in self.items:
      if self.cHP < round(0.25*self.fHP):
        self.fCT = self.fCT + 75

    if "Honjo Masamune" in self.items:
      if self.cHP > round(0.5*self.fHP):
        self.fAPN = self.fAPN + 35

    if self.trying > 0:
      self.fMAT = self.fMAT + (self.trying*0.0025*(self.MP))

    if self.kahoot > 0:
      if self.kahoot > 40:
        self.kahoot = 40
      self.pMAT = self.pMAT * (1+(0.025*self.kahoot))

    if self.javelin > 0:
      self.fCT = self.fCT + (15*self.javelin)
      self.CTdmg = self.CTdmg + (0.15*self.javelin)

    if "Graham's Report" in self.items:
      self.pAT = self.pAT * (1+(0.02*self.graham[0]))
      self.pDF = self.pDF * (1+(0.02*self.graham[1]))
      self.pMAT = self.pMAT * (1+(0.02*self.graham[2]))
      self.pMDF = self.pMDF * (1+(0.02*self.graham[3]))
      self.pSP = self.pSP * (1+(0.02*self.graham[4]))
      self.pAC = self.pAC * (1+(0.02*self.graham[5]))
      self.pEV = self.pEV * (1+(0.02*self.graham[6]))
      self.pCT = self.pCT * (1+(0.1*self.graham[7]))
      self.pAPN = self.pAPN * (1+(0.02*self.graham[8]))
      self.pMPN = self.pMPN * (1+(0.02*self.graham[9]))
      self.pMRG = self.pMRG * (1+(0.02*self.graham[10]))

    #Map effect

    if self.chilled[0] > 0:
      if self.runhigh <= 0:
        self.pSP = self.pSP * (1-(self.chilled[2]*(0.2+(0.0125*self.chilled[1].cLV))))

    #Normal effect

    if self.tethered[0] == 1:
      self.pAT = self.pAT * (0.75-(0.05*self.tethered[1].cLV))
      self.pMAT = self.pMAT * (0.75-(0.05*self.tethered[1].cLV)) 
    
    if self.NAME == "Amira":
      for x in enemy.team:
        if x.tethered[0] == 1:
          self.fAT = self.fAT + ((0.25+(0.05*self.cLV))*x.fAT)
          self.fMAT = self.fMAT + ((0.25+(0.05*self.cLV))*x.fMAT)

    if self.burnt > 0:    #On Turn Debuff
      self.pAT = self.pAT * 0.75
      self.pMAT = self.pMAT * 0.75
    
    if self.bleedt >0:    #On Turn Debuff
      if self.runhigh <= 0:
        self.pSP = self.pSP * 0.75

    if self.poisont >0:   #On Turn Debuff
      self.pDF = self.pDF * 0.75
      self.pMDF = self.pMDF * 0.75

    if self.grievous > 0:
      self.healmod = self.healmod * 0.5
    
    if self.graced[0] > 0:
      self.healmod = self.healmod * (1.25+(0.025*self.graced[1].cLV))

    if self.fear[0] > 0:
      if self.fear[1] > 11:
        self.fear[1] = 11
      self.dmgreduct = self.dmgreduct * (1.25 + (0.075*(self.fear[1]-1)))
      self.pAT = self.pAT * (0.75 - (0.05*(self.fear[1]-1)))
      self.pMAT = self.pMAT * (0.75 - (0.05*(self.fear[1]-1)))

    if self.blind > 0:
      self.pEV = self.pEV * 0.75
      self.pAC = self.pAC * 0.75
      self.pCT = self.pCT * 0.75
    
    if self.deathmark > 0:
      self.dmgreduct = self.dmgreduct + self.deathmark

    if self.ktogg == True:
      self.pAT = self.pAT * 2
      self.pDF = self.pDF * 2
      self.pMAT = self.pMAT * 2
      self.pMDF = self.pMDF * 2
      self.pSP = self.pSP * 2
      
    if self.tremsl > 0:    #Global debuff
      if self.runhigh <= 0:
        self.pSP = self.pSP * 0.5

    if self.delled > 0:
      self.pAC = self.pAC * 0.6

    if self.anime[0] > 0:
      self.fSP = self.fSP + (10+(2*self.anime[1].cLV))

    if self.drift[0] > 0:
      if self.runhigh <= 0:
        self.psP = self.pSP * (0.5-(0.0375*self.drift[1].cLV))

    if self.greased[0] > 0:    #On hit debuff
      self.fEV = self.fEV - (40+(10*self.greased[1].cLV))

    if self.burning > 0:
      self.healmod = self.healmod * 0.5
         
    if self.thehut == True:
      self.dmgreduct = self.dmgreduct * (0.65-(0.05*self.cLV))

    if self.giant == True:
      self.pAT = self.pAT * (3.5+(0.25*self.cLV))
      self.pEV = self.pEV * 0
      self.fHP = self.fHP + (800+(200*self.cLV))
      self.pAC = self.pAC * 1.5

    if self.sitting[0] == 1:
      self.fDF = self.fDF + self.cMAT*(20+(5*self.cLV))
      self.fMDF = self.fMDF + self.cMAT*(20+(5*self.cLV))

    if self.organized > 0:
      for x in ally.team:
        if x.organ == True:
          self.fEV = self.fEV + (14+(2*x.cLV))
          self.fCT = self.fCT + (14+(2*x.cLV))
          self.pMRG = self.pMRG * (1.14+(0.02*x.cLV))
          break

    if self.hogg > 0:
      for x in ally.team:
        if x.hogrider == 1:
          self.pAT = self.pAT * (1.3+(0.03*x.cLV))
          break

    if self.swift > 0:
      self.fEV = self.fEV + (10*self.swift)

    if self.teamed[0] > 0:
      self.fDF = self.fDF + self.teamed[2]*(60+(5*self.teamed[1].cLV))

    if self.sad[0] > 0:
      self.pAT = self.pAT * (1-(self.sad[2]*(0.3+(0.0375*self.sad[1].cLV))))
      if self.pAT < 0:
        self.pAT = 0

    if self.eagle[0] > 0:
      self.pAC = self.pAC * (self.eagle[1]*(1.3+(0.03*self.cLV)))
      self.fCT = self.fCT + (self.eagle[1]*(30+(3*self.cLV)))

    if self.confection[0] > 0:
      if self.confection[2] == 1:
        self.pAT = self.pAT * (self.confection[3]*(1.1+(0.02*self.confection[1].cLV)))
      elif self.confection[2] == 2:
        self.pDF = self.pDF * (self.confection[3]*(1.1+(0.02*self.confection[1].cLV)))
      elif self.confection[2] == 3:
        self.pMAT = self.pMAT * (self.confection[3]*(1.1+(0.02*self.confection[1].cLV)))
      elif self.confection[2] == 4: 
        self.pMDF = self.pMDF * (self.confection[3]*(1.1+(0.02*self.confection[1].cLV)))

    if self.crips[0] > 0:
      if self.runhigh <= 0:
        self.pSP = self.pSP * (1-(self.crips[2]*(0.2+(0.02*self.crips[1].cLV))))
    
    if self.touched[0] > 0:
      self.pAC = self.pAC * (1-(self.touched[2]*(0.2+(0.03*self.touched[1].cLV))))

    if self.rallied[0] > 0:
      self.fAPN = self.fAPN + self.rallied[2]
      self.fMPN = self.fMPN + self.rallied[2]

    if self.simping > 0:
      perc = 0.1+(0.0125*self.cLV)
      for x in range(self.simping):
        self.fHP = self.fHP*(1-perc)
        self.fAT = self.fAT*(1-perc)
        self.fDF = self.fDF*(1-perc)
        self.fMDF = self.fMDF*(1-perc)
        self.fMAT = self.fMAT*(1-perc)
      if self.cHP > self.fHP:
        self.cHP = round(self.fHP)

    if self.simped[0] > 0:
      self.fHP = self.fHP + (self.simped[0]*self.simped[1].HP)
      self.fAT = self.fAT + (self.simped[0]*self.simped[1].AT)
      self.fDF = self.fDF + (self.simped[0]*self.simped[1].DF)
      self.fMAT = self.fMAT + (self.simped[0]*self.simped[1].MAT)
      self.fMDF = self.fMDF + (self.simped[0]*self.simped[1].MDF)

    if self.named[0] > 0:
      self.fMP = self.fMP + round(self.named[2]*(0.2+(.02*self.named[1].cLV))*self.MP)

    if self.chin > 0:
      self.fSP = self.fSP + self.chin

    for x in allfighters:
      if turncount > (7.5*len(allfighters)):
        x.pAT = x.pAT * 1.5
        x.pMAT = x.pMAT * 1.5
        x.healmod = x.healmod * (2/3)
        #x.pAT = x.pAT * (1+(0.01*(turncount-60)))
        #x.pMAT = x.pMAT * (1+(0.01*(turncount-90)))
        #x.healmod = x.healmod * (1-((1/90)*(turncount-90)))
        #if x.healmod < 0:
          #x.healmod = 0

    if self.runhigh > 0:    #Global buff
      cMAT = self.pMAT * self.fMAT
      self.fAT = self.fAT + cMAT*(40+(4*self.cLV))
      self.fDF = self.fDF + cMAT*(40+(4*self.cLV))

    if self.critflow > 0:
      msc = round(self.fMAT*self.pMAT)
      self.CTdmg = self.CTdmg + msc*(0.5+(0.1*self.cLV))
      self.fCT = self.fCT + msc*(25+(7.5*self.cLV))

    if self.NAME == "Ishraq":
      msc = round(self.fMAT*self.pMAT)
      self.pAT = self.pAT * (1+((0.75+(0.1*self.cLV))*(1-(self.cHP/self.fHP))))
      self.pSP = self.pSP * (1+((0.75+(0.1*self.cLV))*(1-(self.cHP/self.fHP))))    
      self.lifesteal = self.lifesteal + msc*(((0.75+(0.1*self.cLV))*(1-(self.cHP/self.fHP))))

    if self.scanned > 0:
      self.pCT = 0

    if "Korean" in self.SYN:
      self.CTdmg = self.CTdmg + 1.5
      tot = round(self.fCT*self.pCT)
      if tot > 100:
        self.fAT = self.fAT + (100-tot)

    if "Duality" in self.items:
      cMAT = self.cMAT*self.fMAT
      self.fAT = self.fAT + (0.35*(100*(cMAT-1)))

      
  def maptimers(self,ally,enemy,skip=""): #Map effects, on no matter what, usually with global timers
    global sett

    if self.chilled[0] > 0:
      self.chilled[0] = self.chilled[0] - 1
      if self.chilled[0] == 0:
        if skip != "Skip":
          time.sleep(0.5)
          print("\nThe chill vibes sway away from the battlefield!")
        for x in ally.team:
          x.chilled = [0]
        for x in ally.backteam:
          x.chilled = [0]
        for x in ally.deadteam:
          x.chilled = [0]

 
  def globaltimers(self,skip=""):
    global sett


    if self.runhigh > 0:
      self.runhigh = self.runhigh - 1
      if self.runhigh == 0 and skip !="Skip":
        res = attr("reset")
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"exits the runner's high!")

    if self.tremsl > 0:
      self.tremsl = self.tremsl - 1

    if self.chilly > 0:
      self.chilly = self.chilly - 1

  def onhittimersdefense(self,ene,timer,dmg=0,mr="",skip=""):

    global sett
    global play1
    global play2

    self.dmgstore = self.dmgstore + dmg
    self.hitcount = self.hitcount + 1
    ene.totaldamage = ene.totaldamage + (sett-self.cHP)
    res = attr("reset")
   
    if "Syrian" in self.SYN:
      self.syria = self.syria + 1

    if self.urug == True and self.cHP <= round(0.5*self.fHP):
      self.urug = False

    #print(ene.NAME,ene.totaldamage)
    if self in play1.team:
      if "Weeb" in self.SYN and play1.wee >=3:
        for x in play1.team:
          if "Weeb" in x.SYN:
            x.cHP = self.cHP
      
      if "Indian" in self.SYN:
        if play1.ind >= 2 and play1.ind < 4:
          ch = random.randint(1,100)
          if ch <= 50:
            if ene.burnt < 2:
              ene.burnt = 2
            ene.burnd = ene.burnd + (self.cMAT*self.cAT*0.5)
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+ene.color+ene.NAME+res,"is burned from attacking",self.color+self.NAME+res+"!")
        if play1.ind >= 4:
          if ene.burnt < 2:
            ene.burnt = 2
          ene.burnd = ene.burnd + (self.cMAT*self.cAT)
          if skip != "Skip":
            time.sleep(timer)
            print("\n"+ene.color+ene.NAME+res,"is burned from attacking",self.color+self.NAME+res+"!")
            
    if self in play2.team:
      if "Weeb" in self.SYN and play2.wee >=3:
        for x in play2.team:
          if "Weeb" in x.SYN:
            x.cHP = self.cHP

      if "Indian" in self.SYN:
        if play2.ind >= 2 and play2.ind < 4:
          ch = random.randint(1,100)
          if ch <= 50:
            if ene.burnt < 2:
              ene.burnt = 2
            ene.burnd = ene.burnd + (self.cMAT*self.cAT*0.5)
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+ene.color+ene.NAME+res,"is burned from attacking",self.color+self.NAME+res+"!")
        if play2.ind >= 4:
          if ene.burnt < 2:
            ene.burnt = 2
          ene.burnd = ene.burnd + (self.cMAT*self.cAT)
          if skip != "Skip":
            time.sleep(timer)
            print("\n"+ene.color+ene.NAME+res,"is burned from attacking",self.color+self.NAME+res+"!")

    if "Grand" in ene.items and "Auto" not in mr:
      if self.grievous < 10:
        self.grievous = 10

    if self.cross == 1 and "Magical" in mr:
      self.cross = 0
      if skip != "Skip":
        time.sleep(timer)
        print("\n"+self.color+self.NAME+res+"'s cross breaks!")

    if self.cHP <= 0:   #Defensive affects that go through death/(Shields,etc.)

      if self.tension > 0:       
        self.prehiteffects(ene)
        sett = ene.cHP
        tdmg = self.tension*self.cMAT*(200+(37*self.cLV))
        ene.defense(self,"Physical",tdmg)
        self.tension = 0
        if skip != "Skip":
          time.sleep(timer)
          if ene.cHP >0:
            if (sett-ene.cHP) == 0:
              print("\n"+self.color+self.NAME+res,"releases all tension at",ene.color+ene.NAME+res,"before he falls, but deals no damage!")
            else:
              print("\n"+self.color+self.NAME+res,"releases all tension at",ene.color+ene.NAME+res,"before he falls, dealing",fore.ORANGE_1 + style.BOLD + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
          else:
            print("\n"+self.color+self.NAME+res,"releases all tension at",ene.color+ene.NAME+res,"before he falls, dealing",fore.ORANGE_1 + style.BOLD + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
          ene.onhittimersdefense(self,0.2,tdmg,"Physical Melee")
        else:
          ene.onhittimersdefense(self,0,tdmg,"Physical Melee",skip="Skip")
        sett = self.cHP + dmg
        
    if self.cHP > 0:


      if "The Gambit" in self.items:
        self.fcMP = self.fcMP + round(1.7*self.cMRG)
      else:
        self.fcMP = self.fcMP + self.cMRG
      if self.fcMP > self.fMP:
        self.fcMP = round(self.fMP) 
        
      if "Thornmail" in self.items and "Melee" in mr:
        if ene.cHP > 0:
          self.prehiteffects(ene)
          sett = ene.cHP
          dmg = (0.2*dmg)
          ene.defense(self,"Magical",dmg)
          if ene.cHP <= 0:
            ene.cHP = 1
          if skip != "Skip":
            time.sleep(timer)
            if (sett-ene.cHP) == 0:
              print("\n"+self.color+self.NAME+res+"'s thornmail spikes hurt",ene.color+ene.NAME+res+", but deal no damage!")
            else:
              print("\n"+self.color+self.NAME+res+"'s thornmail spikes hurt",ene.color+ene.NAME+res+", dealing",fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")

      if "Flaming Cinders" in self.items:
        if ene.grievous < 3:
          ene.grievous = 3

      if "Physics Equation Sheet" in self.items:
        if "Critical" in mr:
          ene.scanned = 4
          if skip != "Skip":
            time.sleep(timer)
            print("\n"+self.color+self.NAME+res,"scans",ene.color+ene.NAME+res,"with their Physics Equation Sheet, reducing their critical strike chance to 0!")  

      if self.greased[0] > 0:
        self.greased[0] = self.greased[0] - 1
        if self.greased[0] == 0:
          if skip != "Skip":
            time.sleep(timer)
            print("\n"+self.color+self.NAME+res,"is ungreased!")  
          self.greased = [0]

      if self.teamed[0] > 0:
        self.teamed[0] = self.teamed[0] - 1
        if self.teamed[0] == 0:
          if skip !="Skip":
            time.sleep(timer)          
            print("\n"+self.color+self.NAME+res,"no longer feels the teamwork!")  
          self.teamed = [0]
        
  def prehiteffects(self,ene):
    global sett
    global play1
    global play2

    if self in play1.team:
      self.currentstats(play1,play2)
      if self != ene:
        ene.currentstats(play2,play1)
    elif self in play2.team:
      self.currentstats(play2,play1)
      if self != ene:
        ene.currentstats(play1,play2)

    if "Colombian" in ene.SYN:
      if self.NAME == "Ishraq" or self.NAME == "Arwyn" or self.NAME == "Richard" or self.NAME == "Ian" or self.NAME == "John" or self.NAME == "Metin" or self.NAME == "David" or self.NAME == "Brandon" or self.NAME == "Jeremy" or self.NAME == "Zaid" or self.NAME == "Brian" or self.NAME == "Siddarth" or self.NAME == "Basel" or self.NAME == "Kholilur" or self.NAME == "Erick":
        self.cAC = round(self.cAC*0.5)

    if "Hater Guard" in ene.items: 
      self.hater = 4
      if self not in ene.hatelis:
        ene.hatelis.append(self)

    if ene.sexy > 0 and self.GEN == "Male":
      self.cAT = 0
      self.cMAT = 0

    if ene.cross == 1:
      ene.cMDF = 1000000

    if self.sexy > 0 and ene.GEN == "Male":
      self.cAT = round(self.cAT*self.cMAT*(1.25+(0.0625*self.cLV)))

    if ene.bleedt > 0:
      self.cCT = round(self.cCT * 1.5)

    if ene.NAME == "Metin":
      if (ene.hitcount + 1) % 5 == 0:
        ene.cDF = 1000000
        ene.cMDF = 1000000

    if self in play1.team:

      if play1.emo == 2:
        if "Emo" in self.SYN:
          self.cAPN = self.cAPN + round(0.5*ene.cDF)
          self.cMPN = self.cMPN + round(0.5*ene.cMDF)

      if play1.emo >= 3:
        if "Emo" in self.SYN:
          self.cAPN = self.cAPN + round(0.75*ene.cDF)
          self.cMPN = self.cMPN + round(0.75*ene.cMDF)
        else:
          self.cAPN = self.cAPN + round(0.25*ene.cDF)
          self.cMPN = self.cMPN + round(0.25*ene.cMDF)

    if self in play2.team:

      if play2.emo == 2:
        if "Emo" in self.SYN:
          self.cAPN = self.cAPN + round(0.5*ene.cDF)
          self.cMPN = self.cMPN + round(0.5*ene.cMDF)

      if play2.emo >= 3:
        if "Emo" in self.SYN:
          self.cAPN = self.cAPN + round(0.75*ene.cDF)
          self.cMPN = self.cMPN + round(0.75*ene.cMDF)
        else:
          self.cAPN = self.cAPN + round(0.25*ene.cDF)
          self.cMPN = self.cMPN + round(0.25*ene.cMDF)

    if "Last Say" in self.items:
      self.cMPN = self.cMPN + round(0.5*ene.cMDF)


    if "Miller's Hearing Aid" in ene.items:
      if (ene.hitcount + 1) % 5 == 0:
        ene.fEV = ene.fEV + 100
        ene.cEV = round(ene.fEV*ene.pEV)

    

      
  def onhittimersoffense(self,ene,timer,mr="",skip=""):
    global sett
    global play1
    global play2
    
    res = attr("reset")

    if self.lifesteal > 0:
      if (sett-ene.cHP) > 0 and round(self.healmod*self.lifesteal*(sett-ene.cHP)) >0:
        butt = self.cHP 
        self.cHP = self.cHP + round(self.healmod*self.lifesteal*(sett-ene.cHP))
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        if skip !="Skip":
          res = attr("reset")
          time.sleep(timer)
          print("\n" + self.color+self.NAME+res,"heals for",fore.MEDIUM_SPRING_GREEN + str(self.cHP-butt) + style.RESET,"health! They now have",self.cHP,"health!")

    if self.NAME == "Abby":
      if ene.cHP < (0.2*ene.fHP) and ene.cHP > 0:
        ene.cHP = 0
        if skip != "Skip":
          res = attr("reset")
          time.sleep(timer)
          print("\n"+self.color+self.NAME+res,"eats",ene.color+ene.NAME+res,"alive, executing them!")

    if self.tension == 3:
      self.tension = 0
      self.prehiteffects(ene)
      dmg = self.cMAT*(600+(111*self.cLV))
      ene.defense(self,"Physical",dmg)
      if skip != "Skip":
        time.sleep(timer)
        if ene.cHP >0:
          if (sett-ene.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"releases all tension at",ene.color+ene.NAME+res+", but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"releases all tension at",ene.color+ene.NAME+res+", dealing",fore.ORANGE_1 + style.BOLD + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"releases all tension at",ene.color+ene.NAME+res+", dealing",fore.ORANGE_1 + style.BOLD + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
        ene.onhittimersdefense(self,0.2,dmg,"Physical Melee")
      else:
        ene.onhittimersdefense(self,0,dmg,"Physical Melee",skip="Skip")

    if self.eagle[0] > 0:
      if ene.bleedt < 1:
        ene.bleedt = 1
      ene.bleedd = ene.bleedd + (self.eagle[1]*(80+(10*self.cLV)))

    if "Bloodrazor" in self.items:
      if ene.bleedt < 5:
        ene.bleedt = 5
      ene.bleedd = ene.bleedd + (ene.fHP*0.015)


    if self in play1.team:
      if "Gay" in self.SYN:
        ch = random.randint(1,100)
        if play1.gay >= 2 and play1.gay < 4:
          if ch <= 45:
            ene.fear[0] = 3
            ene.fear[1] = ene.fear[1] + 1
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"fears",ene.color+ene.NAME+res,"with their gayness!")
        if play1.gay == 4:
          if ch <= 70:
            ene.fear[0] = 3
            ene.fear[1] = ene.fear[1] + 1
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"fears",ene.color+ene.NAME+res,"with their gayness!")
        if play1.gay >= 5:
          ene.fear[0] = 3 
          ene.fear[1] = ene.fear[1] + 1
          if skip != "Skip":
            time.sleep(timer)
            print("\n"+self.color+self.NAME+res,"fears",ene.color+ene.NAME+res,"with their gayness!")

      if "Shy" in self.SYN:
        ch = random.randint(1,100)
        if play1.shy >= 2 and play1.shy < 4:
          if ch <= 20:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")
        elif play1.shy >= 4 and play1.shy < 6:
          if ch <= 40:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")
        elif play1.shy >= 6 and play1.shy < 8:
          if ch <= 60:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")
        elif play1.shy >= 8:
          if ch <= 80:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")

      if play1.chi >= 3:
        ch = random.randint(1,100)
        if play1.chi >= 3 and play1.chi < 6:
          if "Chill" in self.SYN:
            if ch <= 50:
              ene.chilly = 6
              if skip != "Skip":
                time.sleep(timer)
                print("\n"+self.color+self.NAME+res,"chills",ene.color+ene.NAME+res+"!")
        elif play1.chi >= 6:
          if "Chill" in self.SYN:           
            if ene.chilly > 0:
              co = random.randint(1,100)
              if co <= 40:
                ene.frozen = 1
                if skip != "Skip":
                  time.sleep(timer)
                  print("\n"+self.color+self.NAME+res,"freezes",ene.color+ene.NAME+res+"!")
          if ch <= 50:
            ene.chilly = 6
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"chills",ene.color+ene.NAME+res+"!")
    
      if "Bengali" in self.SYN and self.GEN == "Male":
        if play1.ben >= 2:
          self.mferv = self.mferv + 1
          if self.mferv > 5:
            self.mferv = 5

      if "Vulgar" in self.SYN:
        if play1.vul >= 3:
          if play1.vultarg in play2.deadteam:
            if ene.poisont < 11:
              ene.poisont = 11
              ene.poisond = ene.poisond + (0.01*ene.fHP)
          


    if self in play2.team:
      if "Gay" in self.SYN:
        ch = random.randint(1,100)
        if play2.gay >= 2 and play2.gay < 4:
          if ch <= 45:
            ene.fear[0] = 3
            ene.fear[1] = ene.fear[1] + 1
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"fears",ene.color+ene.NAME+res,"with their gayness!")
        if play2.gay == 4:
          if ch <= 70:
            ene.fear[0] = 3
            ene.fear[1] = ene.fear[1] + 1
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"fears",ene.color+ene.NAME+res,"with their gayness!")
        if play2.gay >= 5:
          ene.fear[0] = 3 
          ene.fear[1] = ene.fear[1] + 1
          if skip != "Skip":
            time.sleep(timer)
            print("\n"+self.color+self.NAME+res,"fears",ene.color+ene.NAME+res,"with their gayness!")

      if "Shy" in self.SYN:
        ch = random.randint(1,100)
        if play2.shy >= 2 and play2.shy < 4:
          if ch <= 20:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")
        elif play2.shy >= 4 and play2.shy < 6:
          if ch <= 40:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")
        elif play2.shy >= 6 and play2.shy < 8:
          if ch <= 60:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")
        elif play2.shy >= 8:
          if ch <= 80:
            ene.silenced = 4
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"silences",ene.color+ene.NAME+res+"!")

      if play2.chi >= 3:
        ch = random.randint(1,100)
        if play2.chi >= 3 and play2.chi < 6:
          if "Chill" in self.SYN:
            if ch <= 50:
              ene.chilly = 6
              if skip != "Skip":
                time.sleep(timer)
                print("\n"+self.color+self.NAME+res,"chills",ene.color+ene.NAME+res+"!")
        elif play2.chi >= 6:
          if "Chill" in self.SYN:           
            if ene.chilly > 0:
              co = random.randint(1,100)
              if co <= 40:
                ene.frozen = 1
                if skip != "Skip":
                  time.sleep(timer)
                  print("\n"+self.color+self.NAME+res,"freezes",ene.color+ene.NAME+res+"!")
          if ch <= 50:
            ene.chilly = 6
            if skip != "Skip":
              time.sleep(timer)
              print("\n"+self.color+self.NAME+res,"chills",ene.color+ene.NAME+res+"!")
    
      if "Bengali" in self.SYN and self.GEN == "Male":
        if play2.ben >= 2:
          self.mferv = self.mferv + 1
          if self.mferv > 5:
            self.mferv = 5

      if "Vulgar" in self.SYN:
        if play2.vul >= 3:
          if play2.vultarg in play1.deadteam:
            if ene.poisont < 11:
              ene.poisont = 11
              ene.poisond = ene.poisond + (0.01*ene.fHP)

    if "Tunisian" in self.SYN:
      self.tunis = self.tunis + 1
      if self.tunis == 4:
        self.tunis = 0
        self.attack(ene,skip)      


  def onturntimers(self,ally,enemy,skip=""):

    res = attr("reset")

    if "Cleats" in self.items:
      selfsett = self.cHP
      self.cHP = self.cHP + round(self.healmod*0.025*self.fHP)
      if self.cHP > self.fHP:
        self.cHP = round(self.fHP)
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"recovers",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+ style.RESET,"health from their cleats!",self.NAME,"has",self.cHP,"health now!")

    if "Dominican" in self.SYN:
      selfsett = self.cHP
      if ally.dom < 3:
        self.cHP = self.cHP + round(self.healmod*0.02*self.fHP)
      elif ally.dom >= 3 and ally.dom < 6:
        self.cHP = self.cHP + round(self.healmod*0.05*self.fHP)
      elif ally.dom >= 6:
        self.cHP = self.cHP + round(self.healmod*0.1*self.fHP)
      if self.cHP > self.fHP:
        self.cHP = round(self.fHP)
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"recovers",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+ style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")

    if len(self.ego) > 0:
      selfsett = self.cHP
      self.currentstats(ally,enemy)
      self.cHP = self.cHP + round(len(self.ego)*self.healmod*(0.03+(0.01*self.cLV))*self.fHP*self.cMAT)
      if self.cHP > self.fHP:
        self.cHP = round(self.fHP)
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"recovers",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+ style.RESET,"health from his ego!",self.NAME,"has",self.cHP,"health now!")

    if self.hiding > 0:
      self.hiding = self.hiding - 1
      selfsett = self.cHP
      self.currentstats(ally,enemy)
      self.cHP = self.cHP + round(self.healmod*self.cMAT*(100+(30*self.cLV)))
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"recovers",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+ style.RESET,"health while avoiding combat!",self.NAME,"has",self.cHP,"health now!")
      if self.hiding == 0:
        ally.teamID.append(self.ID)
        if skip != "Skip":
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer invisible!")
    
    if self.graced[0] > 0:
      self.graced[0] = self.graced[0] - 1
      selfsett = self.cHP
      self.currentstats(ally,enemy)
      self.graced[1].currentstats(ally,enemy)
      self.cHP = self.cHP + round(self.healmod*self.graced[1].cMAT*(80+(20*self.graced[1].cLV)))
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"feels graced, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+ style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")
      if self.graced[0] == 0:
        self.graced = [0]
        if skip != "Skip":
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer graced!")

    if self.immortal > 0:
      self.immortal = self.immortal - 1
      if self.immortal == 0:
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.5)
          print("\n"+self.color+self.NAME+res,"is mortal again!")

    if self.burnt > 0 or self.burning == 1:
      self.burnt = self.burnt - 1
      sett = self.cHP
      self.cHP = self.cHP - round(self.burnd * (1-(self.cMDF/(self.cMDF+100))))
      res = attr("reset")
      time.sleep(0.3)
      if self.cHP > 0:
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",fore.ORANGE_RED_1 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.ORANGE_RED_1,"burn damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.burnt == 0 and self.burning == 0:
          if skip != "Skip":
            time.sleep(0.3)
            print("\n" + self.color+self.NAME+res,"is relieved of burning!")
          self.burnd = 0
      else:
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",fore.ORANGE_RED_1 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.ORANGE_RED_1,"burn damage!" + style.RESET,self.NAME,"falls...")

    if self.poisont > 0:
      self.poisont = self.poisont - 1
      sett = self.cHP
      self.cHP = self.cHP - round(self.poisond * (1-(self.cDF/(self.cDF+100))))
      res = attr("reset")
      time.sleep(0.3)
      if self.cHP > 0:
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",fore.GREEN_4 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.GREEN_4,"poison damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.poisont == 0:
          if skip != "Skip":
            time.sleep(0.3)
            print("\n" + self.color+self.NAME+res,"is cured of poisoning!")
          self.poisond = 0
      else: 
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",fore.GREEN_4 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.GREEN_4,"poison damage!" + style.RESET,self.NAME,"falls...")
      
    if self.bleedt > 0:
      self.bleedt = self.bleedt - 1
      sett = self.cHP
      self.cHP = self.cHP - round(self.bleedd * (1-(self.cDF/(self.cDF+100))))
      res = attr("reset")
      time.sleep(0.3)
      if self.cHP > 0:
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",fore.LIGHT_RED + style.BOLD + str(sett-self.cHP) + style.RESET + fore.LIGHT_RED,"bleed damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.bleedt == 0:
          if skip != "Skip":
            time.sleep(0.3)
            print("\n" + self.color+self.NAME+res,"stops bleeding!")
          self.bleedd = 0
      else:
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",fore.LIGHT_RED + style.BOLD + str(sett-self.cHP) + style.RESET + fore.LIGHT_RED,"bleed damage!" + style.RESET,self.NAME,"falls...")

    if self.decayt > 0:
      self.decayt = self.decayt - 1
      sett = self.cHP
      self.cHP = self.cHP - round(self.decayd)
      res = attr("reset")
      time.sleep(0.3)
      if self.cHP > 0:
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",back.GREY_100 + fore.BLACK + style.BOLD + str(sett-self.cHP) + style.RESET + fore.BLACK + back.GREY_100,"decay damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.decayt == 0:
          if skip != "Skip":
            time.sleep(0.3)
            print("\n" + self.color+self.NAME+res,"stops decaying!")
          self.decayd = 0
      else:
        if skip != "Skip":
          print("\n" + self.color+self.NAME+res,"takes",back.GREY_100 + fore.BLACK + style.BOLD + str(sett-self.cHP) + style.RESET + fore.BLACK + back.GREY_100,"decay damage!" + style.RESET,self.NAME,"falls...")

    if self.drift[0] > 0:
      self.drift[0] = self.drift[0] - 1
      if self.drift[0] == 0:
        sett = self.cHP
        dmg = self.drift[2]*(170+(20*self.drift[1].cLV))
        self.defense(self.drift[1],"Magical",dmg)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          if self.cHP >0:
            if (sett-self.cHP) == 0:
              print("\n"+self.color+self.NAME+res,"feels the after-drift, but takes no damage!")
            else:
              print("\n"+self.color+self.NAME+res,"feels the after-drift, taking",fore.PURPLE_1B + str(sett-self.cHP) + style.RESET,"damage!",self.NAME,"has",self.cHP,"health remaining!")
          else:
            print("\n"+self.color+self.NAME+res,"feels the after-drift, taking",fore.PURPLE_1B + str(sett-self.cHP) + style.RESET,"damage!",self.NAME,"falls...")
          self.onhittimersdefense(self.drift[1],0.2,dmg,"Magical Ranged")
        else:
          self.onhittimersdefense(self.drift[1],0,dmg,"Magical Ranged",skip="Skip")

    if self.immortal > 0 and self.cHP <=0:
      self.cHP = 1
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"gets back up!")

      
    if self.cHP > 0 and "Anatomy of Hearts" in self.items:
      peep = []
      for x in enemy.team:
        peep.append(x)
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.2)
        print("\n"+self.color+self.NAME+res+"'s Anatomy of Hearts sends out a pulse towards the enemies!")
      for x in range(2):
        hit = random.choice(peep)
        peep.remove(hit)
        self.prehiteffects(hit)
        sett = hit.cHP
        dmg = (0.05*hit.cHP)
        hit.defense(self,"Magical",dmg)
        if hit.cHP <= 0:
          hit.cHP = 1
        if skip != "Skip":
          time.sleep(0.1)
          if (sett-hit.cHP) == 0:
            print("\n"+hit.color+hit.NAME+res,"takes no damage!")
          else:
            print("\n"+hit.color+hit.NAME+res,"takes",fore.PURPLE_1B+str(sett-hit.cHP)+style.RESET,"damage!",hit.NAME,"has",hit.cHP,"health remaining!")
        if len(peep) == 0:
          break

    if self.cHP > 0 and "Care Package" in self.items:
      peep = []
      for x in ally.team:
        if x != self:
          peep.append(x)
      if len(peep) > 0:
        pers = random.choice(peep)
        selfsett = pers.cHP
        pers.cHP = pers.cHP + round(pers.healmod*0.1*(pers.fHP-pers.cHP))
        if pers.cHP > pers.fHP:
          pers.cHP = round(pers.fHP)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+pers.color+pers.NAME+res,"recovers",fore.MEDIUM_SPRING_GREEN+str(pers.cHP-selfsett)+ style.RESET,"health from",self.color+self.NAME+res+"'s care package!",pers.NAME,"has",pers.cHP,"health now!")

    if self.invis > 0 and self.cHP > 0:
      self.invis = self.invis - 1
      if skip != "Skip" and self.invis != 0:
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"lurks in the darkness...")
      if self.invis == 0:
        self.trig = 2
        ally.teamID.append(self.ID)
        

    if self.cHP > 0 and "Graham's Report" in self.items:
      stat = random.randint(1,11)
      self.graham[stat-1] = self.graham[stat-1] + 1
    
    if self.cHP > 0 and "Kahoot" in self.items:
      self.kahoot = self.kahoot + 1

    if self.cHP > 0 and self.sitting[0] == 1:
      self.prehiteffects(self.sitting[1])
      sett = self.sitting[1].cHP
      dmg = round(0.05*self.sitting[1].fHP)
      self.sitting[1].cHP = self.sitting[1].cHP - dmg
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.2)
        if self.sitting[1].cHP > 0:
          print("\n"+self.sitting[1].color+self.sitting[1].NAME+res,"takes",style.BOLD+str(sett-self.sitting[1].cHP)+style.RESET,"damage from being crushed by",self.NAME+"!",self.sitting[1].NAME,"has",self.sitting[1].cHP,"health remaining!")
        else:
          print("\n"+self.sitting[1].color+self.sitting[1].NAME+res,"takes",style.BOLD+str(sett-self.sitting[1].cHP)+style.RESET,"damage from being crushed by",self.NAME+"!",self.sitting[1].NAME,"falls...")

    if self.hater > 0:
      self.hater = self.hater - 1
      if self.hater == 0:
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer hating!")
        for x in allfighters:
          if self in x.hatelis:
            x.hatelis.remove(self)
        
    if self.ktogg == False and self.NAME == "Kylie" and (self.cHP <= round(self.HP/2)):
      self.ktogg = True
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"ramps up her strength to the next level, increasing her attack, defense, magic attack, magic defense, and speed by 100%!")

    if self.fear[0] > 0:
      self.fear[0] = self.fear[0] - 1
      if skip != "Skip":
        if self.fear[0] == 0:
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer feared!")
          self.fear = [0,0]

    if self.blind > 0:
      self.blind = self.blind - 1
      if skip != "Skip":
        if self.blind == 0:
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer blinded!")

    if self.grievous > 0:
      self.grievous = self.grievous - 1
      if skip != "Skip":
        if self.grievous == 0:
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer wounded!")
    
    if self.silenced > 0:
      self.silenced = self.silenced - 1
      if skip != "Skip":
        if self.silenced == 0:
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is unsilenced!")

    if self.scanned > 0:
      self.scanned = self.scanned - 1
      if skip != "Skip":
        if self.scanned == 0:
          res = attr("reset")
          time.sleep(0.3)
          print("\n" +self.color+self.NAME+res,"is no longer scanned!")

    if self.critflow > 0:
      self.critflow = self.critflow - 1
      if skip != "Skip":
        if self.critflow == 0:
          res = attr("reset")
          time.sleep(0.3)
          print("\n" +self.color+self.NAME+res,"exits her critical flow!")

    if self.rallied[0] > 0:
      self.rallied[0] = self.rallied[0] - 1
      if self.rallied[0] == 0:
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer rallied!")
        self.rallied = [0]

    if self.named[0] > 0:
      self.named[0] = self.named[0] - 1
      if self.named[0] == 0:
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer nick-named!")
        self.named = [0]
    
    if self.crips[0] > 0:
      self.crips[0] = self.crips[0] - 1
      if self.crips[0] == 0:
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"is no longer crippled!")
        self.crips = [0]

    if self.touched[0] > 0:
      self.touched[0] = self.touched[0] - 1
      if self.touched[0] == 0:
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"no longer feels awkward!")
        self.touched = [0]

    if self.delled > 0:
      self.delled = self.delled - 1
      if self.delled == 0:
        for x in enemy.team:
          if x.NAME == "Handell":
            x.ego.remove(self)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"finds out the truth about Handell!")

    if self.confection[0] > 0:
      self.confection[0] = self.confection[0] - 1
      if self.confection[0] == 0:
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.3)
          print("\n"+self.color+self.NAME+res,"no longer tastes the sweets!")
        self.confection = [0]

    if self.eagle[0] > 0:
      self.eagle[0] = self.eagle[0] - 1
      if self.eagle[0] == 0:
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"is no longer in eagle-eye mode!")
        self.eagle = [0]

    if self.sad[0] > 0:
      self.sad[0] = self.sad[0] - 1
      if self.sad[0] == 0:
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"is no longer sad!")
        self.sad = [0]

    if self.organ == True:
      self.organized = self.organized - 1
      if self.organized == 0:
        res = attr("reset")
        time.sleep(0.5)
        print(self.color+"\nThe team is no longer organized!"+res)
        for x in ally.team:
          x.organized = 0
        self.organ = False

    if self.hogrider == 1:
      self.hogg = self.hogg - 1
      if self.hogg == 0:
        res = attr("reset")
        time.sleep(0.5)
        print(self.color+"\nThe horns of battle cease!"+res)
        for x in ally.team:
          x.hogg = 0
        self.hogrider = 2

    if self.anime[0] > 0:
      self.anime[0] = self.anime[0] - 1
      if self.anime[0] == 0:
        res = attr("reset")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"no longer feels the power of anime!")
        self.anime = [0]

    if self.NAME == "Alice":
      self.chin = self.chin + 1

  def stuns(self,ally,enemy,skip=""):
    self.stunned = False
    res = attr("reset")
    if self.stunimmune == True:
      if self.dance > 0 or self.tremstun >0 or self.rooted > 0 or self.frozen > 0 or self.confused > 0 or self.paralyzed > 0:
        self.dance = 0
        self.tremstun = 0
        self.rooted = 0
        self.frozen = 0
        self.paralyzed = 0
        self.confused = 0
        self.disarmed = 0
        if self.NAME == "Mr. Pudup" and skip !="Skip":
          time.sleep(0.5)
          print("\nMr. Pudup: That was a pitiful attempt to try and stop my movements.")
    else:
      if self.rooted > 0:
        self.rooted = self.rooted - 1
        self.stunned = True
        if skip !="Skip":
          time.sleep(0.5)
          print("\n"+self.color+self.NAME+res,"is rooted!")
      elif self.tremstun > 0: 
        self.tremstun = self.tremstun - 1
        self.stunned = True
        if skip !="Skip":
          time.sleep(0.5)
          print("\n"+self.color+self.NAME+res,"is on the ground!")
      elif self.frozen > 0:
        self.frozen = self.frozen - 1
        self.stunned = True
        if skip !="Skip":
          time.sleep(0.5)
          print("\n"+self.color+self.NAME+res,"is frozen!")
      elif self.paralyzed > 0:
        self.paralyzed = self.paralyzed - 1
        self.stunned = True
        if skip !="Skip":          
          time.sleep(0.5)
          print("\n"+self.color+self.NAME+res,"is paralyzed!")
      elif self.dance > 0:
        self.dance = self.dance - 1
        self.stunned = True
        tar = []
        for x in ally.team:
          tar.append(x)
        tar.remove(self)
        if len(tar) != 0:
          att = random.choice(tar)
          if skip != "Skip":
            time.sleep(0.5)
            print("\n"+self.color+self.NAME+res,"is dancing uncontrollably, attacking an allied target!")
            self.attack(att)
          if skip == "Skip":
            self.attack(att,"Skip")
        else:
          if skip != "Skip":
            time.sleep(0.5)
            print("\n"+self.color+self.NAME+res,"is dancing uncontrollably!")
      elif self.confused > 0:
        self.confused = self.confused - 1
        self.stunned = True
        if skip != True:
          time.sleep(0.5)
          print("\n"+self.color+self.NAME+res,"is confused, attacking themselves!")
          self.attack(self)
        else:
          self.attack(self,"Skip")
        
  def currentstats(self,ally,enemy):
    self.CTdmg = 1.5
    self.equipcheck()
    self.pAT = 1.00
    self.pDF = 1.00
    self.pMAT = 1.00
    self.pMDF = 1.00
    self.pSP = 1.00
    self.pAC = 1.00
    self.pEV = 1.00
    self.pCT = 1.00
    self.pAPN = 1.00
    self.pMPN = 1.00
    self.pMRG = 1.00
    self.lifesteal = 0
    self.healmod = 1
    self.dmgreduct = 1
    self.effects(ally,enemy)
    self.cAT = round(self.fAT*self.pAT)
    self.cDF = round(self.fDF*self.pDF)
    self.cMAT = (self.fMAT*self.pMAT)
    self.cMDF = round(self.fMDF*self.pMDF)
    self.cSP = round(self.fSP*self.pSP)
    self.cAC = round(self.fAC*self.pAC)
    self.cEV = round(self.fEV*self.pEV)
    self.cCT = round(self.fCT*self.pCT)
    self.cAPN = round(self.fAPN*self.pAPN)
    self.cMPN = round(self.fMPN*self.pMPN)
    self.cMRG = round(self.fMRG*self.pMRG)


  def equipcheck(self):
    global turncount

    self.fHP = self.HP
    self.fMP = self.MP
    self.fAT = self.AT             
    self.fDF = self.DF
    self.fMAT = self.MAT
    self.fMDF = self.MDF
    self.fSP = self.SP
    self.fAC = self.AC
    self.fEV = self.EV
    self.fCT = self.CT
    self.fAPN = self.APN
    self.fMPN = self.MPN
    self.fMRG = self.MRG
    #items = ["Attack","Defense","Magic Defense","Speed","Magic Attack","Health","Mana","Critical"]

    if "Health" in self.items:
      self.fHP = self.fHP + 150

    if "Mana" in self.items:
      if turncount == 0:
        self.fcMP = self.fcMP + 15

    if "Attack" in self.items:
      self.fAT = self.fAT + 10
    
    if "Defense" in self.items:
      self.fDF = self.fDF + 20
      
    if "Magic Attack" in self.items:
      self.fMAT = self.fMAT + 0.1
    
    if "Magic Defense" in self.items:
      self.fMDF = self.fMDF + 20
    
    if "Speed" in self.items:
      self.fSP = self.fSP + 5
    
    if "Critical" in self.items:
      self.fCT = self.fCT + 5
    
    #Combos
    
    if "Bloodrazor" in self.items:
      self.fAT = self.fAT + 20
    
    if "Zulfiqar" in self.items:
      self.fAT = self.fAT + 10
      self.fDF = self.fDF + 20
    
    if "Anatomy of Hearts" in self.items:
      self.fAT = self.fAT + 10
      self.fHP = self.fHP + 150

    if "Flow of Wind" in self.items:
      self.fAT = self.fAT + 10
      if turncount == 0:
        self.fcMP = self.fcMP + 15
      self.fMRG = self.fMRG + 4
      

    if "Duality" in self.items:
      self.fAT = self.fAT + 10
      self.fMAT = self.fMAT + 0.1
    
    if "Thotslayer" in self.items:
      self.fAT = self.fAT + 10
      self.fMDF = self.fMDF + 20

    if "Rally Banner" in self.items:
      self.fAT = self.fAT + 10
      self.fSP = self.fSP + 5
    
    if "Honjo Masamune" in self.items:
      self.fAT = self.fAT + 10
      self.fCT = self.fCT + 5

    if "Thornmail" in self.items:
      self.fDF = self.fDF + 40

    if "Flaming Cinders" in self.items:
      self.fDF = self.fDF + 20
      self.fHP = self.fHP + 150

    if "The Gambit" in self.items:
      self.fDF = self.fDF + 20
      if turncount == 0:
        self.fcMP = self.fcMP + 15

    if "Feminism" in self.items:
      self.fDF = self.fDF + 20
      self.fMAT = self.fMAT + 0.1

    if "Obscene Wear" in self.items:
      self.fDF = self.fDF + 20
      self.fMDF = self.fMDF + 20

    if "Miller's Hearing Aid" in self.items:
      self.fDF = self.fDF + 20
      self.fSP = self.fSP + 5

    if "Critical Measure" in self.items:
      self.fDF = self.fDF + 20
      self.fCT = self.fCT + 5

    if "Eternal" in self.items:
      self.fHP = self.fHP + 600

    if "Care Package" in self.items:
      self.fHP = self.fHP + 150
      if turncount == 0:
        self.fcMP = self.fcMP + 15

    if "Grand" in self.items:
      self.fHP = self.fHP + 150
      self.fMAT = self.fMAT + 0.1

    if "Devourer" in self.items:
      self.fHP = self.fHP + 150
      self.fMDF = self.fMDF + 20

    if "Cleats" in self.items:
      self.fHP = self.fHP + 150
      self.fSP = self.fSP + 5

    if "Pearson Textbook" in self.items:
      self.fHP = self.fHP + 150
      self.fCT = self.fCT + 5

    if "Endiness" in self.items:
      if turncount == 0:
        self.fcMP = self.fcMP + 30

    if "Tryhard" in self.items:
      if turncount == 0:
        self.fcMP = self.fcMP + 15
      self.fMAT = self.fMAT + 0.1

    if "Rulebook" in self.items:
      if turncount == 0:
        self.fcMP = self.fcMP + 15
      self.fMDF = self.fMDF + 10

    if "Resource Catalysy" in self.items:
      if turncount == 0:
        self.fcMP = self.fcMP + 15
      self.fSP = self.fSP + self.MRG
    
    if "Giancoli Textbook" in self.items:
      if turncount == 0:
        self.fcMP = self.fcMP + 15
      self.fCT = self.fCT + 5

    if "Last Say" in self.items:
      self.fMAT = self.fMAT + 0.2

    if "Cross" in self.items:
      self.fMAT = self.fMAT + 0.1
      self.fMDF = self.fMDF + 20

    if "Kahoot" in self.items:
      self.fMAT = self.fMAT + 0.1
      self.fSP = self.fSP + 5

    if "God's Javelin" in self.items:
      self.fMAT = self.fMAT + 0.1
      self.fCT = self.fCT + 5

    if "Bible" in self.items:
      self.fMDF = self.fMDF + 100

    if "Hater Guard" in self.items:
      self.fMDF = self.fMDF + 20
      self.fSP = self.fSP + 5

    if "Physics Equation Sheet" in self.items:
      self.fMDF = self.fMDF + 20
      self.fCT + self.fCT + 5

    if "Vengeance" in self.items:
      self.fSP = self.fSP + 10
      self.fAC = self.fAC + 200

    if "Sacred Scythe" in self.items:
      self.fSP = self.fSP + 5
      self.fCT = self.fCT + 5
      self.CTdmg = self.CTdmg + 0.5

    if "Graham's Report" in self.items:
      self.fCT = self.fCT + 10

    if self.fcMP >= self.fMP:
      self.fcMP = round(self.fMP)


  def attack(self,enemy,skip=""):
    #print(self.HP,self.MP,self.AT,self.DF,self.MAT,self.MDF,self.SP,self.AC,self.EV,self.CT,self.APN,self.MPN,self.MRG)
    global sett
    global lastat
    trueemo = False
    res = attr("reset")
    if "Emo" in self.SYN:
      self.emohit = self.emohit + 1
      if self.emohit == 3:
        self.prehiteffects(self)
        selfsett = self.cHP
        dmg = self.cAT
        self.defense(self,"Physical",dmg)
        self.emohit = 0
        trueemo = True
        if self.cHP <= 0:
          self.cHP = 1
        if skip != "Skip":
          time.sleep(0.5)
          if self.cHP > 1:
            print("\n" + self.color+self.NAME+res, "hurts themselves just to feel something, taking",fore.ORANGE_1 + str(selfsett-self.cHP) + style.RESET,"damage!",self.NAME,"has",self.cHP,"health remaining!")  
          elif self.cHP <= 1:
            print("\n" + self.color+self.NAME+res, "hurts themselves just to feel something, taking",fore.ORANGE_1 + str(selfsett-self.cHP) + style.RESET,"damage!",self.NAME,"is at critical health!")    
    self.prehiteffects(enemy)
    CT = random.randint(1,100)
    sett = enemy.cHP
    if self.sitting[0] != 1:
      self.fcMP = self.fcMP + self.cMRG
      if self.fcMP > self.fMP:
        self.fcMP = round(self.fMP) 
    self.lastattack = "Auto"
    lastat = "Auto"
    if self.cAT <= 0:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n" + self.color+self.NAME+res, "attacks",enemy.color+enemy.NAME+res+", but deals no damage!")
    else:
      diff = enemy.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          time.sleep(0.5)
          print("\n" + self.color+self.NAME+res, "attacks, but",enemy.color+enemy.NAME+res, "dodges!")
          enemy.specialdodgecases(self,0.5,"Physical Melee",CT)
        else:
          enemy.specialdodgecases(self,0,"Physical Melee",CT,skip="Skip")
      else:
        if skip != "Skip":
          time.sleep(0.5)
        if CT <= self.cCT:
          if trueemo == True:
            dmg = round(2*self.CTdmg*self.cAT)
            enemy.cHP = enemy.cHP - dmg
          else:
            dmg = self.CTdmg*self.cAT
            enemy.defense(self,"Physical",dmg)
          if skip != "Skip":
            if enemy.cHP > 0:
              if (sett-enemy.cHP) == 0:
                print("\n" + self.color+self.NAME+res, "critically attacks", enemy.color+enemy.NAME+res +  ", but deals no damage!")
              else:
                print("\n" + self.color+self.NAME+res, "critically attacks", enemy.color+enemy.NAME+res + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              print("\n" + self.color+self.NAME+res, "critically attacks", enemy.color+enemy.NAME+res + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
            enemy.onhittimersdefense(self,0.2,dmg,"Critical Physical Melee Auto")
          elif skip == "Skip":
            enemy.onhittimersdefense(self,0,dmg,"Critical Physical Melee Auto",skip="Skip")
        else:
          if trueemo == True:
            dmg = round(2*self.cAT)
            enemy.cHP = enemy.cHP - dmg
          else:
            dmg = self.cAT
            enemy.defense(self,"Physical",dmg)
          if skip != "Skip":
            if enemy.cHP > 0:
              if (sett-enemy.cHP) == 0:
                print("\n" + self.color+self.NAME+res, "attacks", enemy.color+enemy.NAME+res +  ", but deals no damage!")
              else:
                print("\n" + self.color+self.NAME+res, "attacks", enemy.color+enemy.NAME+res + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              print("\n" + self.color+self.NAME+res, "attacks", enemy.color+enemy.NAME+res + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
            enemy.onhittimersdefense(self,0.2,dmg,"Physical Melee Auto")
          elif skip == "Skip":
            enemy.onhittimersdefense(self,0,dmg,"Physical Melee Auto",skip="Skip")
        if skip != "Skip":
          self.onhittimersoffense(enemy,0.3) 
        else:
          self.onhittimersoffense(enemy,0,skip="Skip") 

  def defense(self,enemy,ty,dmg):
    if "Thotslayer" in enemy.items and self.GEN == "Female":
      dmg = dmg * 1.2
    if "Feminism" in enemy.items and self.GEN == "Male":
      dmg = dmg * 1.2
    if "Physical" in ty:
      if enemy.cAPN > self.cDF or self.cDF <= 0:
        self.cHP = self.cHP - round(dmg*self.dmgreduct)
      else:
        self.cHP = self.cHP - round(self.dmgreduct*dmg*(1-(((self.cDF)-enemy.cAPN)/((self.cDF+100)-enemy.cAPN))))
    elif "Magical" in ty:
      if enemy.cMPN > self.cMDF or self.cMDF <= 0:
        self.cHP = self.cHP - round(dmg*self.dmgreduct)
      else:
        self.cHP = self.cHP - round(self.dmgreduct*dmg*(1-(((self.cMDF)-enemy.cMPN)/((self.cMDF+100)-enemy.cMPN))))
  
  def specialdodgecases(self,enemy,timer,mr="",CT="",skip=""):
    global sett
     
    self.hitcount = self.hitcount + 1

    if "The Gambit" in self.items:
      if self.sitting[0] != 1:
        self.fcMP = self.fcMP + round(1.7*self.cMRG)
    else:
      if self.sitting[0] != 1:
        self.fcMP = self.fcMP + self.cMRG
    if self.fcMP > self.fMP:
      self.fcMP = round(self.fMP) 

    if self.syria > 0:
      self.syria = 0

    if self.NAME == "Jackie":
      self.prehiteffects(enemy)
      sett = enemy.cHP
      time.sleep(timer)
      dmg = self.cMAT*(125+(35*self.cLV))     
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        res = attr("reset")
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"lashes back at",enemy.color+enemy.NAME+res+", but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"lashes back at",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"lashes back at",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,timer,dmg,"Magical Melee")

    if "Zulfiqar" in self.items:
      enemy.disarmed = 1
      if skip != "Skip":
        res = attr("reset")
        time.sleep(timer)      
        print("\n"+self.color+self.NAME+res,"disarms",enemy.color+enemy.NAME+res+"!")
  
  def purge(self,types,ally="",enemy="",skip=""):
    if types == "Map Reset":
      self.rages = 0
      self.mgh = 0
      self.dark = 0
      self.chilled = [0]
    if types == "Purge":
      None
    if "Cleanse" in types:
      self.fear = [0,0]      #Negative Effects
      self.charmed = 0
      self.poisond = 0
      self.poisont = 0
      self.bleedd = 0
      self.bleedt = 0
      self.burnd = 0
      self.burnt = 0
      self.decayd = 0
      self.decayt = 0
      self.silenced = 0
      self.disarmed = 0
      self.tremsl = 0
      self.greased = [0]
      self.blind = 0
      self.named = [0]
      self.crips = [0]
      self.touched = [0]
      self.deathmark = 0
      self.sad = [0]
      self.drift = [0]
      self.chilly = 0
      self.tethered = [0]
      self.grievous = 0
      self.scanned = 0
      self.stunned = False
      self.tremstun = 0
      self.dance = 0
      self.rooted = 0
      self.taunted = [0]
      self.frozen = 0
      self.paralyzed = 0
      self.confused = 0
      self.delled = 0
      for x in enemy.team:
        if self in x.ego:
          x.ego.remove(self)
      if "Revival" in types:
        for x in enemy.team:
          if x.sitting[0] == 1:
            if self == x.sitting[1]:
              ally.teamS.append(self.NAME)
              ally.teamID.append(self.ID)
              x.sitting = [0]
              if skip != "Skip":
                time.sleep(0.3)
                res = attr("reset")
                print("\n"+self.color+self.NAME+res,"is freed from",x.color+x.NAME+res+"'s ass!") 
    elif types == "Death": 
      self.dmgstore = 0
      self.hitcount = 0
      self.immortal = 0
      self.ktogg = False
      self.dabstack = 0
      self.invis = 0
      self.trig = 0
      self.critflow = 0
      self.runhigh = 0
      self.thehut = False
      self.jabbaroll = 0
      self.tension = 0
      self.rallied = [0]
      self.simping = 0
      self.simped = [0]
      self.giant = False
      self.confection = [0]
      self.eagle = [0]
      self.sexy = 0
      self.teamed = [0]
      if self.sitting[0] == 1:
        enemy.teamS.append(self.sitting[1].NAME)
        enemy.teamID.append(self.sitting[1].ID)
        if skip != "Skip":
          time.sleep(0.3)
          res = attr("reset")
          print("\n"+self.sitting[1].color+self.sitting[1].NAME+res,"is freed from",self.color+self.NAME+res+"'s ass!")
      self.sitting = [0]
      self.hiding = 0
      self.swift = 0
      if self.organ == True:
        for x in ally.team:
          x.organized = 0
      self.organ = False
      self.organized = 0
      if self.hogrider == 1 or self.hogrider == 2:
        for x in ally.team:
          x.hogg = 0
      self.hogrider = 0
      self.hogg = 0
      self.anime = [0]
      if self.jutsu == True:
        for x in enemy.team:
          x.burning = 0
      self.mferv = 0
      self.fferv = 0
      self.trying = 0
      self.jutsu = False
      self.graced = [0]
      for x in self.ego:
        x.delled = 0
      self.ego = []
      self.cross = 0
      self.kahoot = 0
      self.javelin = 0
      self.syria = 0
      self.tunis = 0
      self.chin = 0
      self.urug = False
      self.emohit = 0
      self.graham = [0,0,0,0,0,0,0,0,0,0,0]
      self.fear = [0,0]     #Negative Effects
      self.charmed = 0
      self.poisond = 0
      self.poisont = 0
      self.bleedd = 0
      self.bleedt = 0
      self.burnd = 0
      self.burnt = 0
      self.decayd = 0
      self.decayt = 0
      self.silenced = 0
      self.disarmed = 0
      self.tremsl = 0
      self.greased = [0]
      self.blind = 0
      self.named = [0]
      self.crips = [0]
      self.touched = [0]
      self.deathmark = 0
      self.sad = [0]
      self.drift = [0]
      self.chilly = 0
      self.tethered = [0]
      self.grievous = 0
      self.hater = 0
      for x in allfighters:
        if self in x.hatelis:
          x.hatelis.remove(self)
      self.hatelis = []
      self.delled = 0
      for x in enemy.team:
        if self in x.ego:
          x.ego.remove(self)
      self.scanned = 0
      self.deturn = 0
      #Stuns
      self.stunned = False
      self.stunimmune = False
      self.tremstun = 0
      self.dance = 0
      self.rooted = 0
      self.taunted = [0]
      self.frozen = 0
      self.paralyzed = 0
      self.confused = 0
      #Mob Essentials
      self.setHP = 0

  def AIdetector(self,ally,enemy,skip=""):
    global ski

    ski = 0
    if self.stunned == True and self.NAME != "Mr. Pudup":
      self.stunned = False
    else:
      if self.silenced > 0:
        if self.NAME == "Arwyn":
          if skip == "Skip":
            self.attacksys(self.silenceattack,"Auto",enemy,"Skip")
          else:
            self.attacksys(self.silenceattack,"Auto",enemy)
        else:
          if skip == "Skip":
            self.attacksys(self.attack,"Auto",enemy,"Skip")
          else:
            self.attacksys(self.attack,"Auto",enemy)
      else:     
        #Tier 1
        if self.NAME == "James" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.didiask,"Did I ask",enemy,"Skip")
          else:
            self.attacksys(self.didiask,"Did I ask",enemy)
        elif self.NAME == "Dereck" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.awkwardtouch,"Awkward Touch",enemy,"Skip")
          else:
            self.attacksys(self.awkwardtouch,"Awkward Touch",enemy)
        elif self.NAME == "Octavio" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.ravenous,"Ravenous",enemy,"Skip")
          else:
            self.attacksys(self.ravenous,"Ravenous",enemy)
        elif self.NAME == "Blandino" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.cripple(enemy,skip="Skip")
          else:
            self.cripple(enemy)
        elif self.NAME == "Tahsin" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.seal(ally,enemy,skip="Skip")
          else:
            self.seal(ally,enemy)
        elif self.NAME == "Alvaro" and self.hogrider != 1 and (self.fcMP == self.fMP or self.hogrider == 2):
          if skip == "Skip":
            if self.hogrider == 0 and self.fcMP == self.fMP:
              self.thecall(ally,skip="Skip")
            elif self.hogrider == 2:
              ski = 1
              self.hornofbattle(enemy,skip="Skip")
          else:
            if self.hogrider == 0 and self.fcMP == self.fMP:
              self.thecall(ally)
            elif self.hogrider == 2:
              ski = 1
              self.hornofbattle(enemy)
        elif self.NAME == "Jahir" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.headbutt,"Headbutt",enemy,"Skip")
          else:
            self.attacksys(self.headbutt,"Headbutt",enemy)
        elif self.NAME == "Andrew" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.insult,"Insult",enemy,"Skip")
          else:
            self.attacksys(self.insult,"Insult",enemy)
        elif self.NAME == "Basel" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.dminion,"D-minion",enemy,"Skip")
          else:
            self.attacksys(self.dminion,"D-minion",enemy)
        elif self.NAME == "Kholilur" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.megapunch(enemy,skip="Skip")
          else:
            self.megapunch(enemy)
        elif self.NAME == "Ramirez" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.fencingstab,"Fencing Stab",enemy,"Skip")
          else:
            self.attacksys(self.fencingstab,"Fencing Stab",enemy)
        elif self.NAME == "Siddarth" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.simp(ally,"Skip")
          else:
            self.simp(ally)
        elif self.NAME == "Dylan" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.schoolshooting(enemy,skip="Skip")
          else:
            self.schoolshooting(enemy)
        elif self.NAME == "Erick" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.badwire,"Bad Wire",enemy,"Skip")
          else:
            self.attacksys(self.badwire,"Bad Wire",enemy)
        elif self.NAME == "Anthony" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.soccerrally(ally,"Skip")
          else:
            self.soccerrally(ally)
        #Tier 2
        elif self.NAME == "Jeremy" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.notthatdeep(enemy,skip="Skip")
          else:
            self.notthatdeep(enemy)
        elif self.NAME == "Brian" and self.fcMP == self.fMP and self.stunimmune == False:
          if skip == "Skip":
            self.vibe("Skip")
          else:
            self.vibe()
        elif self.NAME == "Hassan" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.buckets,"Buckets",enemy,"Skip")
          else:
            self.attacksys(self.buckets,"Buckets",enemy)
        elif self.NAME == "Zaid" and self.fcMP == self.fMP:
          high = 0
          pers = []
          for x in enemy.team:
            if x.cAT >= high:
              high = x.cAT
              pers.append(x)
          lol = random.choice(pers)
          if skip == "Skip":
            self.demean(lol,"Skip")
          else:
            self.demean(lol)
        elif self.NAME == "Khalil" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.arrivederci,"Arrivederci",enemy,"Skip")
          else:
            self.attacksys(self.arrivederci,"Arrivederci",enemy)
        elif self.NAME == "Edmond" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.chillvibes(enemy,skip="Skip")
          else:
            self.chillvibes(enemy)
        elif self.NAME == "Reema" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.breakdown(enemy,skip="Skip")
          else:
            self.breakdown(enemy)
        elif self.NAME == "Matvey" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.golfgod("Skip")
          else:
            self.golfgod()
        elif self.NAME == "Shah" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.progressiveoverload("Skip")
          else:
            self.progressiveoverload()
        elif self.NAME == "Amber" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.baking(ally,"Skip")
          else:
            self.baking(ally)
        elif self.NAME == "Noah" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.gaze,"Gaze",enemy,"Skip")
          else:
            self.attacksys(self.gaze,"Gaze",enemy)
        elif self.NAME == "Alberlyn" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.sexappeal("Skip")
          else:
            self.sexappeal()
        elif self.NAME == "Shannae" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.assortment(ally,"Skip")
          else:
            self.assortment(ally)
        #Tier 3
        elif self.NAME == "Najely" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.egirl(enemy,skip="Skip")
          else:
            self.egirl(enemy)
        elif self.NAME == "Kenny" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.stayshut,"Stay Shut",enemy,"Skip")
          else:
            self.attacksys(self.stayshut,"Stay Shut",enemy)
        elif self.NAME == "Brandon" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.grootroot(enemy,skip="Skip")
          else:
            self.grootroot(enemy)
        elif self.NAME == "Tyasia" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.evileye(enemy,skip="Skip")
          else:
            self.evileye(enemy)
        elif self.NAME == "Julius" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.runnershigh("Skip")
          else:
            self.runnershigh()
        elif self.NAME == "Jackie" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.dancersswiftness("Skip")
          else:
            self.dancersswiftness()
        elif self.NAME == "Olivia" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.striker,"Striker",enemy,"Skip")
          else:
            self.attacksys(self.striker,"Striker",enemy)
        elif self.NAME == "Handell" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.cap,"Cap",enemy,"Skip")
          else:
            self.attacksys(self.cap,"Cap",enemy)
        elif self.NAME == "John" and self.fcMP == self.fMP and self.hiding == 0:
          if skip == "Skip":
            self.disappear(ally,"Skip")
          else:
            self.disappear(ally)
        elif self.NAME == "Abida" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.extrabullying,"Extra Bullying",enemy,"Skip",tea=ally)
          else:
            self.attacksys(self.extrabullying,"Extra Bullying",enemy,tea=ally)
        elif self.NAME == "Metin" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.bearrepulse,"Bear Repulse",enemy,"Skip")
          else:
            self.attacksys(self.bearrepulse,"Bear Repulse",enemy)
        elif self.NAME == "Taylor" and self.fcMP == self.fMP and self.sitting[0] != 1:
          if skip == "Skip":
            self.attacksys(self.siton,"Sit on",enemy,"Skip",targ="Enemy")
          else:
            self.attacksys(self.siton,"Sit on",enemy,targ="Enemy")
        elif self.NAME == "David" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.teamteam(ally,"Skip")
          else:
            self.teamteam(ally)
        #Tier 4
        elif self.NAME == "Mohammad" and self.fcMP == self.fMP and self.silenced <= 0:
          if skip == "Skip":
            self.givemeallyourmoney(ally,enemy,"Skip")
          else:
            self.givemeallyourmoney(ally,enemy)
        elif self.NAME == "Arwyn" and self.fcMP == self.fMP and self.silenced <= 0 and self.trig == 0:
          if skip == "Skip":
            self.invisible(ally,"Skip")
          else:
            self.invisible(ally)
        elif self.NAME == "Richard" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.powerpunch,"Power Punch",enemy,"Skip")
          else:
            self.attacksys(self.powerpunch,"Power Punch",enemy)
        elif self.NAME == "Tim" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.dab,"Dab",enemy,"Skip")
          else:
            self.attacksys(self.dab,"Dab",enemy)
        elif self.NAME == "Jaidah" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.record(ally,enemy,"Skip")
          else:
            self.record(ally,enemy)
        elif self.NAME == "Lascelles" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.godandanime(ally,"Skip")
          else:
            self.godandanime(ally) 
        elif self.NAME == "Nicole" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.organization(ally,"Skip")
          else:
            self.organization(ally)     
        elif self.NAME == "Keyur" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.defaultdance(enemy,skip="Skip")
          else:
            self.defaultdance(enemy)  
        elif self.NAME == "Ian" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.blitz(enemy,skip="Skip")
          else:
            self.blitz(enemy)    
        elif self.NAME == "Alice" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.grace(ally,"Skip")
          else:
            self.grace(ally)          
        #Tier 5   
        elif self.NAME == "Ishraq" and self.fcMP == self.fMP and self.immortal == 0:
          if skip == "Skip":
            self.immortality("Skip")
          else:
            self.immortality()    
        elif self.NAME == "Kelly" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.asmr(ally,"Skip")
          else:
            self.asmr(ally)    
        elif self.NAME == "Kylie" and self.fcMP == self.fMP:
          if skip == "Skip":
            self.attacksys(self.spike,"Spike",enemy,"Skip")
          else:
            self.attacksys(self.spike,"Spike",enemy) 
        elif self.NAME == "Daniel" and self.fcMP == self.fMP:
          if self.thehut == False:
            if skip == "Skip":
              self.enlargen("Skip")
            else:
              self.enlargen()   
          else:
            if skip == "Skip":
              self.grubbytides(enemy,"Skip")
            else:
              self.grubbytides(enemy)   
        elif self.NAME == "Norman" and self.fcMP == self.fMP and self.jutsu == False:
          if skip == "Skip":
            self.firestorm(enemy,skip="Skip")
          else:
            self.firestorm(enemy)
        elif self.NAME == "Abby" and self.fcMP == self.fMP and self.giant == False:
          if skip == "Skip":
            self.giantess("Skip")
          else:
            self.giantess()
        elif self.NAME == "Amira" and self.fcMP == self.fMP:
          pers = []
          for x in enemy.team:
            if x.tethered[0] == 0:
              pers.append(x)
          if len(pers) > 0:
            lol = random.choice(pers)
            if skip == "Skip":
              self.powersurge(lol,ally,enemy,"Skip")
            else:
              self.powersurge(lol,ally,enemy)
          else:
            ski = 1
            if skip == "Skip":
              self.attacksys(self.attack,"Auto",enemy,"Skip")
            else:
              self.attacksys(self.attack,"Auto",enemy)
        else:
          if self.trig == 2:
            if skip == "Skip":
              self.fromtheshadows(enemy,skip="Skip")
            else:
              self.fromtheshadows(enemy)
            self.trig = 0
          elif self.hiding == 0 and self.invis == 0:
            ski = 1
            if self.jabbaroll == 1 and self.disarmed == 0:
              if skip == "Skip":
                self.jabbaattack(enemy,"Skip")
              else:
                self.jabbaattack(enemy)
            else:
              if skip == "Skip":
                self.attacksys(self.attack,"Auto",enemy,"Skip")
              else:
                self.attacksys(self.attack,"Auto",enemy)
        if ski == 0:
          self.fcMP = 0
          if "Endiness" in self.items:
            self.fcMP = 20
          if "Tryhard" in self.items:
            self.trying = self.trying + 1
            if self.trying > 4:
              self.trying = 4
          if "God's Javelin" in self.items:
            self.javelin = self.javelin + 1
          if ally.pal >= 2:
            if skip == "Skip":
              self.terrorism(ally,enemy,"Skip")
            else:
              self.terrorism(ally,enemy)

  def attacksys(self,types,name,enemy,skip="",tea="",targ=""):
    global lastat
    global ski
    hit = 0
    targs = []
    for x in enemy.team:
      if self.GEN == "Male":
        if x.sexy <=0: 
          targs.append(x)
      else:
        targs.append(x)
    for x in targs:
      if x.ID not in enemy.teamID:
        targs.remove(x)
    for x in targs:
      if x.cHP <= 0:
        print(x.NAME,x.cHP,x.ID)
        print(enemy.teamS)
        print(enemy.teamID)
    if len(targs) == 0:
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"does nothing!")
      ski = 1
    elif (types == self.attack or types == self.silenceattack) and self.disarmed > 0:  
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"does nothing!")
      self.disarmed = self.disarmed - 1
      ski = 1
    else:
      if self.taunted[0] > 0:
        hit = self.taunted[1]
        self.taunted[0] = self.taunted[0] - 1
        self.taunted = [0]
      else:
        hit = random.choice(targs)
      self.lastattack = name
      lastat = name
      if skip == "Skip":
        if targ == "Enemy" and tea != "":
          types(hit,tea,enemy,"Skip")
        elif targ == "Enemy":
          types(hit,enemy,"Skip")
        elif tea != "":
          types(hit,tea,"Skip")
        else:
          types(hit,"Skip")
      else:
        if targ == "Enemy" and tea != "":
          types(hit,tea,enemy)
        elif targ == "Enemy":
          types(hit,enemy)
        elif tea != "":
          types(hit,tea)
        else:
          types(hit)

  def powersurge(self,target,ally,enemy,skip=""):  #~
    target.tethered = [1,self]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"tethers",target.color+target.NAME+res+", draining their physical and magical attack!")
      if target.GEN == "Female":
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"mimics",target.color+target.NAME+res+"'s ability!")
    if self.NAME == "Tahsin" and self.fcMP == self.fMP:
      if skip == "Skip":
        self.seal(ally,enemy,skip="Skip")
      else:
        self.seal(ally,enemy)
    elif target.NAME == "Shannae":
      if skip == "Skip":
        self.assortment(ally,skip="Skip")
      else:
        self.assortment(ally)
    elif target.NAME == "Alberlyn":
      if skip == "Skip":
        self.sexappeal("Skip")
      else:
        self.sexappeal()
    elif target.NAME == "Amber":
      if skip == "Skip":
        self.baking(ally,skip="Skip")
      else:
        self.baking(ally)
    elif target.NAME == "Reema":
      if skip == "Skip":
        self.breakdown(enemy,skip="Skip")
      else:
        self.breakdown(enemy)
    elif target.NAME == "Taylor" and self.sitting[0] != 1:
      if skip == "Skip":
        self.attacksys(self.siton,"Sit on",enemy,skip="Skip",targ="Enemy")
      else:
        self.attacksys(self.siton,"Sit on",enemy,targ="Enemy")
    elif target.NAME == "Abida":
      if skip == "Skip":
        self.attacksys(self.extrabullying,"Extra Bullying",enemy,skip="Skip",tea=ally)
      else:
        self.attacksys(self.extrabullying,"Extra Bullying",enemy,tea=ally)
    elif target.NAME == "Olivia":
      if skip == "Skip":
        self.attacksys(self.striker,"Striker",enemy,skip="Skip")
      else:
        self.attacksys(self.striker,"Striker",enemy)
    elif target.NAME == "Jackie":
      if skip == "Skip":
        self.dancersswiftness(skip="Skip")
      else:
        self.dancersswiftness()
    elif target.NAME == "Tyasia":
      if skip == "Skip":
        self.evileye(enemy,skip="Skip")
      else:
        self.evileye(enemy)
    elif target.NAME == "Najely":
      if skip == "Skip":
        self.egirl(enemy,skip="Skip")
      else:
        self.egirl(enemy)
    elif target.NAME == "Nicole":
      if skip == "Skip":
        self.organization(ally,skip="Skip")
      else:
        self.organization(ally)
    elif target.NAME == "Jaidah":
      if skip == "Skip":
        self.record(ally,enemy,skip="Skip")
      else:
        self.record(ally,enemy) 
    elif target.NAME == "Abby":
      if skip == "Skip":
        self.giantess(skip="Skip")
      else:
        self.giantess()
    elif target.NAME == "Kylie":
      if skip == "Skip":
        self.attacksys(self.spike,"Spike",enemy,skip="Skip")
      else:
        self.attacksys(self.spike,"Spike",enemy) 
    elif target.NAME == "Kelly":
      if skip == "Skip":
        self.asmr(ally,skip="Skip")
      else:
        self.asmr(ally)
    
    
  def immortality(self,skip=""):
    self.immortal = 2
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"refuses to die!")

  def asmr(self,ally,skip=""):
    for x in ally.team:
      if x != self:
        x.fcMP = x.fcMP + (30+(10*self.cLV))
        if x.fcMP > x.fMP:
          x.fcMP = round(x.fMP)
    self.critflow = 8
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"performs ASMR, recovering everyone's mana by",str(30+(10*self.cLV))+", and increasing her critical damage and chance!")

  def spike(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)    
    selfsett = self.cHP
    self.cHP = round(self.cHP/2)
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        print("\n"+self.color+self.NAME+res, "spikes a volleyball at",enemy.color+enemy.NAME+res+", but misses!")
        enemy.specialdodgecases(self,0.2,"True Ranged")
      else:
        enemy.specialdodgecases(self,0,"True Ranged",skip="Skip")
    else:
      sett = enemy.cHP
      dmg = round(((250+(75*self.cLV))*self.cMAT)+((1+(0.3*self.cLV))*(selfsett-self.cHP)))
      enemy.cHP = enemy.cHP - dmg
      if skip != "Skip":
        if enemy.cHP > 0:
          print("\n"+self.color+self.NAME+res,"spikes a volleyball at",enemy.color+enemy.NAME+res+", dealing",style.BOLD+str(sett-enemy.cHP)+style.RESET,"true damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"spikes a volleyball at",enemy.color+enemy.NAME+res+", dealing",style.BOLD+str(sett-enemy.cHP)+style.RESET,"true damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"True Ranged")
      else:
        enemy.onhittimersdefense(self,0,dmg,"True Ranged",skip="Skip")

  def enlargen(self,skip=""):
    self.thehut = True
    self.jabbaroll = 1
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"increases in size, taking the shape of a round ball to gain damage reduction!")

  def jabbaattack(self,targ,skip=""):
    global sett
    self.jabbaroll = 0
    self.fAT = self.fAT * (1.125 + (0.125*self.cLV))
    self.cAT = round(self.fAT*self.pAT)
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print(back.YELLOW_1 + fore.BLACK + "\n!!!"+ style.RESET,self.color+self.NAME+res,"starts rolling towards the enemies...",back.YELLOW_1 + fore.BLACK + "!!!" + style.RESET)
    for x in targ.team:
      self.prehiteffects(x)       
      sett = x.cHP
      diff = x.cEV - self.cAC 
      CT = random.randint(1,100)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          time.sleep(0.2)
          print("\n"+x.color+x.NAME+res,"moves out of the way!")
          x.specialdodgecases(self,0.1,"Physical Melee",CT)
        else:
          x.specialdodgecases(self,0,"Physical Melee",CT,skip="Skip")
      else:
        self.fcMP = self.fcMP + self.cMRG
        if self.fcMP > self.fMP:
          self.fcMP = self.fMP
        if CT <= self.cCT:
          dmg = self.CTdmg*self.cAT
          x.defense(self,"Physical",dmg)
          if skip != "Skip":
            time.sleep(0.2)
            if x.cHP > 0:
              if (sett-x.cHP) == 0:
                print("\n" + x.NAME,"is crushed but takes no damage!")
              else:
                print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 +style.BOLD+ str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 + style.BOLD+str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
            x.onhittimersdefense(self,0.1,dmg,"Critical Physical Melee Auto")
          else:
            x.onhittimersdefense(self,0,dmg,"Critical Physical Melee Auto",skip="Skip")
        else:
          dmg = self.cAT
          x.defense(self,"Physical",dmg)
          if skip != "Skip":
            time.sleep(0.2)
            if x.cHP > 0:
              if (sett-x.cHP) == 0:
                print("\n" + x.NAME,"is crushed but takes no damage!")
              else:
                print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
            x.onhittimersdefense(self,0.1,dmg,"Physical Melee Auto")
          else:
            x.onhittimersdefense(self,0,dmg,"Physical Melee Auto",skip="Skip")

  def grubbytides(self,targ,skip=""):
    global sett
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"summons the tides of grease, splashing the collosal waves onto all the enemies, damaging and poisoning them, and lowering their evasion!")
    for x in targ.team:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.1)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"avoids the wave!")
          x.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          x.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
      else:
        sett = x.cHP
        if x.poisont < 3:
          x.poisont = 3
        x.greased = [4,self]
        x.poisond = x.poisond + (self.cMAT*(80+(20*self.cLV)))
        dmg = self.cMAT*(300+(50*self.cLV))
        x.defense(self,"Magical",dmg)
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"is squashed by the wave, but takes no damage!")
            else:
              print("\n"+x.color+x.NAME+res,"is squashed by the wave, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"is squashed by the wave, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.1,dmg,"Magical Ranged")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def giantess(self,skip=""):
    selfsett = self.cHP
    self.cHP = self.cHP + round(self.healmod*self.cMAT*(800+(200*self.cLV)))
    self.fHP = self.fHP + round(800+(200*self.cLV))
    if self.cHP > self.fHP:
      self.cHP = round(self.fHP)
    self.giant = True
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"grows into a giant, drastically increasing her physical attack and maximum health, and healing for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health!")

  def firestorm(self,enemy,skip=""):
    self.jutsu = True
    for x in enemy.team:
      x.burnd = x.burnd + self.cMAT*(75+(25*self.cLV))
      x.burning = 1
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"conjures his firestorm jutsu, creating a ring of fire to continuosly burn all enemies and reduce their healing!")

  def givemeallyourmoney(self,ally,targ,skip=""):
    global sett
    
    if targ.gold > round(self.cLV+1):
      targ.gold = targ.gold - round(self.cLV+1)
      ally.gold = ally.gold + round(self.cLV+1)
    elif targ.gold <= round(self.cLV+1):
      ally.gold = ally.gold + targ.gold
      targ.gold = 0
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"steals",targ.Name+"'s money!")

  def fromtheshadows(self,targ,skip=""): #b
    global sett
    bruh = []
    for x in targ.team:
      bruh.append(x)
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"appears from the shadows!")
    for x in range(6):
      hit = random.choice(bruh)
      self.prehiteffects(hit)
      diff = hit.cEV - self.cAC
      CT = random.randint(1,100)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          time.sleep(0.1)
          print("\n"+self.color+self.NAME+res,"slashes",hit.color+hit.NAME+res + ", but they dodge!")
          hit.specialdodgecases(self,0.1,"Physical Melee",CT)
        else:
          hit.specialdodgecases(self,0,"Physical Melee",CT,skip="Skip")
      else:
        sett = hit.cHP
        if CT <= self.cCT:
          dmg = self.CTdmg*((self.cMAT*(50+(25*self.cLV)))+(self.cAT*(1+(0.1*self.cLV))))
          hit.defense(self,"Physical",dmg)
          if skip != "Skip":
            time.sleep(0.1)
            if hit.cHP >0:
              if (sett-hit.cHP) == 0:
                print("\n"+self.color+self.NAME+res, "critically slashes",hit.color+hit.NAME+res + ", but deals no damage!")
              else:
                print("\n"+self.color+self.NAME+res, "critically slashes",hit.color+hit.NAME+res+", dealing",fore.ORANGE_1 + style.BOLD + str(sett-hit.cHP) + style.RESET,"damage!",hit.NAME,"has",hit.cHP,"health remaining!")
            else:
              print("\n"+self.color+self.NAME+res, "critically slashes",hit.color+hit.NAME+res+", dealing",fore.ORANGE_1 + style.BOLD + str(sett-hit.cHP) + style.RESET,"damage!",hit.NAME,"falls...")  
            hit.onhittimersdefense(self,0.1,dmg,"Critical Physical Melee")
          else:
            hit.onhittimersdefense(self,0,dmg,"Critical Physical Melee",skip="Skip")
        else:
          dmg = (self.cMAT*(50+(25*self.cLV)))+(self.cAT*(1+(0.1*self.cLV)))
          hit.defense(self,"Physical",dmg)
          if skip != "Skip":
            time.sleep(0.1)
            if hit.cHP >0:
              if (sett-hit.cHP) == 0:
                print("\n"+self.color+self.NAME+res, "slashes",hit.color+hit.NAME+res + ", but deals no damage!")
              else:
                print("\n"+self.color+self.NAME+res, "slashes",hit.color+hit.NAME+res+", dealing",fore.ORANGE_1 + str(sett-hit.cHP) + style.RESET,"damage!",hit.NAME,"has",hit.cHP,"health remaining!")
            else:
              print("\n"+self.color+self.NAME+res,"slashes",hit.color+hit.NAME+res+", dealing",fore.ORANGE_1 + str(sett-hit.cHP) + style.RESET,"damage!",hit.NAME,"falls...")  
            hit.onhittimersdefense(self,0.1,dmg,"Physical Melee")
          else:
            hit.onhittimersdefense(self,0,dmg,"Physical Melee",skip="Skip")
        if skip != "Skip":
          self.onhittimersoffense(hit,0.1) 
        else:
          self.onhittimersoffense(hit,0,skip="Skip")
        if hit.cHP <= 0:
          bruh.remove(hit)
          if len(bruh) == 0:
            break
          
  def invisible(self,ally,skip=""):
    ally.teamID.remove(self.ID)
    self.invis = 4
    self.trig = 1
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"goes invisible...")

  def silenceattack(self,enemy,skip=""):
    global sett
    res = attr("reset")
    self.prehiteffects(enemy)
    sett = enemy.cHP
    diff = enemy.cEV - self.cAC 
    self.fcMP = self.fcMP + self.cMRG
    if self.fcMP > self.fMP:
      self.fcMP = self.fMP 
    CT = random.randint(1,100)
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res, "silently attacks, but", enemy.color+enemy.NAME+res, "dodges!")
        enemy.specialdodgecases(self,0.2,"True Melee",CT)
      else:
        enemy.specialdodgecases(self,0.2,"True Melee",CT,skip="Skip")
    else:
      if CT <= self.cCT:
        dmg = round(self.CTdmg*self.cAT*self.cMAT)
        enemy.cHP = enemy.cHP - dmg
        if skip != "Skip":
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n" +self.color+self.NAME+res, "dead silently attacks", enemy.color+enemy.NAME+res +  ", but deals no damage!")
            else:
              print("\n" +self.color+self.NAME+res, "dead silently attacks", enemy.color+enemy.NAME+res + ", dealing",fore.GREY_100+ style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n" +self.color+self.NAME+res, "dead silently attacks", enemy.color+enemy.NAME+res + ", dealing",fore.GREY_100 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
          enemy.onhittimersdefense(self,0.2,dmg,"Critical True Melee Auto")
        else:
          enemy.onhittimersdefense(self,0,dmg,"Critical True Melee Auto",skip="Skip")
      else:
        dmg = round(self.cAT*self.cMAT)
        enemy.cHP = enemy.cHP - dmg
        if skip != "Skip":
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n" +self.color+self.NAME+res, "silently attacks", enemy.color+enemy.NAME+res +  ", but deals no damage!")
            else:
              print("\n" +self.color+self.NAME+res, "silently attacks", enemy.color+enemy.NAME+res + ", dealing",fore.GREY_100 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n" +self.color+self.NAME+res, "silently attacks", enemy.color+enemy.NAME+res + ", dealing",fore.GREY_100 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
          enemy.onhittimersdefense(self,0.2,dmg,"True Melee Auto")
        else:
          enemy.onhittimersdefense(self,0,dmg,"True Melee Auto",skip="Skip")

  def powerpunch(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to punch",enemy.color+enemy.NAME+res,"really hard, but misses!")
        enemy.specialdodgecases(self,0.2,"Magical Melee")
      else:
        enemy.specialdodgecases(self,0,"Magical Melee",skip="Skip")
    else:
      sett = enemy.cHP
      dmg = self.cAT + (self.cMAT*(900+(120*self.cLV)))
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"punches",enemy.color+enemy.NAME+res,"really hard, but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"punches",enemy.color+enemy.NAME+res,"really hard, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"punches",enemy.color+enemy.NAME+res,"really hard, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def dab(self,enemy,skip=""): 
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"dabs on",enemy.color+enemy.NAME+res+", but it's power doesn't reach them!")
        enemy.specialdodgecases(self,0.2,"Magical Ranged")
      else:
        enemy.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
    else:
      sett = enemy.cHP
      techm = 1.00
      if self.dabstack == 0:
        daba = 1.00
      else:
        daba = ((1.1+(0.015*self.cLV))**self.dabstack)
      speedm = 1.00 + (0.01*self.cSP)
      if self.cAC > 100:
        techm = 1.00 + (0.005*(self.cAC-100))
      self.dabstack = self.dabstack + 1
      dmg = self.cMAT*self.cAT*techm*speedm*daba
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        tier = "dabs"
        if self.dabstack == 2:
          tier = "Great-dabs"
        elif self.dabstack == 3:
          tier = "Mega-dabs"
        elif self.dabstack == 4:
          tier = "Amazing-dabs"
        elif self.dabstack == 5:
          tier = "Ultra-dabs"
        elif self.dabstack == 6:
          tier = "Spectacular-dabs"
        elif self.dabstack == 7:
          tier = "Super-dabs"
        elif self.dabstack == 8:
          tier = "Superior-dabs"
        elif self.dabstack == 9:
          tier = "Supreme-dabs"
        elif self.dabstack == 10:
          tier = "Ultimate-dabs"
        elif self.dabstack == 11:
          tier = "Legendary-dabs"
        elif self.dabstack == 12:
          tier = "God-dabs"
        elif self.dabstack == 12:
          tier = "Graham-dabs"
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,tier,"on",enemy.color+enemy.NAME+res,"sending the trifecta of power, technique, and speed of the dab at them, but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,tier,"on",enemy.color+enemy.NAME+res,"sending the trifecta of power, technique, and speed of the dab at them, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,tier,"on",enemy.color+enemy.NAME+res,"sending the trifecta of power, technique, and speed of the dab at them, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def record(self,ally,targ,skip=""):
    global sett
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 2:
      di = (len(tempteam)-2)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    if skip != "Skip":
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"releases all the damage she recorded onto select enemies!")
    total = 0
    for x in ally.team:
      total = total + x.totaldamage
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.2)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"is unaffected!")
          x.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          x.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
      else:
        sett = x.cHP
        dmg = self.cMAT*(total*(0.06+(0.02*self.cLV)))
        x.defense(self,"Magical",dmg)
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"feels the damage dealt through battle, but takes no damage!")
            else:
              print("\n"+x.color+x.NAME+res,"feels the damage dealt through battle, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"feels the damage dealt through battle, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.1,dmg,"Magical Ranged")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")
    
  def godandanime(self,ally,skip=""):
    tempteam = []
    remain = []
    for x in ally.team:
      if x.cHP != x.fHP:
        tempteam.append(x.cHP/x.fHP) 
      else:
        remain.append(x)
    tempteam.sort()
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"calls upon the power of god and anime to invigorate his allies!")
    for x in range(3):
      for y in ally.team:
        if len(tempteam) == 0:
          break
        if (y.cHP/y.fHP) == tempteam[0]:
          if "Weeb" in y.SYN and ally.wee >=3:
            bruh = tempteam.count(y.cHP/y.fHP)
            for z in range(bruh):
              tempteam.remove(tempteam[0])
          else:
            tempteam.remove(tempteam[0])
          selfsett = y.cHP
          y.cHP = y.cHP + round(y.healmod*self.cMAT*(500+(100*self.cLV)))
          if y.cHP > y.fHP:
            y.cHP = round(y.fHP)
          y.anime = [4,self]
          if skip != "Skip":
            time.sleep(0.2)
            print("\n"+y.color+y.NAME+res,"receives blessings, recovering",fore.MEDIUM_SPRING_GREEN+str(y.cHP-selfsett)+style.RESET,"health and gaining increased speed! They have",y.cHP,"health now!")
          break
      if len(tempteam) == 0 and len(remain) > 0:
        pers = random.choice(remain)
        remain.remove(pers)
        selfsett = pers.cHP
        pers.anime = [4,self]
        if skip != "Skip":
          time.sleep(0.2)
          print("\n"+pers.color+pers.NAME+res,"receives blessings, gaining increased speed!")
      elif len(tempteam) == 0 and len(remain) == 0:
        break
      

  def organization(self,ally,skip=""):
    self.organ = True
    for x in ally.team:
      x.organized = 4
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"organizes the team into the best positions, increasing everyone's evasion, critical chance, and mana regeneration!")

  def defaultdance(self,targ,skip=""):
    global sett
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 3:
      di = (len(tempteam)-3)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    if skip != "Skip":
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res, "does the default dance!")
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.2)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"looks at him in disgust!")
          x.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          x.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
      else:
        sett = x.cHP
        dmg = self.cMAT*(200+(40*self.cLV))
        x.defense(self,"Magical",dmg)
        x.dance = 2
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"starts to default dance with him, but takes no damage!")
            else:
              print("\n"+x.color+x.NAME+res,"starts to default dance with him, and takes",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"starts to default dance with him, and takes",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.1,dmg,"Magical Ranged")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def blitz(self,targ,skip=""):
    global sett
    reset = 0
    targets = targ.team.copy()
    stacks = 0
    self.SP += 1
    while reset == 0:
      enemy = random.choice(targets)
      targets.remove(enemy)
      self.prehiteffects(enemy)
      diff = enemy.cEV - self.cAC
      CT = random.randint(1,100)
      res = attr("reset")
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          time.sleep(0.5)
          print("\n"+self.color+self.NAME+res,"tries to blitz",enemy.color+enemy.NAME+res+", but they see it coming!")
          enemy.specialdodgecases(self,0.2,"Physical Melee",CT)
        else:
          enemy.specialdodgecases(self,0,"Physical Melee",CT,skip="Skip")
      else:
        sett = enemy.cHP
        if self.cSP > enemy.cSP+25:
          enemy.tremstun = 1
        if CT <= self.cCT:
          if self.cSP > enemy.cSP:
            dmg = (1+(((0.1+(0.01*self.cLV))*(self.cSP-enemy.cSP))))*self.cAT*self.CTdmg*(1+((0.2*stacks*self.cMAT)))
          else:
            dmg = self.cAT*self.CTdmg*(1+((0.2*stacks*self.cMAT)))
          enemy.defense(self,"Physical",dmg)
          if skip != "Skip":
            time.sleep(0.2)
            if enemy.cHP >0:
              if (sett-enemy.cHP) == 0:
                print("\n"+self.color+self.NAME+res,"blitzes",enemy.color+enemy.NAME+res+" at breakneck speeds, but deals no damage1")
              else:
                print("\n"+self.color+self.NAME+res,"blitzes",enemy.color+enemy.NAME+res+" at breakneck speeds, dealing",fore.ORANGE_1 + style.BOLD+ str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              print("\n"+self.color+self.NAME+res,"blitzes",enemy.color+enemy.NAME+res+" at breakneck speeds, dealing",fore.ORANGE_1 + style.BOLD+ str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
            enemy.onhittimersdefense(self,0.2,dmg,"Critical Physical Melee")
          else:
            enemy.onhittimersdefense(self,0,dmg,"Critical Physical Melee",skip="Skip")
        else:
          if self.cSP > enemy.cSP:
            dmg = (1+(((0.1+(0.01*self.cLV))*(self.cSP-enemy.cSP))))*self.cAT*(1+((0.2*stacks*self.cMAT)))
          else:
            dmg = self.cAT*(1+((0.2*stacks*self.cMAT)))
          enemy.defense(self,"Physical",dmg)
          if skip != "Skip":
            time.sleep(0.2)
            if enemy.cHP >0:
              if (sett-enemy.cHP) == 0:
                print("\n"+self.color+self.NAME+res,"blitzes",enemy.color+enemy.NAME+res+", but deals no damage1")
              else:
                print("\n"+self.color+self.NAME+res,"blitzes",enemy.color+enemy.NAME+res+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              print("\n"+self.color+self.NAME+res,"blitzes",enemy.color+enemy.NAME+res+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
            enemy.onhittimersdefense(self,0.2,dmg,"Critical Physical Melee")
          else:
            enemy.onhittimersdefense(self,0,dmg,"Critical Physical Melee",skip="Skip")
        if enemy.cHP > 0:
          reset = 1
        else:
          stacks += 1

 # def tremors(self,targ,skip=""):
   # global sett
   # if skip != "Skip":
     # res = attr("reset")
      #time.sleep(0.5)
      #print("\n"+self.color+self.NAME+res, "sends tremors through the ground!")
    #for x in targ.team:
     # self.prehiteffects(x)
     # diff = x.cEV - self.cAC
     # stunc = round(self.cMAT*50)
      #if skip != "Skip":
        #time.sleep(0.1)
      #if random.randint(1,100) <= diff:
        #if skip != "Skip":
          #print("\n"+x.color+x.NAME+res,"jumps off the ground before they can fall!")
          #x.specialdodgecases(self,0.1,"Physical Ranged")
        #else:
          #x.specialdodgecases(self,0,"Physical Ranged",skip="Skip")
     # else:
        #sett = x.cHP
       # dmg = ((1.25+(0.25*self.cLV))*self.cAT)
        #x.defense(self,"Physical",dmg)
        #if random.randint(0,100) <= stunc:
         # x.tremstun = 1
         ## if skip != "Skip":
          #  if x.cHP > 0:
            #  if (sett-x.cHP) == 0:
             #   print("\n"+x.color+x.NAME+res,"topples over, but takes no damage!")
              #else:
               # print("\n"+x.color+x.NAME+res,"topples over, taking",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
           # else:
            #  print("\n"+x.color+x.NAME+res,"topples over, taking",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
           # x.onhittimersdefense(self,0.1,dmg,"Physical Ranged")
          #else:
           # x.onhittimersdefense(self,0,dmg,"Physical Ranged",skip="Skip")
        #else:
         # x.tremsl = 2
          #if skip != "Skip":
            #if x.cHP > 0:
              #if (sett-x.cHP) == 0:
               # print("\n"+x.color+x.NAME+res,"trembles, but takes no damage!")
              #else:
                #print("\n"+x.color+x.NAME+res,"trembles, taking",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            #else:
              #print("\n"+x.color+x.NAME+res,"trembles, taking",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
            #x.onhittimersdefense(self,0.1,dmg,"Physical Ranged")
          #else:
           # x.onhittimersdefense(self,0,dmg,"Physical Ranged",skip="Skip")

  def grace(self,ally,skip=""):
    for x in ally.team:
      x.graced = [3,self]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"graces her team with the words of Jesus, causing everyone to have increased healing and regenerate health!")

  def egirl(self,targ,skip=""):
    global sett
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 3:
      di = (len(tempteam)-3)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    hit = 0
    print("\n"+self.color+self.NAME+res,"begs the enemies for stream donations for her twitch channel!")
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.5)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"does not donate!")
          x.specialdodgecases(self,0.2,"Magical Melee")
        else:
          x.specialdodgecases(self,0,"Magical Melee",skip="Skip")
      else:
        hit = hit + 1
        sett = x.cHP
        dmg = self.cMAT*(x.fHP*(0.15+(0.0125*self.cLV)))
        x.defense(self,"Magical",dmg) 
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"donates to her, but does not give up any health!")
            else:
              print("\n"+x.color+x.NAME+res,"donates to her, giving up",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"health!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"donates to her, giving up",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"health!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Magical Melee")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")
    selfsett = self.cHP
    self.cHP = self.cHP + round((self.fHP-self.cHP)*(hit*(0.1+(0.01*self.cLV))))
    if skip != "Skip":
      if hit > 0:
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"gets healing from her donations, healing for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health! She has",self.cHP,"health now!")       

  def thecall(self,ally,skip=""):
    self.hogrider = 1
    for x in ally.team:
      x.hogg = 4
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"sounds the horns of battle, increasing everyone's physical attack!")

  def hornofbattle(self,targ,skip=""):
    global sett
    self.hogrider = 0
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"releases the final blast from his trumpet!")
    for x in targ.team:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.1)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"covers their ears!")
          x.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          x.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
      else:
        sett = x.cHP
        dmg = self.cMAT*(200+(20*self.cLV))
        x.defense(self,"Magical",dmg)
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"is earraped, but takes no damage!")
            else:
              print("\n"+x.color+x.NAME+res,"is earraped, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"is earraped, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.1,dmg,"Magical Ranged")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")
  
  def stayshut(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tells",enemy.color+enemy.NAME+res,"to stay shut, but they don't listen!")
        enemy.specialdodgecases(self,0.2,"Magical Ranged")
      else:
        enemy.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
    else:
      sett = enemy.cHP
      dmg = self.cMAT*(300+(40*self.cLV))
      enemy.defense(self,"Magical",dmg)
      enemy.silenced = 1000
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"tells",enemy.color+enemy.NAME+res,"to stay shut, permanently silencing them but dealing no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"tells",enemy.color+enemy.NAME+res,"to stay shut, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and permanently silencing them!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"tells",enemy.color+enemy.NAME+res,"to stay shut, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and permanently silencing them!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def grootroot(self,targ,skip=""):
    global sett
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 6:
      di = (len(tempteam)-6)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res, "sends branches through the ground!")
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.1)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"avoids the branches!")
          x.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          x.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
      else:
        sett = x.cHP
        dmg = self.cMAT*(250+(25*self.cLV))
        x.defense(self,"Magical",dmg)
        x.rooted = 1
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"is rooted by the branches, but takes no damage!")
            else:
              print("\n"+x.color+x.NAME+res,"is rooted by the branches, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"is rooted by the branches, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.1,dmg,"Magical Ranged")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def evileye(self,targ,skip=""):
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 4:
      di = (len(tempteam)-4)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    if skip != "Skip":
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res, "casts the evil eye upon the enemies!")
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.2)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"is unaffected!")
          x.specialdodgecases(self,0.1,"None")
        else:
          x.specialdodgecases(self,0,"None",skip="Skip")
      else:
        if x.decayt < 2:
          x.decayt = 2
        x.decayd = x.decayd + (self.cMAT*(150+(13*self.cLV)))
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"is affected by the omen, starting to decay!")

  def runnershigh(self,skip=""):
    self.runhigh = 26
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"enters the runner's high, removing and becoming immune to slows and increasing his attack and defense!")

  def dancersswiftness(self,skip=""):
    self.swift = self.swift + 1
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"dances around to increase her range of motion, permanently increasing her evasion by 10%!")

  def striker(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    self.cAC = round(self.cAC*(2+(0.125*self.cLV)))
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"strikes a soccer ball at",enemy.color+enemy.NAME+res+", but they miraculously dodge!")
        enemy.specialdodgecases(self,0.2,"Magical Ranged")
      else:
        enemy.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
    else:
      sett = enemy.cHP
      dmg = self.cMAT*(400+(40*self.cLV))
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"strikes a soccer ball at",enemy.color+enemy.NAME+res+", but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"strikes a soccer ball at",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"strikes a soccer ball at",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def disappear(self,ally,skip=""):
    ally.teamID.remove(self.ID)
    self.hiding = 3
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"disappears!")

  def extrabullying(self,enemy,ally,skip=""):
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if ally.ben >= 2:
      for x in ally.team:
        if "Bengali" in x.SYN and x.GEN == "Female":
          x.fferv = x.fferv + 1
          if x.fferv > 5:
            x.fferv = 5
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to bully and harass",enemy.color+enemy.NAME+res+", but they ignore her!")
        enemy.specialdodgecases(self,0.2,"None")
      else:
        enemy.specialdodgecases(self,0,"None",skip="Skip")
    else:
      if enemy.burnt < 2:
        enemy.burnt = 2
      if enemy.decayt < 2:
        enemy.decayt = 2
      enemy.burnd = enemy.burnd + (self.cMAT*(200+(13*self.cLV)))
      enemy.decayd = enemy.decayd + (self.cMAT*(200+(13*self.cLV)))
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"bullies and harasses",enemy.color+enemy.NAME+res+", causing them to burn and decay!")

  def bearrepulse(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to bounce back with the energy he has stored onto",enemy.NAME+", but misses!")
        enemy.specialdodgecases(self,0.2,"Magical Melee")
      else:
        enemy.specialdodgecases(self,0,"Magical Melee",skip="Skip")
    else:
      sett = enemy.cHP
      dmg = self.cMAT*(self.dmgstore*(0.2+(0.1*self.cLV)))
      enemy.defense(self,"Magical",dmg)
      self.dmgstore = 0
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"bounces back with the energy he has stored onto",enemy.NAME+", but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"bounces back with the energy he has stored onto",enemy.NAME+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"bounces back with the energy he has stored onto",enemy.NAME+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")

  def siton(self,enemy,targ,skip=""):
    targ.teamS.remove(enemy.NAME)
    targ.teamID.remove(enemy.ID)
    self.sitting = [1,enemy]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"sits on",enemy.color+enemy.NAME+res+", crushing them beneath her!")


  def teamteam(self,ally,skip=""):
    for x in ally.team:
      x.teamed = [2,self,self.cMAT]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"flaps his arm across his chest, teaming with everyone on his team to increase their defense for the next 2 hits!")

  def notthatdeep(self,targ,skip=""):
    global sett
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      if x.drift[0] == 0:
        tempteam.append(x)
    if len(tempteam) > 3:
      di = (len(tempteam)-3)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    if skip != "Skip":
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res, "states that it ain't that deep, echoing across the battlefield!")
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.2)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"is unaffected!")
          x.specialdodgecases(self,0.1,"None")
        else:
          x.specialdodgecases(self,0,"None",skip="Skip")
      else:
        x.drift = [4,self,self.cMAT]
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"catches the drift, becoming slowed!")

  def vibe(self,skip=""):
    selfsett = self.cHP
    self.cHP = self.cHP + round(self.cMAT*(1000+(250*self.cLV)))
    if self.cHP > self.fHP:
      self.cHP = self.fHP
    self.stunimmune = True
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"starts to just vibe, healing for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health and becoming immune to all stuns! He has",self.cHP,"health now!")

  def buckets(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to dunk on",enemy.color+enemy.NAME+res+", but they guard him!")
        enemy.specialdodgecases(self,0.2,"Magical Melee")
      else:
        enemy.specialdodgecases(self,0,"Magical Melee",skip="Skip")
    else:
      sett = enemy.cHP
      selfsett = self.cHP
      dmg = self.cMAT*((0.3+(0.03*self.cLV))*(enemy.fHP-enemy.cHP))
      enemy.defense(self,"Magical",dmg)
      self.cHP = self.cHP + round((sett-enemy.cHP)*0.5*self.cMAT)
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"dunks on",enemy.color+enemy.NAME+res+", but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"dunks on",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"dunks on",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"heals himself for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health! He has",self.cHP,"health now!")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")

  def demean(self,enemy,skip=""):
    global sett
    enemy.sad = [5,self,self.cMAT]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"breaks",enemy.color+enemy.NAME+res+"'s confidence, lowering their physical attack!")

  def arrivederci(self,enemy,skip=""):
    global sett
    enemy.deathmark = enemy.deathmark + (0.15+(0.0125*self.cLV))
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"bids farewell to",enemy.color+enemy.NAME+res+", causing them to take more damage permanently!")

  def chillvibes(self,targ,skip=""):
    for x in targ.team:
      x.chilled = [21,self,self.cMAT]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"brings the chill vibes into the battlefield, slowing all enemies down!")
    
  def breakdown(self,targ,skip=""):
    global sett
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 3:
      di = (len(tempteam)-3)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    if skip != "Skip":
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res, "breaks down in stress, screaming across the battlefield!")
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.1)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"is unaffected!")
          x.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          x.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
      else:
        sett = x.cHP
        x.fear[0] = 3
        x.fear[1] = x.fear[1] + 1
        dmg = self.cMAT*(150+(25*self.cLV))
        x.defense(self,"Magical",dmg)
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"is startled, getting feared but taking no damage!")
            else:
              print("\n"+x.color+x.NAME+res,"is startled, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage and becoming feared!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"is startled, taking",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage and becoming feared!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.1,dmg,"Magical Ranged")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def golfgod(self,skip=""):
    self.eagle = [5,self.cMAT]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"goes eagle-eye mode, increasing their accuracy, critical chance, and causing bleed on-hit for 4 turns!")

  def progressiveoverload(self,skip=""):
    self.tension = self.tension + 1
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      if self.tension == 1:
        print("\n"+self.color+self.NAME+res,"tenses up, building up his strength!")
      elif self.tension == 2:
        print("\n"+self.color+self.NAME+res,"tenses up greatly, further building up his strength!")
      elif self.tension == 3:
        print("\n"+self.color+self.NAME+res,"tenses up immensely, extremely building up his strength! Shah is ready to unleash his power!")

  def baking(self,tea,skip=""):
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"bakes home goods for the entire team, restoring everyone's health!")
    for x in tea.team:
      selfsett = x.cHP
      x.cHP = x.cHP + round(x.healmod*self.cMAT*(200+(40*self.cLV)))
      if x.cHP > x.fHP:
        x.cHP = round(x.fHP)
      if skip != "Skip":
        print("\n"+x.color+x.NAME+res,"heals for",fore.MEDIUM_SPRING_GREEN+str(x.cHP-selfsett)+style.RESET,"health! They have",x.cHP,"health now!")

  def gaze(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"gazes at",enemy.color+enemy.NAME+res+", but they look away!")
        enemy.specialdodgecases(self,0.2,"Magical Ranged")
      else:
        enemy.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
    else:
      sett = enemy.cHP
      enemy.blind = 4
      dmg = self.cMAT*(140+(30*self.cLV))
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"gazes at",enemy.color+enemy.NAME+res+", blinding them but dealing no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"gazes at",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and blinding them!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"gazes at",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and blinding them!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def sexappeal(self,skip=""):
    self.sexy = 7
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"appeals to all the men on the battlefield with her fat ass, becoming untargetable and immune to their damage, and increasing her damage against males for 6 turns! ")

  def assortment(self,tea,skip=""):
    bruh = [] 
    for x in tea.team:
      if len(x.confection) == 1:
        bruh.append(x)
    if len(bruh) > 0:
      feed = random.choice(bruh)
    else:
      feed = random.choice(tea.team)
    selfsett = feed.cHP
    feed.cHP = feed.cHP + round(feed.healmod*self.cMAT*(300+(50*self.cLV)))
    if feed.cHP > feed.fHP:
      feed.cHP = round(feed.fHP)
    statup = random.randint(1,4)
    feed.confection = [6,self,statup,self.cMAT]
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      if statup == 1:
        print("\n"+self.color+self.NAME+res,"gives",feed.color+feed.NAME+res,"a treat, healing them for",fore.MEDIUM_SPRING_GREEN+str(feed.cHP-selfsett)+style.RESET,"health and boosting their attack! They have",feed.cHP,"health now!")
      elif statup == 2:
        print("\n"+self.color+self.NAME+res,"gives",feed.color+feed.NAME+res,"a treat, healing them for",fore.MEDIUM_SPRING_GREEN+str(feed.cHP-selfsett)+style.RESET,"health and boosting their defense! They have",feed.cHP,"health now!")
      elif statup == 3:
        print("\n"+self.color+self.NAME+res,"gives",feed.color+feed.NAME+res,"a treat, healing them for",fore.MEDIUM_SPRING_GREEN+str(feed.cHP-selfsett)+style.RESET,"health and boosting their magic attack! They have",feed.cHP,"health now!")
      elif statup == 4:
        print("\n"+self.color+self.NAME+res,"gives",feed.color+feed.NAME+res,"a treat, healing them for",fore.MEDIUM_SPRING_GREEN+str(feed.cHP-selfsett)+style.RESET,"health and boosting their magic defense! They have",feed.cHP,"health now!")

  def didiask(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"asks",enemy.color+enemy.NAME+res,"if he asked, but they don't understand!")
        enemy.specialdodgecases(self,0.2,"Magical Ranged")
      else:
        enemy.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
    else:
      sett = enemy.cHP
      selfsett = self.cHP
      dmg = self.cMAT*(200+(25*self.cLV))
      enemy.defense(self,"Magical",dmg)
      self.cHP = self.cHP + round(self.healmod*self.cMAT*(100+(50*self.cLV)))
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"asks",enemy.color+enemy.NAME+res,"if he asked, but deals no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"asks",enemy.color+enemy.NAME+res,"if he asked, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"asks",enemy.color+enemy.NAME+res,"if he asked, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
        time.sleep(0.3)
        print("\n"+self.color+self.NAME+res,"heals himself for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health! He has",self.cHP,"health now!")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")

  def awkwardtouch(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to touch",enemy.color+enemy.NAME+res+", but they push him away!")
        enemy.specialdodgecases(self,0.2,"Magical Melee")
      else:
        enemy.specialdodgecases(self,0,"Magical Melee",skip="Skip")
    else:
      sett = enemy.cHP
      enemy.touched = [4,self,self.cMAT]
      dmg = self.cMAT*(100+(12*self.cLV))
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"awkwardly touches",enemy.color+enemy.NAME+res+", reducing their accuracy but dealing no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"awkwardly touches",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and reducing their accuracy!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"awkwardly touches",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and reducing their accuracy!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")
  
  def ravenous(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"wiles out on",enemy.color+enemy.NAME+res+", but to no avail!")
        enemy.specialdodgecases(self,0.2,"Magical Melee")
      else:
        enemy.specialdodgecases(self,0,"Magical Melee",skip="Skip")
    else:
      if enemy.bleedt < 2:
        enemy.bleedt = 2
      enemy.bleedd = enemy.bleedd + (self.cMAT*(100+(13*self.cLV)))
      sett = enemy.cHP
      dmg = self.cMAT*(200+(25*self.cLV))
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.color+self.NAME+res,"wiles out on",enemy.color+enemy.NAME+res+", causing them to bleed but dealing no damage!")
          else:
            print("\n"+self.color+self.NAME+res,"wiles out on",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and causing them to bleed!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.color+self.NAME+res,"wiles out on",enemy.color+enemy.NAME+res+", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage and causing them to bleed!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")

  def cripple(self,targ,skip=""):
    global sett
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 3:
      di = (len(tempteam)-3)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.5)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+self.color+self.NAME+res, "tries to cripple",x.color+x.NAME+res+", but misses!")
          x.specialdodgecases(self,0.2,"Magical Melee")
        else:
          x.specialdodgecases(self,0,"Magical Melee",skip="Skip")
      else:
        sett = x.cHP
        dmg = self.cMAT*(100+(13*self.cLV))
        x.defense(self,"Magical",dmg)
        x.crips = [5,self,self.cMAT]
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+self.color+self.NAME+res,"cripples",x.color+x.NAME+res+", slowing them but dealing no damage!")
            else:
              print("\n"+self.color+self.NAME+res,"cripples",x.color+x.NAME+res+", slowing them and dealing",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+self.color+self.NAME+res,"cripples",x.color+x.NAME+res+", slowing them and dealing",fore.PURPLE_1B+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Magical Melee")
        else:
          x.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")

  def seal(self,ally,targ,skip=""):
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 3:
      di = (len(tempteam)-3)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    if ally.ben >= 2:
      for x in ally.team:
        if "Bengali" in x.SYN and x.GEN == "Female":
          x.fferv = x.fferv + 1
          if x.fferv > 5:
            x.fferv = 5
    if skip != "Skip":  
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"seals the ability of 3 enemies for 5 turns!")
    for x in tempteam:
      x.silenced = 6
      if skip != "Skip":
        time.sleep(0.1)
        print("\n"+x.color+x.NAME+res,"is silenced by the seal!")

  def headbutt(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to headbutt",enemy.color+enemy.NAME+res+", but they juke him!")
        enemy.specialdodgecases(self,0.2,"Magical Melee")
      else:
        enemy.specialdodgecases(self,0,"Magical Melee",skip="Skip")
    else:
      sett = enemy.cHP
      dmg = self.cMAT*(250+(20*self.cLV))
      enemy.defense(self,"Magical",dmg)
      enemy.confused = 1
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n" + self.color+self.NAME+res,"headbutts",enemy.color+enemy.NAME+res+", confusing them but dealing no damage!")
          else:
            print("\n" + self.color+self.NAME+res,"headbutts",enemy.color+enemy.NAME+res+", confusing them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n" + self.color+self.NAME+res,"headbutts",enemy.color+enemy.NAME+res+", confusing them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Melee",skip="Skip")

  def insult(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to bully",enemy.color+enemy.NAME+res+", but they don't care!")
        enemy.specialdodgecases(self,0.2,"Magical Ranged")
      else:
        enemy.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
    else:
      if enemy.poisont < 2:
        enemy.poisont = 2
      enemy.poisond = enemy.poisond + (self.cMAT*(100+(12*self.cLV)))
      sett = enemy.cHP
      dmg = self.cMAT*(60+(20*self.cLV))
      enemy.defense(self,"Magical",dmg)
      if skip != "Skip":
        time.sleep(0.5)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n" + self.color+ self.NAME+res,"bullies",enemy.color+enemy.NAME+res+", poisoning them but dealing no damage!")
          else:
            print("\n" + self.color+ self.NAME+res,"bullies",enemy.color+enemy.NAME+res+", poisoning them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n" + self.color+ self.NAME+res,"bullies",enemy.color+enemy.NAME+res+", poisoning them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
      else:
        enemy.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")

  def dminion(self,enemy,skip=""):
    global sett
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res, "makes fun of",enemy.color+enemy.NAME+res+"'s name, but they ignore him!")
        enemy.specialdodgecases(self,0.2,"None")
      else:
        enemy.specialdodgecases(self,0,"None",skip="Skip")
    else:
      enemy.named = [6,self,self.cMAT]
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"makes fun of",enemy.color+enemy.NAME+res+"'s name, increasing the cost of their skill for 5 turns!")

  def cap(self,enemy,skip=""):
    self.ego.append(enemy)
    enemy.delled = 4
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"tells",enemy.color+enemy.NAME+res,"about how much sex he has had, boosting his ego and reducing their accuracy!")

  def megapunch(self,targ,skip=""):
    global sett
    res = attr("reset")
    tempteam = []
    for x in targ.team:
      tempteam.append(x)
    if len(tempteam) > 3:
      di = (len(tempteam)-3)
      for x in range(di):
        uni = random.choice(tempteam)
        tempteam.remove(uni)
    for x in tempteam:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.5)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+self.color+self.NAME+res, "tries to strike",x.color+x.NAME+res+", but misses!")
          x.specialdodgecases(self,0.2,"Physical Melee")
        else:
          x.specialdodgecases(self,0,"Physical Melee",skip="Skip")
      else:
        sett = x.cHP
        dmg = self.cAT + (self.cMAT*(50+(25*self.cLV)))
        x.cDF = x.cDF * 0.5
        x.defense(self,"Physical",dmg)
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+self.color+self.NAME+res,"strikes",x.color+x.NAME+res+", but deals no damage!")
            else:
              print("\n"+self.color+self.NAME+res,"strikes",x.color+x.NAME+res+", dealing",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+self.color+self.NAME+res,"strikes",x.color+x.NAME+res+", dealing",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Physical Melee")
        else:
          x.onhittimersdefense(self,0,dmg,"Physical Melee",skip="Skip")


  def fencingstab(self,enemy,skip=""):
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    res = attr("reset")
    if random.randint(1,100) <= diff:
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"tries to stab",enemy.color+enemy.NAME+res,"but they avoid the attack!")
        enemy.specialdodgecases(self,0.2,"None")
      else:
        enemy.specialdodgecases(self,0,"None",skip="Skip")
    else:
      if enemy.bleedt < 15:
        enemy.bleedt = 15
      enemy.bleedd = enemy.bleedd + (self.cMAT*(15+(3*self.cLV)))
      if skip != "Skip":
        time.sleep(0.5)
        print("\n"+self.color+self.NAME+res,"stabs",enemy.color+enemy.NAME+res,"with his sword, causing them to bleed for 15 turns!")
      
  def simp(self,ally,skip=""):
    perc = (0.1+(0.0125*self.cLV))
    love = []
    for x in ally.team:
      if x.GEN == "Female":
        love.append(x)
    if len(love) > 0:
      sim = random.choice(love)
      self.simping = self.simping + 1
      sim.simped = [sim.simped[0]+perc,self]
      inc = round(perc*self.HP)
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)
        if self.cHP > 0:
          print("\n"+self.color+self.NAME+res,"simps for",sim.color+sim.NAME+res+", gifting a percentage of his HP, AT, DF, MAT, and MDF to them!")
      sim.fHP = sim.fHP + inc
      sim.cHP = sim.cHP + inc
      if sim.cHP > sim.fHP:
        sim.cHP = sim.fHP
      if skip != "Skip":
        time.sleep(0.3)
        print("\n"+sim.color+sim.NAME+res,"accepts",self.color+self.NAME+res+"'s gift, healing for and increasing their maximum health by",fore.MEDIUM_SPRING_GREEN+str(inc)+style.RESET+"!")
    else:
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)       
        print("\n"+self.color+self.NAME+res,"senses no girls to simp for!")
    
  def schoolshooting(self,targ,skip=""):
    global sett
    bruh = []
    for x in targ.team:
      bruh.append(x)
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print("\n"+self.color+self.NAME+res,"takes out a gun from his bookbag and gets shootin'!")
    for x in range(6):
      hit = random.choice(bruh)
      self.prehiteffects(hit)
      diff = hit.cEV - self.cAC
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          time.sleep(0.1)
          print("\n"+hit.NAME,"dodged a bullet!")
          hit.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          hit.specialdodgecases(self,0,"Magical Ranged",skip="Skip")
      else:
        sett = hit.cHP
        dmg = self.cMAT*(100+(20*self.cLV))
        hit.defense(self,"Magical",dmg)
        if skip != "Skip":
          time.sleep(0.1)
          if hit.cHP >0:
            if (sett-hit.cHP) == 0:
              print("\n"+hit.color + hit.NAME + res, "is shot, but takes no damage!")
            else:
              print("\n" + hit.color + hit.NAME + res, "is shot, taking",fore.PURPLE_1B + str(sett-hit.cHP) + style.RESET,"damage!",hit.NAME,"has",hit.cHP,"health remaining!")
          else:
            print("\n" + hit.color + hit.NAME + res, "is shot, taking",fore.PURPLE_1B + str(sett-hit.cHP) + style.RESET,"damage!",hit.NAME,"falls...")         
          hit.onhittimersdefense(self,0.1,dmg,"Magical Ranged")
        else:
          hit.onhittimersdefense(self,0,dmg,"Magical Ranged",skip="Skip")
        if hit.cHP <= 0:
          bruh.remove(hit)
          if len(bruh) == 0:
            break

  def badwire(self,enemy,skip=""):
    enemy.paralyzed = 2
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.5)
      print(self.color+"\nErick"+res,"runs current through",enemy.color+enemy.NAME+res+", paralyzing them for two turns!")

  def soccerrally(self,ally,skip=""):
    for x in ally.team:
      val = round(self.cMAT*(10 + self.cLV))
      x.rallied = [4,self,val]
    if skip != "Skip":
      res = attr("reset")
      valu = round(self.cMAT*(10 + self.cLV))
      time.sleep(0.5)
      print(self.color+"\nAnthony"+res,"rallies his team, increasing everyone's APN and MPN by",str(valu)+"!")

  def terrorism(self,ally,targ,skip=""):
    if skip != "Skip":
      res = attr("reset")
      time.sleep(0.3)
      print("\nHamas calls in a missle strike!")
    for x in targ.team:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if skip != "Skip":
        time.sleep(0.1)
      if random.randint(1,100) <= diff:
        if skip != "Skip":
          print("\n"+x.color+x.NAME+res,"dodges the missiles!")
          x.specialdodgecases(self,0.1,"Physical Ranged")
        else:
          x.specialdodgecases(self,0,"Physical Ranged",skip="Skip")
      else:
        sett = x.cHP
        if ally.pal >= 2 and ally.pal < 4:
          dmg = 100
        elif ally.pal >= 4:
          dmg = 300
        x.defense(self,"Physical",dmg)
        if skip != "Skip":
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.color+x.NAME+res,"is hit by a missile, but takes no damage!")
            else:
              print("\n"+x.color+x.NAME+res,"is hit by a missile, taking",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.color+x.NAME+res,"is hit by a missile, taking",fore.ORANGE_1+str(sett-x.cHP)+style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.1,dmg,"Physical Ranged")
        else:
          x.onhittimersdefense(self,0,dmg,"Physical Ranged",skip="Skip")
  
def carousel(types=""):
  global carousellist
  t1 = []
  t2 = []
  t3 = []
  t4 = []
  t5 = []
  for x in tier1:
    t1.append(x)
  for x in tier2:
    t2.append(x)
  for x in tier3:
    t3.append(x)
  for x in tier4:
    t4.append(x)
  for x in tier5:
    t5.append(x)
  carousellist = []
  time.sleep(0.5)
  print("\nPick a free character!\n")
  time.sleep(0.5)
  if types == "Start":
    for x in range(2):
      unit = [random.choice(t1),random.choice(items)]
      p1.purchase(unit,1,True)   
      t1.remove(unit[0])
    for x in range(8):
      unit = [random.choice(t2),random.choice(items)]
      p1.purchase(unit,2,True)   
      t2.remove(unit[0])
  if types == "2":
    for x in range(2):
      unit = [random.choice(t1),random.choice(items)]
      p1.purchase(unit,1,True)   
      t1.remove(unit[0])
    for x in range(4):
      unit = [random.choice(t2),random.choice(items)]
      p1.purchase(unit,2,True)   
      t2.remove(unit[0])
    for x in range(4):
      unit = [random.choice(t3),random.choice(items)]
      p1.purchase(unit,3,True)   
      t3.remove(unit[0])
  if types == "3":
    for x in range(2):
      unit = [random.choice(t1),random.choice(items)]
      p1.purchase(unit,1,True)   
      t1.remove(unit[0])
    for x in range(2):
      unit = [random.choice(t2),random.choice(items)]
      p1.purchase(unit,2,True)   
      t2.remove(unit[0])
    for x in range(6):
      unit = [random.choice(t3),random.choice(items)]
      p1.purchase(unit,3,True)   
      t3.remove(unit[0])
  if types == "4":
    for x in range(2):
      unit = [random.choice(t1),random.choice(items)]
      p1.purchase(unit,1,True)   
      t1.remove(unit[0])
    for x in range(2):
      unit = [random.choice(t2),random.choice(items)]
      p1.purchase(unit,2,True)   
      t2.remove(unit[0])
    for x in range(4):
      unit = [random.choice(t3),random.choice(items)]
      p1.purchase(unit,3,True)   
      t3.remove(unit[0])
    for x in range(2):
      unit = [random.choice(t4),random.choice(items)]
      p1.purchase(unit,4,True)   
      t4.remove(unit[0])
  if types == "5":
    for x in range(2):
      unit = [random.choice(t1),random.choice(items)]
      p1.purchase(unit,1,True)   
      t1.remove(unit[0])
    for x in range(2):
      unit = [random.choice(t2),random.choice(items)]
      p1.purchase(unit,2,True)   
      t2.remove(unit[0])
    for x in range(2):
      unit = [random.choice(t3),random.choice(items)]
      p1.purchase(unit,3,True)   
      t3.remove(unit[0])
    for x in range(2):
      unit = [random.choice(t4),random.choice(items)]
      p1.purchase(unit,4,True)   
      t4.remove(unit[0])
    for x in range(2):
      unit = [random.choice(t5),random.choice(items)]
      p1.purchase(unit,5,True)   
      t5.remove(unit[0])
  for x in carousellist:
    if x.RAR == 1:
      print("("+str(carousellist.index(x)+1)+")",x.NAME,"["+x.items[0]+"]")
    elif x.RAR == 2:
      print("("+str(carousellist.index(x)+1)+")",fore.GREEN_1+x.NAME+style.RESET,"["+x.items[0]+"]")
    elif x.RAR == 3:
      print("("+str(carousellist.index(x)+1)+")",fore.DODGER_BLUE_2+x.NAME+style.RESET,"["+x.items[0]+"]")
    elif x.RAR == 4:
      print("("+str(carousellist.index(x)+1)+")",fore.PURPLE_1B + x.NAME+style.RESET,"["+x.items[0]+"]")
    elif x.RAR == 5:
      print("("+str(carousellist.index(x)+1)+")",fore.DARK_ORANGE+x.NAME+style.RESET,"["+x.items[0]+"]")
  choose = 0
  while choose == 0:
    take = input("\nType a number and click enter to obtain a unit: ")
    if take.isdigit() == True:
      if int(take) <= len(carousellist) and int(take) > 0:
        pick = carousellist[int(take)-1]
        p1.team.append(pick)
        carousellist.remove(pick)
        print("\nYou picked",pick.NAME+"!")
        time.sleep(0.5)
        print("Your opponents choose a unit.")
        time.sleep(0.5)
        for x in opponents:
          x.carouselAI(1)
          time.sleep(0.5)
        choose = 1





def arrange(types=""):
  global elapsed
  global start
  bruh = 1
  if types == "Player":
    while elapsed < 60:
      input("\nTime:",round(60-elapsed),"seconds left.\n(1) Move to Team  (2) Move to Reserve  (Enter) Exit\nAction: ")
      char = getch()
      elapsed = time.time() - start
      if elapsed > 60:      
        break  
      if char == "\r":
        break         
      if char == "1":
        if len(p1.backteamS) > 0:
          for x in p1.backteamS:
            if x in tier1:
              print("("+str(bruh)+")",x)
            if x in tier2:
              print("("+str(bruh)+")",fore.GREEN_1+x+style.RESET)
            if x in tier3:
              print("("+str(bruh)+")",fore.DODGER_BLUE_2+x+style.RESET)
            if x in tier4:
              print("("+str(bruh)+")",fore.PURPLE_1B+x+style.RESET)
            if x in tier5:
              print("("+str(bruh)+")",fore.DARK_ORANGE+x+style.RESET)
            bruh = bruh + 1
          bruh = 1
          print("\nTime:",round(60-elapsed),"seconds left.\n(#) Move to team  (Enter) Exit\nAction: ")
          yes = getch()
          elapsed = time.time() - start
          if elapsed > 60:      
            break  
          if yes == "\r":
            break
          if yes.isdigit() == True:
            if int(yes) <= len(p1.backteam) and int(yes) > 0 and (len(p1.team) < p1.Level):
              pers = p1.backteam[int(yes)-1]
              p1.team.append(pers)
              p1.backteam.remove(pers)
              print("\n"+pers.NAME+"is added to the battlefield!")
            elif int(yes) <= len(p1.backteam) and int(yes) > 0 and (len(p1.team) == p1.Level):
              for x in p1.teamS:
                if x in tier1:
                  print("("+str(bruh)+")",x)
                if x in tier2:
                  print("("+str(bruh)+")",fore.GREEN_1+x+style.RESET)
                if x in tier3:
                  print("("+str(bruh)+")",fore.DODGER_BLUE_2+x+style.RESET)
                if x in tier4:
                  print("("+str(bruh)+")",fore.PURPLE_1B+x+style.RESET)
                if x in tier5:
                  print("("+str(bruh)+")",fore.DARK_ORANGE+x+style.RESET)
                bruh = bruh + 1
              bruh = 1
              deez = getch()
              print("\nSomeone must be removed...(#) Move to Reserve  (Enter) Cancel\nAction: ")
              pers = p1.backteam[int(yes)-1]
              p1.team.append(pers)
              p1.backteam.remove(pers)
              print("\n"+pers.NAME+"is added to the battlefield!")
        else:
          print("\nThere are no units in reserve!")
      if char == "2": 
        None

def sell(types=""):
  None

def equip(types=""):
  None

def giveitem(ran):
  if ran[0] == "Amira":
    ran.append(random.choice(fullitems))
  else:
    ran.append(random.choice(items))
  return ran

def mobs(person):
  prep()
  if person == "2 Freshmen": 
    battle(p1,p9)
    for x in opponents:
      battle(x,p9)
  


def pvp():                                   
  None


def game():
  global rnd
  game = True
  rnd = 0
  carousel("Start")
  while game == True:
    rnd = rnd + 1
    for x in play:
      x.teamset("Team")
    if rnd == 1:
      p1.prep("PvP")
    elif rnd == 2:
      for x in play:
        x.Level = 3
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 15
      p1.prep("PvP")
    elif rnd == 3:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 20
      #Map effect 1
      p1.prep("PvP")
    elif rnd == 4:
      carousel("3")
      for x in play:
        x.Level = 4
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 20     
      p1.prep("PvP")
    elif rnd == 5:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 30
      p1.prep("Mrs. Miller")
    elif rnd == 6:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 30
      #2nd map effect
      p1.prep("PvP")
    elif rnd == 7:
      carousel("4")
      for x in play:
        x.Level = 5
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 25
      p1.prep("PvP")
    elif rnd == 8:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 25
      p1.prep("PvP")
    elif rnd == 9:
      for x in play:
        x.Level = 6
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 30
      #3rd map effect
      p1.prep("PvP")
    elif rnd == 10:
      carousel("5")
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 25
      p1.prep("PvP")
    elif rnd == 11:
      for x in play:
        x.Level = 7
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 40
      p1.prep("Mr. Pudup")
    elif rnd == 12:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 30
      #4th map effect
      p1.prep("PvP")
    elif rnd == 13:
      carousel("6")
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 25
      p1.prep("PvP")
    elif rnd == 14:
      for x in play:
        x.Level = 8
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 25
      p1.prep("PvP")
    elif rnd == 15:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 30
      #Final map effect
      p1.prep("PvP")
    elif rnd == 16:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 40
      p1.prep("Dr. Graham")
      for x in play:
        x.Level = 9
    else:
      for x in play:
        x.gold = math.floor(x.gold/2)
        x.gold = x.gold + 25
      p1.prep("PvP")
    
def prebattleevent(pl1,pl2,skip=""):
  peeps = [pl1,pl2]
  for y in peeps:
    for x in y.team:
      if "Anatomy of Hearts" in x.items:
        x.cHP = x.cHP + 150
      if "Flaming Cinders" in x.items:
        x.cHP = x.cHP + 150
      if "Eternal" in x.items:
        x.cHP = x.cHP + 600
      if "Care Package" in x.items:
        x.cHP = x.cHP + 150
      if "Grand" in x.items:
        x.cHP = x.cHP + 150
      if "Devourer" in x.items:
        x.cHP = x.cHP + 150
      if "Cleats" in x.items:
        x.cHP = x.cHP + 150
      if "Pearson Textbook" in x.items:
        x.cHP = x.cHP + 150
        x.destiny = 1
      if "Giancoli Textbook" in x.items:
        x.knowledge = 1
      if "Cross" in x.items:
        x.cross = 1
      if "Uruguayan" in x.SYN:
        x.urug = True
      x.fcMP = x.cMP

  for x in pl1.team:
    peep = []
    if "Obscene Wear" in x.items:
      peep.append(x)
    if len(peep) > 0:
      for y in pl2.team:
        y.taunted = [1,random.choice(peep)]

  if pl1.lea == 1:
    for x in pl1.team:
      x.fcMP = x.fcMP + 50
      if x.fcMP > x.fMP:
        x.fcMP = round(x.fMP)
  if pl1.gam >= 3:
    if pl1.gam >=3 and pl1.gam < 6:
      for x in pl1.team:
        x.cLV = x.cLV + 1
    if pl1.gam >= 6:
      for x in pl1.team:
        if "Gamer" in x.SYN:
          x.cLV = x.cLV + 3
        else:
          x.cLV = x.cLV + 2
  if pl1.wee >=3:
    tot = 0
    web = []
    for x in pl1.team:
      if "Weeb" in x.SYN:
        tot = tot + x.fHP
        web.append(x)    
    for x in web:
      if pl1.wee < 6:
        x.fHP = tot
        x.cHP = round(x.fHP)
        x.weebHP = tot
      elif pl1.wee >=6:
        x.fHP = round(1.2*tot) 
        x.cHP = round(x.fHP)
        x.weebHP = round(1.2*tot) 
  if pl1.vul == 2:
    dead = random.choice(pl2.team)
    dead.poisond = (0.15*dead.fHP)
    dead.posiont = 100
  if pl1.vul == 3:
    dead = random.choice(pl2.team)
    pl1.vultarg = dead
    dead.poisond = (0.3*dead.fHP)
    dead.poisont = 100

  for x in pl2.team:
    peep = []
    if "Obscene Wear" in x.items:
      peep.append(x)
    if len(peep) > 0:
      for y in pl1.team:
        y.taunted = [1,random.choice(peep)]

  if pl2.lea == 1:
    for x in pl2.team:
      x.fcMP = x.fcMP + 50
      if x.fcMP > x.fMP:
        x.fcMP = round(x.fMP)
  if pl2.gam >= 3:
    if pl2.gam >=3 and pl2.gam < 6:
      for x in pl2.team:
        x.cLV = x.cLV + 1
    if pl2.gam >= 6:
      for x in pl2.team:
        if "Gamer" in x.SYN:
          x.cLV = x.cLV + 3
        else:
          x.cLV = x.cLV + 2
  if pl2.wee >=3:
    tot = 0
    web = []
    for x in pl2.team:
      if "Weeb" in x.SYN:
        tot = tot + x.fHP
        web.append(x)
    for x in web:
      if pl2.wee < 6:
        x.fHP = tot
        x.cHP = round(x.fHP)
        x.weebHP = tot
      elif pl2.wee >=6:
        x.fHP = round(1.2*tot) 
        x.cHP = round(x.fHP)
        x.weebHP = round(1.2*tot)
  if pl2.vul == 2:
    dead = random.choice(pl1.team)
    dead.poisond = (0.15*dead.fHP)
    dead.posiont = 100
  if pl2.vul == 3:
    dead = random.choice(pl1.team)
    pl2.vultarg = dead
    dead.poisond = (0.3*dead.fHP)
    dead.poisont = 100


  

def battleevent(pl1,pl2,skip=""):

  #Weeb
  if pl1.wee >= 3:
    peep = []
    for x in pl1.team:
      if "Weeb" in x.SYN:
        peep.append(x)
    great = 0
    for x in peep:
      if x.cHP > great:
        great = x.cHP
    for x in peep:
      x.cHP = great
  if pl2.wee >= 3:
    peep = []
    for x in pl2.team:
      if "Weeb" in x.SYN:
        peep.append(x)
    great = 0
    for x in peep:
      if x.cHP > great:
        great = x.cHP
    for x in peep:
      x.cHP = great

  for x in pl1.team:
    if x.immortal > 0 and x.cHP <=0:
      x.cHP = 1
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)
        print("\n"+x.color+x.NAME+res,"gets back up!")
    if "Free Spirit" in x.SYN:
      ch = random.randint(1,100)
      if pl1.fre >= 2 and pl1.fre < 4:
        if ch <= 25:
          if skip != "Skip":
            x.purge("Cleanse",pl1,pl2)
          else:
            x.purge("Cleanse",pl1,pl2,"Skip")
      if pl1.fre >= 4 and pl1.fre < 8:
        if ch <= 50:
          if skip != "Skip":
            x.purge("Cleanse",pl1,pl2)
          else:
            x.purge("Cleanse",pl1,pl2,"Skip")
      if pl1.fre >= 8:
        if skip != "Skip":
          x.purge("Cleanse",pl1,pl2)
        else:
          x.purge("Cleanse",pl1,pl2,"Skip")
    if "Pearson Textbook" in x.items or "Giancoli Textbook" in x.items:
      if x.destiny == 1 and x.cHP <= 0:
        x.cHP = round(0.75*x.fHP)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.5)
          print("\n"+x.color+x.NAME+res,"is revived by their Pearson Textbook!")
          x.destiny = 0
        if skip != "Skip":
          x.purge("Revival Cleanse",pl1,pl2)
        else:
          x.purge("Revival Cleanse",pl1,pl2,"Skip")
      elif x.knowledge == 1 and x.cHP <= 0:
        x.cHP = round(0.2*x.fHP)
        x.fcMP = round(0.8*x.fMP)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.5)
          print("\n"+x.color+x.NAME+res,"is revived by their Giancoli Textbook!")
          x.knowledge = 0
        if skip != "Skip":
          x.purge("Revival Cleanse",pl1,pl2)
        else:
          x.purge("Revival Cleanse",pl1,pl2,"Skip")
    if x.cHP <= 0 and "Soy" in x.SYN and pl1.soy >= 2:
      low = 1
      pers = ""
      for y in pl1.team:
        if y.cHP/y.fHP < low and y != x and y.cHP > 0:
          low = y.cHP/y.fHP
          pers = y
      if pers != "":
        selfsett = pers.cHP
        if pl1.soy >= 2 and pl1.soy < 4:
          pers.cHP = pers.cHP + round(pers.healmod*0.25*x.fHP)
        elif pl1.soy >= 4:
          pers.cHP = pers.cHP + round(pers.healmod*0.55*x.fHP)
        if pers.cHP > pers.fHP:
          pers.cHP = round(pers.fHP)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.5)
          print("\n"+x.color+x.NAME+res,"gives away their power to",pers.NAME+", healing them for",fore.MEDIUM_SPRING_GREEN+str(pers.cHP-selfsett)+style.RESET,"health! They have",pers.cHP,"health now!")
        if pl1.lea >= 1:
          for z in pl1.team:
            if "Leader" in z.SYN:
              selfsett = z.cHP
              if pl1.soy >= 2 and pl1.soy < 4:
                z.cHP = z.cHP + round(z.healmod*0.125*x.fHP)
              elif pl1.soy >= 4:
                z.cHP = z.cHP + round(z.healmod*0.275*x.fHP)
              if z.cHP > z.fHP:
                z.cHP = round(z.fHP)
              if skip != "Skip":
                res = attr("reset")
                time.sleep(0.5)
                print("\n"+x.color+x.NAME+res,"simps for",z.NAME,"one last time, healing them for",fore.MEDIUM_SPRING_GREEN+str(z.cHP-selfsett)+style.RESET,"health! They have",z.cHP,"health now!")
      

  for x in pl2.team:
    if x.immortal > 0 and x.cHP <=0:
      x.cHP = 1
      if skip != "Skip":
        res = attr("reset")
        time.sleep(0.5)
        print("\n"+x.color+x.NAME+res,"gets back up!")
    if "Free Spirit" in x.SYN:
      ch = random.randint(1,100)
      if pl2.fre >= 2 and pl2.fre < 4:
        if ch <= 25:
          if skip != "Skip":
            x.purge("Cleanse",pl2,pl1)
          else:
            x.purge("Cleanse",pl2,pl1,"Skip")
      if pl2.fre >= 4 and pl2.fre < 8:
        if ch <= 50:
          if skip != "Skip":
            x.purge("Cleanse",pl2,pl1)
          else:
            x.purge("Cleanse",pl2,pl1,"Skip")
      if pl2.fre >= 8:
        if skip != "Skip":
          x.purge("Cleanse",pl2,pl1)
        else:
          x.purge("Cleanse",pl2,pl1,"Skip")
    if "Pearson Textbook" in x.items or "Giancoli Textbook" in x.items:
      if x.destiny == 1 and x.cHP <= 0:
        x.cHP = round(0.75*x.fHP)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.5)
          print("\n"+x.color+x.NAME+res,"is revived by their Pearson Textbook!")
          x.destiny = 0
        if skip != "Skip":
          x.purge("Revival Cleanse",pl2,pl1)
        else:
          x.purge("Revival Cleanse",pl2,pl1,"Skip")
      elif x.knowledge == 1 and x.cHP <= 0:
        x.cHP = round(0.2*x.fHP)
        x.fcMP = round(0.8*x.fMP)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.5)
          print("\n"+x.color+x.NAME+res,"is revived by their Giancoli Textbook!")
          x.knowledge = 0
        if skip != "Skip":
          x.purge("Revival Cleanse",pl2,pl1)
        else:
          x.purge("Revival Cleanse",pl2,pl1,"Skip")
    if x.cHP <= 0 and "Soy" in x.SYN and pl2.soy >= 2:
      low = 1
      pers = ""
      for y in pl2.team:
        if y.cHP/y.fHP < low and y != x and y.cHP > 0:
          low = y.cHP/y.fHP
          pers = y
      if pers != "":
        selfsett = pers.cHP
        if pl2.soy >= 2 and pl2.soy < 4:
          pers.cHP = pers.cHP + round(pers.healmod*0.25*x.fHP)
        elif pl2.soy >= 4:
          pers.cHP = pers.cHP + round(pers.healmod*0.55*x.fHP)
        if pers.cHP > pers.fHP:
          pers.cHP = round(pers.fHP)
        if skip != "Skip":
          res = attr("reset")
          time.sleep(0.5)
          print("\n"+x.color+x.NAME+res,"gives away their power to",pers.NAME+", healing them for",fore.MEDIUM_SPRING_GREEN+str(pers.cHP-selfsett)+style.RESET,"health! They have",pers.cHP,"health now!")
        if pl2.lea >= 1:
          for z in pl2.team:
            if "Leader" in z.SYN:
              selfsett = z.cHP
              if pl2.soy >= 2 and pl2.soy < 4:
                z.cHP = z.cHP + round(pers.healmod*0.125*x.fHP)
              elif pl2.soy >= 4:
                z.cHP = z.cHP + round(pers.healmod*0.275*x.fHP)
              if z.cHP > z.fHP:
                z.cHP = round(z.fHP)
              if skip != "Skip":
                res = attr("reset")
                time.sleep(0.5)
                print("\n"+x.color+x.NAME+res,"simps for",z.NAME,"one last time, healing them for",fore.MEDIUM_SPRING_GREEN+str(z.cHP-selfsett)+style.RESET,"health! They have",z.cHP,"health now!")
    

  for x in pl1.team:
    if "Devourer" in x.items:
      for y in pl2.team:
        if y.cHP <= 0:
          selfsett = x.cHP
          x.cHP = x.cHP + round(x.healmod*0.2*(x.fHP-x.cHP))
          if skip != "Skip":
            res = attr("reset")
            time.sleep(0.5)
            print("\n"+x.color+x.NAME+res,"is fed by the Devourer, healing for",fore.MEDIUM_SPRING_GREEN+str(x.cHP-selfsett)+style.RESET,"health! They have",x.cHP,"health now!")

  for x in pl2.team:
    if "Devourer" in x.items:
      for y in pl1.team:
        if y.cHP <= 0:
          selfsett = x.cHP
          x.cHP = x.cHP + round(x.healmod*0.2*(x.fHP-x.cHP))
          if skip != "Skip":
            res = attr("reset")
            time.sleep(0.5)
            print("\n"+x.color+x.NAME+res,"is fed by the Devourer, healing for",fore.MEDIUM_SPRING_GREEN+str(x.cHP-selfsett)+style.RESET,"health! They have",x.cHP,"health now!")

  
def battle(pl1,pl2,skip=False):
  global allfighters
  global hpdmg
  global ghost
  global turncount
  global play1
  global play2
  victory = 0
  lastat = ""
  turn = ""
  previous = ""
  turnstack = 0
  turncount = 0
  overtime = False
  allfighters = []
  play1 = pl1
  play2 = pl2
  pl1.teamset("Team",pl1,pl2)
  for x in pl1.team:
    print(x.NAME,x.items)
  pl1.synergy(True)
  input("")
  pl2.teamset("Team",pl1,pl2)
  for x in pl2.team:
    print(x.NAME,x.items)
  pl2.synergy(True)
  input("")
  for x in pl1.team:
    allfighters.append(x)
    pl1.teamID.append(x.ID)
  print(pl1.teamID)
  for x in pl2.team:
    allfighters.append(x)
    pl2.teamID.append(x.ID)
  print(pl2.teamID)
  for x in allfighters:
    x.cLV = x.LV
    if skip == True:
      if x in pl1.team: 
        x.purge("Death",pl1,pl2,"Skip")
        x.purge("Map Reset",pl1,pl2,"Skip")
      if x in pl2.team: 
        x.purge("Death",pl2,pl1,"Skip")
        x.purge("Map Reset",pl2,pl1,"Skip")
    else:
      if x in pl1.team: 
        x.purge("Death",pl1,pl2)
        x.purge("Map Reset",pl1,pl2)
      if x in pl2.team: 
        x.purge("Death",pl2,pl1)
        x.purge("Map Reset",pl2,pl1)
  prebattleevent(pl1,pl2)
  while victory == 0:
    if skip == True:
      battleevent(pl1,pl2,"Skip")
    else:
      battleevent(pl1,pl2)
    battlespeed = []
    p1temp = []
    for x in pl1.team:
      p1temp.append(x)
    for x in p1temp:
      if x.cHP <= 0:
        pl1.team.remove(x)
        if x.ID in pl1.teamID:
          pl1.teamID.remove(x.ID)
        if x.NAME in pl1.teamS:
          pl1.teamS.remove(x.NAME)
        pl1.deadteam.append(x)
        pl1.deadteamS.append(x.NAME)
        if skip == True:
          x.purge("Death",pl1,pl2,"Skip")
        else:
          x.purge("Death",pl1,pl2)
    p2temp = []
    for x in pl2.team:
      p2temp.append(x)
    for x in p2temp:
      if x.cHP <= 0:
        pl2.team.remove(x)
        if x.ID in pl2.teamID:
          pl2.teamID.remove(x.ID)
        if x.NAME in pl2.teamS:
          pl2.teamS.remove(x.NAME)
        pl2.deadteam.append(x)
        pl2.deadteamS.append(x.NAME)
        if skip == True:
          x.purge("Death",pl2,pl1,"Skip")
        else:
          x.purge("Death",pl2,pl1)
    if len(pl1.team) >= 1 and len(pl1.teamS) == 0:
      for x in pl2.team:
        if x.sitting[0] == 1: 
          x.sitting[1].cHP = 0
          if skip == False:
            time.sleep(0.5)
            res = attr("reset")
            print("\n"+x.color+x.NAME+res,"slams her ass on",x.sitting[1].color+x.sitting[1].NAME+res+", destroying them!")
    if len(pl2.team) >= 1 and len(pl2.teamS) == 0:
      for x in pl1.team:
        if x.sitting[0] == 1: 
          x.sitting[1].cHP = 0
          if skip == False:
            time.sleep(0.5)
            res = attr("reset")
            print("\n"+x.color+x.NAME+res,"slams her ass on",x.sitting[1].color+x.sitting[1].NAME+res+", destroying them!")
    if len(pl1.team) == 0 or len(pl2.team) == 0:
      break
    for x in pl1.team:
      if skip == True:
        x.globaltimers("Skip")
      else:
        x.globaltimers()
      x.currentstats(pl1,pl2)
    for x in pl2.team:
      if skip == True:
        x.globaltimers("Skip")
      else:
        x.globaltimers()
      x.currentstats(pl2,pl1)    
    for x in allfighters:
      if x in pl1.team or x in pl1.backteam or x in pl1.deadteam:
        if skip == True:
          x.maptimers(pl1,pl2,"Skip")
        else:
          x.maptimers(pl1,pl2)
      if x in pl2.team or x in pl2.backteam or x in pl2.deadteam:
        if skip == True:
          x.maptimers(pl2,pl1,"Skip")
        else:
          x.maptimers(pl2,pl1)
    battlespeed = []   
    for x in pl1.team:
      if x.NAME in pl1.teamS or x.invis > 0:
        for number in range(x.cSP):
          battlespeed.append(x.ID)
    for x in pl2.team:
      if x.NAME in pl2.teamS or x.invis > 0:
        for number in range(x.cSP):
          battlespeed.append(x.ID)
    for x in allfighters:
      if previous != "":
        x.deturn = x.deturn + 1
        if previous == x.ID:
          x.deturn = 0
        news = 0
        news = ((1+(0.5*x.deturn))*battlespeed.count(x.ID))
        newss = round(news-battlespeed.count(x.ID))
        for t in range(newss):
          battlespeed.append(x.ID)
        if previous == x.ID and turnstack == 2:
          turnstack = 0
          x.deturn = -1
          y = battlespeed.count(x.ID)
          for t in range(y):
            battlespeed.remove(x.ID)
    turn = random.choice(battlespeed)
    if turn == previous:
      turnstack = turnstack + 1
    if turn != previous and previous != "":
      turnstack = 0
    previous = turn
    turncount = turncount + 1
    if turncount > len(allfighters)*7.5 and overtime == False and skip == False:
      overtime = True
      print(style.BOLD+fore.YELLOW_1+"\nOVERTIME! (AT AND MAT ICNREASED BY 50%, HEALING REDUCED BY 33%)\n"+style.RESET)
    for x in pl1.team:
      if skip == True:
        if turn == x.ID:
          x.onturntimers("Skip")
          if x.cHP > 0:
            for y in pl1.team:
              y.currentstats(pl1,pl2)
            for y in pl2.team:
              y.currentstats(pl2,pl1)
            x.stuns(pl1,pl2,"Skip")
            x.AIdetector(pl1,pl2,"Skip")
      else:
        if turn == x.ID:
          x.onturntimers(pl1,pl2)
          if x.cHP > 0:
            for y in pl1.team:
              y.currentstats(pl1,pl2)
            for y in pl2.team:
              y.currentstats(pl2,pl1)
            x.stuns(pl1,pl2)
            x.AIdetector(pl1,pl2)
    for x in pl2.team:
      if skip  == True:
        if turn == x.ID:
          x.onturntimers("Skip")
          if x.cHP > 0:
            for y in pl1.team:
              y.currentstats(pl1,pl2)
            for y in pl2.team:
              y.currentstats(pl2,pl1)
            x.stuns(pl2,pl1,"Skip")
            x.AIdetector(pl2,pl1,"Skip")
      else:
        if turn == x.ID:
          x.onturntimers(pl2,pl1)
          if x.cHP > 0:
            for y in pl1.team:
              y.currentstats(pl1,pl2)
            for y in pl2.team:
              y.currentstats(pl2,pl1)
            x.stuns(pl2,pl1)
            x.AIdetector(pl2,pl1)
  if len(pl1.team) == 0 and len(pl2.team) == 0:
    print("Tie!")
  elif len(pl1.team) == 0:
    dmgcalc(pl2)
    pl1.Health = pl1.Health - hpdmg
    if pl1.Health > 0:
      print("\n"+pl2.Name,"defeats",pl1.Name+", dealing",hpdmg,"to them!",pl1.Name,"has",pl1.Health,"health remaining!")
    else:
      print("\n"+pl2.Name,"defeats",pl1.Name+", dealing",hpdmg,"to them!",pl1.Name,"falls...")
  elif len(pl2.team) == 0:
    if ghost == 1:     
      print("\n"+pl1.Name,"defeats the ghost of",pl2.Name+"!")  
    else:
      dmgcalc(pl1)
      pl2.Health = pl2.Health - hpdmg
      if pl2.Health > 0:
        print("\n"+pl1.Name,"defeats",pl2.Name+", dealing",hpdmg,"to them!",pl2.Name,"has",pl2.Health,"health remaining!")
      else:
        print("\n"+pl1.Name,"defeats",pl2.Name+", dealing",hpdmg,"to them!",pl2.Name,"falls...")

def dmgcalc(t):
  global hpdmg
  hpdmg = t.Level
  for x in t.team:
    if x.RAR == 1:
      hpdmg = hpdmg + 1
    elif x.RAR == 2:
      hpdmg = hpdmg + 2
    elif x.RAR == 3:
      hpdmg = hpdmg + 2
    elif x.RAR == 4:
      hpdmg = hpdmg + 3
    elif x.RAR == 5:
      hpdmg = hpdmg + 3
    elif x.RAR == 6:
      hpdmg = hpdmg + 1

def randombattle(pl1,pl2,rand=""):
  peep = [pl1,pl2]
  unit1  = tier1+tier2+tier3+tier4+tier5+tier6
  unit2  = tier1+tier2+tier3+tier4+tier5+tier6
  alt = 0
  if rand == "":
    for x in range(18):
      if alt == 0:
        per = random.choice(unit1)
        unit1.remove(per)
        pl1.purchase(per,5,back=True)
        pers = pl1.team[len(pl1.team)-1]
        pers.setlevel(8)
        pers.color = pl1.colo
        randomitems(pers)
        alt = 1
      elif alt == 1:
        alt = 0
        per = random.choice(unit2)
        unit2.remove(per)
        pl2.purchase(per,5,back=True)
        pers = pl2.team[len(pl2.team)-1]
        pers.setlevel(8)
        pers.color = pl2.colo
        randomitems(pers)
  elif rand == "Abby":
    pl1.purchase("Abby",5,back=True)
    pl1.team[0].items = ["Bloodrazor","Zulfiqar","Anatomy of Hearts","Flow of Wind","Duality","Thotslayer","Rally Banner","Honjo Masamune","Thornmail","Flaming Cinders","The Gambit","Feminism","Obscene Wear","Miller's Hearing Aid","Critical Measure","Eternal","Care Package","Devourer","Cleats","Pearson Textbook","Endiness","Tryhard","Rulebook","Resource Catalyst","Giancoli Textbook","Last Say","Cross","Kahoot","God's Javelin","Bible","Hater Guard","Physics Equation Sheet","Vengeance","Sacred Scythe","Graham's Report"]
    pl1.team[0].setlevel(10000)
    pl1.team[0].color = pl1.colo
    pl1.team[0].SP = 3000
    unit2.remove("Abby")
    for x in range(55):
      per = random.choice(unit2)
      unit2.remove(per)
      pl2.purchase(per,5,back=True)
      pers = pl2.team[len(pl2.team)-1]
      pers.setlevel(8)
      pers.color = pl2.colo
      randomitems(pers)
  elif rand == "Abby 2":
    pl2.purchase("Abby",5,back=True)
    pl2.team[0].items = ["Cleats","Obscene Wear","Sacred Scythe","Devourer"]
    pl2.team[0].setlevel(8)
    pl2.team[0].color = pl2.colo
    pl2.purchase("Siddarth",4,back=True)
    pl2.team[1].items = ["Endiness","Pearson Textbook","Eternal"]
    pl2.team[1].setlevel(8)
    pl2.team[1].color = pl2.colo
    for x in range(9):
      per = random.choice(unit2)
      unit2.remove(per)
      pl1.purchase(per,5,back=True)
      pers = pl1.team[len(pl1.team)-1]
      pers.setlevel(8)
      pers.color = pl1.colo
      randomitems(pers)
  elif rand == "Ishraq":
    pl1.purchase("Ishraq",5,back=True)
    pl1.team[0].items = ["Zulfiqar","Hater Guard","Critical Measure"]
    pl1.team[0].setlevel(8)
    pl1.team[0].color = pl1.colo
    pl1.purchase("Alice",4,back=True)
    pl1.team[1].items = ["Kahoot","Tryhard","Care Package"]
    pl1.team[1].setlevel(8)
    pl1.team[1].color = pl1.colo
    pl2.purchase("Abby",5,back=True)
    pl2.team[0].items = ["Cleats","Obscene Wear","Sacred Scythe"]
    pl2.team[0].setlevel(8)
    pl2.team[0].color = pl2.colo
    pl2.purchase("Siddarth",4,back=True)
    pl2.team[1].items = ["Endiness","Pearson Textbook","Eternal"]
    pl2.team[1].setlevel(8)
    pl2.team[1].color = pl2.colo

    
  battle(pl1,pl2)
  print("\nThere was",len(pl2.team),"surviving members.\n")
  for x in pl2.team:
    print(x.NAME)

def randomitems(pers):
  if pers.NAME == "Amira":
    for x in range(9):
      pers.items.append(random.choice(fullitems))
  else:
    for x in range(3):
      pers.items.append(random.choice(fullitems))

carousellist = []
items = ("Attack","Defense","Magic Defense","Speed","Magic Attack","Health","Mana","Critical")
fullitems = ("Bloodrazor","Zulfiqar","Anatomy of Hearts","Flow of Wind","Duality","Thotslayer","Rally Banner","Honjo Masamune","Thornmail","Flaming Cinders","The Gambit","Feminism","Obscene Wear","Miller's Hearing Aid","Critical Measure","Eternal","Care Package","Devourer","Cleats","Pearson Textbook","Endiness","Tryhard","Rulebook","Resource Catalyst","Giancoli Textbook","Last Say","Cross","Kahoot","God's Javelin","Bible","Hater Guard","Physics Equation Sheet","Vengeance","Sacred Scythe","Graham's Report")
tier1 = ["Jahir","Blandino","Octavio","Erick","Basel","Kholilur","James","Tahsin","Dylan","Siddarth","Andrew","Dereck","Ramirez","Anthony","Handell"]
tier2 = ["Edmond","Amber","Khalil","Hassan","Noah","Alberlyn","Zaid","Shannae","Shah","Jeremy","Matvey","Reema","Brian"]
tier3 = ["Olivia","Jackie","David","Julius","Najely","Taylor","Metin","Jaidah","Kenny","John","Tyasia","Abida","Alvaro"]
tier4 = ["Brandon","Tim","Mohammad","Richard","Ian","Keyur","Nicole","Arwyn","Lascelles","Alice"]
tier5 = ["Kylie","Kelly","Ishraq","Norman","Abby","Daniel"]
tier6 = ["Amira"]

AI = ["Wakim","Waluigi","Xehanort","Himekawa","Belle Delphine","Aizawa","Espinoza","Eldesouky","RJ","Salem","Josh","Ling Ling","Patrick","Flabby"]
#AI = ["Wakim"]
colors = ["red_1","magenta_1","green_1","yellow_1","cyan_1","dodger_blue_1","orange_red_1","green_3a","violet"]


ID = 0
yes = input("\nWhat is your name? ")
print("")
bruh = 0
while bruh == 0:
  for x in colors:
    print(fg(x)+"("+str(colors.index(x)+1)+")")
  color = input(style.RESET+"\nChoose a color: ")
  if color.isdigit() and color != "0": 
    if int(color) <= 9:
      
      bruh = 1
  

p1 = Player(yes,1,color)
randomAI = random.choice(AI)
color = "green_3a"
p2 = Player(randomAI,2,color)
AI.remove(randomAI)
randomAI = random.choice(AI)
color = "magenta_1"
p3 = Player(randomAI,3,color)
AI.remove(randomAI)
randomAI = random.choice(AI)
color = "yellow_1"
p4 = Player(randomAI,4,color)
AI.remove(randomAI)
randomAI = random.choice(AI)
color = "magenta_1"
p5 = Player(randomAI,5,color)
AI.remove(randomAI)
randomAI = random.choice(AI)
p6 = Player(randomAI,6,color)
AI.remove(randomAI)
randomAI = random.choice(AI)
p7 = Player(randomAI,7,color)
AI.remove(randomAI)
randomAI = random.choice(AI)
p8 = Player(randomAI,8,color)

randombattle(p1,p2)
play = [p1,p2,p3,p4,p5,p6,p7]
opponents = [p2,p3,p4,p5,p6,p7]
ghost = 0
game()