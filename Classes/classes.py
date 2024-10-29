import sys
sys.path.insert(0, './')

import functions as func

class Save:
    def __init__ (self, username, level, wave, items, equipment, difficulty):
        self.username = username
        self.level = level
        self.wave = wave
        self.items = items
        self.equipment = equipment
        self.difficulty = difficulty

    def NewSave(self):
        self.username = input("Enter Player Name: ")
        self.level = 1
        self.wave = 1
        self.items = []
        self.equipment = []
        self.difficulty = 1

        return self

class Unit:
    def __init__ (
        self,
        name,
        level,
        maxhp,
        atk,
        df,
        spd,
        id
    ) :
        self.name = name
        self.level = level
        self.maxhp = maxhp
        self.hp = maxhp
        self.atk = lambda: 5
        self.df = lambda: 3
        self.spd = lambda: 3
        self.id = id 
        
        # stat bonus
        self.atkB = 0
        self.defB = 0
        self.spdB = 0

        # actual Stats
        self.atkA = lambda: self.atkB + self.atk()
        self.defA = lambda: self.defB + self.df()
        self.spdA = lambda: self.spdB + self.spd()

    def Attack(self, x, multiplier = 1):
        x.hp -= (self.atkA() * multiplier) - (x.defA() * 0.8) + 1
        print(self.name, "dealt", str((self.atkA() * multiplier) - (x.defA() * 0.8) + 1), "damage to " + x.name+".", sep = " ")
        return self
    
    def Heal(self, hpHealed, isPercent):
        if isPercent:
            self.hp += self.hp * hpHealed
        else:
            self.hp += hpHealed
        return self
    
    def Buff(self, stat, statBonus, isPercent):
        if stat == 0:
            if isPercent:
                self.atkB += self.atk() * statBonus
            else:
                self.atkB += statBonus
        elif stat == 1:
            if isPercent:
                self.defB += self.defA()() * statBonus
            else:
                self.defB += statBonus
        elif stat == 2:
            if isPercent:
                self.spdB += self.spd() * statBonus
            else:
                self.spdB += statBonus
        return self

class Player(Unit):
    def __init__ (self, name, level):
        self.name = name
        self.level = level
        self.maxhp = lambda: round(self.level * 2.5 + 7.5)
        self.hp = self.maxhp()
        self.atk = lambda: round(self.level * 1.5 + 5)
        self.df = lambda: round(self.level * 0.75 + 3)
        self.spd = lambda: round(self.level * 1.25 + 4)
        
        self.items = []
        self.equipment = []
        self.itemsInEffect = []
        
        # stat bonus
        self.atkB = 0
        self.defB = 0
        self.spdB = 0

        # actual Stats
        self.atkA = lambda: self.atkB + self.atk()
        self.defA = lambda: self.defB + self.df()
        self.spdA = lambda: self.spdB + self.spd()

    # base stat

    def recalculateStatBonus(self):
        pass

    def Item(self):
        pass

    def Attack(self, x, category, multiplier = 1):
        if func.askQuestion(category):
            x.hp -= (self.atkA() * multiplier) - (x.defA() * 0.8) + 1
            print(self.name, "dealt", str((self.atkA() * multiplier) - (x.defA() * 0.8) + 1), "damage to " + x.name+".", sep = " ")
        else:
            x.hp -= (self.atkA()*0.5) - x.defA() * 0.8 + 1
            print(self.name, "dealt", str((self.atkA()*0.5) - x.defA() * 0.8 + 1), "damage to " + x.name+".", sep = " ")
        

class Boss(Unit):
    def Summon(EntityList):
        pass