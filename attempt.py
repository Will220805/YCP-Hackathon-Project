import streamlit as st
import random as r

# Initialize session state for tracking game progress
if 'page' not in st.session_state:
    st.session_state.page = 'menu'
if 'score' not in st.session_state:
    st.session_state.score = 0

# Page navigation and game reset functions
def go_to_page(page_name):
    st.session_state.page = page_name

def reset_game():
    st.session_state.page = 'menu'
    st.session_state.score = 0

# Game class for handling game logic
class RelationshipGame:
    def __init__(self):
        self.doubt_meter = 2  # Starting at a neutral level
        self.game_running = True
        self.scenario_count = 0
        self.neutral_scenarios = [1, 2, 3]
        self.subtle_scenarios = [1, 2, 3]
        self.obvious_scenarios = [1, 2, 3]

    def start_game(self):
        st.write("Welcome to 'Signs of the Relationship'!")
        st.write("You've been dating your partner for six months, and you're noticing some unsettling behaviors.")
        st.write("You'll face different scenarios that affect your doubt meter. Let’s see how your relationship unfolds...\n")
        self.relationship_scenarios()

    def relationship_scenarios(self):
        while self.game_running and self.scenario_count < 10:
            sNum = r.choice(self.obvious_scenarios if self.doubt_meter <= 0 else 
                            self.subtle_scenarios if self.doubt_meter >= 4 else 
                            self.neutral_scenarios)
            self.scenario_count += 1

            if self.doubt_meter <= 0 and sNum in self.obvious_scenarios:
                self.obvious_scenario(sNum)
                self.obvious_scenarios.remove(sNum)
            elif self.doubt_meter >= 4 and sNum in self.subtle_scenarios:
                self.subtle_scenario(sNum)
                self.subtle_scenarios.remove(sNum)
            else:
                self.neutral_scenario(sNum)
                self.neutral_scenarios.remove(sNum)
            
            if not self.neutral_scenarios and not self.subtle_scenarios and not self.obvious_scenarios:
                break  # End game if all scenarios are used up

        st.session_state.page = 'ending'
        st.write(f"\nYour final Doubt Meter level is: {self.doubt_meter}")
        self.end_game()

    def neutral_scenario(self, sNum):
        st.write(f"Scenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
        self.process_choice()

    def subtle_scenario(self, sNum):
        st.write(f"Scenario {self.scenario_count}: Your partner frequently downplays your achievements.")
        self.process_choice()

    def obvious_scenario(self, sNum):
        st.write(f"Scenario {self.scenario_count}: Your partner checks your phone without asking.")
        self.process_choice()

    def process_choice(self):
        choice = st.radio("What will you do?", 
                          ["Ignore the comment", 
                           "Defend your career choice", 
                           "Ask why they feel this way"])
        
        if st.button("Submit"):
            if choice == "Ignore the comment":
                self.doubt_meter += 0
            elif choice == "Defend your career choice":
                self.doubt_meter += 1
            elif choice == "Ask why they feel this way":
                self.doubt_meter -= 1
            st.write(f"Doubt Meter: {self.doubt_meter}")

    def end_game(self):
        st.write("The game has ended. Thank you for playing!")


if st.session_state.page == 'menu':
    st.title("Welcome to BUILD A RELATIONSHIP!")
    st.write("Press to start.")
    if st.button("Start Game", key="start"):
        game = RelationshipGame()
        game.start_game()