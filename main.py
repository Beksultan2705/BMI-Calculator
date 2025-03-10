import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMenuBar, QAction, QMessageBox

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("BMI Calculator")
        
        self.weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()
        
        self.height_label = QLabel("Height (m):")
        self.height_input = QLineEdit()
        
        self.result_label = QLabel("BMI: ")
        self.status_label = QLabel("Status: ")
        
        self.calc_button = QPushButton("Calculate BMI")
        self.calc_button.clicked.connect(self.calculate_bmi)
        
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
        
        layout = QVBoxLayout()
        layout.setMenuBar(menu_bar)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")
            
            bmi = weight / (height ** 2)
            self.result_label.setText(f"BMI: {bmi:.2f}")
            self.status_label.setText(f"Status: {self.get_bmi_status(bmi)}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for weight and height.")
    
    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("BMI: ")
        self.status_label.setText("Status: ")
    
    def show_help(self):
        QMessageBox.information(self, "How to Use", "Enter your weight in kg and height in meters, then click 'Calculate BMI' to see your BMI and status.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())
