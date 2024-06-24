"""
====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Model Classes
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|

CSI API Model Classes. Gives access to model properties and methods for different CSI software
"""
import os
from typing import cast
from typing import Optional

from pyCSI.components import Analysis
from pyCSI.components import File
from pyCSI.components import Group
from pyCSI.components import Helper
from pyCSI.components import Tables
from pyCSI.enums import ForceUnit
from pyCSI.enums import LengthUnit
from pyCSI.enums import TemperatureUnit
from pyCSI.protocols import IModel
from pyCSI.protocols import IApi
from pyCSI.utils import APIConnectionError
from pyCSI.utils import raise_api_error
from pyCSI.utils import raise_model_error
from pyCSI.utils import check_request
from pyCSI.utils import check_valid_model


class ETABSModel:
    '''ETABS Model class for CSI API connection

    Arguments:
            software_version -- Optional. Version of the software as an integer, this argument will be ignored when
                                connecting to an existing instance of a model (default: {None})
            custom_path -- Optional. Custom path to CSI installation folder. If not provided the default path will
                            be considered (default: {None})
    '''

    CLSID = 'CSI.ETABS.API.ETABSObject'
    SOFTWARE = 'ETABS'

    def __init__(self, version: Optional[int] = None, custom_path: Optional[str] = None) -> None:
        # Class private properties
        self._software_version: Optional[int] = version
        self._installation_path: str = self.__get_installation_path(custom_path)
        self._helper: Helper = Helper(self.CLSID)  # Create Helper object
        self._api_object: IApi | None = None
        self._model_object: IModel | None = None

        # Class properties
        self._visible: bool | None = None
        self.api_path: str | None = self.__get_api_path(self._software_version)
        self._lock: bool | None = None
        self._force_unit: str | None = None
        self._length_unit: str | None = None
        self._temperature_unit: str | None = None
        self._analysis: Analysis | None = None
        self._file: File | None = None
        self._group: Group | None = None
        self._tables: Tables | None = None
        self.connected_to_model: bool = False

    ###################################################################################################################
    # Properties getters
    ###################################################################################################################

    @property
    def software_version(self) -> int:
        '''ETABS GUI version

        Returns:
            Current assigned version of ETABS GUI in int format
        '''
        if self._model_object is None:
            raise_model_error(self.SOFTWARE)

        if self._software_version is None:
            request = self._model_object.GetVersion()
            check_request(request[-1])
            version = request[0].split('.')[0]
            self._software_version = int(version)

        return self._software_version

    @property
    def installation_path(self) -> str:
        '''Path for the CSI installation folder, default path is %ProgramFiles%/Computers and Structures'''
        return self._installation_path

    @property
    def visible(self) -> bool:
        '''Boolean that represents window visibility. If True window is visible, otherwise is hidden'''
        if self._api_object is None:
            raise_api_error()

        if self._visible is None:
            self._visible = self._api_object.Visible()

        return self._visible

    @property
    def lock(self) -> bool:
        '''Boolean that represents the lock/unlocked state of the model'''

        if self._lock is None:
            raise_model_error(self.SOFTWARE)

        return self._lock

    @property
    def force_unit(self) -> str:
        '''String that represents the current model force units. If return_enum is True, the Python enumerator
        representation of the unit is returned'''

        if self._force_unit is None:
            raise_model_error(self.SOFTWARE)

        return self._force_unit

    @property
    def length_unit(self) -> str:
        '''String that represents the current model length units. If return_enum is True, the Python enumerator
        representation of the unit is returned'''

        if self._length_unit is None:
            raise_model_error(self.SOFTWARE)

        return self._length_unit

    @property
    def temperature_unit(self) -> str:
        '''String that represents the current model temperature units. If return_enum is True, the Python enumerator
        representation of the unit is returned'''

        if self._temperature_unit is None:
            raise_model_error(self.SOFTWARE)

        return self._temperature_unit

    @property
    def analysis(self) -> Analysis:
        '''Class property that gives access to analysis operations'''

        if self._analysis is None:
            raise_model_error(self.SOFTWARE)

        return self._analysis

    @property
    def file(self) -> File:
        '''Class property that gives access to file operations'''

        if self._file is None:
            raise_model_error(self.SOFTWARE)

        return self._file

    @property
    def group(self) -> Group:
        '''Class property that gives access to group operations'''

        if self._group is None:
            raise_model_error(self.SOFTWARE)

        return self._group

    @property
    def tables(self) -> Tables:
        '''Class property that gives access to the model database tables'''

        if self._tables is None:
            raise_model_error(self.SOFTWARE)

        return self._tables

    ###################################################################################################################
    # Properties setters
    ###################################################################################################################

    @visible.setter
    def visible(self, visibility: bool) -> None:
        if self._api_object is None:
            raise_api_error()

        if visibility:
            return_code: int = self._api_object.Unhide()
        else:
            return_code: int = self._api_object.Hide()

        check_request(return_code)
        self._visible = visibility

    @lock.setter
    def lock(self, lock_it: bool):
        if self._model_object is None:
            raise_model_error(self.SOFTWARE)

        return_code: int = self._model_object.SetModelIsLocked(lock_it)
        check_request(return_code)
        self._lock = lock_it

    @force_unit.setter
    def force_unit(self, unit: ForceUnit):
        if self._model_object is None:
            raise_model_error(self.SOFTWARE)

        length_unit_label = cast(str, self._length_unit)
        length_unit = LengthUnit[length_unit_label]

        temp_unit_label = cast(str, self._temperature_unit)
        temperature_unit = TemperatureUnit[temp_unit_label]

        self.set_units(unit, length_unit, temperature_unit)
        self._force_unit = unit.name

    @length_unit.setter
    def length_unit(self, unit: LengthUnit):
        if self._model_object is None:
            raise_model_error(self.SOFTWARE)

        force_unit_label = cast(str, self._force_unit)
        force_unit = ForceUnit[force_unit_label]

        temp_unit_label = cast(str, self._temperature_unit)
        temperature_unit = TemperatureUnit[temp_unit_label]

        self.set_units(force_unit, unit, temperature_unit)
        self._length_unit = unit.name

    @temperature_unit.setter
    def temperature_unit(self, unit: TemperatureUnit):
        if self._model_object is None:
            raise_model_error(self.SOFTWARE)

        force_unit_label = cast(str, self._force_unit)
        force_unit = ForceUnit[force_unit_label]

        length_unit_label = cast(str, self._length_unit)
        length_unit = LengthUnit[length_unit_label]

        self.set_units(force_unit, length_unit, unit)
        self._temperature_unit = unit.name

    @analysis.setter
    def analysis(self, new_value: Analysis | None):
        if isinstance(new_value, Analysis) or new_value is None:
            self._analysis = new_value
        else:
            raise ValueError('New value must be an instance of Analysis class')

    @file.setter
    def file(self, new_value: File | None):
        if isinstance(new_value, File) or new_value is None:
            self._file = new_value
        else:
            raise ValueError('New value must be an instance of File class')

    @group.setter
    def group(self, new_value: Group | None):
        if isinstance(new_value, Group) or new_value is None:
            self._group = new_value
        else:
            raise ValueError('New value must be an instance of Group class')

    @tables.setter
    def tables(self, new_value: Tables | None):
        if isinstance(new_value, Tables) or new_value is None:
            self._tables = new_value
        else:
            raise ValueError('New value must be an instance of Tables class')

    ###################################################################################################################
    # Setup
    ###################################################################################################################

    def __get_installation_path(self, custom_path: Optional[str]) -> str:
        '''Set CSI install folder location, if provided a custom path will be used, otherwise the default installation
        folder is considered

        Arguments:
        custom_path -- Optional, Custom path to CSI installation folder,
                        example: C:/Program Files/Computers and Structures (default: {None})
        '''
        if custom_path is not None:
            return custom_path

        return os.sep.join([os.environ["ProgramFiles"], "Computers and Structures"])

    def __get_api_path(self, version: Optional[int]) -> str | None:
        '''Set path to API executable, this is used when creating a new instance of the program

        Arguments:
            software_version -- Version of the CSI software, if not provided the default API will be used
                                (default: None)
        '''

        if version is None:
            return None

        # Define ETABS version folder and exec file
        software_version: str = self.SOFTWARE + ' ' + str(version)
        software_executable: str = self.SOFTWARE + '.exe'
        return os.sep.join([self.installation_path, software_version, software_executable])

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
                            be initialized (default = None)
            visibility -- Optional. If true sets the application window visible on the screen,
                            otherwise it is hidden (default = True)
        '''
        if active_model:
            # Attach to active model
            self._connect_to_active_model()
        else:
            # Creates a new instance
            self._create_new_instance(visibility)

        if file_location is not None:
            # Open the specified model
            self.file.open_file(file_location)

    def _connect_to_active_model(self) -> None:
        '''Attach to active running instance of the program'''
        self._api_object = self._helper.get_api_object()

        if self._api_object is not None:
            self._set_model_object(self._api_object.SapModel)
            print(f'Successfully connected to {self.get_file_name()}')
        else:
            raise APIConnectionError(f'an error ocurred while connecting to {self.SOFTWARE} model')

    def _create_new_instance(self, visibility: bool):
        '''Creates and attach to a new instance of the program

        Arguments:
            visibility -- If true sets the application window visible on the screen, otherwise it is hidden
        '''
        self._api_object = self._helper.create_api_object(self.api_path)
        if self._api_object is not None:
            self._api_object.ApplicationStart()
            self.visible = visibility
            self._set_model_object(self._api_object.SapModel)
        else:
            raise APIConnectionError(f'an error ocurred while connecting to {self.SOFTWARE} model')

    def _set_model_object(self, model_object: IModel | None) -> None:
        '''Sets instance of model_object and instantiates the model subclasses.

        Arguments:
            model_object -- Instance of Sap Model Interface
        '''

        self._model_object = model_object
        self.connected_to_model = model_object is not None

        # Instantiate API Interfaces with new SapModel
        if self._model_object is not None:
            self._lock = self._model_object.GetModelIsLocked()
            self._force_unit = self.get_units()[0].name
            self._length_unit = self.get_units()[1].name
            self._temperature_unit = self.get_units()[2].name
            self.analysis = Analysis(self)
            self.file = File(self)
            self.group = Group(self)
            self.tables = Tables(self)
        else:
            self._lock = None
            self._force_unit = None
            self._length_unit = None
            self._temperature_unit = None
            self.analysis = None
            self.file = None
            self.group = None
            self.tables = None

    ###################################################################################################################
    # Model methods
    ###################################################################################################################

    @check_valid_model
    def get_model_object(self) -> IModel:
        '''Returns the instance of the model object'''
        model_object = cast(IModel, self._model_object)
        return model_object

    @check_valid_model
    def set_units(self, force_unit: ForceUnit = ForceUnit.KIP, length_unit: LengthUnit = LengthUnit.FT,
                  temperature_unit: TemperatureUnit = TemperatureUnit.FAHRENHEIT):
        '''Sets the present units for the model

        Arguments:
            force_unit -- Optional. Value representing the force units to be set. See ForceUnit.help() for valid
                            values (default: ForceUnit.KIP)
            length_unit -- Optional. Value representing the length units to be set. See LengthUnit.help() for valid
                             values (default: LengthUnit.FT)
            temperature_unis -- Optional. Value representing the temperature units to be set.
                                See TemperatureUnit.help() for valid values (default: TemperatureUnit.FAHRENHEIT)
        '''
        model_object = cast(IModel, self._model_object)
        return_code: int = model_object.SetPresentUnits_2(force_unit, length_unit, temperature_unit)
        check_request(return_code)

        self._force_unit = force_unit.name
        self._length_unit = length_unit.name
        self._temperature_unit = temperature_unit.name

    @check_valid_model
    def get_units(self) -> tuple[ForceUnit, LengthUnit, TemperatureUnit]:
        '''Gets the present units for the model

        Returns: A list containing the following
            force_unit: ForceUnit
            length_unit: LengthUnit
            temperature_unis: TemperatureUnit
        '''
        model_object = cast(IModel, self._model_object)
        units: list[int]
        return_code: int
        *units, return_code = model_object.GetPresentUnits_2()
        check_request(return_code)

        return ForceUnit(units[0]), LengthUnit(units[1]), TemperatureUnit(units[2])

    @check_valid_model
    def get_file_name(self, include_path: bool = False) -> str:
        '''Get file name of current model instance

        Arguments:
            include_path -- If true, the returned file name includes full path of the model (default: {False})

        Returns:
            File name of current instance of model
        '''

        model_object = cast(IModel, self._model_object)
        return model_object.GetModelFilename(include_path)

    @check_valid_model
    def get_file_path(self) -> str:
        '''Get file path of current model instance

        Returns:
            File path of current instance of model
        '''

        model_object = cast(IModel, self._model_object)
        return model_object.GetModelFilepath()

    @check_valid_model
    def get_load_cases(self) -> list[str]:
        '''Get the load cases defined in the model

        Returns:
            A list of strings that contain the name of all the load cases defined in the model
        '''

        model_object = cast(IModel, self._model_object)
        api_return = model_object.LoadCases.GetNameList()

        # Unpack return from API
        load_cases: tuple[str]
        return_code: int
        _, load_cases, return_code = api_return
        check_request(return_code)

        # Remove Load Cases generated by the software
        return [load_case for load_case in load_cases if '~' not in load_case]

    @check_valid_model
    def get_load_combos(self) -> list[str]:
        '''Get the load combinations defined in the model

        Returns:
            A list of strings that contain the name of all the load combinations defined in the model
        '''

        model_object = cast(IModel, self._model_object)
        api_return = model_object.RespCombo.GetNameList()

        # Unpack return from API
        load_combos: tuple[str]
        return_code: int
        _, load_combos, return_code = api_return
        check_request(return_code)

        # Remove Load Cases generated by the software
        return [load_combo for load_combo in load_combos if '~' not in load_combo]

    @check_valid_model
    def get_load_patterns(self) -> list[str]:
        '''Get the load patterns defined in the model

        Returns:
            A list of strings that contain the name of all the load patterns defined in the model
        '''

        model_object = cast(IModel, self._model_object)
        api_return = model_object.LoadPatterns.GetNameList()

        # Unpack return from API
        load_patterns: tuple[str]
        return_code: int
        _, load_patterns, return_code = api_return
        check_request(return_code)

        # Remove Load Pattern generated by the software
        return [load_pattern for load_pattern in load_patterns if '~' not in load_pattern]

    def close_application(self, save_model: bool = True):
        '''Closes the current model object. If save_model is True, the model is saved in its current location
        before closing

        Keyword Arguments:
            save_model -- If True, saves the model before closing (default: {True})
        '''

        if self._api_object is not None:
            self._api_object.ApplicationExit(save_model)
            self._set_model_object(None)
            self._api_object = None


class SAPModel(ETABSModel):
    '''SAP Model class for CSI API connection

    Arguments:
            software_version -- Optional. Version of the software as an integer, this argument will be ignored when
                                connecting to an existing instance of a model (default: {None})
            custom_path -- Optional. Custom path to CSI installation folder. If not provided the default path will
                            be considered (default: {None})
    '''

    CLSID = 'CSI.SAP2000.API.SapObject'
    SOFTWARE = 'SAP2000'

    @check_valid_model
    def create_group(self, group_name: str):
        '''Defines a new group'''

        model_object = cast(IModel, self._model_object)
        return_code = model_object.GroupDef.SetGroup(group_name)
        check_request(return_code)


class SAFEModel(ETABSModel):
    '''SAFE Model class for CSI API connection

    Arguments:
            software_version -- Optional. Version of the software as an integer, this argument will be ignored when
                                connecting to an existing instance of a model (default: {None})
            custom_path -- Optional. Custom path to CSI installation folder. If not provided the default path will
                            be considered (default: {None})
    '''

    CLSID = 'CSI.SAFE.API.ETABSObject'
    SOFTWARE = 'SAFE'

    @check_valid_model
    def create_group(self, group_name: str):
        '''Defines a new group'''

        model_object = cast(IModel, self._model_object)
        return_code = model_object.GroupDef.SetGroup(group_name)
        check_request(return_code)
