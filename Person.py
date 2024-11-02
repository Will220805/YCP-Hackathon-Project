import random as r

class Person:
    # added Status, other places not updated
    def __init__(self, name = "Bob Ross", gender = "Male", age = r.randint(1,100), occupation = "unemployed", health = 10, network = [], cautious = 0):
        self.name = name
        self.gender = gender
        self.age = age
        if (occupation != "unemployed" | occupation != "student" | occupation != "employed"):
            self.occupation = "unemployed"
        else:
            self.occupation = occupation
        self.health = health
        self.network = network #list of Network type variables
        self.cautious = cautious
        
    def print(self):
        print("__________________________________")
        print("         ID CARD         ")
        print("Name:  " + self.name)
        print("Age:  " + str(self.age) + "   -   " + "Gender:  " + self.gender)
        print("Occupation Status:  " + self.occupation)
        print("Health Status: " + str(self.health))
        cn = ""
        for connection in self.network:
            cn += connection.person.name + "  "
        print("Network:  " + cn)
        print("__________________________________")
        print()

    
class Network:
    def __init__(self, protag, person, relationship = "aquaintance"):
        self.protag = protag
        self.person = person #Person class
        self.developRltn(relationship)
    
    def developRltn(self, relationship):
        self.relationship = relationship
        self.protag.network.append(self)

    def printNetwork(self):
        print(self.protag.name + " is " + self.relationship + " with " + self.person.name)

