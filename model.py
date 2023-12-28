###############################################################################
#
# File: model.py
#
# Author: Isaac Ingram
#
# Purpose: Run a parallel thread to the UI that connects to skylights and 
# updates their values based on the UI
#
###############################################################################

import time
import threading
from enum import Enum

class Skylight:

    lock: threading.Lock

    # Data
    id: int
    display_name: str
    target_blackout: float
    target_filter: float
    actual_blackout: float
    actual_filter: float
    last_hb_millis: float # Time of last heartbeat

    def __init__(self, id: int, display_name: str, initial_blackout_val: float, initial_diffuse_val: float) -> None:
        """
        Initialize this skylight

        Params:
        id (int): id
        """
        self.id = id
        self.lock = threading.Lock()
        self.display_name = display_name
        self.target_blackout = initial_blackout_val
        self.target_filter = initial_diffuse_val
        self.last_hb_millis = None

    def get_id(self) -> int:
        """
        Get the ID of this skylight

        Returns:
        int: ID
        """
        with self.lock:
            return self.id

    def get_display_name(self) -> str:
        """
        Get the display name

        Returns:
        str: The display name of this skylight
        """
        with self.lock:
            return self.display_name
    
    def set_blackout(self, val: float) -> None:
        """
        Set the blackout value

        Params:
        val (float): Value
        """
        with self.lock:
            self.target_blackout = val

    def set_filter(self, val: float) -> None:
        """
        Set the filter value

        Params:
        val (float): Value
        """
        with self.lock:
            self.target_filter = val

    def get_blackout(self) -> float:
        """
        Get the current blackout value (actual, NOT target)

        Returns:
        float: Value
        """
        with self.lock:
            return self.actual_blackout
    
    def get_filter(self) -> float:
        """
        Get the current filter value (actual, NOT target)

        Returns:
        float: Value
        """
        with self.lock:
            return self.actual_filter
    
    def _update():
        """
        Update the values of this skylight based on current
        """
        #TODO implement

class ControllerModes(Enum):
    NORMAL = 0
    PAIRING = 1

_controller_mode: ControllerModes = ControllerModes.NORMAL
_controller_mode_lock: threading.Lock = threading.Lock()
_signal_end: bool = False
_signal_end_lock: threading.Lock = threading.Lock()
_skylights: [Skylight] = []
_skylights_lock: threading.Lock = threading.Lock()
_LOOP_DELAY_MS: float = 100

def add_skylight(display_name: str, initial_blackout_val: float, initial_diffuse_val: float) -> Skylight:
    """
    Add a new skylight

    Params:
    display_name (str): Display name
    initial_blackout_val (float): Initial blackout value
    initial_diffuse_val (float): Initial diffuse value

    Returns:
    Skylight: The Skylight object that was added
    """
    with _skylights_lock:
        skylight = Skylight(len(_skylights), display_name, initial_blackout_val, initial_diffuse_val)
        _skylights.append(skylight)
    return skylight

def clear_skylights():
    """
    Clear all skylights
    """
    with _skylights_lock:
        _skylights.clear()

def enter_pairing_mode():
    """
    Switch to pairing mode
    """
    global _controller_mode, _controller_mode_lock, _signal_end, _signal_end_lock
    with _controller_mode_lock:
        _controller_mode = ControllerModes.PAIRING

def enter_normal_mode():
    """
    Switch to normal mode
    """
    global _controller_mode, _controller_mode_lock, _signal_end, _signal_end_lock
    with _controller_mode_lock:
        _controller_mode = ControllerModes.NORMAL

def signal_stop():
    """
    Signal to all threads that they should stop
    """
    global _signal_end, _signal_end_lock

    with _signal_end_lock:
        _signal_end = True

def main_loop():
    """
    Main loop responsible for controlling all skylights
    """
    global _controller_mode, _controller_mode_lock, _signal_end, _signal_end_lock
    last_loop_ms: float = time.time()*1000

    while True:

        # Break out of loop if the end flag was set
        with _signal_end_lock:
            if _signal_end:
                break

        # Store current controller mode
        with _controller_mode_lock:
            mode = _controller_mode

        if mode == ControllerModes.PAIRING:
            # TODO implement pairing logic
            print("Pairing mode...")
        else:
            # Normal mode
            print("Normal mode")
            with _skylights_lock:
                for skylight in _skylights:
                    print(f"\t{skylight.display_name}")

        # Wait for next iteration
        while time.time() < (last_loop_ms + _LOOP_DELAY_MS) / 1000:
            pass
        last_loop_ms = time.time() * 1000
