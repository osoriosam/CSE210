import random

class SWord:

#Change this
    """The person who handles the things of the secret word. 
    
    The responsibility of SWord is to choose a secret word from a list,
    check if the user guesses a letter and
    print the guessed characters. 

    Attributes:
        _SWords_list (List[String]): The secret words list.
        _SWord (String): The secret chosen word.
    """

    def __init__(self):
        """Constructs a new SWord.

        Args:
            self (SWord): An instance of SWord.
        """
        self._SWords_list = ["random", "instance", "location", "parachute", "distance", "responsability"]
        self._SWord = ""
        self._characters = ""
        self._possition = 0
        self._found = False

    def get_SWord(self):
        """Gets a word from the SWord list.

        Args:
            self (SWord): An instance of SWord.
        
*        Returns:
*            string: A word from the SWord list.
        """
        self._SWord = random.choice(self._SWords_list)
        self._characters = self._characters.ljust(len(self._SWord), "_")

    def check_letter(self, letter):
        """Looks for a letter into the SWord.

        Args:
            self (SWord): An instance of SWord.
        
        Returns:
            Boolean: The letter was or wasn't found into the SWord.
        """
        self._found = False
        i = 0
        p = ""
        w = ""
        try:
            self._found = self._SWord.index(letter)
            for character in self._SWord:
                if character == letter:
                    p = self._characters
                    w = list(p)
                    w[i] = letter
                    self._characters = "".join(w)
                    self._found = True
                i += 1
        except ValueError:
            self._found = False
        if self._SWord == self._characters:
            self._found = "End"
        return self._found

    def dsp_characters(self):
        """displays the characters.

        Args:
            self (SWord): An instance of SWord.
        
        """
        formatted = " ".join(self._characters)
        print()
        print(formatted)

