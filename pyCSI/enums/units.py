"""
Provides access to units enumerators classes for use with the PyCSI library

====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Enums.units
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|
"""

from enum import IntEnum


class UnitEnum(IntEnum):
    '''Enumerator parent class used in CSI API.
    '''
    @classmethod
    def help(cls):
        '''Display the class docstring
        '''
        print(cls.__doc__)


class ForceUnit(UnitEnum):
    '''Force unit class enumerator.

    Properties:
        NA -- Not applicable \n
        LB, LBS -- Imperial system, pounds \n
        KIP, KIPS -- Imperial system, kips \n
        N -- International System (SI), Newtons \n
        KN -- International System (SI), Kilonewtons \n
        KGF -- Metric System, Kilogram-force \n
        TONF -- Metric System, Ton-force
    '''
    NOT_APPLICABLE = 0
    LB = 1
    LBS = 1
    KIP = 2
    KIPS = 2
    N = 3
    KN = 4
    KGF = 5
    TONF = 6


class LengthUnit(UnitEnum):
    '''Length unit class enumerator.

    Properties:
        NA -- Not applicable \n
        IN, INCH -- Imperial system, inches \n
        FT, FEET -- Imperial system, feet \n
        MICRON -- International System (SI), microns [μm] \n
        MM -- International System (SI), millimeters \n
        CM -- International System (SI), centimeters \n
        M -- Metric System, meters
    '''
    NOT_APPLICABLE = 0
    IN = 1
    INCH = 1
    FT = 2
    FEET = 2
    MICRON = 3
    MM = 4
    CM = 5
    M = 6
    METERS = 6


class TemperatureUnit(UnitEnum):
    '''Temperature unit class enumerator.

    Properties:
        NA -- Not applicable \n
        F -- Imperial system, Fahrenheit \n
        C -- International System (SI), Celsius
    '''
    NOT_APPLICABLE = 0
    F = 1
    FAHRENHEIT = 1
    C = 2
    CELSIUS = 2
