"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Miscellaneous interfaces
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol
from typing import Optional


class ICombo(Protocol):
    '''CSI API Load Combinations Interface'''

    def GetNameList(self) -> tuple[int, tuple[str], int]:
        '''Retrieves the name of all defined load combinations

        Returns:
            A list containing the following:
                number_load_cases -- The number of load cases returned by the request
                load_cases -- A list of the available load cases names of the specified type
                return_code -- Zero if the request was successful, otherwise return a nonzero value
        '''
        ...


class ILoadCases(Protocol):
    '''CSI API Load Cases Interface'''

    def GetNameList(self) -> tuple[int, tuple[str], int]:
        '''Retrieves the name of all defined load cases

        Returns:
            A list containing the following:
                number_load_cases -- The number of load cases returned by the request
                load_cases -- A list of the available load cases names of the specified type
                return_code -- Zero if the request was successful, otherwise return a nonzero value
        '''
        ...


class ILoadPatterns(Protocol):
    '''CSI API Load Cases Interface'''

    def GetNameList(self) -> tuple[int, tuple[str], int]:
        '''Retrieves the name of all defined load patterns

        Returns:
            A list containing the following:
                number_load_patterns -- The number of load cases returned by the request
                load_patterns -- A list of the available load cases names of the specified type
                return_code -- Zero if the request was successful, otherwise return a nonzero value
        '''
        ...
