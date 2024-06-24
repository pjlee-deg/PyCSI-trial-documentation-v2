"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: File interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol
from typing import Optional


class IFile(Protocol):
    '''CSI API FIle Interface'''

    def OpenFile(self, file_name: str) -> int:
        '''Opens an existing model file

        Arguments:
            file_name -- The full path of a model to be opened in the application

        Returns:
            Zero if the file is successfully opened and nonzero if it is not opened
        '''
        ...

    def Save(self, file_name: str = '') -> int:
        '''Saves the present model

        Keyword Arguments:
            file_name -- Optional, the full path to which the model is saved, if omitted the file is saved using 
                        the current name. If the file has not been saved previously and file_name is omitted an error 
                        will be returned (default: '')

        Returns:
            Zero if the file is successfully saved and nonzero if it is not saved
        '''
        ...
