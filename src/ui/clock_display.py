"""Module containing clock display components and time management logic.

This module provides components for displaying time and date information
for different timezones in a customizable format.
"""

from datetime import datetime
from typing import Optional, Any

import customtkinter as ctk
import pytz
from pytz.tzinfo import DstTzInfo, BaseTzInfo


class TimeFrame(ctk.CTkFrame):
    """A frame component for displaying time and date for a specific timezone.

    This class creates a frame that displays the current time and date
    for a given timezone with customizable formatting.

    Attributes:
        header (ctk.CTkLabel): The title label for the time frame
        time_label (ctk.CTkLabel): Label displaying the current time
        date_label (ctk.CTkLabel): Label displaying the current date
    """

    def __init__(
        self,
        master: Any,
        title: str,
        time_format: str = "%H:%M:%S",
        date_format: str = "%B %d, %Y",
        **kwargs,
    ) -> None:
        """Initialize the time frame with title and display labels.

        Args:
            master: Parent widget
            title (str): Title for the time frame
            time_format (str, optional): Format string for time display. Defaults to "%H:%M:%S".
            date_format (str, optional): Format string for date display. Defaults to "%B %d, %Y".
            **kwargs: Additional keyword arguments for the frame
        """
        super().__init__(master, **kwargs)

        # Store format strings
        self.time_format: str = time_format
        self.date_format: str = date_format

        # Header with customizable font
        self.header = ctk.CTkLabel(
            self, text=title, font=("Helvetica", 16, "bold")
        )
        self.header.pack(pady=5)

        # Time display with larger font
        self.time_label = ctk.CTkLabel(self, text="", font=("Helvetica", 36))
        self.time_label.pack()

        # Date display with medium font
        self.date_label = ctk.CTkLabel(self, text="", font=("Helvetica", 20))
        self.date_label.pack(pady=(0, 5))

    def update_time(self, time_obj: datetime) -> None:
        """Update the time and date display with the given datetime object.

        Args:
            time_obj (datetime): Datetime object to display

        Raises:
            ValueError: If time_obj is not a valid datetime object
        """
        try:
            self.time_label.configure(text=time_obj.strftime(self.time_format))
            self.date_label.configure(text=time_obj.strftime(self.date_format))
        except Exception as e:
            # Log error and show error state
            print(f"Error updating time display: {e}")
            self.time_label.configure(text="--:--:--")
            self.date_label.configure(text="Error")


class ClockDisplay:
    """Manager for multiple time displays.

    This class manages multiple TimeFrame instances for different timezones
    and handles their updates.

    Attributes:
        master: Parent widget
        local_frame (TimeFrame): Frame displaying local time
        est_frame (Optional[TimeFrame]): Frame displaying EST time (if enabled)
        est_tz (BaseTzInfo): EST timezone object
    """

    def __init__(
        self,
        master: Any,
        show_est: bool = False,
        time_format: str = "%H:%M:%S",
        date_format: str = "%B %d, %Y",
    ) -> None:
        """Initialize the clock display manager.

        Args:
            master: Parent widget
            show_est (bool, optional): Whether to show EST time. Defaults to False.
            time_format (str, optional): Format string for time display. Defaults to "%H:%M:%S".
            date_format (str, optional): Format string for date display. Defaults to "%B %d, %Y".
        """
        self.master: Any = master

        # Initialize timezone
        try:
            self.est_tz: BaseTzInfo = pytz.timezone("US/Eastern")
        except pytz.exceptions.UnknownTimeZoneError:
            print("Error: EST timezone not available, falling back to UTC")
            self.est_tz = pytz.UTC

        # Local time frame with error handling
        try:
            self.local_frame = TimeFrame(
                master=master,
                title="Local Time",
                time_format=time_format,
                date_format=date_format,
            )
            self.local_frame.pack(pady=10, padx=20, fill="x")
        except Exception as e:
            print(f"Error creating local time frame: {e}")
            self.local_frame = None

        # EST time frame (optional)
        self.est_frame: Optional[TimeFrame] = None
        if show_est:
            try:
                self.est_frame = TimeFrame(
                    master=master,
                    title="EST Time",
                    time_format=time_format,
                    date_format=date_format,
                )
                self.est_frame.pack(pady=10, padx=20, fill="x")
            except Exception as e:
                print(f"Error creating EST time frame: {e}")

    def update(self) -> None:
        """Update all time displays with current time.

        This method updates both local and EST time displays if they exist.
        It handles timezone conversions and error cases gracefully.
        """
        try:
            # Update local time if frame exists
            if self.local_frame:
                local_time: datetime = datetime.now()
                self.local_frame.update_time(local_time)

            # Update EST time if frame exists
            if self.est_frame:
                try:
                    est_time: datetime = datetime.now(self.est_tz)
                    self.est_frame.update_time(est_time)
                except Exception as e:
                    print(f"Error updating EST time: {e}")
                    # Reset EST frame on error
                    if self.est_frame:
                        self.est_frame.time_label.configure(text="--:--:--")
                        self.est_frame.date_label.configure(text="Error")
        except Exception as e:
            print(f"Error in clock update: {e}")
