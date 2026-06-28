
import pygame as pg

events: dict[str, int] = {}
hooks: dict[int, function] = {}


def set_event(name: str, event: int) -> None:
    """
    Adds a named event to the global events
    :param name: (str) the name of the event
    :param event: (int)
    :return: None
    """
    global events
    events[name] = event


def remove_event(name: str) -> None:
    """
    Removes a named event from the global events
    :param name:
    :return: None
    """
    global events
    events.pop(name)


def get_event(name: str) -> int:
    """
    Gets a named event from the global events
    :param name:
    :return: int
    """
    global events
    return events[name]


def hook_event(event: int, action: function) -> None:
    """
    Hooks a function to the global events
    :param event: (int) the event to hook
    :param action: (function) the function that runs when the event is triggered
    :return: None
    """
    global hooks
    hooks[event] = action


def unhook_event(event: int) -> None:
    """
    Unhooks a function to the global events
    :param event: (int) the event to unhook
    :return: None
    """
    global hooks
    hooks.pop(event)


def get_hook(event: int) -> function:
    """
    Gets a function that is hooked to the specified event
    :param event: the event to get its hook from
    :return: function
    """
    global hooks
    return hooks[event]


def run_events() -> None:
    """
    Runs through all the events hooked into a function and excecutes them.
    :return: None
    """
    global hooks

    for event in pg.event.get():
        for e in hooks:
            if event.type == e:
                hooks[e]()
