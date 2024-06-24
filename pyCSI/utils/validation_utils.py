"""
Created on Thurs Feb 01 12:33:45 2024
@author: lpancardo  

CSI API Model Class
"""

import functools
from typing import NoReturn

from pyCSI.enums import ReturnCode


class APIBadRequest(Exception):
    '''API Error Exception

    Arguments:
        message -- Error message
        error_code -- The integer error code from the CSI API request

    Raises:
        Exception APIBadRequest
    '''

    def __init__(self, message: str, error_code: int) -> None:
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


class APIConnectionError(Exception):
    '''API Connection Error 

    Arguments:
        message -- Error message

    Raises:
        Exception APIConnectionError
    '''

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def raise_api_error() -> NoReturn:
    '''Raises an Attribute error for an invalid call to api_object.

    Raises:
        AttributeError
    '''
    error_message: str = 'API Object has not been initialized, use ' \
        '.get_model() to initialize the API Object'
    raise AttributeError(error_message.format())


def raise_model_error(software: str) -> NoReturn:
    '''Raises an Attribute error for an invalid call to model_object.

    Arguments:
        software -- Name of software class that raised the error

    Raises:
        AttributeError
    '''
    error_message: str = '{0} Model Object has not been initialized, use .get_model() to initialize' \
        ' the Model Object'
    raise AttributeError(error_message.format(software))


def check_valid_model(class_method):
    '''Checks that model_object in the model class is a valid object before executing the class_method. If model_object 
        is valid then the class_method is run, otherwise an Attribute error is raised.
    '''

    @functools.wraps(class_method)
    def wrapper(self, *args, **kwargs):
        if not self.connected_to_model:
            software = self.SOFTWARE
            raise_model_error(software)

        result = class_method(self, *args, **kwargs)
        return result

    return wrapper


def check_request(return_code: int) -> None:
    '''Validates the return code from an API request

    Arguments:
        return_code -- Return value of the API request

    Raises:
        APIError: If return code is an error
    '''
    if return_code != ReturnCode.NO_ERROR:
        error_name = ReturnCode(return_code).name
        message = f'APIBadRequest: {error_name} (Error code:{return_code})'
        raise APIBadRequest(message, return_code)
