"""
Provides protocol definitions for the Base Model class, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Model interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file


from typing import ClassVar
from typing import Optional
from typing import Protocol

from pyCSI.enums import ForceUnit
from pyCSI.enums import LengthUnit
from pyCSI.enums import TemperatureUnit
from pyCSI.protocols.imodel import IModel


class BaseModel(Protocol):
    '''Base Model class for CSI API connection'''

    CLSID: ClassVar[str]
    SOFTWARE: ClassVar[str]

    # Class properties
    visible: bool
    api_path: str | None
    lock: bool | None

    ##################################################################################################################
    # Setup
    ###################################################################################################################

    def __get_installation_path(self, custom_path: Optional[str]) -> str:
        '''Set CSI install folder location, if provided a custom path will be used, otherwise the default installation
        folder is considered

        Arguments:
        custom_path -- Optional, Custom path to CSI installation folder,
                        example: C:/Program Files/Computers and Structures (default: {None})
        '''
        ...

    def __get_api_path(self, version: Optional[int]) -> str | None:
        '''Set path to API executable, this is used when creating a new instance of the program

        Arguments:
            software_version -- Version of the CSI software, if not provided the default API will be used
                                (default: None)
        '''
        ...

    ###################################################################################################################
    # API methods
    ###################################################################################################################

    def get_model(self, active_model: bool = True, file_location: Optional[str] = None, visibility: bool = True):
        '''Connects to an active or a new window of the software

        Keyword Arguments:
            active_model -- Optional. If True, connects to active instance of the model, otherwise creates a 
                            new window (default: True)

            The following arguments will be ignored if active_model is True
            file_location -- Optional. Complete path to model file as string. If not provided a new model will
                            be initialized (default = None) \n
            visibility -- Optional. If true sets the application window visible on the screen,
                            otherwise it is hidden (default = True)
        '''
        ...

    ###################################################################################################################
    # Model methods
    ###################################################################################################################

    def get_model_object(self) -> IModel:
        '''Returns the instance of the model object'''
        ...

    def set_units(self, force_unit: ForceUnit = ForceUnit.KIP, length_unit: LengthUnit = LengthUnit.FT,
                  temperature_unit: TemperatureUnit = TemperatureUnit.F):
        '''Sets the present units for the model 

        Arguments:
            force_unit -- Optional. Value representing the force units to be set. See ForceUnit.help() for valid
                            values (default: ForceUnit.KIP) \n
            length_unit -- Optional. Value representing the length units to be set. See LengthUnit.help() for valid
                             values (default: LengthUnit.FT) \n
            temperature_unis -- Optional. Value representing the temperature units to be set.
                                See TemperatureUnit.help() for valid values (default: TemperatureUnit.F)
        '''
        ...

    def get_file_name(self, include_path: bool = False) -> str:
        '''Get file name of current model instance

        Arguments:
            include_path -- If true, the returned file name includes full path of the model (default: {False})

        Returns:
            File name of current instance of model
        '''
        ...

    def get_file_path(self) -> str:
        '''Get file path of current model instance

        Returns:
            File path of current instance of model
        '''
        ...

    def new_model(self) -> None:
        '''Initialize a new model on the active api_object'''
        ...

    def get_load_cases(self) -> list[str]:
        '''Get the load cases defined in the model

        Returns:
            A list of strings that contain the name of all the load cases defined in the model
        '''
        ...

    def get_load_combos(self) -> list[str]:
        '''Get the load combinations defined in the model

        Returns:
            A list of strings that contain the name of all the load combinations defined in the model
        '''
        ...

    def get_load_patterns(self) -> list[str]:
        '''Get the load patterns defined in the model

        Returns:
            A list of strings that contain the name of all the load patterns defined in the model
        '''
        ...

    def close_model(self, save_model: bool = True):
        ...
