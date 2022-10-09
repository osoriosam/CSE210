from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """The person who make new artifact in the game

    The responsibility of a Artifact is to create a new artifact and set the color, 
    possition, font size through inherited attributes from Actor class
    and message for display.
    
    Attributes:
        points (int): The points to add when robot touch an artifact.    
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._points = 0

    def get_points(self):
        """Get points when robot touch an artifact.

        Returns:
            Points: 1 if touch a gem, -1 if touch a rock
        """
        if (self.get_text == "*"):
            self._points = 1
        else:
            self._points = -1
        return self._points


    

    

