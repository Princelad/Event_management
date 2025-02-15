# College Event Management System

This is a College Event Management System built using PySide6 for the GUI and pandas for handling Excel files. The system allows users to manage events and participants, import participant data from Excel files, and mark attendance.

## Features

- **Event Management**: Add and manage events.
- **Participant Management**: Add participants to events with details such as name, student ID, and status.
- **Import from Excel**: Import participant data from Excel files.
- **Export to Excel**: Export participant data to Excel files.
- **Attendance Marking**: Mark participants as attended.
- **Summary**: View a summary of total participants in each event.

## Screenshots
### Start Screen
![Start Screen](images/Start.png)

### Main Screen
![Main Screen](images/Main.png)


## Requirements

- Python 3.6+
- PySide6==6.3.1
- pandas==1.3.3
- openpyxl==3.0.9

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Princelad/Event_management.git
    cd Event_management
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python src/main.py
    ```

2. The start screen will appear. Click "Enter" to go to the main event management window.

3. In the main window, you can:
    - Add events and participants.
    - Import participant data from an Excel file.
    - Mark participants as attended.
    - View a summary of total participants in each event.

### Sample Input

To add a participant, enter the details in the following format:
```
Name, Student ID, Status
```
For example:
```
Alice, 12xx123, Not Attended
```

## Project Structure

- [main.py](src/main.py): Entry point of the application.
- [event_manager.py](src/event_manager.py): Contains the [EventManager](src/event_manager.py) class for managing events and participants.
- [start_screen.py](src/ui/start_screen.py): Contains the [StartMenu](src/ui/start_screen.py) class for the start screen.
- [main_screen.py](src/ui/main_screen.py): Contains the [MainWindow](src/ui/main_screen.py) class for the main event management window.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
