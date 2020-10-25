


class Character:
    intelligence = 0
    wisdom = 0
    strength = 0
    endurance = 0
    vitality = 0
    charm = 0

    def getIntell():
        return intelligence
    def getWisdom():
        return wisdom
    def getStrength():
        return strength
    def getEndurance():
        return endurance
    def getVitality():
        return vitality
    def getCharm():
        return charm
    
    def setIntelligence(intel):
        intelligence = intel
    def setWisdom(wis):
        wisdom = wis
    def setStength(str):
        strength = str
    def setEndurance(end):
        endurance = end
    def setVitality(vit):
        vitality = vit
    def setCharm(ch):
        charm = ch

class Modifiers:
    variable = 0

class Buffs(Modifiers):
    variable = 0

class Debuffs(Modifiers):
    variable = 0
