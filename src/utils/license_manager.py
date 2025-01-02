"""Module for handling software licensing and trial period management.

This module provides functionality for managing software licenses,
including trial period tracking, license validation, and machine-specific
license management.
"""

import hashlib
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Literal, Optional, Union

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Type aliases
LicenseStatus = Literal["TRIAL", "LICENSED", "INVALID", "EXPIRED"]
LicenseData = Dict[str, Union[str, bool]]


class LicenseManager:
    """Handles license validation and trial period management.

    This class manages software licensing, including trial periods,
    license key validation, and machine-specific license management.

    Attributes:
        license_file (Path): Path to the license data file
        trial_duration (int): Duration of trial period in days
        license_key (Optional[str]): Valid license key from environment
    """

    def __init__(self, trial_duration: int = 30) -> None:
        """Initialize the license manager with default settings.

        Args:
            trial_duration (int, optional): Duration of trial period in days. Defaults to 30.
        """
        self.license_file: Path = Path("license_data.json")
        self.trial_duration: int = trial_duration
        self.license_key: Optional[str] = os.getenv("LICENSE_KEY")

    def generate_machine_id(self) -> str:
        """Generate a unique machine identifier based on hardware info.

        This method creates a unique identifier for the current machine
        using available system information.

        Returns:
            str: A hashed machine identifier

        Note:
            In production, you should use more hardware-specific identifiers
            for better security.
        """
        try:
            # Using username and hostname as a simple machine identifier
            username: str = os.getenv("USERNAME", "unknown")
            hostname: str = os.getenv("COMPUTERNAME", "unknown")
            machine_id: str = f"{username}_{hostname}"
            return hashlib.md5(machine_id.encode()).hexdigest()
        except Exception as e:
            print(f"Error generating machine ID: {e}")
            # Fallback to a temporary ID
            return hashlib.md5(b"temporary").hexdigest()

    def check_license(self) -> LicenseStatus:
        """Check if the software is licensed or in trial period.

        This method validates the current license status by checking
        the license file and trial period.

        Returns:
            LicenseStatus: Current license status
            ('LICENSED', 'TRIAL', 'EXPIRED', or 'INVALID')

        Raises:
            json.JSONDecodeError: If license file is corrupted
            OSError: If there are file system related errors
        """
        try:
            if not self.license_file.exists():
                # First time running - start trial
                trial_data: LicenseData = {
                    "machine_id": self.generate_machine_id(),
                    "trial_start": datetime.now().isoformat(),
                    "is_licensed": False,
                }
                self._save_license_data(trial_data)
                return "TRIAL"

            data: LicenseData = self._load_license_data()

            if data.get("is_licensed"):
                if data["machine_id"] == self.generate_machine_id():
                    return "LICENSED"
                return "INVALID"

            # Check trial period
            trial_start: datetime = datetime.fromisoformat(str(data["trial_start"]))
            if datetime.now() - trial_start > timedelta(
                days=self.trial_duration
            ):
                return "EXPIRED"
            return "TRIAL"

        except (json.JSONDecodeError, OSError) as e:
            print(f"Error checking license: {e}")
            return "INVALID"

    def activate_license(self, license_key: str) -> bool:
        """Activate the software with a license key.

        This method validates the provided license key and activates
        the software if the key is valid.

        Args:
            license_key (str): The license key to validate

        Returns:
            bool: True if activation successful, False otherwise

        Note:
            In production, you should validate the key against a secure server
        """
        try:
            # In production, validate against a server
            valid_key: str | None = os.getenv("LICENSE_KEY")

            if not valid_key:
                print("Warning: No valid license key found in environment")
                return False

            if license_key == valid_key:
                data: LicenseData = self._load_license_data()
                data["is_licensed"] = True
                data["machine_id"] = self.generate_machine_id()
                self._save_license_data(data)
                return True

            return False

        except Exception as e:
            print(f"Error activating license: {e}")
            return False

    def get_remaining_trial_days(self) -> int:
        """Calculate remaining days in trial period.

        Returns:
            int: Number of days remaining in trial period.
            Returns 0 if trial has expired or there's an error.
        """
        try:
            if not self.license_file.exists():
                return self.trial_duration

            data: LicenseData = self._load_license_data()
            if data.get("is_licensed", False):
                return 0

            trial_start: datetime = datetime.fromisoformat(str(data["trial_start"]))
            remaining = (
                self.trial_duration - (datetime.now() - trial_start).days
            )
            return max(0, remaining)

        except Exception as e:
            print(f"Error calculating remaining trial days: {e}")
            return 0

    def _load_license_data(self) -> LicenseData:
        """Load license data from file.

        Returns:
            LicenseData: Dictionary containing license information

        Raises:
            json.JSONDecodeError: If license file is corrupted
            OSError: If there are file system related errors
        """
        with open(self.license_file, "r") as f:
            return json.load(f)

    def _save_license_data(self, data: LicenseData) -> None:
        """Save license data to file.

        Args:
            data (LicenseData): Dictionary containing license information

        Raises:
            OSError: If there are file system related errors
        """
        with open(self.license_file, "w") as f:
            json.dump(data, f)
