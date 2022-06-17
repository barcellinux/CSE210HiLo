from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.hilo = ""
        self.score = 0
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.draw_first_card()
            self.get_input_hilo()
            self.draw_second_card()
            self.calculate_score()
            self.get_input_play_again()
            #self.do_updates()
            #self.do_outputs()
    
    def draw_first_card(self):
        self.cards = []
        card = Card()
        self.cards.append(card.value)
        print (f"The card is: {card.value}") 

    def get_input_hilo(self):
        hilo = input("Higher or lower? [h/l]")
        self.hilo = hilo

    def draw_second_card(self):        
        card = Card()
        self.cards.append(card.value)
        print (f"Next card was: {card.value}")    

    def calculate_score(self):
        choice = self.hilo.lower()
        if choice == "l" and self.cards[1] < self.cards[0]:
            self.score = 100
        elif choice == "h" and self.cards[1] > self.cards[0]:
            self.score = 100
        else:
            self.score = -75
        self.total_score += self.score
        if self.total_score > 0:
            print (f"Your score is: {self.total_score}")
        else:
            print ("Game over...")
    
    def get_input_play_again(self):        
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")


'''
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        self.score = 0 #
        
        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score        

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}")
        self.is_playing = (self.score > 0) #'''