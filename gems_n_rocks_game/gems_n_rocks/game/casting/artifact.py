from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """The person who make new artifact in the game

    The responsibility of a Artifact is to create a new artifact and set the color, 
    possition, font size through inherited attributes from Actor class
    and message for display.
    
    Attributes:
        message (String): The message to display when the robot touch each artifact.    
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._points = 0

    def get_points(self):
        

    

    

