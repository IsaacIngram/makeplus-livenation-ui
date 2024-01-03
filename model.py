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
from typing import Callable

connection_timeout_ms: float = 2000 # Consider a skylight dead if heartbeat hasn't been sent in this time (ms)

class Skylight:

    lock: threading.Lock

    # Data
    id: int
    display_name: str
    target_blackout: float
    target_filter: float
    actual_blackout: float
    actual_filter: float
    last_hb_ms: float # Time of last heartbeat

    # Callback functions
    not_connected_func: Callable[[], None] # Called when skylight is not connected
    connected_func: Callable[[], None] # Called when skylight is connected

    def __init__(
            self, id: int, display_name: str, initial_blackout_val: float, 
            initial_diffuse_val: float, not_connected_callback: Callable[[], None] = None,
            connected_callback: Callable[[], None] = None
            ) -> None:
        """
        Initialize this skylight

        Params:
        id (int): id
        display_name (str): Display name
        initial_blackout_val (float): Initial blackout value
        initial_diffuse_val (float): Initial diffuse value
        not_connected_callback (Callable[[], None]): Optional callback function for when skylight is not connected
        connected_callback (Callable[[], None]): Optional callback function for when skylight is connected
        """
        self.lock = threading.Lock()
        with self.lock:
            self.id = id
            self.display_name = display_name
            self.target_blackout = initial_blackout_val
            self.target_filter = initial_diffuse_val
            self.last_hb_ms = None
            self.not_connected_func = not_connected_callback
            self.connected_func = connected_callback
            self.connected = False
            
            #TODO remove
            self.last_hb_ms = 0

    def get_id(self) -> int:
        """
        Get the ID of this skylight

        Returns:
        int: ID
        """
        return self.id

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
        
    def execute_connected_func(self) -> None:
        """
        Execute the connected callback function if it is set
        """
        if self.connected_func is not None:
            self.connected_func()

    def execute_not_connected_func(self) -> None:
        """
        Execute the not connected callback function if it is set
        """
        if self.not_connected_func is not None:
            self.not_connected_func()
    
    def _update(self):
        """
        Update the values of this skylight based on current status. 
        NOTE: This function handles locking. If this object is already locked,
        an error message will be printed and this function will return before doing anything.
        """
        if self.lock.locked():
            print(f"Error when updating {self} \nAlready locked.")
            return
        
        if time.time() * 1000 > self.last_hb_ms + connection_timeout_ms:
            self.execute_not_connected_func()
        else:
            self.execute_connected_func()
        

class ControllerModes(Enum):
    NORMAL = 0
    PAIRING = 1

_controller_mode: ControllerModes = ControllerModes.NORMAL
_controller_mode_lock: threading.Lock = threading.Lock()
_signal_end: bool = False
_signal_end_lock: threading.Lock = threading.Lock()
_skylights: [Skylight] = []
_skylights_lock: threading.Lock = threading.Lock()
_LOOP_DELAY_MS: float = 200

def add_skylight(
        display_name: str, initial_blackout_val: float, initial_diffuse_val: float, 
        not_connected_callback: Callable[[], None] = None, 
        connected_callback: Callable[[], None] = None
                 ) -> Skylight:
    """
    Add a new skylight

    Params:
    display_name (str): Display name
    initial_blackout_val (float): Initial blackout value
    initial_diffuse_val (float): Initial diffuse value
    not_connected_callback (Callable[[], None]): Optional callback function for when skylight is not connected
        connected_callback (Callable[[], None]): Optional callback function for when skylight is connected

    Returns:
    Skylight: The Skylight object that was added
    """
    with _skylights_lock:
        skylight = Skylight(len(_skylights), display_name, initial_blackout_val, initial_diffuse_val, not_connected_callback, connected_callback)
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
            # Pairing mode
            # TODO implement pairing logic
            print("Pairing mode")

        else:
            # Normal mode
            # print("Normal mode")

            # Update all skylights
            with _skylights_lock:

                for skylight in _skylights:
                    skylight._update()

            
        # Wait for next iteration
        while time.time() < (last_loop_ms + _LOOP_DELAY_MS) / 1000:
            pass
        last_loop_ms = time.time() * 1000
