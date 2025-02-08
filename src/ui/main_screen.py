from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QListWidget, QMessageBox, QFileDialog, QHBoxLayout, QComboBox
from event_manager import EventManager
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.event_manager = EventManager()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Event Management System')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel('Manage Events & Participants')
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.event_input = QComboBox()
        self.event_input.setEditable(True)
        self.event_input.setPlaceholderText("Select or enter event name")
        self.event_input.currentTextChanged.connect(self.on_event_selected)
        layout.addWidget(self.event_input)

        self.participant_list = QListWidget()
        layout.addWidget(self.participant_list)

        self.participant_input = QLineEdit()
        self.participant_input.setPlaceholderText(
            "Enter: Name, Student ID, Status")
        layout.addWidget(self.participant_input)

        # Apply stylesheet to change placeholder text color
        self.setStyleSheet("""
            QComboBox QAbstractItemView {
                color: gray;
            }
            QLineEdit[placeholderText] {
                color: gray;
            }
        """)

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()

        self.add_event_button = QPushButton("Add Event")
        self.add_event_button.clicked.connect(self.add_event)
        button_layout.addWidget(self.add_event_button)

        self.add_participant_button = QPushButton("Add Participant")
        self.add_participant_button.clicked.connect(self.add_participant)
        button_layout.addWidget(self.add_participant_button)

        self.import_button = QPushButton("Import from Excel")
        self.import_button.clicked.connect(self.import_from_excel)
        button_layout.addWidget(self.import_button)

        self.export_button = QPushButton("Export to Excel")
        self.export_button.clicked.connect(self.export_participants)
        button_layout.addWidget(self.export_button)

        # Add the horizontal layout to the main layout
        layout.addLayout(button_layout)

        self.mark_attended_button = QPushButton("Mark as Attended")
        self.mark_attended_button.clicked.connect(self.mark_as_attended)
        layout.addWidget(self.mark_attended_button)

        self.summary_button = QPushButton("Show Summary")
        self.summary_button.clicked.connect(self.show_summary)
        layout.addWidget(self.summary_button)

        self.show()

    def import_from_excel(self):
        """Loads participant data from an Excel file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")
        if not file_path:
            return

        try:
            df = pd.read_excel(file_path)

            # Validate required columns
            required_columns = {"Event Name",
                                "Participant Name", "Student ID", "Status"}
            if not required_columns.issubset(df.columns):
                QMessageBox.warning(
                    self, "Error", "Invalid Excel format. Required columns: Event Name, Participant Name, Student ID, Status")
                return

            for _, row in df.iterrows():
                event_name = row["Event Name"]
                participant = (
                    row["Participant Name"], row["Student ID"], row["Status"])

                self.event_manager.add_event(event_name)
                self.event_manager.add_participant(event_name, participant)

            self.refresh_event_list()
            QMessageBox.information(
                self, "Success", "Participants imported successfully!", QMessageBox.StandardButton.Ok)

        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Failed to read Excel file:\n{str(e)}")

    def export_participants(self):
        """Exports participant data to an Excel file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            if not file_path.endswith('.xlsx'):
                file_path += '.xlsx'
            try:
                self.event_manager.export_participants(file_path)
                QMessageBox.information(
                    self, "Success", "Participants exported successfully!", QMessageBox.StandardButton.Ok)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to export data to Excel file: {e}", QMessageBox.StandardButton.Ok)

    def refresh_event_list(self):
        """Refresh the event list in UI."""
        self.event_input.clear()
        for event_name in self.event_manager.events.keys():
            self.event_input.addItem(event_name)

    def on_event_selected(self):
        """Updates participant list when an event is selected."""
        event_name = self.event_input.currentText().strip()
        self.update_participant_list(event_name)

    def add_event(self):
        """Adds an event to the system."""
        event_name = self.event_input.currentText().strip()
        if event_name:
            self.event_manager.add_event(event_name)
            self.event_input.addItem(event_name)
            self.event_input.setCurrentText("")
        else:
            QMessageBox.warning(self, "Input Error",
                                "Event name cannot be empty")

    def add_participant(self):
        """Adds a participant to the selected event."""
        event_name = self.event_input.currentText().strip()
        details = self.participant_input.text().split(", ")

        if event_name and len(details) == 3:
            self.event_manager.add_participant(event_name, tuple(details))
            self.participant_input.clear()
            self.update_participant_list(event_name)
        else:
            QMessageBox.warning(self, "Input Error",
                                "Enter valid details: Name, Student ID, Status")

    def update_participant_list(self, event_name):
        """Displays the list of participants for the selected event."""
        self.participant_list.clear()
        if not event_name:
            return
        participants = self.event_manager.display_participants(event_name)
        unique_participants = set(participants)
        for participant in unique_participants:
            self.participant_list.addItem(
                f"{participant[0]} ({participant[2]})")

    def mark_as_attended(self):
        """Marks a participant as 'Attended'."""
        selected_participant = self.participant_list.currentItem()
        if selected_participant:
            name = selected_participant.text().split(" (")[0]
            self.event_manager.mark_participation(name, "Attended")
            self.update_participant_list(
                self.event_input.currentText().strip())

    def show_summary(self):
        """Displays a summary of total participants in each event."""
        summary = self.event_manager.generate_summary()
        msg = "\n".join(
            f"{event}: {count} participants" for event, count in summary.items())
        QMessageBox.information(
            self, "Event Summary", msg if msg else "No events available", QMessageBox.StandardButton.Ok)
