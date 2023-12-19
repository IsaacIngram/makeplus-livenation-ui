###############################################################################
#
# File: skylight_model.py
#
# Author: Isaac Ingram
#
# Purpose: Facilitate storage and control of skylights 
#
###############################################################################


class Skylight:
    id: int
    display_name: str
    target_blackout: float
    target_filter: float
    actual_blackout: float
    actual_filter: float

    def __init__(self, id: int, display_name: str, initial_blackout_val: float, initial_diffuse_val: float) -> None:
        """
        Initialize this skylight

        Params:
        id (int): id
        """
        self.id = id
        self.display_name = display_name
        self.target_blackout = initial_blackout_val
        self.target_filter = initial_diffuse_val

    def get_id(self) -> int:
        """
        Get the ID of this skylight

        Returns:
        int: ID
        """

    def get_display_name(self) -> str:
        """
        Get the display name

        Returns:
        str: The display name of this skylight
        """
        return self.display_name
    
    def set_blackout(self, val: float) -> None:
        """
        Set the blackout value

        Params:
        val (float): Value
        """
        self.target_blackout = val

    def set_filter(self, val: float) -> None:
        """
        Set the filter value

        Params:
        val (float): Value
        """
        self.target_filter = val

    def get_blackout(self) -> float:
        """
        Get the current blackout value (actual, NOT target)

        Returns:
        float: Value
        """
        return self.actual_blackout
    
    def get_filter(self) -> float:
        """
        Get the current filter value (actual, NOT target)

        Returns:
        float: Value
        """
        return self.actual_filter
