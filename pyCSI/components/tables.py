"""
====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Tables Class
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|

Gives access to model Database Tables interface
"""

from typing import Literal
from typing import Optional

import numpy as np
import pandas as pd

from pyCSI.protocols import IDatabaseTables
from pyCSI.protocols import BaseModel
from pyCSI.utils import check_request


class Tables:
    '''Database Tables interface of the Model object

    Arguments:
        model_object -- Instance of a model object
    '''

    def __init__(self, parent) -> None:
        self._parent: BaseModel = parent
        self._database_tables: IDatabaseTables = parent.get_model_object().DatabaseTables
        self._load_cases = None
        self._load_combos = None
        self._load_patterns = None

###################################################################################################################
# Class initialize setup
###################################################################################################################

###################################################################################################################
# Class properties
###################################################################################################################

    @property
    def load_cases(self) -> list[str]:
        '''Load cases set for display in table returned data'''
        if self._load_cases is None:
            # Initialize load cases
            number_cases, load_cases, return_code = self._database_tables.GetLoadCasesSelectedForDisplay()
            if number_cases != 0:
                check_request(return_code)
            self._load_cases = [case for case in load_cases if case is not None]
        return self._load_cases

    @property
    def load_combos(self) -> list[str]:
        '''Load combinations set for display in table returned data'''
        if self._load_combos is None:
            # Initialize load combos
            number_combos, load_combos, return_code = self._database_tables.GetLoadCombinationsSelectedForDisplay()
            if number_combos != 0:
                check_request(return_code)
            self._load_combos = [combo for combo in load_combos if combo is not None]
        return self._load_combos

    @property
    def load_patterns(self) -> list[str]:
        '''Load patterns set for display in table returned data'''
        if self._load_patterns is None:
            # Initialize load patterns
            number_patterns, load_patterns, return_code = self._database_tables.GetLoadPatternsSelectedForDisplay()
            if number_patterns != 0:
                check_request(return_code)
            self._load_patterns = [pattern for pattern in load_patterns if pattern is not None]
        return self._load_patterns

###################################################################################################################
# Class properties setters
###################################################################################################################

    @load_cases.setter
    def load_cases(self, new_value: Literal['all'] | list[str] | None):
        if new_value is None:
            # If None, set new_value to empty list
            new_value = []

        if isinstance(new_value, str):
            if new_value.lower() != 'all':
                raise ValueError('Assigned value not valid')

            # if 'all', select all cases
            new_value = self._parent.get_load_cases()

        _, return_code = self._database_tables.SetLoadCasesSelectedForDisplay(new_value)
        check_request(return_code)
        self._load_cases = new_value

    @load_combos.setter
    def load_combos(self, new_value: Literal['all'] | list[str] | None):
        if new_value is None:
            # If None, set new_value to empty list
            new_value = []

        if isinstance(new_value, str):
            if new_value.lower() != 'all':
                raise ValueError('Assigned value not valid')

            # if 'all', select all combos
            new_value = self._parent.get_load_combos()

        _, return_code = self._database_tables.SetLoadCombinationsSelectedForDisplay(new_value)
        check_request(return_code)
        self._load_combos = new_value

    @load_patterns.setter
    def load_patterns(self, new_value: Literal['all'] | list[str] | None):
        if new_value is None:
            # If None, set new_value to empty list
            new_value = []

        if isinstance(new_value, str):
            if new_value.lower() != 'all':
                raise ValueError('Assigned value not valid')

            # if 'all', select all patterns
            new_value = self._parent.get_load_patterns()

        _, return_code = self._database_tables.SetLoadPatternsSelectedForDisplay(new_value)
        check_request(return_code)
        self._load_patterns = new_value

###################################################################################################################
# Class methods
###################################################################################################################

    def get_available_tables(self) -> list[str]:
        '''Gets a list containing the names of all available tables in the model'''

        request_result = self._database_tables.GetAvailableTables()
        return_code = request_result[-1]
        check_request(return_code)  # Check API request

        return request_result[1]

    def get_table_dataframe(self, table_key: str, group: Optional[str] = None,
                            include_all_headers: bool = False) -> pd.DataFrame:
        '''Gets the specified table in a dataframe format

        Arguments:
            table_key -- The name of the table which data will be returned \n
            group -- Optional. The name of the objects group for which the data will be returned. If not provided
                        data for all available objects will be returned. (default: {None}) \n
            include_all_headers -- Optional. If true, the return data will contain all available fields for the 
                        specified table. If the field has no data it will be filled with NaN values (default: {False})

        Returns:
            Table data in dataframe format
        '''
        if group is None:
            # If group is None, select all objects for display
            group = 'All'

        # Get table from API
        field_keys = []
        request_result = self._database_tables.GetTableForDisplayArray(table_key, field_keys, group)
        return_code = request_result[-1]
        check_request(return_code)  # Check API request
        headers = request_result[2]
        number_records = request_result[3]
        data = np.array(request_result[4])
        data = data.reshape(number_records, len(headers))

        # Get table data into dataframe
        table_data = pd.DataFrame(data, columns=headers)

        # Turn number values into numbers
        for column in table_data:
            try:
                table_data[column] = pd.to_numeric(table_data[column])
            except ValueError:
                pass

        if include_all_headers:
            # Get all available headers for the table
            request_result = self._database_tables.GetAllFieldsInTable(table_key)
            return_code = request_result[-1]
            check_request(return_code)  # Check API request
            field_keys = request_result[2]

            # Insert missing fields into dataframe
            missing_fields = {field: index for index, field in enumerate(field_keys) if field not in headers}
            for field, index in missing_fields.items():
                table_data.insert(index, field, np.nan)

        return table_data
