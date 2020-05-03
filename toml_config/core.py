import os
from typing import Callable

import toml


class Config:
    """
    Реализация обработчика конфигурационных toml файлов.
    """
    path: str

    def __init__(self, path: str):
        """

        :param path: Путь к файлу
        """
        self.default_section = 'default'
        self.path = path
        self.config = {}
        self.section = {}
        self.value = None
        self.active_section = self.default_section
        self.e = None
        self.state = True
        self.load()

    def __str__(self):
        return str(self.config)

    def add_section(self, section_name: str) -> 'Config':
        """
        Метод добавляет секцию в файл.
        :param section_name: Название секции.

        """
        if self.state:
            self.config[section_name] = {}
            self.get_section(section_name)
        return self

    def get_section(self, section_name: str) -> 'Config':
        """
        Метод делает секцию активной.
        :param section_name: Название секции.

        """
        if self.state:
            self.active_section = section_name
            self.section = self.config.get(self.active_section)
        return self

    def load(self) -> 'Config':
        """
        Метод загружает в self.config содержимое файла.
        Если файл отсутствует - создает новый файл по пути self.path
        Путь к файлу получен при инициализации, параметр - path.

        """
        if self.state:
            try:
                if not os.path.exists(self.path):
                    with open(self.path, 'w', encoding='utf8') as f:
                        toml.dump(self.config, f)
                with open(self.path, encoding='utf8', ) as f:
                    self.config = toml.load(f)
                    return self
            except Exception as e:
                self.state = False
                self.e = e

    def save(self) -> 'Config':
        """
        Метод сохраняет в файл содержимое self.config
        :return: Если все прошло без ошибок - True
        """
        if self.state:
            try:
                with open(self.path, 'w', encoding='utf8') as f:
                    toml.dump(self.config, f)
                    return self
            except Exception as e:
                self.state = False
                self.e = e

    def get(self, param: str) -> 'Config':
        """
        Метод получает значение параметра из активнгой секции
        :param param:
        :return:
        """
        if self.state:
            self.value = self.section.get(param)
            return self

    def set(self, params: dict) -> 'Config':
        """
        Записывает параметры в активную секцию.
        :param params: Словарь параметров.
        :return:
        """
        if self.state:
            if isinstance(self.section, dict):
                for key, value in params.items():
                    self.section.setdefault(key, value)
                self.save()
            return self

    def catch(self, callback: Callable) -> 'Config':
        """
        Метод вызывается в случае ошибки в одном
        из методов стоящих в цепрочке перед ним.
        :param callback: Функция.
        :return:
        """
        if self.state is False:
            callback(self)
        return self
