"""Main entry point for the Licensed Clock Application.

This module serves as the entry point for the Multi-Timezone Clock application.
It initializes and runs the main application window with error handling.
"""

import sys
import traceback
from typing import NoReturn

from ui.app import App


def handle_exception(
    exc_type: type, exc_value: Exception, exc_tb: traceback
) -> NoReturn:
    """Handle uncaught exceptions in the application.

    This function provides a graceful way to handle unexpected errors,
    logging them and showing an error message to the user.

    Args:
        exc_type: The type of the exception
        exc_value: The exception instance
        exc_tb: The traceback object

    Note
        In production, you might want to log errors to a file or error tracking service.
    """
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(f"An error occurred:\n{error_msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    """Initialize and run the application.

    This function sets up the main application window and starts
    the event loop. It also configures global exception handling.
    """
    try:
        # Set up global exception handler
        sys.excepthook = handle_exception

        # Initialize and run the application
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Failed to start application: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
