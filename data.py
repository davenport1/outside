


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
    def modifyIntelligence(currentChar, modifier, effect):
        if effect:
            Buffs.buffIntelligence(currentChar,modifier)
        else:
            Debuffs.debuffIntelligence(currentChar,modifier)
    
    def modifyWisdom(currentChar, modifier, effect):
        if effect:
            Buffs.buffWisdom(currentChar, modifier)
        else: 
            Debuffs.debuffWisdom(currentChar, modifier)
    
    def modifyStrength(currentChar, modifier, effect):
        if effect:
            Buffs.buffStrength(currentChar,modifier)
        else: 
            Debuffs.debuffStrength(currentChar, modifier)
    
    def modifyEndurance(currentChar, modifier, effect):
        if effect:
            Buffs.buffEndurance(currentChar, modifier)
        else:
            Debuffs.debuffEndurance(currentChar, modifier)

    def modifyVitality(currentChar, modifier, effect):
        if effect:
            Buffs.buffVitality(currentChar, modifier)
        else:
            Debuffs.debuffVitality(currentChar, modifier)
    def modifyCharm(currentChar, modifier, effect):
        if effect:
            Buffs.buffCharm(currentChar, modifier)
        else:
            Debuffs.debuffCharm(currentChar, modifier)

class Buffs(Modifiers):
    def buffIntelligence(currentChar,modifier):
        oldIntel = currentChar.getIntelligence()
        newIntel = oldIntel + (oldIntel * modifier)
        currentChar.setIntelligence(newIntel)

    def buffWisdom(currentChar, modifier):
        oldWis = currentChar.getWisdom()
        newWis = oldWis + (oldWis * modifier)
        currentChar.setWisdom(newWis)
    
    def buffStrength(currentChar, modifier):
        oldStr = currentChar.getStrength()
        newStr = oldStr + (oldStr * modifier)
        currentChar.setStrength(newStr)

    def buffEndurance(currentChar, modifier):
        oldEnd = currentChar.getEndurance()
        newEnd = oldEnd + (oldEnd * modifier)
        currentChar.setEndurance(newEnd)

    def buffVitality(currentChar, modifier):
        oldVit = currentChar.getVitality()
        newVit = oldVit + (oldVit * modifier)
        currentChar.setVitality(newVit)

    def buffCharm(currentChar, modifier):
        oldCha = currentChar.getCharm()
        newCha = oldCha + (oldCha * modifier)
        currentChar.setCharm(newCha)
    
class Debuffs(Modifiers):
    def debuffIntelligence(currentChar, modifier):
        oldIntel = currentChar.getIntelligence()
        newIntel = oldIntel - (oldIntel * modifier)
        currentChar.setIntelligence(newIntel)

    def debuffWisdom(currentChar, modifier):
        oldWis = currentChar.getWisdom()
        newWis = oldWis - (oldWis * modifier)
        currentChar.setWisdom(newWis)

    def debuffStrength(currentChar, modifier):
        oldStr = currentChar.getStrength()
        newStr = oldStr - (oldStr * modifier)
        currentChar.setStrength(newStr)

    def debuffEndurance(currentChar, modifier):
        oldEnd = currentChar.getEndurance()
        newEnd = oldEnd - (oldEnd * modifier)
        currentChar.setEndurance(newEnd)

    def debuffVitality(currentChar, modifier):
        oldVit = currentChar.getVitality()
        newVit = oldVit - (oldVit * modifier)
        currentChar.setVitality(newVit)

    def debuffCharm(currentChar, modifier):
        oldCha = currentChar.getCharm()
        newCha = oldCha - (oldCha * modifier)
        currentChar.setCharm(newCha)
    
