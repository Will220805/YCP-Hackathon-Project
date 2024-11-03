import streamlit as st
import Person as p
import Scenario as s
import time
import inkle
import random as r

class RelationshipGame:
    def __init__(self):
        self.doubt_meter = 2  # Starting at 1 for the obvious scenario
        self.game_running = True
        self.scenario_count = 0
        self.neutral_scenarios = [1, 2, 3, 4, 5]
        self.subtle_scenarios = [1, 2, 3, 4, 5]
        self.obvious_scenarios = [1, 2, 3, 4, 5]

    def writeSth(self):
        st.write("SOMETHING!")

    def start_game(self):
        st.write("Welcome to 'Signs of the Relationship'!")
        st.write("You've been dating your partner for six months, but recently you've noticed a few unsettling things.")
        st.write("Throughout this game, you'll experience different situations and make choices that affect your doubt level.")
        st.write("Let's see how your relationship unfolds...\n")
        self.relationship_scenarios()

    def relationship_scenarios(self):
        while self.game_running and self.scenario_count < 20:
            sNum = r.randint(1,3)
            if self.doubt_meter <= 0:
                if (sNum in self.obvious_scenarios):
                    self.scenario_count += 1
                    if (sNum == 1):
                        self.obvious_scenario1()
                        self.obvious_scenarios.remove(sNum)
                    elif (sNum == 2):
                        self.obvious_scenario2()
                        self.obvious_scenarios.remove(sNum)
                    elif (sNum == 3):
                        self.obvious_scenario3()
                        self.obvious_scenarios.remove(sNum)
                else:
                    st.write(f"\nYou ran out of same scenarios. Your final Doubt Meter level is: {self.doubt_meter}")
                    self.end_game()
                    return 0
            elif self.doubt_meter >= 4:
                if (sNum in self.subtle_scenarios):
                    self.scenario_count += 1
                    if (sNum == 1):
                        self.subtle_scenario1()
                        self.subtle_scenarios.remove(sNum)
                    elif (sNum == 2):
                        self.subtle_scenario2()
                        self.subtle_scenarios.remove(sNum)
                    elif (sNum == 3):
                        self.subtle_scenario3()
                        self.subtle_scenarios.remove(sNum)
                else:
                    st.write(f"\nYou ran out of same scenarios. Your final Doubt Meter level is: {self.doubt_meter}")
                    self.end_game()
                    return 0
            else:
                if (sNum in self.neutral_scenarios):
                    self.scenario_count += 1
                    if (sNum == 1):
                        self.neutral_scenario1()
                        self.neutral_scenarios.remove(sNum)
                    elif (sNum == 2):
                        self.neutral_scenario2()
                        self.neutral_scenarios.remove(sNum)
                    elif (sNum == 3):
                        self.neutral_scenario3()
                        self.neutral_scenarios.remove(sNum)
                else:
                    st.write(f"\nYou ran out of same scenarios. Your final Doubt Meter level is: {self.doubt_meter}")
                    self.end_game()
                    return 0

        st.write(f"\nYour final Doubt Meter level is: {self.doubt_meter}")
        self.end_game()
        return 0

    def obvious_scenario1(self):
        # An obvious red flag scenario if doubt is low
        st.write(f"\nScenario {self.scenario_count}: Your partner checks your phone without asking.")
        st.write("They say they're just 'making sure' you're being honest.")
        st.write("1. Ask them to respect your privacy\n2. Allow it, hoping it reassures them\n3. Confront them and express discomfort")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You ask them to respect your privacy, but they brush it off.")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("You let them check, feeling uneasy but hoping it calms their fears.")
            self.doubt_meter -= 1
        elif choice == "3":
            st.write("You express discomfort, and they respond with defensiveness.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def obvious_scenario2(self):
        # An obvious red flag scenario if doubt is low
        st.write(f"\nScenario {self.scenario_count}: Your partner checks your phone without asking.")
        st.write("They say they're just 'making sure' you're being honest.")
        st.write("1. Ask them to respect your privacy\n2. Allow it, hoping it reassures them\n3. Confront them and express discomfort")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You ask them to respect your privacy, but they brush it off.")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("You let them check, feeling uneasy but hoping it calms their fears.")
            self.doubt_meter -= 1
        elif choice == "3":
            st.write("You express discomfort, and they respond with defensiveness.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def obvious_scenario3(self):
        # An obvious red flag scenario if doubt is low
        st.write(f"\nScenario {self.scenario_count}: Your partner checks your phone without asking.")
        st.write("They say they're just 'making sure' you're being honest.")
        st.write("1. Ask them to respect your privacy\n2. Allow it, hoping it reassures them\n3. Confront them and express discomfort")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You ask them to respect your privacy, but they brush it off.")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("You let them check, feeling uneasy but hoping it calms their fears.")
            self.doubt_meter -= 1
        elif choice == "3":
            st.write("You express discomfort, and they respond with defensiveness.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def subtle_scenario1(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: Your partner keeps jokingly putting you down in front of friends.")
        st.write("They laugh it off, but you feel a bit embarrassed.")
        st.write("1. Laugh along with them\n2. Ask them to ease up on the jokes\n3. Confront them privately about how it makes you feel")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You laugh along, hoping it’s harmless. They keep doing it throughout the night.")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("You ask them to ease up, and they act surprised, saying you’re ‘too sensitive.’")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("You confront them about it privately, and they seem taken aback, saying they didn't mean harm.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    
    def subtle_scenario2(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: Your partner keeps jokingly putting you down in front of friends.")
        st.write("They laugh it off, but you feel a bit embarrassed.")
        st.write("1. Laugh along with them\n2. Ask them to ease up on the jokes\n3. Confront them privately about how it makes you feel")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You laugh along, hoping it’s harmless. They keep doing it throughout the night.")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("You ask them to ease up, and they act surprised, saying you’re ‘too sensitive.’")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("You confront them about it privately, and they seem taken aback, saying they didn't mean harm.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    
    def subtle_scenario3(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: Your partner keeps jokingly putting you down in front of friends.")
        st.write("They laugh it off, but you feel a bit embarrassed.")
        st.write("1. Laugh along with them\n2. Ask them to ease up on the jokes\n3. Confront them privately about how it makes you feel")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You laugh along, hoping it’s harmless. They keep doing it throughout the night.")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("You ask them to ease up, and they act surprised, saying you’re ‘too sensitive.’")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("You confront them about it privately, and they seem taken aback, saying they didn't mean harm.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def neutral_scenario1(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
        st.write("They imply that you'd be more interesting if you had a higher-paying job.")
        st.write("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You ignore it, but the comment lingers in your mind.")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("You defend your career, but they dismiss your response, saying it's ‘just their opinion.’")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("You stay silent.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def neutral_scenario2(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
        st.write("They imply that you'd be more interesting if you had a higher-paying job.")
        st.write("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You ignore it, but the comment lingers in your mind.")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("You defend your career, but they dismiss your response, saying it's ‘just their opinion.’")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("You stay silent.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    
    def neutral_scenario3(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
        st.write("They imply that you'd be more interesting if you had a higher-paying job.")
        st.write("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You ignore it, but the comment lingers in your mind.")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("You defend your career, but they dismiss your response, saying it's ‘just their opinion.’")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("You stay silent.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def end_game(self):
        st.write("\nThank you for playing 'Signs of the Relationship.'")
        st.write("We hope this experience helped you recognize the importance of healthy relationship dynamics.")
        self.game_running = False


# Start the game

if st.button("Start Game"):
    game = RelationshipGame()
    game.start_game()
    game.writeSth()
if st.button("Instructions"):
    st.write("Instructions:  ")
