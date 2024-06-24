"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: DatabaseTables interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol
from typing import Optional


class IDatabaseTables(Protocol):
    '''CSI API Database Tables Interface'''

    def ApplyEditedTables(self, fill_import_log: bool) -> tuple[int, int, int, int, str, int]:
        '''Instructs the program to interactively import all of the tables stored in the table list using the 
            SetTableForEditing... functions.

        Arguments:
            fill_import_log -- Indicates whether the import log should be filled.

        Returns: A list containing the following
            number_fatal_errors: int -- The number of fatal errors that occurred during the import \n
            number_error_msgs: int -- The number of error messages logged during the import \n
            number_warn_msgs: int -- The number of warning messages logged during the import \n
            number_info_msgs: int -- The number of informational messages logged during the import \n
            import_log: str -- A string containing all messages logged during the import \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero

        Remarks:
            If the model is locked at the time this command is called then only tables that can be interactively 
            imported when the model is locked will be imported.  \n
            IMPORTANT NOTE: Please save your model before calling this function. If a fatal error occurs, or this
            function returns nonzero, the model may be in a corrupted state and it is recommended that the user close 
            the model without saving and reopen. 
        '''
        ...

    def CancelTableEditing(self) -> int:
        '''Clears all tables that were stored in the table list using one of the SetTableForEditing... functions. 

        Returns:
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetAllFieldsInTable(self, table_name: str) -> tuple[int, int, list[str], list[str], list[str],
                                                            list[str], list[bool], int]:
        '''Returns the available fields in a specified table

        Arguments:
            table_name -- The table name for the table for which the fields will be returned

        Returns: A list containing the following
            table_version: int -- The version number of the specified table \n
            number_fields: int -- The number of available fields in the specified table \n
            field_key: list[str] -- List of the field keys for the specified table \n
            field_name: list[str] -- A list of the field names for the specified table \n
            description: list[str] -- A list of the field descriptions for the specified table \n
            units_string: list[str] -- A list containing the field units for the specified table \n
            is_importable: list[bool] -- List containing whether the field is importable for the specified table \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetAllTables(self) -> tuple[int, list[str], list[str], list[bool], list[bool], int]:
        '''Returns all of the tables along with their import type and indicates if any data is available in the model 
        to fill the table

        Returns: A list containing the following
            number_tables: int -- The number of tables that are currently available for display \n
            table_key: list[str] -- A list of the table keys for the available tables \n
            table_name: list[str] -- A list of the table names for the available tables \n
            import_type: list[bool] -- A list indicating the import type for the table
                                    0. Not importable \n
                                    1. Importable but not interactively importable \n
                                    2. Importable and interactively importable when the model is unlocked \n
                                    3. Importable and interactively importable when the model is unlocked and locked \n
            is_empty: list[bool] -- List containing whether there is data is available to fill the table \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetAvailableTables(self) -> tuple[int, list[str], list[str], list[bool], list[bool], int]:
        '''Returns all of the tables along with their import type and indicates if any data is available in the model 
        to fill the table

        Returns: A list containing the following
            number_tables: int -- The number of tables that are currently available for display \n
            table_key: list[str] -- A list of the table keys for the available tables \n
            table_name: list[str] -- A list of the table names for the available tables \n
            import_type: list[bool] -- A list indicating the import type for the table
                                    0. Not importable \n
                                    1. Importable but not interactively importable \n
                                    2. Importable and interactively importable when the model is unlocked \n
                                    3. Importable and interactively importable when the model is unlocked and locked
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetLoadCasesSelectedForDisplay(self) -> tuple[int, list[str], int]:
        '''Returns a list of load cases that are selected for table display. 

        Returns: A list containing the following
            number_selected_load_cases: int -- The number of load cases selected for table display \n
            load_case_list: list[str] -- List of load cases selected for table display \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetLoadCombinationsSelectedForDisplay(self) -> tuple[int, list[str], int]:
        '''Returns a list of load combinations that are selected for table display. 

        Returns: A list containing the following
            number_selected_load_combinations: int -- The number of load combinations selected for table display \n
            load_combos_list: list[str] -- List of load combinations selected for table display \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetLoadPatternsSelectedForDisplay(self) -> tuple[int, list[str], int]:
        '''Returns a list of load patterns that are selected for table display. 

        Returns: A list containing the following
            number_selected_load_patterns: int -- The number of load patterns selected for table display \n
            load_patterns_list: list[str] -- List of load patterns selected for table display \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetTableForDisplayArray(self, table_name: str,
                                field_names: list[str], group_name: str) -> tuple[list[str], int, list[str], int, list[str], int]:
        '''Returns data for a single table in a single array. If there is nothing to be shown in the table then no 
        data is returned

        Arguments:
            table_name -- The name of the table for which data is requested \n
            field_names -- A list containing the field keys associated with the specified table for which data is
                            requested. If field_names contains a blank string, the data will be provided for all fields \n
            group_name -- The name of the group for which data will be returned. If group_name = All or a blank string 
                            then the data will be returned for all applicable objects in the model

        Returns: A list containing the following
            field_names: list[str] -- A list containing the field keys associated with the specified table for 
                                        which data is requested. If field_names contains a blank string, the data will 
                                        be provided for all fields \n
            table_version: int -- The version number of the specified table \n
            field_keys_included: list[str] -- A list containing the field keys associated with the specified table
                                                for which data is reported in the order it is reported in the TableData
                                                array \n
            number_records: int -- The number of records of data returned for each field \n
            table_data: list[str] -- A list containing the table data, excluding headers, returned row by row \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def GetTableForEditingArray(self, table_name: str, group_name: str) -> tuple[int, list[str], int, list[str], int]:
        '''Returns data for a single table in a single array. If there is nothing to be shown in the table then no 
        data is returned

        Arguments:
            table_name -- The name of the table for which data is requested. The table must be one that can be 
                            interactively edited. \n
            group_name -- The name of the group for which data will be returned

        Returns: A list containing the following
            table_version: int -- The version number of the specified table \n
            field_keys_included: list[str] -- A list containing the field keys associated with the specified table
                                                for which data is reported in the order it is reported in the TableData
                                                array \n
            number_records: int -- The number of records of data returned for each field \n
            table_data: list[str] -- A list containing the table data, excluding headers, returned row by row \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def SetLoadCasesSelectedForDisplay(self, load_case_list: list[str]) -> tuple[list[str], int]:
        '''Sets the load cases that are selected for table display

        Arguments:
            load_case_list -- List of load cases selected for table display. If no load cases are to be selected the a 
                                load_case_list must be equal to a blank string

        Returns: A list containing the following
            load_cases_list: list[str] -- List of load cases selected for table display \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def SetLoadCombinationsSelectedForDisplay(self, load_combo_list: list[str]) -> tuple[list[str], int]:
        '''Sets the load combinations that are selected for table display

        Arguments:
            load_combo_list -- List of load combinations selected for table display. If no load combinations are to be 
                                selected the load_combo_list must be equal to a blank string

        Returns: A list containing the following
            load_combos_list: list[str] -- List of load combinations selected for table display \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def SetLoadPatternsSelectedForDisplay(self, load_patterns_list: list[str]) -> tuple[list[str], int]:
        '''Sets the load patterns that are selected for table display

        Arguments:
            load_patterns_list -- List of load patterns selected for table display. If no load patterns are to be 
                                selected the load_patterns_list must be equal to a blank string

        Returns: A list containing the following
            load_patterns_list: list[str] -- List of load patterns selected for table display \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...

    def SetTableForEditingArray(self, table_name: str) -> tuple[int, int]:
        '''Reads a table from a string array and adds it to a stored table list until either the 
            ApplyEditedTables() or CancelTableEditing method is used

        Arguments:
            table_name: str -- The name of the table for which data is requested. The table must be one that can be 
                            interactively edited. \n
            field_keys_included: list[str] -- A list containing the field keys associated with the specified table
                                                for which data is reported in the order it is reported in the TableData
                                                array \n
            number_records: int -- The number of records of data returned for each field \n
            table_data: list[str] -- A list containing the table data, excluding headers, returned row by row

        Returns: A list containing the following
            table_version: int -- The version number of the specified table \n
            return_code: int -- Returns 0 if the function executes correctly, otherwise returns nonzero
        '''
        ...
