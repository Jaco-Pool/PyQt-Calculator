# pycalc.py

"""PyCalc is a simple calculator built with Python and PyQt."""

import sys  # imports sys. This module provides the exit() function, which we use to terminate.
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget  #  imports the required classes from PyQt6.QtWidgets.

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235  # creates a Python constant to hold a fixed window size in pixels for our calculator app.
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class PyCalcWindow(QMainWindow):  # creates the PyCalcWindow class to provide the app’s GUI. This class inherits from QMainWindow.
    """PyCalc's main window (GUI or view)."""

    def __init__(self):  # defines the class initializer.
        super().__init__()   # calls .__init__() on the super class for initialization purposes.
        self.setWindowTitle("PyCalc")  # sets the window’s title to "PyCalc".
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)  # uses .setFixedSize() to give the window a fixed size.
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self) 
        centralWidget.setLayout(self.generalLayout)        
        self.setCentralWidget(centralWidget)  ## create a QWidget object and set it as the window’s central widget. 
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")

def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])  # creates a QApplication object named pycalcApp
    pycalcWindow = PyCalcWindow()  # creates an instance of the app’s window, pycalcWindow
    pycalcWindow.show()  # shows the GUI by calling .show() on the window object.
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())  # runs the application’s event loop with .exec().

if __name__ == "__main__":
    main()  # calls main() to execute.