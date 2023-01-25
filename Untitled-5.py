import sys
import time
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class View1GraphVisualization(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        canvas = FigureCanvas(Figure(figsize = (20, 15)))
        vbox = QVBoxLayout(self.main_widget)

        self.addToolBar(NavigationToolbar(canvas, self))

        dynamic_canvas = FigureCanvas(Figure(figsize = (20, 15)))
        vbox.addWidget(dynamic_canvas)

        self.dynamic_ax = dynamic_canvas.figure.subplots()
        #100ms의 시간간격으로 그래프를 업데이트함
        self.timer = dynamic_canvas.new_timer(100, [(self.update_canvas, (), {})])
        self.timer.start()

        self.setWindowTitle('view1')
        #창의 위치를 모니터 좌상단에서부터 가로 300px, 세로 100px, 창의 크기를 가로 600px, 세로 400px로 설정
        self.setGeometry(300, 100, 600, 400)
        #그래프 띄움
        self.show()
    
    def update_canvas(self):
        self.dynamic_ax.clear()
        self.dynamic_ax.plot(self.datahub.timestampOfView1, self.datahub.view1)
        self.dynamic_ax.figure.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = View1GraphVisualization()
    sys.exit(app.exec_())
