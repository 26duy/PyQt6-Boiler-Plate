import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
 
class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("score_board.ui", self)

        #--- initialise variables

        #--- connect signals and slots
        self.signals()
    def connect_buttons(self):
        # Team A score buttons
        self.pushButton_team_a_plus1.clicked.connect(lambda: self.update_score(0, 1))
        self.pushButton_team_a_plus2.clicked.connect(lambda: self.update_score(0, 2))
        self.pushButton_team_a_plus3.clicked.connect(lambda: self.update_score(0, 3))

        # Team B score buttons
        self.pushButton_team_b_plus1.clicked.connect(lambda: self.update_score(1, 1))
        self.pushButton_team_b_plus2.clicked.connect(lambda: self.update_score(1, 2))
        self.pushButton_team_b_plus3.clicked.connect(lambda: self.update_score(1, 3))

        # Timer control buttons
        self.pushButton_pause.clicked.connect(self.pause_timer)
        self.pushButton_continue.clicked.connect(self.resume_timer)
        self.pushButton_reclock.clicked.connect(self.reset_timer)
        self.pushButton_start.clicked.connect(self.start_timer)

    def signals(self):
        """
        Connect signals to the corresponding slots.
        """
        pass #Add signal connections here
    # --- slots ---#
        """
        functions that are cslls from the signals go below here.
        """
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())