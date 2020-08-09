import sys, pyowm
from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Any
from test import Ui_Dialog

# Create app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


# Hook Logic
def get_weather_city():
    owm = pyowm.OWM('591a3d5959297c7a6ad638f83431deb7')
    city = ui.lineEdit.text()
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']
    ui.label.setText(f'Темпераура: {temperature}')


ui.pushButton.clicked.connect(get_weather_city)

# Main Loop
sys.exit(app.exec_())
