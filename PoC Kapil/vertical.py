import sys
from PyQt5.QtWidgets import (
    QMainWindow,  QWidget, QTabBar, QApplication, QTabWidget,
    QStyle, QStylePainter, QStyleOptionTab, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPoint, QRect


class TabBar(QTabBar):
    def tabSizeHint(self, index):
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QStylePainter(self)
        opt = QStyleOptionTab()

        for index in range(self.count()):
            self.initStyleOption(opt, index)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            # painter.setBrush(Qcolor(0, 100, 0, 100))
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QRect(QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(index).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt)
            painter.style()
            painter.restore()
            painter.setOpacity(500)


class VerticalTabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.setStyleSheet(
            "QTabWidget::pane{border: 0}")
        # self.setStyleSheet("QTabBar::tab{background:white}")
        self.setStyleSheet(
            "QTabBar::tab::selected{background:#787E49}")
        # self.setStyleSheet(
        #     "QTabBar::tab{ margin-left:20px; margin-right:20px}")
        self.setTabBar(TabBar())
        self.setTabPosition(QTabWidget.West)


class app_window(QMainWindow):
    def __init__(self):
        super().__init__()
        print("heya")
        tabs = VerticalTabWidget()
        # a = QWidget.setWindowIcon(self, QIcon('display.png'))
        liz = ["Display", "Diagnostics", "Data Management",
               "User Management", "Maintenence", "Hardware",
               "Privacy & Security", "Licence Management", "Help & Support"]
        icon_liz = ['display.png', 'diagnostics.png', 'data.png', 'User.png',
                    'maintenance.png', 'HW.png', 'privacy.png', 'licence.png',
                    'help.png']

        for i in range(len(liz)):
            tabs.addTab(QWidget(), liz[i])
            tabs.setTabIcon(i, QIcon(icon_liz[i]))

            self.setCentralWidget(tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = app_window()
    w.show()
    sys.exit(app.exec_())
