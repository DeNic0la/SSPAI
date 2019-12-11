import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

#App Definieren mit den Parametern welche vom System eingegeben werden
app = QApplication(sys.argv)
app.setStyle('WindowsVista')

#Neues Fenster Definieren
mainGUI = QWidget()

#Layout des Fensters Festlegen
mainLayout = QVBoxLayout()
mainLayout.addWidget(QPushButton("Panic Button"))


mainGUI.setLayout(mainLayout)

#Fenster Anzeigen
mainGUI.show()

#Beim Schliessen des Fensters die Komplette Applikation Beenden
sys.exit(app.exec_())

