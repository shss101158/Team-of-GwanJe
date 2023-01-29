from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import QObject, QThread, pyqtSlot, QRunnable, QThreadPool
import sys
import threading
import sys, os
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import time
from Untitled10Basis import View1GraphVisualization

class MapViewer_Thread(QThread):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        # self.setWindowTitle("Real-time Dynamic Map")

        # Create the QWebEngineView widget
        self.view = QWebEngineView(self.mainwindow)
        self.view.setGeometry(0, 0, 800, 600)

        # Load the HTML file that contains the leaflet map
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        file_path = os.path.join(dir_path, 'map.html')
        self.view.load(QUrl.fromLocalFile(file_path))
        self.view.show()


    def on_load_finished(self):
        # Get the QWebEnginePage object
        try:
            page = self.view.page()
            print("eeeeeee")

            # Inject a JavaScript function to update the marker's location
            script = """
            var map = L.map("map").setView([51.5, -0.09], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
                maxZoom: 18,
            }).addTo(map);
            var marker = L.marker([51.5, -0.09]).addTo(map);
            var lat = 51.5;
            var lng = -0.09;
            function updateMarker() {
                lat = lat + 0.001;
                lng = lng + 0.001;
                marker.setLatLng([lat, lng]);
            }
            """
            print("wwwwwwwwww")
            page.runJavaScript(script)

            # Create a QTimer to call the updateMarker function every second
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_marker)
            self.timer.start(1000)
        except:
            print("error appeared!")
    def update_marker(self):
        # Call the JavaScript function to update the marker's location
        self.view.page().runJavaScript("updateMarker()")

    # Connect the QWebEngineView's loadFinished signal to the on_load_finished slot
    def run(self):
        self.view.loadFinished.connect(self.on_load_finished)
        print("showed")

class GraphViewer_Thread(QThread):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow

        self.view = QWebEngineView(self.mainwindow)
        self.view.setGeometry(0, 0, 800, 600)

        hbox = QHBoxLayout()
        self.pw1 = pg.PlotWidget(title="line chart")

        hbox.addWidget(self.pw1)
        self.setLayout(hbox)

        # self.setGeometry(300, 100, 800, 500)  # x, y, width, height
        self.setWindowTitle("Untitled-10Base")

        self.x = []
        self.y = []
        # self.pw1.setXRange(1, 10)
        # self.pw1.setYRange(1, 10)
        # self.pw1.enableAutoScale()
        # self.pw1.enableAutoRange()  # x,y축 모두 autorange..
        # self.pw1.enableAutoRange(axis='x', enable=True)
        # self.pw1.enableAutoRange(axis='x')
        # self.pw1.enableAutoRange(axis='y')
        # self.pw1.enableAutoRange(axis='xy')

        # self.pw2.enableAutoRange()
        self.pl = self.pw1.plot(pen='g')

        self.mytimer = QTimer()
        self.mytimer.start(1000)  # 1초마다 차트 갱신 위함...
        self.mytimer.timeout.connect(self.get_data)

        self.draw_chart(self.x, self.y)
        self.show()

    def draw_chart(self, x, y):
        self.pl.setData(x=x, y=y)  # line chart 그리기

    @pyqtSlot()
    def get_data(self):
        # print(time.localtime())
        # print(time.strftime("%H%M%S", time.localtime()))
        data: str = time.strftime("%S", time.localtime())  # 초 단위만 구함.

        last_x = self.datahub.timeSpace [-1]
        self.x.append(last_x)

        self.y.append(self.datahub.View1 [-1])
        self.draw_chart(self.x, self.y)
        

class MainWindow(QMainWindow):
    def __init__(self, datahub):
        self.app = QApplication(sys.argv)
        super().__init__()
        # self.widgethub = Widgethub()
        self.datahub = datahub
        self.mapviewer = MapViewer_Thread(self)

        #버튼 누르면 연결해야하는 것
        self.show_map_button = QPushButton("Show map",self)
        self.show_map_button.clicked.connect(self.start_mapviewer)
   
    def start_mapviewer(self):

        self.mapviewer.start()


    def start_View1GraphVisualization(self):
    
        self.show()


    def setEventLoop(self):
        sys.exit(self.app.exec_())
