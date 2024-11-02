class RelationshipGame:
    def __init__(self):
        self.doubt_meter = 2  # Starting at 1 for the obvious scenario
        self.game_running = True
        self.scenario_count = 0

    def start_game(self):
        print("Welcome to 'Signs of the Relationship'!")
        print("You've been dating your partner for six months, but recently you've noticed a few unsettling things.")
        print("Throughout this game, you'll experience different situations and make choices that affect your doubt level.")
        print("Let's see how your relationship unfolds...\n")
        self.relationship_scenarios()

    def relationship_scenarios(self):
        while self.game_running and self.scenario_count < 5:
            self.scenario_count += 1
            if self.doubt_meter <= 0:
                self.obvious_scenario()
            elif self.doubt_meter >= 4:
                self.subtle_scenario()
            else:
                self.neutral_scenario()

        print(f"\nYour final Doubt Meter level is: {self.doubt_meter}")
        self.end_game()

    def obvious_scenario(self):
        # An obvious red flag scenario if doubt is low
        print(f"\nScenario {self.scenario_count}: Your partner checks your phone without asking.")
        print("They say they're just 'making sure' you're being honest.")
        print("1. Ask them to respect your privacy\n2. Allow it, hoping it reassures them\n3. Confront them and express discomfort")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You ask them to respect your privacy, but they brush it off.")
            self.doubt_meter += 0
        elif choice == "2":
            print("You let them check, feeling uneasy but hoping it calms their fears.")
            self.doubt_meter -= 1
        elif choice == "3":
            print("You express discomfort, and they respond with defensiveness.")
            self.doubt_meter += 1
        else:
            print("Invalid choice. Try again.")
            self.obvious_scenario()

    def subtle_scenario(self):
        # A subtle red flag scenario if doubt is moderate
        print(f"\nScenario {self.scenario_count}: Your partner keeps jokingly putting you down in front of friends.")
        print("They laugh it off, but you feel a bit embarrassed.")
        print("1. Laugh along with them\n2. Ask them to ease up on the jokes\n3. Confront them privately about how it makes you feel")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You laugh along, hoping it’s harmless. They keep doing it throughout the night.")
            self.doubt_meter += -1
        elif choice == "2":
            print("You ask them to ease up, and they act surprised, saying you’re ‘too sensitive.’")
            self.doubt_meter += 0
        elif choice == "3":
            print("You confront them about it privately, and they seem taken aback, saying they didn't mean harm.")
            self.doubt_meter += 1
        else:
            print("Invalid choice. Try again.")
            self.subtle_scenario()

    def neutral_scenario(self):
        # Same level of obviousness if doubt meter hasn't changed
        
        print(f"\nScenario {self.scenario_count}: Your partner criticizes your career choice, saying it’s 'not ambitious enough.'")
        print("They imply that you'd be more interesting if you had a higher-paying job.")
        print("1. Ignore the comment\n2. Defend your career choice\n3. Ask why they feel this way")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("You ignore it, but the comment lingers in your mind.")
            self.doubt_meter -= 0
        elif choice == "2":
            print("You defend your career, but they dismiss your response, saying it's ‘just their opinion.’")
            self.doubt_meter += 1
        elif choice == "3":
            print("You stay silent.")
            self.doubt_meter += 1
        else:
            print("Invalid choice. Try again.")

    def end_game(self):
        print("\nThank you for playing 'Signs of the Relationship.'")
        print("We hope this experience helped you recognize the importance of healthy relationship dynamics.")
        self.game_running = False

# Start the game
game = RelationshipGame()
game.start_game()
