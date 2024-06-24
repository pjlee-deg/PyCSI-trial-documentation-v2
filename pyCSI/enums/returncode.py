"""
Provides access to Return Code enumerators classes for use with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Enums.returncode
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""

from enum import IntEnum


class ReturnCode(IntEnum):
    '''Return Code enumerator class'''

    NOT_APPLICABLE = -100
    NOT_IMPLEMENTED = -99
    NO_ERROR = 0
    UNSPECIFIED_ERROR = 1
    DEPRECATED = -98
    TABLE_OBSOLETE = -97
    TABLE_DOES_NOT_EXIST = -96
