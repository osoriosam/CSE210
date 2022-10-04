class Parachute:
    """The person drawing the parachute. 

    The responsibility of a Prachute is to draw the diferent intances of prachute.
    
    Attributes:
        line[0-8] nine lines of a drawing.
    """

    def __init__(self) -> None:
        """Constructs a new Parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._line= ["", "", "", "", "", "", "", "", ""]
        self._line[0] = "  ___  "
        self._line[1] = " /___\ "
        self._line[2] = " \   / "
        self._line[3] = "  \ /  "
        self._line[4] = "   O   "
        self._line[5] = "  /|\  "
        self._line[6] = "  / \  "
        self._line[7] = "       "
        self._line[8] = "^^^^^^^"

    def dsp_parachute(self, line_from):
        """Displays parachute from line_from.

        """
        if line_from == 4:
            self._line[4] = "   X   "
        for i in range(line_from, 9):
            print(f"{self._line[i]}")
