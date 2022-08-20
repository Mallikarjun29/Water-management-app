from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
from PyQt5.QtWidgets import *
import mplcursors

class MplWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure(tight_layout=True))

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        self.canvas.axes.spines[["right",'top']].set_visible(False)
        sns.set()
        sns.set_context("talk")
        self.toolbar = NavigationToolbar(self.canvas, self)



        
