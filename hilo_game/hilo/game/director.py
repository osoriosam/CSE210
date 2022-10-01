from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hilo (List[Card]): A list of Hilo instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.card_value = 0
        self.next_card = 0
        self.usr_guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_card()
            self.get_hilo()
            self.get_next_card()
            self.get_score(self.card_value, self.next_card, self.usr_guess)
            self.get_again()

    def get_card(self):
        """ Display the card number
        Args:
            self (Director): n instance of Director.
        """
        if not self.is_playing:
            return

        self.card = Card()
        self.card.pick_one()
        self.card_value = self.card.value
        print(f"\nThe card is: {self.card_value} ")

    def get_hilo(self):
        """Ask the user Higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        self.usr_guess = ""
        while self.usr_guess != "h" and self.usr_guess != "l":
            self.usr_guess = input("Higher or lower? [h/l] ")

    def get_next_card(self):
        """ Display the next card number
        Args:
            self (Director): n instance of Director.
        """
        if not self.is_playing:
            return

        self.card = Card()
        self.card.pick_one()
        self.next_card = self.card.value
        print(f"Next card was: {self.next_card} ")

    def get_score(self, card, next_card, usr_guess):
        """ Display the score
        Args:
            self (Director): n instance of Director.
        """
        if not self.is_playing:
            return
        
        if (usr_guess == "h" and card < next_card) or (usr_guess == "l" and card > next_card):
            self.score = 100
        else:
            self.score = -75
        
        self.total_score +=self.score

        print(f"Your score: {self.total_score} ")

    def get_again(self):
        """Ask the user play again.

        Args:
            self (Director): An instance of Director.
        """
        play_again = ""

        if self.total_score <= 0 :
            play_again = "n"

        while play_again != "y" and play_again != "n":
            play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")
