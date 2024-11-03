import streamlit as st
import Person as p
import Scenario as s
import time
import random as r

if 'page' not in st.session_state:
    st.session_state.page = 'menu'
if 'score' not in st.session_state:
    st.session_state.score = 0

def go_to_page(page_name):
    st.session_state.page = page_name

def reset_game():
    st.session_state.page = 'menu'
    st.session_state.score = 0

class RelationshipGame:
    def __init__(self):
        self.doubt_meter = 2  # Starting at 1 for the obvious scenario
        self.game_running = True
        self.scenario_count = 0
        self.neutral_scenarios = [1, 2, 3, 4, 5]
        self.subtle_scenarios = [1, 2, 3, 4, 5]
        self.obvious_scenarios = [1, 2, 3, 4, 5]

    def start_game(self):
        st.write("Welcome to 'Signs of the Relationship'!")
        st.write("You've been dating your partner for six months, but recently you've noticed a few unsettling things.")
        st.write("Throughout this game, you'll experience different situations and make choices that affect your doubt level.")
        st.write("Let's see how your relationship unfolds...\n")
        self.relationship_scenarios()

    def relationship_scenarios(self):
        while self.game_running and self.scenario_count < 20:
            sNum = 1    # r.randint(1,3)
            if self.doubt_meter <= 0:
                if (sNum in self.obvious_scenarios):
                    self.scenario_count += 1
                    st.session_state.page = "scenario" + str(self.scenario_count)
                    print("scenario:  " + self.scenario_count)
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
                    st.session_state.page = "scenario" + str(self.scenario_count)
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
                    print("scene count:    " + str(self.scenario_count))
                    self.scenario_count += 1
                    st.session_state.page = "scenario" + "5"
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
        
        st.session_state.page = 'ending'

        st.write(f"\nYour final Doubt Meter level is: {self.doubt_meter}")
        self.end_game()
        return 0

    def neutral_scenario1(self):
        if st.session_state.page == "scenario" + "5":
            st.title = "SCENARIO" + str(self.scenario_count)
            # Same level of obviousness if doubt meter hasn't changed
            
            st.write(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
            st.write("They imply that you'd be more interesting if you had a higher-paying job.")
            # st.write("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

            st.write("What will you do?")

            button1 = st.button("Ignore the comment")
            button2 = st.button("Defend your career choice")
            button3 = st.button("Ask why they feel this way")
            c = False
            while (c == False):
                if button1:
                    self.doubt_meter -= 0
                elif button2:
                    self.doubt_meter += 1
                elif button3:
                    self.doubt_meter -= 1
                    print("Where are you??")
                    st.write("Where are you??")
                    c = True
                # elif st.button("Ask why", key="choice4"):
                #     self.doubt_meter -= 1
                #     print("Where ??")
                #     st.write("Where ??")
                #     st.session_state.page = 'question_2.2'
                #     c = True
                print(self.doubt_meter)
            
    # if st.session_state.page == 'question_2.2':
    #     # An obvious red flag scenario if doubt is low
    #     st.write(f"\nScenario {__init__.scenario_count}: Your partner checks your phone without asking.")
    #     st.write("They say they're just 'making sure' you're being honest.")

    #     st.write("What will you do?")
    #     button1 = st.empty()
    #     button2 = st.empty()
    #     button3 = st.empty()

    #     if button1.button("Ask them to respect your privacy"):
    #         st.write("You ask them to respect your privacy, but they brush it off.")
    #         __init__.doubt_meter += 0            
    #     if button2.button("Allow it, hoping it reassures them"):
    #         st.write("You let them check, feeling uneasy but hoping it calms their fears.")
    #         __init__.doubt_meter -= 1
    #     if button3.button.button("Confront them and express discomfort"):
    #         st.write("You express discomfort, and they respond with defensiveness.")
    #         __init__.doubt_meter += 1
    
    # def obvious_scenario1(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)

    #         # An obvious red flag scenario if doubt is low
    #         st.write(f"\nScenario {self.scenario_count}: Your partner checks your phone without asking.")
    #         st.write("They say they're just 'making sure' you're being honest.")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Ask them to respect your privacy"):
    #             st.write("You ask them to respect your privacy, but they brush it off.")
    #             self.doubt_meter += 0
    #         if button2.button("Allow it, hoping it reassures them"):
    #             st.write("You let them check, feeling uneasy but hoping it calms their fears.")
    #             self.doubt_meter -= 1
    #         if button3.button.button("Confront them and express discomfort"):
    #             st.write("You express discomfort, and they respond with defensiveness.")
    #             self.doubt_meter += 1
            

    # def obvious_scenario2(self):
    #     # An obvious red flag scenario if doubt is low
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)

    #         st.write(f"\nScenario {self.scenario_count}: Arguement.")
    #         st.write(" During an argument, your partner loses control and throws something across the room, narrowly missing you.")
    #         # st.write("n1. Calmly ask to take a break and revisit the conversation later.\n2. Apologize and try to calm them down, blaming yourself.\n3. Leave the room immediately to protect yourself and avoid further escalation. ")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Calmly ask to take a break and revisit the conversation later..."):
    #             self.doubt_meter += 0
    #         if button2.button("Apologize and try to calm them down, blaming yourself."):
    #             self.doubt_meter -= 1
    #         if button3.button("Leave the room immediately to protect yourself and avoid further escalation."):
    #             self.doubt_meter += 1

    # def obvious_scenario3(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # An obvious red flag scenario if doubt is low
    #         st.write(f"\nScenario {self.scenario_count}: You mention wanting to visit family over the weekend, and your partner becomes furious.")
    #         st.write("saying, “If you leave, don’t bother coming back. You don’t get to just do whatever you want without thinking about me")
    #         # st.write("n1. Suggest a compromise, like visiting family for part of the weekend and spending the rest of the time with them.\n2. Agree to stay home to avoid their anger and make them feel more secure\n3. Calmly tell them that their reaction is unfair ")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Compromise, visit family for part of the weekend and spend the rest of the time with them."):
    #             self.doubt_meter += 0
    #         if button2.button("Agree to stay home to avoid their anger and make them feel more secure"):
    #             self.doubt_meter -= 1
    #         if button3.button("Calmly tell them that their reaction is unfair"):
    #             self.doubt_meter += 1

    # def obvious_scenario4(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # An obvious red flag scenario if doubt is low
    #         st.write(f"\nScenario {self.scenario_count}: Your partner demands access to your bank account, saying, “We need to share everything if this relationship is going to work.")
    #         st.write("I don’t trust you unless I can see where your money is going.")
    #         # st.write("n1. Agree to discuss your spending and big purchases together without sharing full access.\n2.Reluctantly agree to share your bank account information, even if it makes you uncomfortable.\n3. Firmly refuse, explaining that financial independence is important to you. ")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Agree to discuss your spending and big purchases together without sharing full access."):
    #             self.doubt_meter += 0
    #         if button2.button("Reluctantly agree to share your bank account information, even if it makes you uncomfortable."):
    #             self.doubt_meter -= 1
    #         if button3.button("Firmly refuse, explaining that financial independence is important to you."):
    #             self.doubt_meter += 1

    # def obvious_scenario5(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # An obvious red flag scenario if doubt is low
    #         st.write(f"\nScenario {self.scenario_count}: You’re at a social gathering, and your partner makes an embarrassing comment about you in front of others")
    #         st.write("then laughs and says, “I’m just kidding!")
    #         # st.write("n1. Give a slight smile and change the subject, not giving their comment much energy.\n2.Laugh along to keep the peace, even though it hurts.\n3. Firmly refuse, explaining that financial independence is important to you. ")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Give a slight smile and change the subject"):
    #             self.doubt_meter += 0
    #         if button2.button("ouble down and make fun of yourself."):
    #             self.doubt_meter -= 1
    #         if button3.button("Pull them aside afterward and explain that their comment hurt you."):
    #             self.doubt_meter += 1

    # def subtle_scenario1(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # A subtle red flag scenario if doubt is moderate
    #         st.write(f"\nScenario {self.scenario_count}: Your partner keeps jokingly putting you down in front of friends.")
    #         st.write("They laugh it off, but you feel a bit embarrassed.")
    #         # st.write("1. Laugh along with them\n2. Ask them to ease up on the jokes\n3. Confront them privately about how it makes you feel")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Laugh along with them"):
    #             self.doubt_meter -= 1
    #         if button2.button("Ask them to ease up on the joke"):
    #             self.doubt_meter += 0
    #         if button3.button("Confront them privately about how it makes you feel"):
    #             self.doubt_meter += 1

    
    # def subtle_scenario2(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # A subtle red flag scenario if doubt is moderate
    #         st.write(f"\nScenario {self.scenario_count}: Your partner keeps jokingly putting you down in front of friends.")
    #         st.write("They laugh it off, but you feel a bit embarrassed.")
    #         # st.write("1. Laugh along with them\n2. Ask them to ease up on the jokes\n3. Confront them privately about how it makes you feel")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Laugh along with them"):
    #             self.doubt_meter -= 1
    #         if button2.button("Ask them to ease up on the joke"):
    #             self.doubt_meter += 0
    #         if button3.button("Confront them privately about how it makes you feel"):
    #             self.doubt_meter += 1
    
    # def subtle_scenario3(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # A subtle red flag scenario if doubt is moderate
    #         st.write(f"\nScenario {self.scenario_count}: Your partner keeps jokingly putting you down in front of friends.")
    #         st.write("They laugh it off, but you feel a bit embarrassed.")
    #         # st.write("1. Laugh along with them\n2. Ask them to ease up on the jokes\n3. Confront them privately about how it makes you feel")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Laugh along with them"):
    #             self.doubt_meter -= 1
    #         if button2.button("Ask them to ease up on the joke"):
    #             self.doubt_meter += 0
    #         if button3.button("Confront them privately about how it makes you feel"):
    #             self.doubt_meter += 1




    # def neutral_scenario2(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # Same level of obviousness if doubt meter hasn't changed
            
    #         st.write(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
    #         st.write("They imply that you'd be more interesting if you had a higher-paying job.")
    #         # st.write("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Ignore the comment"):
    #             self.doubt_meter -= 0
    #         if button2.button("Defend your career choice"):
    #             self.doubt_meter += 1
    #         if button3.button("Ask why they feel this way"):
    #             self.doubt_meter -= 1
    
    # def neutral_scenario3(self):
    #     if st.session_state.page == "scenario" + str(self.scenario_count):
    #         st.title = "SCENARIO" + str(self.scenario_count)
    #         # Same level of obviousness if doubt meter hasn't changed
            
    #         st.write(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
    #         st.write("They imply that you'd be more interesting if you had a higher-paying job.")
    #         # st.write("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

    #         st.write("What will you do?")

    #         button1 = st.empty()
    #         button2 = st.empty()
    #         button3 = st.empty()

    #         if button1.button("Ignore the comment"):
    #             self.doubt_meter -= 0
    #         if button2.button("Defend your career choice"):
    #             self.doubt_meter += 1
    #         if button3.button("Ask why they feel this way"):
    #             self.doubt_meter -= 1

    def end_game(self):
        if st.session_state.page == 'ending':
            st.title("The End")
            st.write(f"Your final score is: {st.session_state.score}")
            st.write("\nThank you for playing 'Signs of the Relationship.'")
            st.write("We hope this experience helped you recognize the importance of healthy relationship dynamics.")
            self.game_running = False
        if st.button("Play Again"):
            reset_game()


# Start the game

#st.set_page_config(layout="wide")

# Menu page
if st.session_state.page == 'menu':
    # st.title("Welcome to BUILD A RELATIONSHIP!")
    st.write("Press to start.")
    if st.button("Start Game", key="start"):
        game = RelationshipGame()
        game.start_game()
    if st.button("Instructions", key="instruction"):
        st.session_state.page = 'instructions'

css = """
       <style>
       </style>
       """
st.markdown(css, unsafe_allow_html=True)