from PySide2.QtWidgets import QWidget, QApplication
from button_ui import Ui_Form
import sys
import aiohttp
import asyncio


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()

        self.page = Ui_Form()
        self.page.setupUi(self)
        self.page.SEND.clicked.connect(self.sendClicked)

    def sendClicked(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())

    async def fetch_data(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # data = await asyncio.gather(response.json())
                data = await response.json()
                return data

    async def main(self):
        url = 'http://localhost:8080/api/users'
        data = await self.fetch_data(url)
        print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())
