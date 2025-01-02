"""Main application window module for the Multi-Timezone Clock application.

This module contains the main application window class that manages the UI and license state.
"""

from typing import Optional, Literal
import customtkinter as ctk

from ui.clock_display import ClockDisplay
from utils.license_manager import LicenseManager


class App(ctk.CTk):
    """Main application window with license management functionality.

    This class handles the main application window, including license management,
    clock display, and UI state management.

    Attributes:
        license_manager (LicenseManager): Handles license validation and trial management
        clock_display (Optional[ClockDisplay]): Manages the clock display components
    """

    def __init__(self) -> None:
        """Initialize the main application window with default settings."""
        super().__init__()

        self.title("Multi-Timezone Clock @Mrjxtr")
        self.geometry("400x400")
        self.minsize(300, 350)  # Set minimum window size for better UI

        self.license_manager: LicenseManager = LicenseManager()
        self.clock_display: Optional[ClockDisplay] = None

        # Initialize UI based on license status
        self.check_license_status()

    def check_license_status(self) -> None:
        """Check license status and setup appropriate UI based on the status."""
        try:
            status: Literal["LICENSED", "TRIAL", "EXPIRED", "INVALID"] = (
                self.license_manager.check_license()
            )

            # Clear existing widgets safely
            for widget in self.winfo_children():
                widget.destroy()

            # Setup UI based on status
            if status == "LICENSED":
                self.setup_main_app("Licensed Version")
            elif status == "TRIAL":
                remaining_days: int = self.license_manager.get_remaining_trial_days()
                self.setup_main_app(
                    f"Trial Version - {remaining_days} days remaining"
                )
            elif status == "EXPIRED":
                self.setup_expired_ui()
            else:
                self.setup_invalid_ui()
        except Exception as e:
            self.setup_error_ui(str(e))

    def setup_main_app(self, status_text: str) -> None:
        """Setup the main application UI with clock functionality.

        Args:
            status_text (str): Text to display in the status label indicating license status
        """
        try:
            # Status label with distinctive styling
            status_label = ctk.CTkLabel(
                master=self, text=status_text, font=("Helvetica", 14, "bold")
            )
            status_label.pack(pady=10)

            # Setup clock display with license-based features
            is_licensed: bool = "Licensed" in status_text
            self.clock_display = ClockDisplay(master=self, show_est=is_licensed)

            # Add activation UI for trial version
            if "Trial" in status_text:
                self.add_activation_ui()

            # Start the time update loop
            self.update_time()
        except Exception as e:
            self.setup_error_ui(str(e))

    def update_time(self) -> None:
        """Update the time display and schedule next update.

        This method is called every second to update the clock display.
        """
        try:
            if self.clock_display and not self.winfo_exists():
                return  # Stop updates if window is destroyed
            if self.clock_display:
                self.clock_display.update()
                self.after(1000, self.update_time)
        except Exception as e:
            self.setup_error_ui(str(e))

    def add_activation_ui(self) -> None:
        """Add license activation UI elements with input validation."""
        license_frame = ctk.CTkFrame(self)
        license_frame.pack(pady=20, padx=20, fill="x")

        license_entry = ctk.CTkEntry(
            master=license_frame, placeholder_text="Enter License Key", width=200
        )
        license_entry.pack(pady=10, padx=10, fill="x")

        # Add validation and activation button
        activate_btn = ctk.CTkButton(
            master=license_frame,
            text="Activate License",
            command=lambda: self.activate_license(license_entry.get().strip()),
        )
        activate_btn.pack(pady=10)

    def activate_license(self, license_key: str) -> None:
        """Handle license activation with input validation.

        Args:
            license_key (str): The license key to validate
        """
        try:
            if not license_key:
                self.show_error_message("Please enter a license key")
                return

            if self.license_manager.activate_license(license_key):
                self.check_license_status()
            else:
                self.show_error_message("Invalid license key!")
        except Exception as e:
            self.show_error_message(str(e))

    def show_error_message(self, message: str) -> None:
        """Display an error message to the user.

        Args:
            message (str): The error message to display
        """
        error_label = ctk.CTkLabel(
            master=self, text=message, text_color="red", font=("Helvetica", 12)
        )
        error_label.pack(pady=10)
        # Auto-remove error message after 3 seconds
        self.after(3000, error_label.destroy)

    def setup_expired_ui(self) -> None:
        """Setup the expired trial UI with clear instructions."""
        label = ctk.CTkLabel(
            master=self,
            text="Trial Period Expired!",
            font=("Helvetica", 16, "bold"),
            text_color="red",
        )
        label.pack(pady=20)

        info_label = ctk.CTkLabel(
            master=self,
            text="Please purchase a license to continue using the application.",
            wraplength=300,
            font=("Helvetica", 12),
        )
        info_label.pack(pady=10)

        self.add_activation_ui()

    def setup_invalid_ui(self) -> None:
        """Setup the invalid license UI with error details."""
        label = ctk.CTkLabel(
            master=self,
            text="Invalid License!",
            font=("Helvetica", 16, "bold"),
            text_color="red",
        )
        label.pack(pady=20)

        info_label = ctk.CTkLabel(
            master=self,
            text="The license is not valid for this machine. Please contact support.",
            wraplength=300,
            font=("Helvetica", 12),
        )
        info_label.pack(pady=10)

    def setup_error_ui(self, error_message: str) -> None:
        """Setup error UI when unexpected errors occur.

        Args:
            error_message (str): The error message to display
        """
        label = ctk.CTkLabel(
            master=self,
            text="An Error Occurred",
            font=("Helvetica", 16, "bold"),
            text_color="red",
        )
        label.pack(pady=20)

        error_label = ctk.CTkLabel(
            master=self, text=error_message, wraplength=300, font=("Helvetica", 12)
        )
        error_label.pack(pady=10)
