import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTime,QTimer
 
class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the main window and set up the UI.
        """
        super().__init__()
        uic.loadUi("time_machine.ui", self)

        self.show_time()

        # --- initialise variables
        self.clock_timer = QTimer()
        self.clock_timer. start(1000)
       

        self.signals()

    def signals(self):
        """
        Connect UI signals to the corresponding slots.
        """
        self.clock_timer.timeout.connect(self.show_time)
     
    # ---- SLOTS ---- #
    """
    functions that are called from the signals go below here
    """
    # clock
    def show_time(self):
        """
        Update the clock display with the current time.
        """
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("h:mm:ssa")
        self.label_clock.setText(formatted_time)

  