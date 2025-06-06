import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer, QTime, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("score_board.ui", self)

        # Initialize scores
        self.team_a_score = 0
        self.team_b_score = 0

        # Initialize timer - related variables
        self.timer_running = False
        self.game_time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        # Connect button signals to slot functions
        self.connect_buttons()

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

    def update_score(self, team_index, increment):
        if team_index == 0:
            self.team_a_score += increment
            self.label_team_a_score.setText(str(self.team_a_score))
        else:
            self.team_b_score += increment
            self.label_team_b_score.setText(str(self.team_b_score))

    def start_timer(self):
        self.timer_running = True
        self.timer.start(1000)

    def pause_timer(self):
        self.timer_running = False
        self.timer.stop()

    def resume_timer(self):
        self.timer_running = True
        self.timer.start(1000)

    def reset_timer(self):
        self.timer_running = False
        self.timer.stop()
        self.game_time = QTime(0, 0, 0, 0)
        self.update_time_display()

    def update_time(self):
        if self.timer_running:
            self.game_time = self.game_time.addSecs(1)
            self.update_time_display()

    def update_time_display(self):
        formatted_time = self.game_time.toString("hh:mm:ss")
        self.label_time.setText(formatted_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())