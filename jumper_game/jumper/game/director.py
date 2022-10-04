from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.secret_word import SWord

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret_word (SWord): Secret Word methods.
        is_playing (boolean): Whether or not to keep playing.
        parachuter (Parachute): To display the parachute drawing.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret_word = SWord()
        self._is_playing = True
        self._parachute = Parachute()
        self._terminal_service = TerminalService()
        self._character_guessed = ""
        self._word_guessed = False
        self._letter_from = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret_word.get_SWord()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Displays the parachute and ask for guess a letter.

        Args:
            self (Director): An instance of Director.
        """
        self._secret_word.dsp_characters()
        print()
        self._parachute.dsp_parachute(self._letter_from)
        if self._letter_from >= 4:
            self._is_playing = False
        if self._word_guessed == True:
            self._is_playing = False
        if self._is_playing == True:
            self._character_guessed = self._terminal_service.read_text("\nGuess a letter [a-z]: ")

    def _do_updates(self):
        """Keeps watch if the character is guessed.

        Args:
            self (Director): An instance of Director.
        """

        guessed = True
        guessed = self._secret_word.check_letter(self._character_guessed)
        if guessed == False:
            self._letter_from += 1
        if guessed == "End":
            self._word_guessed = True

    def _do_outputs(self):
        """Sent messages for the terminal.

        Args:
            self (Director): An instance of Director.
        """
        if self._word_guessed == True and self._is_playing == False:
            self._terminal_service.write_text("\nCongratultions, You WIN!!!!\n")
        if self._is_playing == False:
            self._terminal_service.write_text("\nGame over, thanks for playing!!!!\n")
