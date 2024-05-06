"""command_line.py - Command line interface for the application."""

from ..logs.setup_logging import setup_logging

interface_logger = setup_logging()


def command_line_interface() -> None:
    """Command line interface for the application."""
    interface_logger.info("Command line interface started.")