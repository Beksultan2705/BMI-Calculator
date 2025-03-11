import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QMenuBar, QAction, QMessageBox, QFrame
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(350, 300)
        
        self.title_label = QLabel("BMI Calculator", self)
        self.title_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        
        self.weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()
        
        self.height_label = QLabel("Height (cm):")
        self.height_input = QLineEdit()
        
        self.calc_button = QPushButton("Calculate BMI")
        self.calc_button.clicked.connect(self.calculate_bmi)
        
        self.result_label = QLabel("Your BMI:")
        self.result_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFrameShape(QFrame.Box)
        self.result_label.setStyleSheet("background-color: lightgray;")
        
        self.status_label = QLabel("Status:")
        self.status_label.setAlignment(Qt.AlignCenter)
        
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        help_menu = menu_bar.addMenu("Help")
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)
        
        help_action = QAction("How to Use", self)
        help_action.triggered.connect(self.show_help)
        
        file_menu.addAction(clear_action)
        file_menu.addAction(exit_action)
        help_menu.addAction(help_action)
        
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.weight_label, 0, 0)
        grid_layout.addWidget(self.weight_input, 0, 1)
        grid_layout.addWidget(self.height_label, 1, 0)
        grid_layout.addWidget(self.height_input, 1, 1)
        
        vbox = QVBoxLayout()
        vbox.setMenuBar(menu_bar)
        vbox.addWidget(self.title_label)
        vbox.addLayout(grid_layout)
        vbox.addWidget(self.calc_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.status_label)
        
        self.setLayout(vbox)
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text()) / 100
            
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")
            
            bmi = weight / (height ** 2)
            self.result_label.setText(f"Your BMI: {bmi:.1f}")
            self.update_bmi_status(bmi)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for weight and height.")
    
    def update_bmi_status(self, bmi):
        if bmi < 18.5:
            status = "Underweight"
            color = "#FFC107"  # Yellow
        elif 18.5 <= bmi < 25:
            status = "Normal weight"
            color = "#4CAF50"  # Green
        elif 25 <= bmi < 30:
            status = "Overweight"
            color = "#FF9800"  # Orange
        else:
            status = "Obese"
            color = "#F44336"  # Red
        
        self.status_label.setText(f"Status: {status}")
        self.result_label.setStyleSheet(f"background-color: {color}; color: white;")
    
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("Your BMI:")
        self.result_label.setStyleSheet("background-color: lightgray;")
        self.status_label.setText("Status:")
    
    def show_help(self):
        QMessageBox.information(self, "How to Use", "Enter your weight in kg and height in cm, then click 'Calculate BMI' to see your BMI and status.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())
