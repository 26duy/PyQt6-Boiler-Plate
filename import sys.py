import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QSpinBox)
from PyQt6.QtCore import QTime, QTimer, Qt

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Countdown Timer")
        self.setGeometry(100, 100, 400, 200)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Time display label
        self.time_label = QLabel("00:00:00")
        self.time_label.setStyleSheet("font-size: 48px; font-weight: bold;")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.time_label)
        
        # Time setting controls
        time_set_layout = QHBoxLayout()
        self.hour_spin = QSpinBox()
        self.hour_spin.setRange(0, 23)
        self.min_spin = QSpinBox()
        self.min_spin.setRange(0, 59)
        self.sec_spin = QSpinBox()
        self.sec_spin.setRange(0, 59)
        
        time_set_layout.addWidget(QLabel("Hours:"))
        time_set_layout.addWidget(self.hour_spin)
        time_set_layout.addWidget(QLabel("Minutes:"))
        time_set_layout.addWidget(self.min_spin)
        time_set_layout.addWidget(QLabel("Seconds:"))
        time_set_layout.addWidget(self.sec_spin)
        main_layout.addLayout(time_set_layout)
        
        # Control buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.pause_button = QPushButton("Pause")
        self.reset_button = QPushButton("Reset")
        
        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.reset_button)
        main_layout.addLayout(button_layout)
        
        # Initialize timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.current_time = QTime(0, 0, 0)
        self.is_running = False
        
        # Initial display
        self.update_time_display()
    
    def start_timer(self):
        """Start or resume the timer"""
        if not self.is_running:
            self.is_running = True
            self.timer.start(1000)  # Trigger every second
    
    def pause_timer(self):
        """Pause the timer"""
        if self.is_running:
            self.is_running = False
            self.timer.stop()
    
    def reset_timer(self):
        """Reset the timer to the currently set time"""
        self.pause_timer()
        self.current_time = QTime(
            self.hour_spin.value(), 
            self.min_spin.value(), 
            self.sec_spin.value()
        )
        self.update_time_display()
    
    def update_timer(self):
        """Update the timer display and handle countdown completion"""
        if self.current_time == QTime(0, 0, 0):
            self.pause_timer()
            return
            
        self.current_time = self.current_time.addSecs(-1)
        self.update_time_display()
    
    def update_time_display(self):
        """Update the time display label"""
        time_str = self.current_time.toString("hh:mm:ss")
        self.time_label.setText(time_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec())