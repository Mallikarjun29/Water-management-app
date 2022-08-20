from PyQt5 import QtWidgets, QtCore, QtGui
from dashboard import Ui_MainWindow
import threading
from PyQt5.QtWidgets import *
import matplotlib.dates as md
from datetime import datetime
import mysql.connector as mysql
from mplwidget import MplWidget
import time
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('build/main_new/water-drop-png-46392.png'))
        self.setWindowTitle('Water Dashboard')
        self.conn = mysql.connect(
            host="10.21.163.236",
            database="new_water_dashboard",
            user="root",
            password="realtime123")
        self.cur = self.conn.cursor(buffered=True)
        sha = QGraphicsDropShadowEffect()
        sha.setBlurRadius(20)
        self.tabWidget.setGraphicsEffect(sha)
        self.stop=False
        self.t = threading.Thread(target=self.plot_main)
        self.t.start()
        self.pushButton.clicked.connect(lambda: self.stop_thread())

    def stop_thread(self):
        # MplWidget.blah()
        time.sleep(10)
        self.stop = True

    def reproduce_tab(self, s):
        globals()[s+'tab_2']= QtWidgets.QWidget()
        globals()[s+'tab_2'].setObjectName(s+"tab_2")
        globals()[s+'gridLayout_2'] = QtWidgets.QGridLayout(globals()[s+'tab_2'])
        globals()[s+'gridLayout_2'].setObjectName(s+"gridLayout_2")
        globals()[s+'verticalLayout_6'] = QtWidgets.QVBoxLayout()
        globals()[s+'verticalLayout_6'].setObjectName(s+"verticalLayout_6")
        globals()[s+'horizontalLayout_3'] = QtWidgets.QHBoxLayout()
        globals()[s+'horizontalLayout_3'].setObjectName(s+"horizontalLayout_3")
        globals()[s+'widget_10'] = MplWidget(globals()[s+'tab_2'])
        globals()[s+'widget_10'].setObjectName(s+"widget_10")
        globals()[s+'horizontalLayout_3'].addWidget(globals()[s+'widget_10'])
        globals()[s+'horizontalLayout_4'] = QtWidgets.QHBoxLayout()
        globals()[s+'horizontalLayout_4'].setObjectName(s+"horizontalLayout_4")
        globals()[s+'verticalLayout_7'] = QtWidgets.QVBoxLayout()
        globals()[s+'verticalLayout_7'].setObjectName(s+"verticalLayout_7")
        globals()[s+'label_14'] = QtWidgets.QLabel(globals()[s+'tab_2'])
        globals()[s+'label_14'].setStyleSheet("background-color: rgb(35, 122, 181);")
        globals()[s+'label_14'].setObjectName(s+"label_14")
        globals()[s + 'label_14'].setAlignment(QtCore.Qt.AlignCenter)
        globals()[s + 'label_14'].setStyleSheet("background-color: rgb(35, 122, 181);font-size:18pt; font-weight:600; color:#ffffff;")
        globals()[s+'label_14'].setText(s)
        globals()[s+'verticalLayout_7'].addWidget(globals()[s+'label_14'])
        globals()[s+'label_15'] = QtWidgets.QLabel(globals()[s+'tab_2'])
        globals()[s+'label_15'].setStyleSheet("background-color: rgb(35, 122, 181);")
        globals()[s+'label_15'].setObjectName(s+"label_15")
        globals()[s + 'label_15'].setAlignment(QtCore.Qt.AlignCenter)
        globals()[s + 'label_15'].setStyleSheet("background-color: rgb(35, 122, 181);font-size:18pt; color:#ffffff;")
        globals()[s + 'label_15'].setText('FLOW A')
        globals()[s+'verticalLayout_7'].addWidget(globals()[s+'label_15'])
        globals()[s+'lcdNumber_10'] = QtWidgets.QLCDNumber(globals()[s+'tab_2'])
        globals()[s+'lcdNumber_10'].setObjectName(s+"lcdNumber_10")
        globals()[s+'verticalLayout_7'].addWidget(globals()[s+'lcdNumber_10'])
        globals()[s+'label_16'] = QtWidgets.QLabel(globals()[s+'tab_2'])
        globals()[s+'label_16'].setStyleSheet("background-color: rgb(35, 122, 181);")
        globals()[s+'label_16'].setObjectName(s+"label_16")
        globals()[s + 'label_16'].setAlignment(QtCore.Qt.AlignCenter)
        globals()[s + 'label_16'].setStyleSheet("background-color: rgb(35, 122, 181);font-size:18pt; color:#ffffff;")
        globals()[s + 'label_16'].setText('FLOW B')
        globals()[s+'verticalLayout_7'].addWidget(globals()[s+'label_16'])
        globals()[s+'lcdNumber_11'] = QtWidgets.QLCDNumber(globals()[s+'tab_2'])
        globals()[s+'lcdNumber_11'].setObjectName(s+"lcdNumber_11")
        globals()[s+'verticalLayout_7'].addWidget(globals()[s+'lcdNumber_11'])
        globals()[s+'label_17'] = QtWidgets.QLabel(globals()[s+'tab_2'])
        globals()[s+'label_17'].setStyleSheet("background-color: rgb(35, 122, 181);")
        globals()[s+'label_17'].setObjectName(s+"label_17")
        globals()[s+'label_17'].setAlignment(QtCore.Qt.AlignCenter)
        globals()[s + 'label_17'].setStyleSheet("background-color: rgb(35, 122, 181);font-size:18pt; color:#ffffff;")
        globals()[s + 'label_17'].setText('LEVEL')
        globals()[s+'verticalLayout_7'].addWidget(globals()[s+'label_17'])
        globals()[s+'lcdNumber_12'] = QtWidgets.QLCDNumber(globals()[s+'tab_2'])
        globals()[s+'lcdNumber_12'].setObjectName(s+"lcdNumber_12")
        globals()[s+'verticalLayout_7'].addWidget(globals()[s+'lcdNumber_12'])
        globals()[s+'horizontalLayout_4'].addLayout(globals()[s+'verticalLayout_7'])
        globals()[s+'horizontalLayout_3'].addLayout(globals()[s+'horizontalLayout_4'])
        globals()[s+'widget_3'] = MplWidget(globals()[s+'tab_2'])
        globals()[s+'widget_3'].setObjectName(s+"widget_3")
        globals()[s+'horizontalLayout_3'].addWidget(globals()[s+'widget_3'])
        globals()[s+'verticalLayout_6'].addLayout(globals()[s+'horizontalLayout_3'])
        globals()[s+'gridLayout_2'].addLayout(globals()[s+'verticalLayout_6'], 0, 0, 1, 1)
        globals()[s+'widget_4'] = MplWidget(globals()[s+'tab_2'])
        globals()[s+'widget_4'].setObjectName(s+"widget_4")
        globals()[s+'gridLayout_2'].addWidget(globals()[s+'widget_4'], 1, 0, 1, 1)
        _translate = QtCore.QCoreApplication.translate
        index = self.tabWidget.addTab(globals()[s + 'tab_2'], s)
        self.tabWidget.setTabText(self.tabWidget.indexOf(globals()[s+'tab_2']), _translate("MainWindow", s))
        print('new tab created')


    def plot_main(self):
        nodes = {}
        o=1
        while True:
            time.sleep(2)
            try:
                # plotting bar
                self.cur.execute('SELECT * FROM water_table ORDER BY id DESC LIMIT 1')
                y=self.cur.fetchone()
                self.conn.commit()
                print(y)
                nodes[y[2]]=(y[3],y[4],y[5])
                y1=[]
                x = []
                y2 = []
                y3 = []
                st='Node_'
                st +='{0}'
                for i in nodes.keys():
                    y1.append(nodes[i][2])
                    x.append(st.format(i))
                    y2.append(nodes[i][0])
                    y3.append(nodes[i][1])

                self.widget.canvas.axes.clear()
                ax=self.widget.canvas.axes.bar(x, y1)
                self.widget.canvas.axes.set_xlabel("Nodes")
                self.widget.canvas.axes.set_ylabel("Tank Level")
                self.widget.canvas.draw()
                ax.remove()


                # #plotting horizontal bar graph
                #     #left horizontal
                self.widget_13.canvas.axes.clear()
                ax=self.widget_13.canvas.axes.barh(x, y2)
                self.widget_13.canvas.axes.set_xlabel("Flow A")
                self.widget_13.canvas.axes.set_ylabel("Nodes")
                self.widget_13.canvas.draw()

                #     #right horizontal
                self.widget_2.canvas.axes.clear()
                ax=self.widget_2.canvas.axes.barh(x, y3)
                self.widget.canvas.axes.set_xlabel("Flow B")
                self.widget.canvas.axes.set_ylabel("Nodes")
                self.widget_2.canvas.draw()
                ax.remove()

                if self.stop:
                    time.sleep(20)
                    self.stop=False



                # # tab
                if o==1:
                    self.cur.execute('SELECT * FROM water_table ORDER BY id DESC LIMIT 25000')
                    h = self.cur.fetchall()
                    self.conn.commit()
                    l_node={}
                    h.reverse()
                    k=[]
                    c=[]
                    for i in range(len(h)):
                        if not h[i][2] in l_node.keys():
                            l_node[h[i][2]] = [[], [], [], []]
                            st = 'Node_'
                            st += '{0}'
                            k.append(st.format(h[i][2]))
                            c.append(h[i][2])
                            self.reproduce_tab(st.format(h[i][2]))
                            # self.reproduce_lcd(st.format(h[i][2]))


                            # call a function here (first make different file)
                        g = datetime.strptime(h[i][1], '%d/%m/%Y %H:%M:%S')
                        l_node[h[i][2]][0].append(g)
                        l_node[h[i][2]][1].append(h[i][3])
                        l_node[h[i][2]][2].append(h[i][4])
                        l_node[h[i][2]][3].append(h[i][5])

                g=datetime.strptime(y[1], '%d/%m/%Y %H:%M:%S')
                l_node[y[2]][0].append(g)
                l_node[y[2]][1].append(y[3])
                l_node[y[2]][2].append(y[4])
                l_node[y[2]][3].append(y[5])
                del l_node[y[2]][0][0]
                del l_node[y[2]][1][0]
                del l_node[y[2]][2][0]
                del l_node[y[2]][3][0]

                o=9
                time.sleep(1)
                for i in range(len(k)):
                    #bottom tab
                    globals()[k[i] + 'widget_4'].canvas.axes.clear()
                    globals()[k[i] + 'widget_4'].canvas.axes.plot(l_node[c[i]][0], l_node[c[i]][3], linestyle='solid')
                    globals()[k[i] + 'widget_4'].canvas.axes.xaxis.set_major_locator(md.HourLocator(interval=1))
                    globals()[k[i] + 'widget_4'].canvas.axes.xaxis.set_major_formatter(md.DateFormatter('%d %b\n%H:%M'))
                    globals()[k[i] + 'widget_4'].canvas.axes.set_ylabel("Tank Level")
                    globals()[k[i] + 'widget_4'].canvas.draw()

                    #left tab
                    globals()[k[i] + 'widget_10'].canvas.axes.plot(l_node[c[i]][0], l_node[c[i]][1], 'b', linestyle='solid')
                    globals()[k[i] + 'widget_10'].canvas.axes.xaxis.set_major_locator(md.HourLocator(interval=3))
                    globals()[k[i] + 'widget_10'].canvas.axes.xaxis.set_major_formatter(md.DateFormatter('%d %b\n%H:%M'))
                    globals()[k[i] + 'widget_10'].canvas.axes.set_ylabel("Flow A")
                    globals()[k[i] + 'widget_10'].canvas.draw()

                    #right tab
                    globals()[k[i] + 'widget_3'].canvas.axes.plot(l_node[c[i]][0], l_node[c[i]][2], 'b', linestyle='solid')
                    globals()[k[i]+ 'widget_3'].canvas.axes.xaxis.set_major_locator(md.HourLocator(interval=3))
                    globals()[k[i] + 'widget_3'].canvas.axes.xaxis.set_major_formatter(md.DateFormatter('%d %b\n%H:%M'))
                    globals()[k[i] + 'widget_3'].canvas.axes.set_ylabel("Flow B")
                    globals()[k[i] + 'widget_3'].canvas.draw()

                    #lcd
                    globals()[k[i]+'lcdNumber_10'].display(str(l_node[c[i]][1][-1]))
                    globals()[k[i]+'lcdNumber_11'].display(str(l_node[c[i]][2][-1]))
                    globals()[k[i]+'lcdNumber_12'].display(str(l_node[c[i]][3][-1]))

                    # print('updated')



                # self.lcdNumber.display(str(l_node[2][1]))
                # self.lcdNumber_2.display(str(l_node[2][2]))
                # self.lcdNumber_3.display(str(l_node[2][3]))



            except (KeyboardInterrupt, SystemExit):
                self.conn.close()
                self.t.join()
                break



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
