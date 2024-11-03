import Person as p
import Scenario as s
import time
import random as r

class RelationshipGame:
    def __init__(self):
        self.doubt_meter = 2  # Starting at 1 for the obvious scenario
        self.game_running = True
        self.scenario_count = 0
        self.neutral_scenarios = [1, 2, 3, 4, 5]
        self.subtle_scenarios = [1, 2, 3, 4, 5]
        self.obvious_scenarios = [1, 2, 3, 4, 5]

    def start_game(self):
        string = "Welcome to 'Signs of the Relationship'!" + "\n" + "You've been dating your partner for six months, but recently you've noticed a few unsettling things." + "\n" + "Throughout this game, you'll experience different situations and make choices that affect your doubt level."  + "\n" +  "Let's see how your relationship unfolds...\n"
        return string

    
    def get_random_scenario(self, scenarios):
        """Generate a random number and ensure it hasn’t been used yet.
           Reset scenarios if all have been used."""
        if not scenarios:  # Reset the scenarios list if empty
            return -1
        
        sNum = r.choice(scenarios)
        scenarios.remove(sNum)
        return sNum

    def relationship_scenarios(self):
        if self.doubt_meter <= 0:
            sNum = self.get_random_scenario(self.obvious_scenarios)
            self.scenario_count += 1
            if (sNum == 1):
                return self.obvious_scenario1()
            elif (sNum == 2):
                return self.obvious_scenario2()
            elif (sNum == 3):
                return self.obvious_scenario3()
            elif (sNum == 4):
                return self.obvious_scenario4()
            elif (sNum == 5):
                return self.obvious_scenario5()
            else:
                return self.end_game()
        elif self.doubt_meter >= 4:
            sNum = self.get_random_scenario(self.subtle_scenarios)
            self.scenario_count += 1
            if (sNum == 1):
                return self.subtle_scenario1()
            elif (sNum == 2):
                return self.subtle_scenario2()
            elif (sNum == 3):
                return self.subtle_scenario3()
            elif (sNum == 4):
                return self.subtle_scenario4()
            elif (sNum == 5):
                return self.subtle_scenario5()
            else:
                return self.end_game()
        elif self.doubt_meter < 4 and self.doubt_meter > 0:
            sNum = self.get_random_scenario(self.neutral_scenarios)
            self.scenario_count += 1
            if (sNum == 1):
                return self.neutral_scenario1()
            elif (sNum == 2):
                return self.neutral_scenario2()
            elif (sNum == 3):
                return self.neutral_scenario3()
            elif (sNum == 4):
                return self.neutral_scenario4()
            elif (sNum == 5):
                return self.neutral_scenario5()
            else:
                print(self.end_game(), str(self.scenario_count), sNum)
                return self.end_game()
        # return self.end_game()
    
    def rtnScene(self, string, choice = None):
        from app import choice
        return string, choice

    def obvious_scenario1(self):
        # An obvious red flag scenario if doubt is low
        string = f"\nScenario {self.scenario_count}: Your partner checks your phone without asking." + "\n" + "They say they're just 'making sure' you're being honest." + "\n" + "1. Ask them to respect your privacy\n2. Allow it, hoping it reassures them\n3. Confront them and express discomfort"

        choice = {}
        choice[0] = "You ask them to respect your privacy, but they brush it off."
        choice[-1] = "You let them check, feeling uneasy but hoping it calms their fears."
        choice[1] = "You express discomfort, and they respond with defensiveness."
        return string, choice # string, dictionary

    def obvious_scenario2(self):
        # An obvious red flag scenario if doubt is low
        string = f"\nScenario {self.scenario_count}: Arguement." + "\n" + " During an argument, your partner loses control and throws something across the room, narrowly missing you." + "\n" +"1. Calmly ask to take a break and revisit the conversation later.\n2. Apologize and try to calm them down, blaming yourself.\n3. Leave the room immediately to protect yourself and avoid further escalation. "
        choice = {}

        choice[0] = "Calmly ask to take a break and revisit the conversation later"
        choice[-1] = "Apologize and try to calm them down, blaming yourself."
        choice[1] = "Leave the room immediately to protect yourself and avoid further escalation."
        return string, choice # string, dictionary

    def obvious_scenario3(self):
        # An obvious red flag scenario if doubt is low
        string = f"\nScenario {self.scenario_count}: You mention wanting to visit family over the weekend, and your partner becomes furious." + "\n" + "saying, “If you leave, don’t bother coming back. You don’t get to just do whatever you want without thinking about me" + "\n" + "1. Suggest a compromise, like visiting family for part of the weekend and spending the rest of the time with them.\n2. Agree to stay home to avoid their anger and make them feel more secure\n3. Calmly tell them that their reaction is unfair "

        choice = {}
        choice[0] = "Suggest a compromise, like visiting family for part of the weekend and spending the rest of the time with them."
        choice[-1] = "Agree to stay home to avoid their anger and make them feel more secure."
        choice[1] = "Calmly tell them that their reaction is unfair."
        return string, choice # string, dictionary

    def obvious_scenario4(self):
        # An obvious red flag scenario if doubt is low
        string = f"\nScenario {self.scenario_count}: Your partner demands access to your bank account, saying, “We need to share everything if this relationship is going to work." + "\n" + "I don’t trust you unless I can see where your money is going." + "1. Agree to discuss your spending and big purchases together without sharing full access.\n2.Reluctantly agree to share your bank account information, even if it makes you uncomfortable.\n3. Firmly refuse, explaining that financial independence is important to you."

        choice = {}
        choice[0] = "Agree to discuss your spending and big purchases together without sharing full access"
        choice[-1] = "Reluctantly agree to share your bank account information, even if it makes you uncomfortable."
        choice[1] = "Firmly refuse, explaining that financial independence is important to you."
        return string, choice # string, dictionary

    def obvious_scenario5(self):
        # An obvious red flag scenario if doubt is low
        string = f"\nScenario {self.scenario_count}: You’re at a social gathering, and your partner makes an embarrassing comment about you in front of others" + "\n" + "then laughs and says, “I’m just kidding!" + "\n" + "1. Give a slight smile and change the subject, not giving their comment much energy.\n2.Laugh along to keep the peace, even though it hurts.\n3.Pull them aside afterward and explain that their comment hurt you."

        choice = {}
        choice[0] = "Give a slight smile and change the subject, not giving their comment much energy."
        choice[-1] = "Double down and make fun of yourself"
        choice[1] = "Pull them aside afterward and explain that their comment hurt you."
        return string, choice # string, dictionary

    def neutral_scenario1(self):
        # A subtle red flag scenario if doubt is moderate
        string = f"\nScenario {self.scenario_count}: You share a small success, and they respond dismissively, like “Oh, that’s nice, but it’s not that big of a deal.”" + "\n" + "It makes you feel deflated and unimportant." + "\n" + "1. Brush it off, but feel disappointed\n2.Thank them for listening and decide to keep it to yourself next time. \n3. Tell them it bothers you and seek validation"

        choice = {}
        choice[0] = "Thank them for listening and decide to keep it to yourself next time."
        choice[-1] = "Brush it off, but feel disappointed"
        choice[1] = "Tell them it bothers you and seek validation"
        return string, choice # string, dictionary
    
    def neutral_scenario2(self):
        # A subtle red flag scenario if doubt is moderate
        string = f"\nScenario {self.scenario_count}: Your partner makes negative comments about your friends, like saying they’re “a bad influence” or “not good for you,”" + "\n" + "implying you should stop seeing them." + "\n" + "1. Consider distancing yourself from friends to appease them.\n2.Defend your friends and tell them it’s not their choice.\n3. Acknowledge their opinion but mention you’ll decide who to spend time with."
        choice = {}
        choice[0] = "Defend your friends and tell them it’s not their choice.’"
        choice[-1] = "Consider distancing yourself from friends to appease them."
        choice[1] = "Acknowledge their opinion but mention you’ll decide who to spend time with."
        return string, choice # string, dictionary
    
    def neutral_scenario3(self):
        # A subtle red flag scenario if doubt is moderate
        string = f"\nScenario {self.scenario_count}: You express that you’d like some time alone, but your partner insists on staying with you," + "\n" + "saying, “Why don’t you want to be with me?." + "\n" + "1. Reconsider and let them stay, feeling like you need to reassure them.\n2. Politely insist that alone time is important to you.\n3. Confront them privately about how it makes you feel"

        choice = {}
        choice[0] = "Politely insist that alone time is important to you."
        choice[-1] = "Reconsider and let them stay, feeling like you need to reassure them."
        choice[1] = "Say you’re tired and hint that you’ll catch up later."
        return string, choice # string, dictionary

    def neutral_scenario4(self):
        # A subtle red flag scenario if doubt is moderate
        string = f"\nScenario {self.scenario_count}: You excitedly share a new hobby or interest you’ve taken up, but your partner responds with," + "\n" + "“That seems like a waste of time. Why are you even interested in that?”" + "\n" + "1. Reconsider and start doubting your interest, feeling deflated.\n2. Calmly explain why the hobby is important to you and continue with it. .\n3. Thank them for their opinion and decide not to share similar interests in the future. "
        choice = {}
        choice[0] = "Calmly explain why the hobby is important to you and continue with it. "
        choice[-1] = "Reconsider and start doubting your interest, feeling deflated. "
        choice[1] = "Thank them for their opinion and decide not to share similar interests in the future. "
        return string, choice # string, dictionary

    def neutral_scenario5(self):
        # A subtle red flag scenario if doubt is moderate
        string = f"\nScenario {self.scenario_count}: You mention a new job opportunity, and your partner says, “Do you really think you’re ready for that?" + "\n" + "I just don’t want to see you disappointed.” " + "\n" + "1. Decide not to pursue the job, doubting your readiness.\n2. Explain that you believe you’re ready and want to go for it.\n3. Thank them for their concern and say you’ll think about it. "

        choice = {}
        choice[0] = "Explain that you believe you’re ready and want to go for it."
        choice[-1] = "Decide not to pursue the job, doubting your readiness."
        choice[1] = "Thank them for their concern and say you’ll think about it. "
        return string, choice # string, dictionary

    def subtle_scenario1(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'" + "\n" + "They imply that you'd be more interesting if you had a higher-paying job." + "\n" + "1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way"

        choice = {}

        choice[0] = "You ignore it, but the comment lingers in your mind."
        choice[-1] = "Reflect on input and work harder"
        choice[1] = "You defend your career, but they dismiss your response, saying it's ‘just their opinion.’"
        return string, choice # string, dictionary

    def subtle_scenario2(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}: You excitedly share a project you’ve been working hard on. Your partner responds with, “Wow, it’s great! But you know, if you had just done it this way, it would have been even better.”" + "\n" + "While they start with a compliment, their follow-up undermines your achievement." + "\n" + "1. Feel slightly deflated but try to improve based on their feedback.\n2. ake the compliment at face value but feel a nagging sense of frustration about the criticism afterward.\n3. Accept their feedback with a forced smile"

        choice = {}

        choice[0] = "Feel slightly deflated but try to improve based on their feedback.."
        choice[-1] = "Accept their feedback with a smile"
        choice[1] = "What makes you say that?"
        return string, choice # string, dictionary
    
    def subtle_scenario3(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}: You mention you're overwhelmed with chores. Your partner responds, “I can help you with that, but you owe me a favor later.”" + "\n" + "They offer assistance but frame it as a transactional exchange." + "\n" + "1. Accept the help without much thought, feeling indifferent to the situation\n2. \n3. Ask why they feel this way"

        choice = {}
        choice[0] = "Accept the help without much thought, feeling indifferent to the situation."
        choice[-1] = "You stay silent."
        choice[1] = "Say thank you to them for the offer, deciding it’s better to take this into your own hands."
        return string, choice # string, dictionary

    def subtle_scenario4(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}:You express uncertainty about an upcoming social event. Your partner confidently states, “I’ve already told everyone we’re going!”" + "\n" + "They act decisively but without including you in the decision.." + "\n" + "1. Feel grateful they took charge but quietly frustrated at not being consulted.\n2.Express your desire to be included in decisions like this in the future. \n3.Go along with their decision, telling yourself it’s not a big deal."

        choice = {}
        choice[0] = "Feel grateful they took charge but quietly frustrated at not being consulted"
        choice[-1] = "Go along with their decision, telling yourself it’s not a big deal."
        choice[1] = "Express your desire to be included in decisions like this in the future."
        return string, choice # string, dictionary

    def subtle_scenario5(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}:You tell your partner that you’re planning to start a new fitness routine at the gym." + "\n" + "They respond with, “Oh, that’s ambitious. Are you sure you’ll keep up with it?" + "\n" + "1. Agree with them and start doubting your ability to follow through, feeling discouraged.\n2.Respond confidently, saying you’re excited about the challenge and committed to sticking with it. \n3.Brush off their comment but it lingers on you."

        choice = {}

        choice[0] = "Agree with them and start doubting your ability to follow through, feeling discouraged."
        choice[-1] = "Brush off their comment but it lingers on you."
        choice[1] = "Respond confidently, saying you’re excited about the challenge and committed to sticking with it. "
        return string, choice # string, dictionary

    def positive_scenario1(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}:You mention that you’re stressed out with a work deadline. " + "\n" + "Your partner responds casually, “Well, you’ll figure it out; you’re good at that. " + "\n" + "1. Brush off their compliments, deciding to take matters into your own hands.\n2.Feel slightly dismissed, but realize later that you appreciate the trust they place in you to manage things yourself.  \n3.Brush off their comment but it lingers on you."

        choice = {}

        choice[0] = "Brush off their compliments, deciding to take matters into your own hands. "
        choice[-1] = "Call them out for not being able to support you when you need help."
        choice[1] = "Feel slightly dismissed, but realize later that you appreciate the trust they place in you to manage things yourself."
        return string, choice # string, dictionary

    def positive_scenario2(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}:After a busy day, you don’t hear from your partner. When you check in with them, " + "\n" + "they respond promptly but explain that they assumed you might want some quiet time, so they held back from messaging first." + "\n" + "1. Acknowledge it without comment, feeling quietly thankful that they didn’t intrude.\n2.Feel a bit neglected at first, but later appreciate that they didn’t pressure you.  \n3.Express mild disappointment, but realize you enjoy having the freedom to set the pace."

        choice = {}

        choice[0] = "Acknowledge it without comment, feeling quietly thankful that they didn’t intrude. "
        choice[-1] = "Express mild disappointment, but realize you enjoy having the freedom to set the pace."
        choice[1] = "Feel a bit neglected at first, but later appreciate that they didn’t pressure you. "
        return string, choice # string, dictionary

    def positive_scenario3(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}:You tell your partner about a small success at work or school. Instead of celebrating it enthusiastically " + "\n" + "they respond with a simple “Nice” and carry on with the conversation." + "\n" + "1. Acknowledge their calm response, realizing it helps you not feel pressured to constantly prove yourself.\n2.Feel a bit let down by their response but later find comfort in knowing that they don’t overhype small things.  \n3.Brush off their comment but it lingers on you."

        choice = {}
        choice[0] = "Acknowledge their calm response, realizing it helps you not feel pressured to constantly prove yourself "
        choice[-1] = "Call them out for not being able to support you when you need help."
        choice[1] = "Feel a bit let down by their response but later find comfort in knowing that they don’t overhype small things.. "
        return string, choice # string, dictionary

    def positive_scenario4(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        string = f"\nScenario {self.scenario_count}:You share your plans for the weekend. Your partner responds, “Sounds fun! I guess I’ll just be stuck here alone, huh?” " + "\n" + "They express interest but with a hint of resentment. " + "\n" + "1. Nod along and change the subject, not wanting to dwell on their reaction.\n2.Acknowledge their response and refocus on your accomplishment, staying proud of your achievement.  \n3.Laugh it off, thinking they’re joking, but later feel guilty for wanting to enjoy your own time."

        choice = {}
        choice[0] = "Nod along and change the subject, not wanting to dwell on their reaction. "
        choice[-1] = "Laugh it off, thinking they’re joking, but later feel guilty for wanting to enjoy your own time."
        choice[1] = "Acknowledge their response and refocus on your accomplishment, staying proud of your achievement."
        return string, choice # string, dictionary

    
        

    def end_game(self):
        string = "\nThank you for playing 'Signs of the Relationship.'" + "\n" + "We hope this experience helped you recognize the importance of healthy relationship dynamics."
        print("Your final Doubt Meter Level is:  " + str(self.doubt_meter) + "!!")
        self.game_running = False
        return string, {0: "finished"}


# Start the game

# if st.button("Start Game"):
#     game = RelationshipGame()
#     game.start_game()
#     game.writeSth()
# if st.button("Instructions"):
#     st.write("Instructions:  ")

# css = """
#        <style>
#        </style>
#        """
# st.markdown(css, unsafe_allow_html=True)