from PyQt6.QtWidgets import QMainWindow,QApplication,QLabel
import sys
from PyQt6.QtGui import QPixmap,QPainter,QPen,QColor,QMouseEvent,QPaintEngine
from PyQt6.QtCore import Qt
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(400,400)
        self.setWindowTitle("Paint App") 

    def paintEvent(self,event):
        painter=QPainter()  
        painter.begin(self)
        pen=QPen(QColor("#ebe834"),5)
        painter.setPen(pen)
        painter.drawPoint(100,100)
        painter.drawLine(0,0,100,100)
        painter.drawRect(100,100,200,200)
        painter.drawEllipse(100,100,200,200)
        painter.end()  

app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec())            