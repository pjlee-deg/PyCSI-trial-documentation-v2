"""
Provides protocol definitions of CSI API interface, used for static type hinting with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Group interface
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol


class IGroup(Protocol):
    '''CSI API Group Definition Interface'''

    def Count(self) -> int:
        '''Returns the number of defined groups'''
        ...

    def Delete(self, name: str) -> int:
        '''Deletes a specified group

        Arguments:
            name -- The name of an existing group

        Returns:
            Zero if the group is successfully deleted, otherwise returns a nonzero value
        '''
        ...

    def GetAssignments(self, name: str) -> tuple[int, list[int], list[str], int]:
        '''Retrieves the assignments to a specified group

        Arguments:
            name -- The name of an existing group

        Returns: A list containing the following
            number_items: int -- The number of assignments made to the specified group
            object_type: list[int] -- List that includes the object type of each item in the group
                1. Point object
                2. Frame object
                3. Cable object
                4. Tendon object
                5. Area object
                6. Solid object
                7 Link object
            object_name: list[str] -- List that includes the name of each item in the group
            return_code: int -- Zero if the group assignment is successfully retrieved, otherwise nonzero
        '''
        ...

    def GetGroup(self, name: str) -> tuple[int, bool, bool, bool, bool, bool, bool, bool,
                                           bool, bool, bool, bool, int]:
        '''Retrieves the specified group data

        Arguments:
            name -- The name of an existing group

        Returns: A list containing the following
            color
            specified_for_selection
            specified_for_section_cut
            specified_for_steel_design
            specified_for_concrete_design
            specified_for_aluminum_design
            specified_for_cold_formed_design
            specified_for_static_NL_analysis
            specified_for_bridge_response_output
            specified_for_auto_seismic_output
            specified_for_auto_wind_output
            specified_for_mass_and_weight
            return_code: int -- Zero if the group data is successfully retrieved, otherwise nonzero
        '''
        ...

    def GetGroup_1(self, name: str) -> tuple[int, bool, bool, bool, bool, bool, bool, bool,
                                             bool, bool, bool, bool, bool, bool, int]:
        '''Retrieves the specified group data, primarily for ETABS

        Arguments:
            name -- The name of an existing group

        Returns: A list containing the following
            color
            specified_for_selection
            specified_for_section_cut
            specified_for_steel_design
            specified_for_concrete_design
            specified_for_aluminum_design
            specified_for_static_NL_analysis
            specified_for_auto_seismic_output
            specified_for_auto_wind_output
            specified_for_mass_and_weight
            specified_for_steel_joist_design
            specified_for_wall_design
            specified_for_base_plate_design
            specified_for_connection_design
            return_code: int -- Zero if the group data is successfully retrieved, otherwise nonzero
        '''
        ...

    def GetNameList(self) -> tuple[int, list[str], int]:
        '''Gets the names of all defined groups

        Returns:
            number_names: int -- Number of groups retrieved
            names: list[str] -- List containing the names of the defined groups
            return_code: int -- Zero if the group names is successfully retrieved, otherwise nonzero
        '''
        ...

    def SetGroup(self, name: str, color: int = -1,
                 specified_for_selection: bool = True,
                 specified_for_section_cut: bool = True,
                 specified_for_steel_design: bool = True,
                 specified_for_concrete_design: bool = True,
                 specified_for_aluminum_design: bool = True,
                 specified_for_cold_formed_design: bool = True,
                 specified_for_static_NL_analysis: bool = True,
                 specified_for_bridge_response_output: bool = True,
                 specified_for_auto_seismic_output: bool = False,
                 specified_for_auto_wind_output: bool = False,
                 specified_for_mass_and_weight: bool = True) -> int:
        '''Sets the group data

        Arguments:
            name -- The name of an existing group
            color
            specified_for_selection
            specified_for_section_cut
            specified_for_steel_design
            specified_for_concrete_design
            specified_for_aluminum_design
            specified_for_cold_formed_design
            specified_for_static_NL_analysis
            specified_for_bridge_response_output
            specified_for_auto_seismic_output
            specified_for_auto_wind_output
            specified_for_mass_and_weight

        Returns:
            return_code: int -- Zero if the group data is successfully set, otherwise nonzero
        '''
        ...

    def SetGroup_1(self, name: str, color: int = -1,
                   specified_for_selection: bool = True,
                   specified_for_section_cut: bool = True,
                   specified_for_steel_design: bool = True,
                   specified_for_concrete_design: bool = True,
                   specified_for_aluminum_design: bool = True,
                   specified_for_static_NL_analysis: bool = True,
                   specified_for_auto_seismic_output: bool = False,
                   specified_for_auto_wind_output: bool = False,
                   specified_for_mass_and_weight: bool = True,
                   specified_for_steel_joist_design: bool = True,
                   specified_for_wall_design: bool = True,
                   specified_for_base_plate_design: bool = True,
                   specified_for_connection_design: bool = True) -> int:
        '''Sets the specified group data, primarily for ETABS

            Arguments:
                name -- The name of an existing group
                color
                specified_for_selection
                specified_for_section_cut
                specified_for_steel_design
                specified_for_concrete_design
                specified_for_aluminum_design
                specified_for_static_NL_analysis
                specified_for_auto_seismic_output
                specified_for_auto_wind_output
                specified_for_mass_and_weight
                specified_for_steel_joist_design
                specified_for_wall_design
                specified_for_base_plate_design
                specified_for_connection_design

            Returns:
                return_code: int -- Zero if the group data is successfully retrieved, otherwise nonzero
            '''
        ...
