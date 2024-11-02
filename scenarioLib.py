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

        
class oldFriend(s.Scenario):
    pass
    def __init__(self, protag, npc1):
        super().__init__("oldFriend", "progression", {"energy": 2, "network": None})
        self.addDescription("You ran into " + npc1.name + ", an Old Friend while running errands. He called you with excitement!")    
        
        greet = s.Choice("Short Greeting", [])
        self.addChoice(greet)

        coffee  = s.Choice("Wanna get some coffee?")
        cOut = s.Outcome({"energy": 4})
        cOut.setNextScenario("goSchool")
        coffee.addOutcome(cOut)
        self.addChoice(coffee)

        whenMet = s.Choice("Where we know each other?")
        wOut = s.Outcome({"network": p.Network(protag, npc1, "old friend"), "health": 3})
        wOut.setNextScenario("goSchool")
        whenMet.addOutcome(wOut)
        self.addChoice(whenMet)

        print(self.checkCondition(protag))
        self.displayScenario()


