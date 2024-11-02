import Person as p
import Scenario as s

class goSchool(s.Scenario):
    pass
    def __init__(self, protag):
        super().__init__("goSchool", "Progression", {"occupation": "student", "health": 7})
        self.addDescription("You walked out of the house and went to school early morning")    
        
        toClass = s.Normal("Go to class", [])
        self.addChoice(toClass)
        skipClass  = s.Normal("skipClass")
        self.addChoice(skipClass)

        print(self.checkCondition(protag))
        self.displayScenario()

    def create(self):
        if (type == "Normal"):
            n1 = s.Choice()