"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Model interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol
from typing import Optional

from pyCSI.enums import ForceUnit
from pyCSI.enums import LengthUnit
from pyCSI.enums import TemperatureUnit
from pyCSI.protocols.ianalysis import IAnalysis
from pyCSI.protocols.idatabase import IDatabaseTables
from pyCSI.protocols.ifile import IFile
from pyCSI.protocols.igroup import IGroup
from pyCSI.protocols.imiscellaneous import ICombo
from pyCSI.protocols.imiscellaneous import ILoadCases
from pyCSI.protocols.imiscellaneous import ILoadPatterns
from pyCSI.protocols.iobjects import IArea
from pyCSI.protocols.iobjects import IFrame
from pyCSI.protocols.iobjects import ILink
from pyCSI.protocols.iobjects import IPoint


class IModel(Protocol):
    '''CSI API Sap Model Object'''

    Analyze: IAnalysis
    DatabaseTables: IDatabaseTables
    File: IFile
    LoadCases: ILoadCases
    LoadPatterns: ILoadPatterns
    RespCombo: ICombo
    GroupDef: IGroup
    AreaObj: IArea
    FrameObj: IFrame
    LinkObj: ILink
    PointObj: IPoint

    def GetModelFilename(self, include_path: bool = True) -> str:
        '''Returns a string that represents the filename of the current model, with or without the full path.

        Arguments:
            include_path -- A boolean (True or False) value. When this item is True, the returned filename 
                            includes the full path where the file is located (default: {True})

        Returns:
            String that represents the filename of the current model, with or without the full path
        '''
        ...

    def GetModelFilepath(self) -> str:
        '''Returns the filepath of the current model 

        Returns:
            String that represents the filepath of the current model
        '''
        ...

    def GetModelIsLocked(self) -> bool:
        '''Check the status of the SAP Model

        Returns:
            True if the model is locked, otherwise False
        '''
        ...

    def GetPresentUnits_2(self) -> list[int]:
        '''Retrieves the present units for the model

        Returns:
            A list containing the following:
                ForceUnits
                LengthUnits
                TemperatureUnits
                Zero if units are successfully retrieved, otherwise returns non-zero value'''
        ...

    def GetVersion(self) -> tuple[str, float, int]:
        '''Returns the program version. 

        Returns: A list containing the following
            version: str -- Version of the software
            my_version_number: float -- Program version number internally used by the program.
            return_code: int -- Zero if the information is successfully retrieved
        '''
        ...

    def InitializeNewModel(self) -> int:
        '''Clear the previous model and initializes the program for a new model

        Returns:
            Zero if new model is successfully created, otherwise returns non-zero value
        '''
        ...

    def SetModelIsLocked(self, lock_model: bool) -> int:
        '''Locks or unlocks the model

        Arguments: 
            lock_model -- Model will be locked if True, otherwise it will be unlocked

        Returns:
            Zero if new model is successfully created, otherwise returns non-zero value
        '''
        ...

    def SetPresentUnits_2(self, force_units: ForceUnit, length_units: LengthUnit, temperature_units: TemperatureUnit) -> int:
        '''Sets the present units for the model 

        Arguments:
            force_units -- Value representing the force units to be set
            length_units -- Value representing the length units to be set
            temperature_units -- Value representing the temperature units to be set

        Returns:
            Zero if new model is successfully created, otherwise returns non-zero value
        '''
        ...
