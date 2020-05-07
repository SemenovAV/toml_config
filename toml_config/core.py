"""
Module for easy work with configuration files in toml format.

Released under the MIT license.
"""

import os
from typing import Callable

import toml


class Config:
    """
    Implementation of the handler for configuration toml files.

    """
    path: str

    def __init__(self, path: str):
        """

        :param path: Путь к файлу
        """
        self.path = path
        self.config = {}
        self.section = {}
        self.value = None
        self.active_section = 'default'
        self.err = None
        self.state = True
        self.load()

    def __str__(self):
        return str(self.config)

    def add_section(self, section_name: str) -> 'Config':
        """
        The method adds a section to the file.
        :param section_name: str

        """
        if self.state:
            if not self.config.get(section_name):
                self.config[section_name] = {}
                self.get_section(section_name)
                self.save()
        return self

    def get_section(self, section_name: str) -> 'Config':
        """
        This method makes the section active.
        :param section_name: str

        """

        if self.state:
            section = self.config.get(section_name)
            if isinstance(section, dict):
                self.active_section = section_name
                self.section = section
            else:
                self.state = False
                self.err = f'not section: {section_name}'

        return self

    def load(self) -> 'Config':
        """
        The method loads the contents of the file to self.config property".
        If the file is missing, it creates a new file along the path specified
        in the self.path property.The path to the file was obtained during
        initialization in the path parameter.

        """
        if self.state:
            try:
                if not os.path.exists(self.path):
                    with open(self.path, 'w', encoding='utf8') as file:
                        toml.dump(self.config, file)
                with open(self.path, encoding='utf8', ) as file:
                    self.config = toml.load(file)
                    return self
            except OSError as err:
                self.state = False
                self.err = err
            except TypeError as err:
                self.state = False
                self.err = err
        return self

    def save(self) -> 'Config':
        """
       The method saves the contents of the self.config property to a file

        """
        if self.state:
            try:
                with open(self.path, 'w', encoding='utf8') as file:
                    toml.dump(self.config, file)
                    return self
            except OSError as err:
                self.state = False
                self.err = err
            except TypeError as err:
                self.state = False
                self.err = err
        return self

    def get(self, param: str) -> 'Config':
        """
        The method gets the parameter value from the active section
        :param param: str Parameter name.

        """
        if self.state:
            value = self.section.get(param, )
            if value is not None:
                self.value = self.section.get(param)
            else:
                self.state = False
                self.err = f'not key: {param} from section{self.active_section}'
        return self

    def set(self, **kwargs) -> 'Config':
        """
        Writes parameters to the active section.
        :param kwargs: Parameters.

        """
        if self.state:
            if isinstance(self.section, dict):
                for key, value in kwargs.items():
                    self.section[key] = value
                self.save()
        return self

    def catch(self, callback: Callable) -> 'Config':
        """
        The method is called if there is an error in one
        of the methods in front of him.

        :param callback: Function.

        """
        if self.state is False:
            callback(self)
        return self
