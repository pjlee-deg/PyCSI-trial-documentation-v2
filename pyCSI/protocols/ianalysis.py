"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Analysis interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Optional
from typing import Protocol


class IAnalysis(Protocol):
    '''CSI API Analyze Interface'''

    def DeleteResults(self, name: str, all: Optional[bool] = False) -> int:
        '''Deletes results for load cases

        Keyword Arguments:
            name -- Name of an existing load case whose results will be deleted \n
            all -- Optional. If true, the results are deleted for all load cases, and the name argument is ignored
                    (default: {False})
         Returns:
            Zero if the results are successfully deleted, otherwise returns a nonzero value
        '''
        ...

    def GetRunCaseFlag(self) -> tuple[int, list[str], list[bool], int]:
        '''Retrieves the run flags for all analysis cases

        Returns: A list containing the following
            number_items: int -- The number of load cases for which the run flag us reported \n
            case_name: list[str] -- A list containing the names of each analysis case for which the run flag is reported \n
            run: list[bool] -- A list containing wether the specified load case is set to be run \n
            return_code: int -- Returns zero if the flags are successfully retrieved; otherwise returns a nonzero value
            '''
        ...

    def RunAnalysis(self) -> int:
        '''Runs the analysis

        Returns:
            Zero if the analysis model is successfully run, otherwise returns a nonzero value
        '''
        ...

    def SetRunCaseFlag(self, name: str, run: bool, all: Optional[bool] = False) -> int:
        '''Set the run flag for load cases

        Arguments:
            name -- The name of an existing load case that is to have its run flag set. This argument is ignored when 
                    all is set to True \n
            run -- If True, the specified load case is to be run \n
            all -- If True, the run flag is set as specified by the run item for all load cases, and the name argument
                    is ignored (default: {False})

        Returns:
            Returns zero if the flag is successfully set; otherwise it returns a nonzero value
        '''
        ...
