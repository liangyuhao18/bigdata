import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from GUItest01 import Ui_MainWindow

states = {
    "阿拉巴马州": "Alabama",
    "阿拉斯加州": "Alaska",
    "亚利桑那州": "Arizona",
    "阿肯色州": "Arkansas",
    "加利福尼亚州": "California",
    "科罗拉多州": "Colorado",
    "康涅狄格州": "Connecticut",
    "特拉华州": "Delaware",
    "佛罗里达州": "Florida",
    "乔治亚州": "Georgia",
    "夏威夷州": "Hawaii",
    "爱达荷州": "Idaho",
    "伊利诺伊州": "Illinois",
    "印第安纳州": "Indiana",
    "爱荷华州": "Iowa",
    "堪萨斯州": "Kansas",
    "肯塔基州": "Kentucky",
    "路易斯安那州": "Louisiana",
    "缅因州": "Maine",
    "马里兰州": "Maryland",
    "马萨诸塞州": "Massachusetts",
    "密歇根州": "Michigan",
    "明尼苏达州": "Minnesota",
    "密西西比州": "Mississippi",
    "密苏里州": "Missouri",
    "蒙大拿州": "Montana",
    "内布拉斯加州": "Nebraska",
    "内华达州": "Nevada",
    "新罕布什尔州": "New Hampshire",
    "新泽西州": "New Jersey",
    "新墨西哥州": "New Mexico",
    "纽约州": "New York",
    "北卡罗来纳州": "North Carolina",
    "北达科他州": "North Dakota",
    "俄亥俄州": "Ohio",
    "俄克拉何马州": "Oklahoma",
    "俄勒冈州": "Oregon",
    "宾夕法尼亚州": "Pennsylvania",
    "罗德岛州": "Rhode Island",
    "南卡罗来纳州": "South Carolina",
    "南达科他州": "South Dakota",
    "田纳西州": "Tennessee",
    "德克萨斯州": "Texas",
    "犹他州": "Utah",
    "佛蒙特州": "Vermont",
    "弗吉尼亚州": "Virginia",
    "华盛顿州": "Washington",
    "西弗吉尼亚州": "West Virginia",
    "威斯康星州": "Wisconsin",
    "怀俄明州": "Wyoming"
}


class MyMainWindows(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def returnstate(self):
        print(self.comboBox.currentText())
        print(states[self.comboBox.currentText()])

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainWindows()
    mainWindow.show()
    sys.exit(app.exec())
