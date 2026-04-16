import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QSize
from PyQt5.QtGui import QFont

class JarvisUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Irfan AI")
        self.setFixedSize(300, 400)

        # Transparent + always on top
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Title
        self.label = QLabel("IRFAN AI")
        self.label.setFont(QFont("Arial", 16))
        self.label.setStyleSheet("color: white;")
        layout.addWidget(self.label)

        # Status
        self.status = QLabel("Idle")
        self.status.setStyleSheet("color: #94a3b8;")
        layout.addWidget(self.status)

        # Mic Button
        self.button = QPushButton("🎤")
        self.button.setFixedSize(100, 100)
        self.button.setStyleSheet("""
            QPushButton {
                border-radius: 50px;
                background-color: #1e293b;
                color: white;
                font-size: 30px;
            }
            QPushButton:hover {
                background-color: #3b82f6;
            }
        """)
        self.button.clicked.connect(self.animate_button)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def animate_button(self):
        self.status.setText("Listening...")

        self.anim = QPropertyAnimation(self.button, b"size")
        self.anim.setDuration(500)
        self.anim.setStartValue(QSize(100, 100))
        self.anim.setEndValue(QSize(120, 120))
        self.anim.setLoopCount(2)
        self.anim.start()

        # Yaha baad me voice + AI connect karenge

app = QApplication(sys.argv)
window = JarvisUI()
window.show()
sys.exit(app.exec_())