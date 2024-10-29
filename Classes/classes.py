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
    # stat bonus
    self.atkB = 0
    self.defB = 0
    self.spdB = 0

    # actual Stats
    self.atkA = lambda: self.atkB + self.atk
    self.defA = lambda: self.defB + self.df
    self.spdA = lambda: self.spdB + self.spd

    def __init__ (
        self,
        name,
        level,
        hp,
        atk,
        df,
        spd,
        id
    ) :
        self.name = name
        self.level = level
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.id = id

    def Attack(self, x, multiplier = 1):
        x.hp -= (self.atk * multiplier) - (x.df * 0.8)
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
                self.atk += self.atk * statBonus
            else:
                self.atk += statBonus
        elif stat == 1:
            if isPercent:
                self.df += self.df * statBonus
            else:
                self.df += statBonus
        elif stat == 2:
            if isPercent:
                self.spd += self.atk * statBonus
            else:
                self.spd += statBonus
        return self
        

class Player(Unit):
    self.items = []
    self.equipment = []
    self.itemsInEffect = []

    # base stat
    self.atk = lambda: self.level * 1.5 + 5
    self.df = lambda: self.level * 0.75 + 3
    self.spd = lambda: self.level * 1.25 + 4

    def recalculateStatBonus(self):
        pass

    def Item(self, ):
        pass