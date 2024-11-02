import Person as p
import Scenario as s
import scenarioLib as lib

if __name__ == '__main__':
    # Test Person class
    protag = p.Person("Keanu Reaves", "Male", 43, 1,7)
    protag.print()
    
    npc1 = p.Person("Person One", "Male", 3, 1)
    nw = p.Network(protag, npc1, "friends")
    nw.printNetwork()
    protag.print()

    #Test Scenario matching
    # goSchool = s.Scenario("goSchool", "Progression", {"occupation": "student", "health": 7})
    # goSchool.addDescription("You walked out of the house and went to school early morning")
    
    # toClass = s.Choice("Go to class")
    # goSchool.addChoice(toClass)
    # skipClass  = s.Choice("skipClass")
    # goSchool.addChoice(skipClass)
    # print(goSchool.checkCondition(protag))
    # goSchool.displayScenario()
    goSchool = lib.goSchool(protag)
    goSchool.chooseChoice(s.Choice("Go to class"))
    goSchool.displayScenario()
