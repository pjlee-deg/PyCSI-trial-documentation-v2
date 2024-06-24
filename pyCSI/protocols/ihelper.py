"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Helper interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol
from typing import Optional

from pyCSI.protocols import IApi


class IHelper(Protocol):
    '''CSI API Helper object'''

    def CreateObject(self, full_path: str) -> IApi | None:
        '''Starts API at the given path

        Returns:
            An instance of APIObject if successful, None otherwise
        '''
        ...

    def CreateObjectProgID(self, program_ID: str) -> IApi | None:
        '''Starts the program and returns the API object for the given program ID

        Returns:
            An instance of APIObject if successful, None otherwise
        '''
        ...

    def GetObject(self, program_ID: str) -> IApi | None:
        '''Attaches to running instance of the program

        Returns:
            An instance of APIObject if successful, None otherwise
        '''
        ...

    def GETOAPIVersionNumber(self) -> float:
        '''Retrieves the API version

        Returns:
            API version number as a float value
        '''
        ...
