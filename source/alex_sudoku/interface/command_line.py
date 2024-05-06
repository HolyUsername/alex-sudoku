"""command_line.py - Command line interface for the application."""

from ..logs.setup_logging import setup_logging

interface_logger = setup_logging()


def command_line_interface() -> None:
    """
    Controls the command line.
    
    Notes
    -----
    Asks for their name and then greets the user.
    """
    interface_logger.info("Command line interface started.")
    
    name = input("What is your name?")
    
    print(f"Hello, {name}!")