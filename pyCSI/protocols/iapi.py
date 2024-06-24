"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: API interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol
from typing import Optional

from pyCSI.protocols.imodel import IModel


class IApi(Protocol):
    '''CSI API Object'''

    SapModel: IModel

    def ApplicationExit(self, FileSave: bool) -> int:
        '''Exits the application

        Returns:
            Zero if the function succeeds and nonzero if it fails'''
        ...

    def ApplicationStart(self) -> None:
        '''Start the application'''
        ...

    def GETOAPIVersionNumber(self) -> float:
        '''Retrieves the API version implemented by the GUI

        Returns:
            API version number as a float value
        '''
        ...

    def Hide(self) -> int:
        '''This function hides the application making it not visible on the screen or on the Windows task bar

        Returns:
            Zero if window is successfully hidden, otherwise returns non-zero value
        '''
        ...

    def Unhide(self) -> int:
        '''This function unhide the application, making it visible on the screen or on the Windows task bar

        Returns:
            Zero if window is successfully unhidden, otherwise returns non-zero value
        '''
        ...

    def Visible(self) -> bool:
        '''Return application visibility

        Returns:
            True if the application is visible, otherwise returns False
        '''
        ...
