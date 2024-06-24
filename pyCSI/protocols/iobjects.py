"""
====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: Objects interfaces
    By: LDP
    Date: 05/02/2024
=====================================================================================================================>>|
"""
# pylint: skip-file

from typing import Protocol
from pyCSI.enums import ItemType


class IObject(Protocol):
    '''CSI API Base Object Interface'''

    def SetGroupAssign(self, name: str, group_name: str, remove: bool = False, item_type: ItemType = ItemType.OBJECTS) -> int:
        '''Sets object to specified group

        Arguments:
            name -- The name of an existing object or group, depending of the value of the item_type argument
            group_name -- The name of an existing group to which the assignment is made
            remove -- If True, removes object from group (default: {False})
            item_type -- If this item is OBJECTS the object specified by name is added from the group
                If this item is GROUP, all objects in the group specified by name are added to the group
                If this item is SelectedObjects, all selected objects are added to the group and name is ignored
                (default: {ItemType.OBJECTS})

        Returns:
            Returns zero if the group assignment is successful, otherwise returns nonzero value
        '''
        ...

    def GetNameFromLabel(self, label: str, story: str) -> tuple[str, int]:
        '''Retrieves the unique name of an object, given the label and story

        Arguments:
            label -- Object label \
            story -- Object story level

        Returns: A list containing the following
            name: str -- Unique name of the object \
            return_code: int -- Zero if data is successfully retrieved, otherwise nonzero
        '''
        ...


class IArea(IObject):
    '''CSI API Area Object Interface'''


class IFrame(IObject):
    '''CSI API Frame Object Interface'''


class ILink(IObject):
    '''CSI API Link Object Interface'''


class IPoint(IObject):
    '''CSI API Point Object Interface'''
