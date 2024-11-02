import Person as p
import Scenario as s

class goSchool(s.Scenario):
    pass
    def __init__(self, protag):
        super().__init__("goSchool", "progression", {"occupation": "student", "health": 7})
        self.addDescription("You walked out of the house and went to school early morning")    
        
        toClass = s.Normal("Go to class", [])
        self.addChoice(toClass)
        skipClass  = s.Normal("skipClass")
        self.addChoice(skipClass)

        print(self.checkCondition(protag))
        self.displayScenario()

    def isClue(self):
        if (type == "progression"):
            return True
        
class oldFriend(s.Scenario):
    pass
    def __init__(self, protag, npc1):
        super().__init__("goSchool", "progression", {"occupation": "student", "health": 7})
        self.addDescription("You ran into " + npc1 + ", an Old Friend while running errands. He called you with excitement!")    
        
        greet = s.Normal("Short Greeting", [])
        self.addChoice(greet)
        self.defineCondition()
        coffee  = s.Normal("Wanna get some coffee?")
        self.addChoice(coffee)
        whenMet = s.Weird("Where we know each other?")
        self.addChoice(whenMet)

        print(self.checkCondition(protag))
        self.displayScenario()

    def isClue(self):
        if (type == "progression"):
            return True
