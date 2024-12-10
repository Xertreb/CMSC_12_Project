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
        id,
    ) :
        self.name = name
        self.level = level
        self.maxhp = maxhp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.id = id 
        self.wave = 0
        
        # stat bonus
        self.atkB = 0
        self.defB = 0
        self.spdB = 0

        # actual Stats
        self.atkA = lambda: self.atkB + self.atk(self.level(self.wave))
        self.defA = lambda: self.defB + self.df(self.level(self.wave))
        self.spdA = lambda: self.spdB + self.spd(self.level(self.wave))


    def SetWave (self, wave):
        self.wave = wave
        self.hp = self.maxhp(self.level(self.wave))

    def Attack(self, x, multiplier = 1):
        dmg = round(((self.atkA() * multiplier) - (x.defA() * 0.8) + 1)*10)/10
        if dmg <= 0:
            dmg = 0
        x.hp -= dmg
        x.hp = round(x.hp*10)/10
        return self.name + " dealt " + str(dmg) +  " damage to " + x.name+"."        
    
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
        self.maxhp = lambda: round(10*(1.06**(self.level+1))+0.5*self.level+8)
        self.hp = self.maxhp()
        self.atk = lambda: round(3*(1.05**(self.level-1)) + 0.2*self.level+2)
        self.df = lambda: round(3*((1.02)**(self.level-1))+0.05*self.level+1)
        self.spd = lambda: round(4.5*((1.06)**self.level) + 0.7*self.level + 5)
        self.exp = 0
        self.expCap = lambda: round((1.01)**self.level+ 5* self.level - 1)
               
        # stat bonus
        self.atkB = 0
        self.defB = 0
        self.spdB = 0

        # actual Stats
        self.atkA = lambda: self.atkB + self.atk()
        self.defA = lambda: self.defB + self.df()
        self.spdA = lambda: self.spdB + self.spd()

    def Attack(self, x, category, diff = 0):
        diffBonus = [1, 1.3, 1.5]
        multiplier = diffBonus[diff]

        if func.askQuestion(category, diff):
            dmg = round(((self.atkA() * multiplier) - (x.defA() * 0.8) + 1)*10)/10
            if dmg <= 0:
                dmg = 0
            x.hp -= dmg
            x.hp = round(x.hp*10)/10
            
            return "Success! "+ self.name + " dealt " + str(dmg) + " damage to " + x.name+"."
        else:
            dmg = round(((self.atkA()*0.5) - x.defA() * 0.8 + 1)*10)/10
            if dmg <= 0:
                dmg = 0
            x.hp -= dmg
            x.hp = round(x.hp*10)/10
            return "Blunder! "+ self.name + " dealt " + str(dmg) + " damage to " + x.name+"."
    
    def GainXP(self, exp):
        self.exp += exp
        #print(self.expCap(), self.exp, self.expCap()>=self.exp)
        st = ""
        while self.expCap() <= self.exp:
            self.exp -= self.expCap()
            self.level += 1
            self.hp = self.maxhp()
            
            st += self.name + " leveled up!\n"

            r = []
            r.append(["Max HP", self.maxhp()])
            r.append(["ATK", self.atk()])
            r.append(["DEF", self.df()])
            r.append(["SPD", self.spd()])
            st += func.TableDisplay(r, [-1,-1], border = " ")
        st += str(self.expCap() - self.exp) + " until next level up."

        return st


    def Heal(self, category ,diff):
        diffHeal = [0.1, 0.20, 0.3]

        if func.askQuestion(category, diff):
            heal = self.maxhp() * diffHeal[diff]
            if heal + self.hp > self.maxhp():
                heal = self.maxhp() - self.hp
            heal = round(heal*10)/10
            self.hp += heal
            return self.name + " healed for " + str(heal) + " HP!"
        else:
            heal = self.maxhp() * 0.05
            if heal + self.hp > self.maxhp():
                heal = self.maxhp() - self.hp
            heal = round(heal*10)/10
            self.hp += heal
            return self.name + " healed for " + str(heal) + " HP!"
