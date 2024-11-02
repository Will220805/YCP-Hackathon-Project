import Person as p

class Scenario:
    def __init__(self, name,type = "Normal", conditions = {}):
        self.name = name
        self.type = type
        self.choices = []
        self.description = ""
        self.chsnChoice = None
        self.conditions = conditions
        self.next = None
        if (self.chsnChoice != None):
            self.next = self.chsnChoice.outcome.next
        

    def print(self):
        for choice in self.choices:
            print(choice)
    
    def addChoice(self, choice):
        self.choices.append(choice)

    def addDescription(self, description):
        self.description = description

    def chooseChoice(self, choice):
        self.chsnChoice = choice
    
    def checkCondition(self, protag):
        for condition in self.conditions.keys():
            if (condition == "occupation"):
                if (self.conditions[condition] != protag.occupation):
                    return False
            if (condition== "health"):
                if (self.conditions[condition] != protag.health):
                    return False
            if (condition== "health"):
                if (self.conditions[condition] != protag.health):
                    return False
        return True
    
    def displayScenario(self):
        print("Name:  " + self.name)
        print("Type:  " + self.type)
        print("Description:  " + self.description)
        conds = ""
        for condition in self.conditions.keys():
            conds += condition + " -- " + str(self.conditions[condition]) + "  &  "
        print("Conditions:  " + conds)
        for choice in self.choices:
            choice.print()
        if (self.chsnChoice != None):
            print("Chosen Choice:  " + self.chsnChoice.name)


class Choice:
    def __init__(self, name, outcome = {}, conditions = {}):
        self.outcome = outcome
        self.name = name
        self.conditions = conditions
    
    def defineCondition(self, attribute, value):
        self.conditions[attribute] = value

    def print(self):
        print(self.name)
    
    def addOutcome(self, outcome):
        self.outcome = outcome

class Weird(Choice):
    pass
class Normal(Choice):
    pass
        
class Outcome:
    def __init__(self, outcome = {}):
        self.outcome = outcome
        self.next = None
    
    def setOutcome(self,attribute, value):
        self.outcome[attribute] = value
    
    def adjustAttributes(self, protag):
        for outcome in self.outcome.keys():
            if (outcome == "age"):
                protag.age == self.outcome[outcome]
            if (outcome == "occupation"):
                protag.occupation == self.outcome[outcome]
            if (outcome == "health"):
                protag.health == self.outcome[outcome]
            if (outcome == "energy"):
                protag.energy == self.outcome[outcome]

    def setNextScenario(self, next):
        self.next = next # Scenario class