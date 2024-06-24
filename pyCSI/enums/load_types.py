"""
Provides access to Load Cases and Load Patterns types Code enumerators classes for use with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Enums.load_types
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""

from enum import IntEnum


class LoadTypeEnum(IntEnum):
    '''Enumerator parent class used in CSI API.
    '''
    @classmethod
    def help(cls):
        '''Display the class docstring
        '''
        print(cls.__doc__)


class LoadCaseType(LoadTypeEnum):
    '''Load cases type enumerator class

    Properties:
        LINEAR_STATIC \n
        NONLINEAR_STATIC \n
        MODAL \n
        RESPONSE_SPECTRUM \n
        LINEAR_HISTORY \n
        NONLINEAR_HISTORY \n
        LINEAR_DYNAMIC \n
        NONLINEAR_DYNAMIC \n
        MOVING_LOAD \n
        BUCKLING \n
        STEADY_STATE \n
        POWER_SPECTRAL_DENSITY \n
        LINEAR_STATIC_MULTISTEP \n
        HYPERSTATIC

    '''
    LINEAR_STATIC = 1
    NONLINEAR_STATIC = 2
    MODAL = 3
    RESPONSE_SPECTRUM = 4
    LINEAR_HISTORY = 5
    NONLINEAR_HISTORY = 6
    LINEAR_DYNAMIC = 7
    NONLINEAR_DYNAMIC = 8
    MOVING_LOAD = 9
    BUCKLING = 10
    STEADY_STATE = 11
    POWER_SPECTRAL_DENSITY = 12
    LINEAR_STATIC_MULTISTEP = 13
    HYPERSTATIC = 14
