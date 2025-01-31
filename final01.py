import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QDateTime, QDate, QTime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sources/img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(130, 40, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setObjectName("label_20")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 100, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(90, 180, 321, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(90, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 110, 160, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setMaximumDate(QtCore.QDate(2022, 5, 13))
        self.dateEdit.setMinimumDate(QtCore.QDate(2020, 1, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_2.setMaximumDate(QtCore.QDate(2022, 5, 13))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(2020, 1, 21))
        self.dateEdit_2.setDateTime(QDateTime(QDate(2022, 5, 13), QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout.addWidget(self.dateEdit_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 260, 241, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setMaxVisibleItems(50)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems([
            "美国全境", "阿拉巴马州", "阿拉斯加州", "亚利桑那州", "阿肯色州", "加利福尼亚州", "科罗拉多州", "康涅狄格州",
            "特拉华州", "佛罗里达州", "乔治亚州", "夏威夷州", "乔治亚州", "爱达荷州", "伊利诺伊州", "印第安纳州"
            , "爱荷华州", "堪萨斯州", "肯塔基州", "路易斯安那州", "缅因州", "马里兰州", "马萨诸塞州"
            , "密歇根州", "明尼苏达州", "密西西比州", "密苏里州", "蒙大拿州", "内布拉斯加州", "内华达州"
            , "新罕布什尔州", "新泽西州", "新墨西哥州", "纽约州", "北卡罗来纳州", "北达科他州", "俄亥俄州"
            , "俄克拉何马州", "俄勒冈州", "宾夕法尼亚州", "罗德岛州", "南卡罗来纳州", "南达科他州", "田纳西州", "德克萨斯州"
            , "犹他州", "佛蒙特州", "弗吉尼亚州", "华盛顿州", "西弗吉尼亚州", "威斯康星州", "怀俄明州"
        ])
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 250, 241, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setMaxVisibleItems(50)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems([
            "美国全境", "阿拉巴马州", "阿拉斯加州", "亚利桑那州", "阿肯色州", "加利福尼亚州", "科罗拉多州", "康涅狄格州",
            "特拉华州", "佛罗里达州", "乔治亚州", "夏威夷州", "乔治亚州", "爱达荷州", "伊利诺伊州", "印第安纳州"
            , "爱荷华州", "堪萨斯州", "肯塔基州", "路易斯安那州", "缅因州", "马里兰州", "马萨诸塞州"
            , "密歇根州", "明尼苏达州", "密西西比州", "密苏里州", "蒙大拿州", "内布拉斯加州", "内华达州"
            , "新罕布什尔州", "新泽西州", "新墨西哥州", "纽约州", "北卡罗来纳州", "北达科他州", "俄亥俄州"
            , "俄克拉何马州", "俄勒冈州", "宾夕法尼亚州", "罗德岛州", "南卡罗来纳州", "南达科他州", "田纳西州", "德克萨斯州"
            , "犹他州", "佛蒙特州", "弗吉尼亚州", "华盛顿州", "西弗吉尼亚州", "威斯康星州", "怀俄明州"
        ])
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 100, 161, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(180)
        self.verticalLayout_3.addWidget(self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(["线性回归模型", "随机森林回归模型", "梯度上升决策树回归模型"])
        self.verticalLayout_3.addWidget(self.comboBox_3)
        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.comboBox_4 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.addItems(["病例数", "死亡数"])
        self.verticalLayout_3.addWidget(self.comboBox_4)

        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(100, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_2.clicked.connect(Form.showhistory) # type: ignore
        self.pushButton_3.clicked.connect(Form.predict) # type: ignore
        self.pushButton.clicked.connect(Form.getdata) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "基于spark的疫情分析系统"))
        self.label_20.setText(_translate("Form", "基于spark的疫情分析系统"))
        self.pushButton.setText(_translate("Form", "数据获取"))
        self.label_5.setText(_translate("Form", "历史疫情数据查看"))
        self.label_2.setText(_translate("Form", "请选择时间"))
        self.dateEdit.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.label_3.setText(_translate("Form", "到"))
        self.dateEdit_2.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.label.setText(_translate("Form", "请选择地区"))
        self.pushButton_2.setText(_translate("Form", "确认"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "历史数据"))
        self.label_9.setText(_translate("Form", "请选择地区"))
        self.pushButton_3.setText(_translate("Form", "确认"))
        self.label_7.setText(_translate("Form", "请输入未来想预测的天数"))
        self.label_8.setText(_translate("Form", "自2022-05-13开始"))
        self.label_4.setText(_translate("Form", "请选择你使用的模型"))
        self.label_6.setText(_translate("Form", "疫情数据预测"))
        self.label_10.setText(_translate("Form", "请选择预测的标签"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "未来预测"))
