#! /usr/bin/python3
## -*- coding: utf-8 -*-
# @author: Andrey Pakhomenkov pakhomenkov@yandex.ru
""" Органайзер задач. """
import sys

from pathlib import Path

from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

import c_ancestor as anc
import c_config as cfg
import c_context as ctx
import c_tag as tag
import c_task as tsk  # =)
    
PROGRAM_VERSION = "0.0"
MAIN_WINDOW_FORM = "mainwindow.ui"
FORM_FOLDER = "ui/"
HEADER_TEXT = "Ты должен делать то, что должен."

class CMainWindow(QtWidgets.QMainWindow):
    """Класс."""
    def __init__(self):
        """Конструктор класса."""
        super(CMainWindow, self).__init__()
        self.application_folder = Path.cwd()
        
        # *** Интерфейс
        ui_folder = self.application_folder / FORM_FOLDER / MAIN_WINDOW_FORM
        uic.loadUi(self.application_folder / FORM_FOLDER / MAIN_WINDOW_FORM, self)

        # *** Конфигурация
        self.config = cfg.CConfiguration()

        # *** База данных
        self.__db_connect()
        if not self.__db_exists():
        
            self.__db_create()
        # self.session = None
        
        window_title = f"Tasks board ver. {PROGRAM_VERSION} : \"{HEADER_TEXT}\""
        self.setWindowTitle(window_title)
        # self.setWindowIcon(QtGui.QIcon('ui/forget-me-not.ico'))
        # self.update()
        # *** Компоненты
        # comboBox_Contexts
        # lineEdit_TagsFilter
        # lineEdit_TextFilter
        # checkBox_ShowCompleted
        # checkBox_ShowDeleted
        # lineEdit_Tags
        # spinBox_Urgency
        # lineEdit_Task
        # tableWidget_Tasks
        # statusBar
        # *** Обработчики
        # toolButton_TagsFilter
        # toolButton_TextFilter
        # toolButton_Quit
        # toolButton_Apply
        self.show()


    def __db_connect(self):
        """Устанавливает соединение с БД."""
        self.engine = create_engine('sqlite:///'+self.config.restore_value(cfg.DATABASE_FILE_KEY))
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        anc.Base.metadata.bind = self.engine


    def __db_create(self):
        """Создает или изменяет БД в соответствии с описанной в классах структурой."""
        anc.Base.metadata.create_all()



    def __db_exists(self):
        """Проверяет наличие базы данных по пути в конфигурации."""
        db_folder_path = Path(self.config.restore_value(cfg.DATABASE_FILE_KEY))
        return db_folder_path.exists()

        
if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    main_window = CMainWindow()
    application.exec_()    
