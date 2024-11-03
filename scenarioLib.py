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

    def obvious_scenario2(self):
        # An obvious red flag scenario if doubt is low
        st.write(f"\nScenario {self.scenario_count}: Arguement.")
        st.write(" During an argument, your partner loses control and throws something across the room, narrowly missing you.")
        st.write("1. Calmly ask to take a break and revisit the conversation later.\n2. Apologize and try to calm them down, blaming yourself.\n3. Leave the room immediately to protect yourself and avoid further escalation. ")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Calmly ask to take a break and revisit the conversation later..")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("Apologize and try to calm them down, blaming yourself.")
            self.doubt_meter -= 1
        elif choice == "3":
            st.write("Leave the room immediately to protect yourself and avoid further escalation. ")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def obvious_scenario3(self):
        # An obvious red flag scenario if doubt is low
        st.write(f"\nScenario {self.scenario_count}: You mention wanting to visit family over the weekend, and your partner becomes furious.")
        st.write("saying, “If you leave, don’t bother coming back. You don’t get to just do whatever you want without thinking about me")
        st.write("1. Suggest a compromise, like visiting family for part of the weekend and spending the rest of the time with them.\n2. Agree to stay home to avoid their anger and make them feel more secure\n3. Calmly tell them that their reaction is unfair ")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Suggest a compromise, like visiting family for part of the weekend and spending the rest of the time with them.")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("Agree to stay home to avoid their anger and make them feel more secure.")
            self.doubt_meter -= 1
        elif choice == "3":
            st.write("Calmly tell them that their reaction is unfair.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    def obvious_scenario4(self):
        # An obvious red flag scenario if doubt is low
        st.write(f"\nScenario {self.scenario_count}: Your partner demands access to your bank account, saying, “We need to share everything if this relationship is going to work.")
        st.write("I don’t trust you unless I can see where your money is going.")
        st.write("1. Agree to discuss your spending and big purchases together without sharing full access.\n2.Reluctantly agree to share your bank account information, even if it makes you uncomfortable.\n3. Firmly refuse, explaining that financial independence is important to you. ")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Agree to discuss your spending and big purchases together without sharing full access")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("Reluctantly agree to share your bank account information, even if it makes you uncomfortable.")
            self.doubt_meter -= 1
        elif choice == "3":
            st.write("Firmly refuse, explaining that financial independence is important to you.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    def obvious_scenario5(self):
        # An obvious red flag scenario if doubt is low
        st.write(f"\nScenario {self.scenario_count}: You’re at a social gathering, and your partner makes an embarrassing comment about you in front of others")
        st.write("then laughs and says, “I’m just kidding!")
        st.write("1. Give a slight smile and change the subject, not giving their comment much energy.\n2.Laugh along to keep the peace, even though it hurts.\n3.Pull them aside afterward and explain that their comment hurt you.  ")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Give a slight smile and change the subject, not giving their comment much energy.")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("Double down and make fun of yourself")
            self.doubt_meter -= 1
        elif choice == "3":
            st.write("Pull them aside afterward and explain that their comment hurt you. ")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")



    def neutral_scenario1(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: You share a small success, and they respond dismissively, like “Oh, that’s nice, but it’s not that big of a deal.”")
        st.write("It makes you feel deflated and unimportant.")
        st.write("n1. Brush it off, but feel disappointed\n2.Thank them for listening and decide to keep it to yourself next time. \n3. Tell them it bothers you and seek validation")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Brush it off, but feel disappointed")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("Thank them for listening and decide to keep it to yourself next time. ’")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("Tell them it bothers you and seek validation")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    
    def neutral_scenario2(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: Your partner makes negative comments about your friends, like saying they’re “a bad influence” or “not good for you,”")
        st.write("implying you should stop seeing them.")
        st.write("1. Consider distancing yourself from friends to appease them.\n2.Defend your friends and tell them it’s not their choice.\n3. Acknowledge their opinion but mention you’ll decide who to spend time with.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Consider distancing yourself from friends to appease them.")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("Defend your friends and tell them it’s not their choice.’")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("Acknowledge their opinion but mention you’ll decide who to spend time with.")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    
    def neutral_scenario3(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: You express that you’d like some time alone, but your partner insists on staying with you,")
        st.write("saying, “Why don’t you want to be with me?.")
        st.write("1. Reconsider and let them stay, feeling like you need to reassure them.\n2. Politely insist that alone time is important to you.\n3. Confront them privately about how it makes you feel")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Reconsider and let them stay, feeling like you need to reassure them.")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("Politely insist that alone time is important to you.")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("Say you’re tired and hint that you’ll catch up later. ")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")
    def neutral_scenario3(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: You express that you’d like some time alone, but your partner insists on staying with you,")
        st.write("saying, “Why don’t you want to be with me?.")
        st.write("1. Reconsider and let them stay, feeling like you need to reassure them.\n2. Politely insist that alone time is important to you.\n3. Say you’re tired and hint that you’ll catch up later. ")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Reconsider and let them stay, feeling like you need to reassure them.")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("Politely insist that alone time is important to you.")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("Say you’re tired and hint that you’ll catch up later. ")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def neutral_scenario4(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: You excitedly share a new hobby or interest you’ve taken up, but your partner responds with,")
        st.write("“That seems like a waste of time. Why are you even interested in that?”")
        st.write("1. Reconsider and start doubting your interest, feeling deflated.\n2. Calmly explain why the hobby is important to you and continue with it. .\n3. Thank them for their opinion and decide not to share similar interests in the future. ")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Reconsider and start doubting your interest, feeling deflated. ")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("Calmly explain why the hobby is important to you and continue with it. ")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("Thank them for their opinion and decide not to share similar interests in the future. ")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")

    def neutral_scenario5(self):
        # A subtle red flag scenario if doubt is moderate
        st.write(f"\nScenario {self.scenario_count}: You mention a new job opportunity, and your partner says, “Do you really think you’re ready for that?")
        st.write("I just don’t want to see you disappointed.” ")
        st.write("1. Decide not to pursue the job, doubting your readiness.\n2. Explain that you believe you’re ready and want to go for it.\n3. Thank them for their concern and say you’ll think about it. ")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Decide not to pursue the job, doubting your readiness.")
            self.doubt_meter += -1
        elif choice == "2":
            st.write("Explain that you believe you’re ready and want to go for it.")
            self.doubt_meter += 0
        elif choice == "3":
            st.write("Thank them for their concern and say you’ll think about it. ")
            self.doubt_meter += 1
        else:
            st.write("Invalid choice. Try again.")




    def subtle_scenario1(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
        st.write("They imply that you'd be more interesting if you had a higher-paying job.")
        st.write("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("You ignore it, but the comment lingers in your mind.")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("You defend your career, but they dismiss your response, saying it's ‘just their opinion.’")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Reflect on input and work harder")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")

    def subtle_scenario2(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}: You excitedly share a project you’ve been working hard on. Your partner responds with, “Wow, it’s great! But you know, if you had just done it this way, it would have been even better.”")
        st.write("While they start with a compliment, their follow-up undermines your achievement.")
        st.write("1. Feel slightly deflated but try to improve based on their feedback.\n2. ake the compliment at face value but feel a nagging sense of frustration about the criticism afterward.\n3. Accept their feedback with a forced smile")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Feel slightly deflated but try to improve based on their feedback..")
            self.doubt_meter += 0
        elif choice == "2":
            st.write("What makes you say that?")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Accept their feedback with a smile")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")
    
    def subtle_scenario3(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}: You mention you're overwhelmed with chores. Your partner responds, “I can help you with that, but you owe me a favor later.”")
        st.write("They offer assistance but frame it as a transactional exchange.")
        st.write("1. Accept the help without much thought, feeling indifferent to the situation\n2. \n3. Ask why they feel this way")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Accept the help without much thought, feeling indifferent to the situation.")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("Say thank you to them for the offer, deciding it’s better to take this into your own hands.")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("You stay silent.")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")
    def subtle_scenario4(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}:You express uncertainty about an upcoming social event. Your partner confidently states, “I’ve already told everyone we’re going!”")
        st.write("They act decisively but without including you in the decision..")
        st.write("1. Feel grateful they took charge but quietly frustrated at not being consulted.\n2.Express your desire to be included in decisions like this in the future. \n3.Go along with their decision, telling yourself it’s not a big deal.")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Feel grateful they took charge but quietly frustrated at not being consulted")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("Express your desire to be included in decisions like this in the future.")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Go along with their decision, telling yourself it’s not a big deal.")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")
    def subtle_scenario5(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}:You tell your partner that you’re planning to start a new fitness routine at the gym.")
        st.write("They respond with, “Oh, that’s ambitious. Are you sure you’ll keep up with it?")
        st.write("1. Agree with them and start doubting your ability to follow through, feeling discouraged.\n2.Respond confidently, saying you’re excited about the challenge and committed to sticking with it. \n3.Brush off their comment but it lingers on you.")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Agree with them and start doubting your ability to follow through, feeling discouraged.")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("Respond confidently, saying you’re excited about the challenge and committed to sticking with it. ")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Brush off their comment but it lingers on you.")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")

    def positive_scenario1(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}:You mention that you’re stressed out with a work deadline. ")
        st.write("Your partner responds casually, “Well, you’ll figure it out; you’re good at that. ")
        st.write("1. Brush off their compliments, deciding to take matters into your own hands.\n2.Feel slightly dismissed, but realize later that you appreciate the trust they place in you to manage things yourself.  \n3.Brush off their comment but it lingers on you.")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Brush off their compliments, deciding to take matters into your own hands. ")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("Feel slightly dismissed, but realize later that you appreciate the trust they place in you to manage things yourself.. ")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Call them out for not being able to support you when you need help.")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")

    def positive_scenario2(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}:After a busy day, you don’t hear from your partner. When you check in with them, ")
        st.write("they respond promptly but explain that they assumed you might want some quiet time, so they held back from messaging first.")
        st.write("1. Acknowledge it without comment, feeling quietly thankful that they didn’t intrude.\n2.Feel a bit neglected at first, but later appreciate that they didn’t pressure you.  \n3.Express mild disappointment, but realize you enjoy having the freedom to set the pace.")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Acknowledge it without comment, feeling quietly thankful that they didn’t intrude. ")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("Feel a bit neglected at first, but later appreciate that they didn’t pressure you. ")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Express mild disappointment, but realize you enjoy having the freedom to set the pace.")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")

    def positive_scenario3(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}:You tell your partner about a small success at work or school. Instead of celebrating it enthusiastically ")
        st.write("they respond with a simple “Nice” and carry on with the conversation.")
        st.write("1. Acknowledge their calm response, realizing it helps you not feel pressured to constantly prove yourself.\n2.Feel a bit let down by their response but later find comfort in knowing that they don’t overhype small things.  \n3.Brush off their comment but it lingers on you.")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Acknowledge their calm response, realizing it helps you not feel pressured to constantly prove yourself ")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("Feel a bit let down by their response but later find comfort in knowing that they don’t overhype small things.. ")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Call them out for not being able to support you when you need help.")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")
    def positive_scenario4(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        st.write(f"\nScenario {self.scenario_count}:You share your plans for the weekend. Your partner responds, “Sounds fun! I guess I’ll just be stuck here alone, huh?” ")
        st.write("They express interest but with a hint of resentment. ")
        st.write("1. Nod along and change the subject, not wanting to dwell on their reaction.\n2.Acknowledge their response and refocus on your accomplishment, staying proud of your achievement.  \n3.Laugh it off, thinking they’re joking, but later feel guilty for wanting to enjoy your own time.")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            st.write("Nod along and change the subject, not wanting to dwell on their reaction. ")
            self.doubt_meter -= 0
        elif choice == "2":
            st.write("Acknowledge their response and refocus on your accomplishment, staying proud of your achievement.. ")
            self.doubt_meter += 1
        elif choice == "3":
            st.write("Laugh it off, thinking they’re joking, but later feel guilty for wanting to enjoy your own time.")
            self.doubt_meter -= 1
        else:
            st.write("Invalid choice. Try again.")
    
    
        

    def end_game(self):
        st.write("\nThank you for playing 'Signs of the Relationship.'")
        st.write("We hope this experience helped you recognize the importance of healthy relationship dynamics.")
        self.game_running = False


# Start the game

st.set_page_config(layout="wide")

if st.button("Start Game"):
    game = RelationshipGame()
    game.start_game()
    game.writeSth()
if st.button("Instructions"):
    st.write("Instructions:  ")

css = """
       <style>
       </style>
       """
st.markdown(css, unsafe_allow_html=True)