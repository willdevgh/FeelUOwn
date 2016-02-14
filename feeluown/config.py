# -*- coding: utf-8 -*-

from collections.abc import MutableMapping

import yaml

from feeluown.constants import CONFIG_FILE_PATH
from feeluown.constants import DEFAULT_CONFIG_FILE_PATH
from feeluown.logger import LOG


class Config(MutableMapping):
    def __init__(self):
        self._data = dict()

    def load(self, path=CONFIG_FILE_PATH):
        try:
            with open(path, 'r') as f:
                self._data.update(yaml.load(f))
        except OSError:
            LOG.error('user config file not found, will load default config')
            with open(DEFAULT_CONFIG_FILE_PATH, 'r') as f:
                self._data.update(yaml.load(f))

    def save(self, path=CONFIG_FILE_PATH):
        with open(path, 'w') as f:
            f.write(yaml.dump(self._data))

    def __getitem__(self, key):
        return self._data[self.__keytransform__(key)]

    def __setitem__(self, key):
        return self._data[self.__keytransform__(key)]

    def __keytransform__(self, key):
        return key

    def __delitem__(self, key):
        del self._data[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return iter(self._data)


config = Config()