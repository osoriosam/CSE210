import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction0 = Point(constants.CELL_SIZE, 0)
        self._direction1 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        new_dir_0 = ""
        new_dir_1 = ""

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction0 = Point(-constants.CELL_SIZE, 0)
            new_dir_0 = "x"
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction0 = Point(constants.CELL_SIZE, 0)
            new_dir_0 = "x"
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction0 = Point(0, -constants.CELL_SIZE)
            new_dir_0 = "y"
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction0 = Point(0, constants.CELL_SIZE)
            new_dir_0 = "y"
        
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)
            new_dir_1 = "x"

        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction1 = Point(constants.CELL_SIZE, 0)
            new_dir_1 = "x"

        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
            new_dir_1 = "y"

        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction1 = Point(0, constants.CELL_SIZE)
            new_dir_1 = "y"

        cycle0 = cast.get_actor("cycles", 0)
        cycle0.turn_head(self._direction0)
        dir_0 = cycle0.get_direction()
        if  dir_0 != new_dir_0 and new_dir_0 != "":
            cycle0.set_move(True)
            cycle0.set_direction(new_dir_0)

        cycle1 = cast.get_actor("cycles", 1)
        cycle1.turn_head(self._direction1)
        dir_1 = cycle1.get_direction()
        if  dir_1 != new_dir_1 and new_dir_1 != "":
            cycle1.set_move(True)
            cycle1.set_direction(new_dir_1)
