class Chess(object):
    def __init__(self, name, HP, MP, ATK, MATK, DEF, MDEF, MS, AD):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.ATK = ATK
        self.MATK = MATK
        self.DEF = DEF
        self.MDEF = MDEF
        self.MS = MS
        self.AD = AD
        self.AT = ''

    def getName(self):
        return self.name

    def toString(self):
        print(self.name, self.HP, self.MP, self.ATK, self.MATK, self.DEF, self.MDEF, self.MS, self.AD, end=" ")

class Poppy(Chess):
    def __init__(self):
        super().__init__('Poppy',100,20,40,20,50,50,1,1)

    def skill(self):
        return '丟盾牌'

    def getName(self):
        return super().getName()

    def toString(self):
        super().toString()

class Ziggs(Chess):
    def __init__(self):
        super().__init__('Ziggs',80,20,40,20,20,50,0.8,4)

    def skill(self):
        return '丟炸彈'

    def getName(self):
        return super().getName()

    def toString(self):
        super().toString()