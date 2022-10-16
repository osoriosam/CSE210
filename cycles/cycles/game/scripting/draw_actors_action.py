from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_actor("scores", 0)
        score2 = cast.get_actor("scores", 1)
#        food = cast.get_first_actor("foods")
        cycle_1 = cast.get_actor("cycles", 0)
        cycle_2 = cast.get_actor("cycles", 1)
        segments_1 = cycle_1.get_segments()
        messages_1 = cast.get_actors("messages")
        segments_2 = cycle_2.get_segments()
        messages_2 = cast.get_actors("messages")

        self._video_service.clear_buffer()
#        self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments_1)
        self._video_service.draw_actors(segments_2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages_1, True)
        self._video_service.draw_actors(messages_2, True)
        self._video_service.flush_buffer()