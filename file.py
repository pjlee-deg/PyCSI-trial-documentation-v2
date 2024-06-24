"""
====================================================================================================================>>|
    DEGENKOLB ENGINEERS
    Job: PyCSI
    Subject: File Class
    By: LDP
    Date: 03/03/2024
=====================================================================================================================>>|

Gives access to model File interface
"""
import os
from typing import Optional

from pyCSI.protocols.ifile import IFile
from pyCSI.utils.validation_utils import check_request
from pyCSI.protocols.ibasemodel import BaseModel


class File:
    '''File interface of the Model object

    Arguments:
        model_object -- Instance of a model object
    '''

    def __init__(self, parent) -> None:
        self._parent: BaseModel = parent
        self._file: IFile = parent.get_model_object().File

    def open_file(self, file: str) -> None:
        '''Opens an existing model file

        Arguments:
            file_name -- The full path of a model to be opened in the application
        '''

        # Check that the specified file exists
        if not os.path.isfile(file):
            raise FileNotFoundError(f'File {file} not found')

        return_code = self._file.OpenFile(file)
        check_request(return_code)
        print(f'Successfully connected to {self._parent.get_file_name()}')

    def new_model(self):
        '''Initialize a new model on the active api_object'''

        model_object = self._parent.get_model_object()
        return_code: int = model_object.InitializeNewModel()
        check_request(return_code)

    def save(self, file_name: Optional[str] = None, path: Optional[str] = None) -> None:
        '''Saves the model with the specified path and file name

        Arguments:
            file_name -- Optional. The name to which the model file is saved. If not provided, the model is saved 
                            using the current name. If the file has not been saved previously and file_name is omitted 
                            an error will be raised.\n
            path -- Optional. The full path where the model will be saved. If not provided, the model is saved in the
                        current location
        '''

        if file_name is None and path is None:
            self._file.Save()
            return

        if path is None:
            path = self._parent.get_file_path()

        if file_name is None:
            file_name = self._parent.get_file_name()

        # Concatenate full name and save the model
        full_name = os.sep.join([path, file_name])
        self._file.Save(full_name)
