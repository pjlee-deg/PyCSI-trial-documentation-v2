"""
Provides access to miscellaneous enumerators classes for use with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Enums.units
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""

from enum import IntEnum


class ItemType(IntEnum):
    '''Item type class enumerator'''

    OBJECTS = 0
    GROUP = 1
    SELECTED_OBJECTS = 2
