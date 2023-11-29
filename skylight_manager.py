###############################################################################
#
# File: skylight_manager.py
#
# Author: Isaac Ingram
#
# Purpose: Facilitate storage and control of skylights 
#
###############################################################################


class Skylight:
    id: int
    display_name: str
    target_blackout_val: float
    target_diffuse_val: float
    actual_blackout_val: float
    actual_diffuse_val: float

    def __init__(self, id: int, display_name: str, initial_blackout_val: float, initial_diffuse_val: float) -> None:
        """
        Initialize this skylight

        Params:
        id (int): id
        """
        self.id = id
        self.display_name = display_name
        self.target_blackout_val = initial_blackout_val
        self.target_diffuse_val = initial_diffuse_val

_skylights: dict[int, Skylight] = dict()


def add(display_name: str) -> Skylight:
    """
    Add a skylight

    Params:
    display_name (str): Display name for this skylight

    Return:
    Skylight: Created Skylight object
    """
    # Generate new id
    id = len(_skylights) + 1
    # If this id is already taken, increment until free ID is found
    while id in _skylights:
        id += 1
    # Create skylight
    new_skylight = Skylight(
        id,
        display_name,
        #TODO consider making it so initial value can be set? Thinking if power goes out that
        # initial value shoudl be set to the value the skylight already has
    )

def remove_all():
    """
    Remove all skylights from the manager
    """
    _skylights.clear()

def get(id: int) -> Skylight:
    """
    Get a skylight object

    Params:
    id (int): The id of the skylight

    Return:
    Skylight: A Skylight object, or None if it doesn't exist
    """
    for key in _skylights:
        if _skylights[key].id == id:
            return _skylights[key]
    return None

def get_display_name(id: int):
    """
    Get the display name of a skylight

    Params:
    id (int): The id of the skylight

    Return:
    str: The display name of the skylight, or None if it doesn't exist
    """
    skylight = get(id)
    if skylight is None:
        return None
    else:
        return skylight.display_name

def get_target_diffuse(id: int) -> int:
    """
    Get the target diffuse value

    Params:
    id (int): The id of the skylight

    Return:
    float: The target diffuse value, or None if it doesn't exist
    """
    skylight = get(id)
    if skylight is None:
        return None
    else:
        return skylight.target_diffuse_val

def get_target_blackout(id: int):
    """
    Get the target blackout value

    Params:
    id (int): The id of the skylight

    Return:
    float: The target blackout value, or None if it doesn't exist
    """
    skylight = get(id)
    if skylight is None:
        return None
    else:
        return skylight.target_blackout_val

def get_actual_diffuse(id: int):
    """
    Get the target diffuse value

    Params:
    id (int): The id of the skylight

    Return:
    float: The actual diffuse value of the skylight, or None if it doesn't exist
    """
    skylight = get(id)
    if skylight is None:
        return None
    else:
        return skylight.actual_diffuse_val

def get_actual_blackout(id: int):
    """
    Get the actual blackout value

    Params:
    id (int): The id of the skylight

    Return:
    float: The actual blackout value of the skylight, or None if it doesn't exist
    """
    skylight = get(id)
    if skylight is None:
        return None
    else:
        return skylight.actual_blackout_val

def set_target_diffuse(id: int, value: float) -> bool:
    """
    Set the target diffuse value

    Params:
    id (int): The id of the skylight
    value (float): The new diffuse value

    Return:
    bool: Whether there was as an error when setting
    """
    skylight = get(id)
    if skylight is None:
        return True
    else:
        skylight.target_diffuse_val = value
        return False

def set_target_blackout(id: int, value: float) -> None:
    """
    Set the target blackout value

    Params:
    id (int): The id of the skylight
    value (float): The new blackout value

    Return:
    bool: Whether there was an error when setting
    """
    skylight = get(id)
    if skylight is None:
        return True
    else:
        skylight.target_blackout_val = value