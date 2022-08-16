#!/usr/bin/python#-*-coding:utf-8-*-
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication,QWidget,QGridLayout, QPushButton)

class set_map(QWidget):
    """地图属性初始化"""
    def __init__(self):
        super(set_map, self).__init__()
        # 地图初始大小
        self.size_x = 5
        self.size_y = 5
        # 地图储存
        self.cache = []
        #调用Ui
        self.init_ui()
    """ui界面初始化"""
    def init_ui(self):
        self.setWindowTitle('blue and red war')
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        #设置主页面大小
        self.setGeometry(QtCore.QRect(720, 150, 681, 680))
        #设置网格大小
        self.grid.width = 54
        self.grid.highth = 130
        self.setMinimumSize(QtCore.QSize(self.grid.width, self.grid.highth))
        self.init_set()
    """创建初始地图"""
    def init_set(self):
        positions = [(i, j) for i in range(self.size_x) for j in range(self.size_y)]
        name = [(i, j) for i in range(self.size_x) for j in range(self.size_y)]
        name = map(str,name)
        self.set(positions,name)
    """地图生成器"""
    def set(self, positions,name):
        for position, name in zip(positions, name):
            button = QPushButton(name)
            #设置按钮与网格大小相同
            button.setMinimumSize(QtCore.QSize(self.grid.width,self.grid.highth))
            #button.setStyleSheet("background-color : red")
            self.grid.addWidget(button, *position)
            #将地图储存，便于后续操作调整
            self.cache.append(button)

#测试ui界面
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = set_map()
    w.show()
    app.exec()