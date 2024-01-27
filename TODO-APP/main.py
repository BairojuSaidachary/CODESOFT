import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QCheckBox,
    QComboBox,
    QCalendarWidget,
    QDateTimeEdit,
    QMessageBox,
    QFileDialog,
    QDialog,
    QTextEdit,
)
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QDateTime, Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize an empty list to store tasks
        self.tasks = []

        # Initialize the user interface
        self.init_ui()

    def init_ui(self):
        # Task Entry
        self.task_entry = QLineEdit(self)
        self.task_entry.setPlaceholderText("Enter Task")

        # Priority ComboBox
        self.priority_combo = QComboBox(self)
        self.priority_combo.addItems(["Low", "Medium", "High"])
        self.priority_combo.setCurrentIndex(1)

        # Due Date
        self.due_date_edit = QDateTimeEdit(self)
        self.due_date_edit.setCalendarPopup(True)

        # Completed Checkbox
        self.completed_checkbox = QCheckBox("Completed", self)

        # Buttons
        self.add_button = QPushButton("Add Task", self)
        self.add_button.clicked.connect(self.add_task)

        self.edit_button = QPushButton("Edit Task", self)
        self.edit_button.clicked.connect(self.edit_task)

        self.remove_button = QPushButton("Remove Task", self)
        self.remove_button.clicked.connect(self.remove_task)

        self.clear_button = QPushButton("Clear All", self)
        self.clear_button.clicked.connect(self.clear_all_tasks)

        self.show_button = QPushButton("Show Tasks", self)
        self.show_button.clicked.connect(self.show_tasks)

        self.save_button = QPushButton("Save Tasks", self)
        self.save_button.clicked.connect(self.save_tasks)

        self.load_button = QPushButton("Load Tasks", self)
        self.load_button.clicked.connect(self.load_tasks)

        # Task Table
        self.task_table = QTableWidget(self)
        self.task_table.setColumnCount(5)
        self.task_table.setHorizontalHeaderLabels(
            ["Task", "Priority", "Due Date", "Completed", "Edit"]
        )
        self.task_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.task_table.verticalHeader().setVisible(False)

        # Layout
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.task_entry)
        form_layout.addWidget(self.priority_combo)
        form_layout.addWidget(QLabel("Due Date:"))
        form_layout.addWidget(self.due_date_edit)
        form_layout.addWidget(self.completed_checkbox)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.edit_button)
        buttons_layout.addWidget(self.remove_button)
        buttons_layout.addWidget(self.clear_button)
        buttons_layout.addWidget(self.show_button)
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.load_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.task_table)

        self.setLayout(main_layout)

        # Window settings
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("To-Do App")

    # Function to add a task to the list
    def add_task(self):
        task = self.task_entry.text().strip()
        priority = self.priority_combo.currentText()
        due_date = self.due_date_edit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        completed = self.completed_checkbox.isChecked()

        if task:
            self.tasks.append(
                {
                    "task": task,
                    "priority": priority,
                    "due_date": due_date,
                    "completed": completed,
                }
            )
            self.update_task_table()
            QMessageBox.information(self, "Task Added", f'Task "{task}" added.')
            self.clear_input_fields()
        else:
            QMessageBox.warning(self, "Empty Task", "Please enter a task.")

    # Function to edit a selected task
    def edit_task(self):
        selected_item = self.task_table.currentItem()
        if selected_item:
            row = selected_item.row()
            task_data = self.tasks[row]

            new_task = self.task_entry.text().strip()
            new_priority = self.priority_combo.currentText()
            new_due_date = self.due_date_edit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            new_completed = self.completed_checkbox.isChecked()

            task_data.update(
                {
                    "task": new_task,
                    "priority": new_priority,
                    "due_date": new_due_date,
                    "completed": new_completed,
                }
            )

            self.update_task_table()
            QMessageBox.information(self, "Task Edited", "Task has been edited.")
            self.clear_input_fields()
        else:
            QMessageBox.warning(
                self, "No Task Selected", "Please select a task to edit."
            )

    # Function to remove a selected task
    def remove_task(self):
        selected_item = self.task_table.currentItem()
        if selected_item:
            row = selected_item.row()
            task = self.tasks[row]["task"]
            del self.tasks[row]
            QMessageBox.information(self, "Task Removed", f'Task "{task}" removed.')
            self.update_task_table()
        else:
            QMessageBox.warning(
                self, "No Task Selected", "Please select a task to remove."
            )

    # Function to clear all tasks
    def clear_all_tasks(self):
        reply = QMessageBox.question(
            self,
            "Clear All Tasks",
            "Are you sure you want to clear all tasks?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.tasks.clear()
            self.update_task_table()
            QMessageBox.information(
                self, "All Tasks Cleared", "All tasks have been cleared."
            )
            self.clear_input_fields()

    # Function to display tasks in a dialog box
    def show_tasks(self):
        if not self.tasks:
            QMessageBox.information(self, "No Tasks", "No tasks in the list.")
        else:
            tasks_text = "\n".join(
                [
                    f"{i + 1}. {task['task']} (Priority: {task['priority']}, "
                    f"Due Date: {task['due_date']}, {'Completed' if task['completed'] else 'Not Completed'})"
                    for i, task in enumerate(self.tasks)
                ]
            )

            # Use a QTextEdit for better task display
            tasks_dialog = QDialog(self)
            tasks_dialog.setWindowTitle("Tasks")
            tasks_dialog.setGeometry(100, 100, 400, 300)

            text_edit = QTextEdit(tasks_dialog)
            text_edit.setPlainText(tasks_text)
            text_edit.setReadOnly(True)

            ok_button = QPushButton("OK", tasks_dialog)
            ok_button.clicked.connect(tasks_dialog.accept)

            dialog_layout = QVBoxLayout()
            dialog_layout.addWidget(text_edit)
            dialog_layout.addWidget(ok_button)

            tasks_dialog.setLayout(dialog_layout)

            tasks_dialog.exec_()

    # Function to save tasks to a file
    def save_tasks(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Tasks", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            with open(file_path, "w") as file:
                for task in self.tasks:
                    file.write(
                        f"{task['task']}|{task['priority']}|{task['due_date']}|{task['completed']}\n"
                    )
            QMessageBox.information(
                self, "Tasks Saved", "Tasks have been saved to the file."
            )

    # Function to load tasks from a file
    def load_tasks(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Load Tasks", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            with open(file_path, "r") as file:
                self.tasks = []
                for line in file:
                    task, priority, due_date, completed = line.strip().split("|")
                    self.tasks.append(
                        {
                            "task": task,
                            "priority": priority,
                            "due_date": due_date,
                            "completed": completed.lower() == "true",
                        }
                    )
            self.update_task_table()
            QMessageBox.information(
                self, "Tasks Loaded", "Tasks have been loaded from the file."
            )

    # Function to update the task table with the current task list
    def update_task_table(self):
        self.task_table.setRowCount(len(self.tasks))
        for row, task_data in enumerate(self.tasks):
            self.task_table.setItem(row, 0, QTableWidgetItem(task_data["task"]))
            self.task_table.setItem(row, 1, QTableWidgetItem(task_data["priority"]))
            self.task_table.setItem(row, 2, QTableWidgetItem(task_data["due_date"]))
            completed_item = QTableWidgetItem(
                "Completed" if task_data["completed"] else "Not Completed"
            )
            completed_item.setCheckState(2 if task_data["completed"] else 0)
            self.task_table.setItem(row, 3, completed_item)

            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(self.edit_selected_task)
            self.task_table.setCellWidget(row, 4, edit_button)

    # Function to edit a selected task from the table
    def edit_selected_task(self):
        button = self.sender()
        index = self.task_table.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            task_data = self.tasks[row]

            self.task_entry.setText(task_data["task"])
            self.priority_combo.setCurrentText(task_data["priority"])

            # Convert the string to a QDateTime object
            due_date = QDateTime.fromString(
                task_data["due_date"], "yyyy-MM-dd hh:mm:ss"
            )
            self.due_date_edit.setDateTime(due_date)

            self.completed_checkbox.setChecked(task_data["completed"])

    # Function to clear input fields
    def clear_input_fields(self):
        self.task_entry.clear()
        self.priority_combo.setCurrentIndex(1)
        self.due_date_edit.setDateTime(self.due_date_edit.minimumDateTime())
        self.completed_checkbox.setChecked(False)


def main():
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
