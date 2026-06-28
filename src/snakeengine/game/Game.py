
import typing
if typing.TYPE_CHECKING:
    from snakeengine.Engine import Engine

import abc


class Game(abc.ABC):
    """
    Abstract class representing the actual playable game.
    """

    def __init__(self, engine: "Engine"):
        """
        :param engine: The engine that runs the game.
        """

        self.engine: "Engine" = engine

    @abc.abstractmethod
    def on_initialize(self) -> None:
        """
        Runs when the game is initialised.

        :returns: None
        """

    @abc.abstractmethod
    def on_step(self) -> None:
        """
        Runs every tick of the game.

        :returns: None
        """

        self.engine.WINDOW.flip()
        self.engine.CLOCK.tick(self.engine.TICKRATE)
