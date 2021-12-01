"""`Dori Calculator` Application Made With Qt
"""

# Standard library imports
from time import sleep
from threading import Thread

# Third party imports
from PyQt5 import QtCore, QtGui, QtWidgets

# Local library imports
from assets import num_btn_stylesheet
from assets import operator_btn_stylesheet, mul_pow_btn_stylesheet
from assets import equal_btn_stylesheet, equal_btn_stylesheet2, delete_btn_stylesheet
from assets import line_edit_stylesheet, window_stylesheet


class Calculator:
    """ui dialog class
    """

    def __init__(self):
        # number
        self.num1_button = None
        self.num2_button = None
        self.num3_button = None
        self.num4_button = None
        self.num5_button = None
        self.num6_button = None
        self.num7_button = None
        self.num8_button = None
        self.num9_button = None
        # operator
        self.sub_button = None
        self.mul_button = None
        self.div_button = None
        self.plus_button = None
        self.power_button = None
        # other
        self.num0_button = None
        self.dot_button = None
        self.line_edit = None
        self.equal_button = None
        self.back_button = None
        self.clear_button = None

    def number_button_ui(self, window_):
        """setup number buttons ui

        Args:
            window_ (QtWidgets.QDialog): application window
        """
        cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        # number 1
        self.num1_button = QtWidgets.QPushButton(window_)
        self.num1_button.setGeometry(QtCore.QRect(20, 230, 120, 40))
        self.num1_button.setCursor(cursor)
        self.num1_button.setStyleSheet(num_btn_stylesheet)
        self.num1_button.setObjectName("num1_button")
        # number 2
        self.num2_button = QtWidgets.QPushButton(window_)
        self.num2_button.setGeometry(QtCore.QRect(150, 230, 120, 40))
        self.num2_button.setCursor(cursor)
        self.num2_button.setStyleSheet(num_btn_stylesheet)
        self.num2_button.setObjectName("num2_button")
        # number 3
        self.num3_button = QtWidgets.QPushButton(window_)
        self.num3_button.setGeometry(QtCore.QRect(280, 230, 120, 40))
        self.num3_button.setCursor(cursor)
        self.num3_button.setStyleSheet(num_btn_stylesheet)
        self.num3_button.setObjectName("num3_button")
        # number 4
        self.num4_button = QtWidgets.QPushButton(window_)
        self.num4_button.setGeometry(QtCore.QRect(20, 180, 120, 40))
        self.num4_button.setCursor(cursor)
        self.num4_button.setStyleSheet(num_btn_stylesheet)
        self.num4_button.setObjectName("num4_button")
        # number 5
        self.num5_button = QtWidgets.QPushButton(window_)
        self.num5_button.setGeometry(QtCore.QRect(150, 180, 120, 40))
        self.num5_button.setCursor(cursor)
        self.num5_button.setStyleSheet(num_btn_stylesheet)
        self.num5_button.setObjectName("num5_button")
        # number 6
        self.num6_button = QtWidgets.QPushButton(window_)
        self.num6_button.setGeometry(QtCore.QRect(280, 180, 120, 40))
        self.num6_button.setCursor(cursor)
        self.num6_button.setStyleSheet(num_btn_stylesheet)
        self.num6_button.setObjectName("num6_button")
        # number 7
        self.num7_button = QtWidgets.QPushButton(window_)
        self.num7_button.setGeometry(QtCore.QRect(20, 130, 120, 40))
        self.num7_button.setCursor(cursor)
        self.num7_button.setStyleSheet(num_btn_stylesheet)
        self.num7_button.setObjectName("num7_button")
        # number 8
        self.num8_button = QtWidgets.QPushButton(window_)
        self.num8_button.setGeometry(QtCore.QRect(150, 130, 120, 40))
        self.num8_button.setCursor(cursor)
        self.num8_button.setStyleSheet(num_btn_stylesheet)
        self.num8_button.setObjectName("num8_button")
        # number 9
        self.num9_button = QtWidgets.QPushButton(window_)
        self.num9_button.setGeometry(QtCore.QRect(280, 130, 120, 40))
        self.num9_button.setCursor(cursor)
        self.num9_button.setStyleSheet(num_btn_stylesheet)
        self.num9_button.setObjectName("num9_button")

    def operator_button_ui(self, window_):
        """setup operator buttons ui

        Args:
            window_ (QtWidgets.QDialog): application window
        """
        cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        # operator +
        self.plus_button = QtWidgets.QPushButton(window_)
        self.plus_button.setGeometry(QtCore.QRect(410, 230, 120, 40))
        self.plus_button.setCursor(cursor)
        self.plus_button.setStyleSheet(operator_btn_stylesheet)
        self.plus_button.setObjectName("plus_button")
        # operator -
        self.sub_button = QtWidgets.QPushButton(window_)
        self.sub_button.setGeometry(QtCore.QRect(410, 180, 120, 40))
        self.sub_button.setCursor(cursor)
        self.sub_button.setStyleSheet(operator_btn_stylesheet)
        self.sub_button.setObjectName("sub_button")
        # operator *
        self.mul_button = QtWidgets.QPushButton(window_)
        self.mul_button.setGeometry(QtCore.QRect(410, 80, 120, 40))
        self.mul_button.setCursor(cursor)
        self.mul_button.setStyleSheet(mul_pow_btn_stylesheet)
        self.mul_button.setObjectName("mul_button")
        # operator /
        self.div_button = QtWidgets.QPushButton(window_)
        self.div_button.setGeometry(QtCore.QRect(410, 130, 120, 40))
        self.div_button.setCursor(cursor)
        self.div_button.setStyleSheet(operator_btn_stylesheet)
        self.div_button.setObjectName("div_button")
        # operator **
        self.power_button = QtWidgets.QPushButton(window_)
        self.power_button.setGeometry(QtCore.QRect(280, 80, 120, 40))
        self.power_button.setCursor(cursor)
        self.power_button.setStyleSheet(mul_pow_btn_stylesheet)
        self.power_button.setObjectName("power_button")

    def other_button_ui(self, window_):
        """setup other widgets ui

        Args:
            window_ (QtWidgets.QDialog): application window
        """
        cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        # number 0
        self.num0_button = QtWidgets.QPushButton(window_)
        self.num0_button.setGeometry(QtCore.QRect(20, 280, 120, 40))
        self.num0_button.setCursor(cursor)
        self.num0_button.setStyleSheet(num_btn_stylesheet)
        self.num0_button.setObjectName("num0_button")
        # character .
        self.dot_button = QtWidgets.QPushButton(window_)
        self.dot_button.setGeometry(QtCore.QRect(150, 280, 120, 40))
        self.dot_button.setCursor(cursor)
        self.dot_button.setStyleSheet(num_btn_stylesheet)
        self.dot_button.setObjectName("dot_button")
        # character =
        self.equal_button = QtWidgets.QPushButton(window_)
        self.equal_button.setGeometry(QtCore.QRect(280, 280, 250, 40))
        self.equal_button.setCursor(cursor)
        self.equal_button.setStyleSheet(equal_btn_stylesheet)
        self.equal_button.setObjectName("equal_button")
        # back button
        self.back_button = QtWidgets.QPushButton(window_)
        self.back_button.setGeometry(QtCore.QRect(150, 80, 120, 40))
        self.back_button.setCursor(cursor)
        self.back_button.setStyleSheet(delete_btn_stylesheet)
        self.back_button.setObjectName("back_button")
        # clear button
        self.clear_button = QtWidgets.QPushButton(window_)
        self.clear_button.setGeometry(QtCore.QRect(20, 80, 120, 40))
        self.clear_button.setCursor(cursor)
        self.clear_button.setStyleSheet(delete_btn_stylesheet)
        self.clear_button.setObjectName("clear_button")
        # line edit
        self.line_edit = QtWidgets.QLineEdit(window_)
        self.line_edit.setGeometry(QtCore.QRect(20, 20, 510, 50))
        self.line_edit.setStyleSheet(line_edit_stylesheet)
        self.line_edit.setText("")
        self.line_edit.setReadOnly(True)
        self.line_edit.setObjectName("line_edit")

    def setup_ui(self, window_):
        """setup ui of application

        Args:
            window_ (QtWidgets.QDialog): application window
        """
        window_.setObjectName("QDialog")
        window_.setEnabled(True)
        window_.resize(551, 343)
        window_.setMinimumSize(QtCore.QSize(551, 343))
        window_.setMaximumSize(QtCore.QSize(551, 343))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_.setWindowIcon(icon)
        window_.setAutoFillBackground(False)
        window_.setStyleSheet(window_stylesheet)
        # call other function
        self.number_button_ui(window_)
        self.operator_button_ui(window_)
        self.other_button_ui(window_)
        self.retranslate_ui(window_)
        QtCore.QMetaObject.connectSlotsByName(window_)
        self.set_buttons_signal()

    def retranslate_ui(self, window_):
        """retranslate ui

        Args:
            window_ (QtWidgets.QDialog): application window
        """
        _translate = QtCore.QCoreApplication.translate
        window_.setWindowTitle(_translate("QDialog", "Dori Calculator"))
        # numbers
        self.num0_button.setText(_translate("QDialog", "0"))
        self.num1_button.setText(_translate("QDialog", "1"))
        self.num2_button.setText(_translate("QDialog", "2"))
        self.num3_button.setText(_translate("QDialog", "3"))
        self.num4_button.setText(_translate("QDialog", "4"))
        self.num5_button.setText(_translate("QDialog", "5"))
        self.num6_button.setText(_translate("QDialog", "6"))
        self.num7_button.setText(_translate("QDialog", "7"))
        self.num8_button.setText(_translate("QDialog", "8"))
        self.num9_button.setText(_translate("QDialog", "9"))
        # operator
        self.plus_button.setText(_translate("QDialog", "➕"))
        self.sub_button.setText(_translate("QDialog", "➖"))
        self.mul_button.setText(_translate("QDialog", "✖️"))
        self.div_button.setText(_translate("QDialog", "➗"))
        self.power_button.setText(_translate("QDialog", "^"))
        # others
        self.equal_button.setText(_translate("QDialog", "="))
        self.dot_button.setText(_translate("QDialog", "."))
        self.back_button.setText(_translate("QDialog", "⟵"))
        self.clear_button.setText(_translate("QDialog", "⌫"))

    def set_buttons_signal(self):
        """set signal & slot of buttons
        """
        # numbers
        self.num0_button.clicked.connect(lambda: self.number_press('0'))
        self.num1_button.clicked.connect(lambda: self.number_press('1'))
        self.num2_button.clicked.connect(lambda: self.number_press('2'))
        self.num3_button.clicked.connect(lambda: self.number_press('3'))
        self.num4_button.clicked.connect(lambda: self.number_press('4'))
        self.num5_button.clicked.connect(lambda: self.number_press('5'))
        self.num6_button.clicked.connect(lambda: self.number_press('6'))
        self.num7_button.clicked.connect(lambda: self.number_press('7'))
        self.num8_button.clicked.connect(lambda: self.number_press('8'))
        self.num9_button.clicked.connect(lambda: self.number_press('9'))
        self.dot_button.clicked.connect(lambda: self.number_press('.'))
        # operator
        self.mul_button.clicked.connect(lambda: self.operator_press('×'))
        self.div_button.clicked.connect(lambda: self.operator_press('÷'))
        self.plus_button.clicked.connect(lambda: self.operator_press('+'))
        self.sub_button.clicked.connect(lambda: self.operator_press('₋'))
        self.power_button.clicked.connect(lambda: self.operator_press('^'))
        # back, clear, equal
        self.back_button.clicked.connect(self.back_press)
        self.clear_button.clicked.connect(self.clear_press)
        self.equal_button.clicked.connect(self.equal_press)

    def number_press(self, number: str):
        """slot of number buttons

        Args:
            number (str): number type
        """
        expression = self.line_edit.text()
        if expression and number == "." and expression[-1] == ".":
            return
        self.line_edit.setText(expression + number)

    def operator_press(self, operator: str):
        """slot of operator buttons

        Args:
            operator (str): operator type
        """
        expression = self.line_edit.text()
        if not expression:
            return
        if expression[-1] in ("×", "+", "₋", "÷", "^"):
            expression = expression[:-1]
        self.line_edit.setText(expression + operator)

    def back_press(self):
        """slot of back button
        """
        expression = self.line_edit.text()
        self.line_edit.setText(expression[:-1])

    def clear_press(self):
        """slot of clear button
        """
        self.line_edit.setText("")

    def default_stylesheet(self):
        """after x second back to default stylesheet of equal_button
        """
        sleep(0.3)
        self.equal_button.setStyleSheet(equal_btn_stylesheet)

    def show_warning(self):
        """change equal_button stylesheet to
        show not valid expression warning.
        """
        self.equal_button.setStyleSheet(equal_btn_stylesheet2)
        Thread(target=self.default_stylesheet).start()

    def equal_press(self):
        """slot of equal button
        """
        expression = self.line_edit.text()
        if not expression:
            return
        # change expression character for eval() function
        expression = expression.replace("×", "*")
        expression = expression.replace("₋", "-")
        expression = expression.replace("÷", "/")
        expression = expression.replace("^", "**")
        # calculate expression, if not valid show warning
        try:
            value = eval(expression)
        except:
            self.show_warning()
        else:
            self.line_edit.setText(str(value))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Calculator()
    ui.setup_ui(window)
    window.show()
    sys.exit(app.exec_())
