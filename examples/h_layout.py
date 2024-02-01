# h_layout.py

"""Horizontal layout example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")

layout = QHBoxLayout()                    # creates a QHBoxLayout object called layout
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))   # add three buttons to layout by calling the .addWidget() method.
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)                  # sets layout as your window’s layout with .setLayout().

window.show()
sys.exit(app.exec())