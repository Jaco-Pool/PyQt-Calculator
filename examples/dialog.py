# dialog.py

"""Dialog-style application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class Window(QDialog):  # defines a Window class for the app’s GUI by inheriting from QDialog.
    def __init__(self):
        super().__init__(parent=None)  # calls the parent class’s .__init__() method using super().
        self.setWindowTitle("QDialog") # sets the window’s title.
        dialogLayout = QVBoxLayout()  # assigns a QVBoxLayout object to dialogLayout.
        formLayout = QFormLayout()  #assigns a QFormLayout object to formLayout.
        formLayout.addRow("Name:", QLineEdit())      #
        formLayout.addRow("Age:", QLineEdit())       ##  add
        formLayout.addRow("Job:", QLineEdit())       ##  widgets
        formLayout.addRow("Hobbies:", QLineEdit())   #
        dialogLayout.addLayout(formLayout)  # This call embeds the form layout into the global dialog layout.
        buttons = QDialogButtonBox()  # defines a button box, which provides a convenient space to display the dialog’s buttons.
        buttons.setStandardButtons(  # add two standard buttons, Ok and Cancel, to the dialog.
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)  # adds the button box to the dialog by calling .addWidget().
        self.setLayout(dialogLayout)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())