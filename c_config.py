#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Andrey Pakhomenkov pakhomenkov@yandex.ru
"""Модуль конфигурации."""
from pathlib import Path
import json

APP_NAME = "tasks_board"
ALL_CONFIGS_FOLDER = ".config/"
CONFIG_FOLDER = f"{ALL_CONFIGS_FOLDER}/{APP_NAME}/" 
CONFIG_FILE_NAME = f"{APP_NAME}.json"
DATABASE_FILE_NAME = f"{APP_NAME}.db"
DATABASE_FILE_KEY = "database_file_name"


class CConfiguration(object):
    """Класс конфигурации программы."""
    def __init__(self):
        """Конструктор."""

        all_configs_folder_path = Path(Path.home() / ALL_CONFIGS_FOLDER)
        if not all_configs_folder_path.exists():
            
            all_configs_folder_path.mkdir()

        config_folder_path = Path(Path.home() / CONFIG_FOLDER)
        if not config_folder_path.exists():
            
            config_folder_path.mkdir()
        config_file = config_folder_path / CONFIG_FILE_NAME
        if config_file.exists():
            
            self.read_config()
        else:
            
            self.config = dict()

        if not DATABASE_FILE_KEY in self.config:
        
            self.store_value(DATABASE_FILE_KEY, 
                             str(Path.home() / CONFIG_FOLDER / DATABASE_FILE_NAME))
            self.write_config()
        # if not MAX_BACKUP_FILES_KEY in self.config:
        
            # self.store_value(MAX_BACKUP_FILES_KEY, 5)
            # self.write_config()
            
    
    def store_value(self, pkey, pvalue):
        """Сохраняет заданное значение по заданному ключу в словарь конфигурации."""
        result = False
        if pkey:
            
            if pvalue:
                
                self.config[pkey] = pvalue
                result = True
        return result        
    
    
    def restore_value(self, pkey):
        """Возвращает значение, сохраненное в словаре конфигурации по заданному ключу."""
        if pkey in self.config:

            return self.config[pkey]
        return None
    
        
    def write_config(self):
        """Сохраняет словарь конфигурации в файл в формате json."""
        config_file = open(Path.home() / CONFIG_FOLDER / CONFIG_FILE_NAME, "w", encoding="utf-8")
        config_file.write(json.dumps(self.config, sort_keys=True, indent=4))
        config_file.close()
        
        
    def read_config(self):
        """Считывает сохраненную конфигурацию из json файла в словарь."""
        config_file = open(Path.home() / CONFIG_FOLDER / CONFIG_FILE_NAME, "r", encoding="utf-8")
        self.config = json.load(config_file)
        config_file.close()
   
    
