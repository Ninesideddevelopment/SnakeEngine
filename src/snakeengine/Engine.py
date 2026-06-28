import sys
import typing

import pygame

if typing.TYPE_CHECKING:
    from snakeengine.core.enums.GameDimension import GameDimension
    from src.snakeengine.game.Game import Game

import abc
import pygame as pg

from snakeengine.core import EventHandler


class Engine(abc.ABC):

    """
    The main engine class that coordinates the running of the game class.
    \n Further documentation required.
    """

    def __init__(self, game_dimension: "GameDimension", game: "Game|None" = None):
        """
        :param game_dimension: Specifies the game's dimension; 2D, 3D, or MIXED.
        :param game: Specifies the game object that the engine operates on.
        """
        self.GAME_DIMENSION: "GameDimension" = game_dimension
        self.GAME: "Game" = game

        self.WINDOW: "pg.Window|None" = None
        self.CLOCK: "pg.time.Clock" = pg.time.Clock()

        self.TICKRATE: int = 60

    @abc.abstractmethod
    def initialise(self, **kwargs) -> Engine:
        """
        Initialise the engine object.
        :returns: None
        """
        self.WINDOW.get_surface()

        EventHandler.hook_event(pg.QUIT, self.stop)

        return self

    def begin(self) -> None:
        """
        Begins the game.
        :returns: None
        """
        while 1:
            self.GAME.on_step()
            EventHandler.run_events()

    def configure(self, **kwargs) -> None:
        """
        Used to set any values after creation of the engine object.
        :returns: None
        """
        for name, value in kwargs.items():
            setattr(self, name, value)

    def stop(self):
        pygame.quit()
        sys.exit()
