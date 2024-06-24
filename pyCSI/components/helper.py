"""
====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Helper Class
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|

Gives access to the CSI API Helper Interface
"""

from typing import cast
from typing import Optional

from comtypes.client import CreateObject

from pyCSI.protocols import IHelper
from pyCSI.protocols import IApi


class Helper:
    '''Represents the CSI API Helper Object

    Arguments:
            clsid --Class ID that represents the API Object to be created. 
                    Valid CLIDs:
                    ETABS: 'CSI.ETABS.API.ETABSObject' \n
                    SAP2000: 'CSI.SAP2000.API.SapObject' \n
                    SAFE: 'CSI.SAFE.API.ETABSObject'
    '''

    HELPER_CLSID = 'CSiAPIv1.Helper'

    def __init__(self, clsid: str) -> None:
        # Use cast function to assign helper object as type IHelper
        helper_object = cast(IHelper, CreateObject(self.HELPER_CLSID))
        self.helper = helper_object
        self.clsid: str = clsid

    def get_api_object(self) -> IApi | None:
        '''Gets the active API Object

        Returns:
            APIObject if successful, otherwise None
        '''
        return self.helper.GetObject(self.clsid)

    def create_api_object(self, api_path: Optional[str] = None) -> IApi | None:
        '''Creates a new instance of the API Object

        Returns:
            APIObject if successful, otherwise None
        '''

        if api_path is None:
            # Creates the default API Object
            return self.helper.CreateObjectProgID(self.clsid)

        # Create a new API from the specified path
        return self.helper.CreateObject(api_path)
