import sys
from qtpy import QtWidgets
from UI.mainwindow import Ui_MainWindow
from FetcherArticle import ArticleFetcher


app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Twitter Crawler")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.onPushButtonClick)

    def onPushButtonClick(self):
        url = self.ui.urlInput.text()
        directory = (self.ui.directory.text())
        filename = (self.ui.filename.text())
        fetcher = ArticleFetcher(url, directory, filename)
        fetcher.fetch()
        self.ui.finished.setText("Done!")


window = MainWindow()
window.show()
sys.exit(app.exec())
