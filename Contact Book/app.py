import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QInputDialog,
    QMessageBox,
    QFormLayout,
    QDialog,
)


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        if name not in self.contacts:
            self.contacts[name] = {
                "phone_number": phone_number,
                "email": email,
                "address": address,
            }
            self.show_message("Success", f"Contact {name} added successfully!")
        else:
            self.show_message("Duplicate Contact", f"Contact {name} already exists.")

    def view_contact_list(self):
        return self.contacts

    def search_contact(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details["phone_number"]:
                results.append((name, details))

        return dict(results)

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name]["phone_number"] = phone_number
            self.contacts[name]["email"] = email
            self.contacts[name]["address"] = address
            self.show_message("Success", f"Contact {name} updated successfully!")
        else:
            self.show_message("Contact Not Found", f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.show_message("Success", f"Contact {name} deleted successfully!")
        else:
            self.show_message("Contact Not Found", f"Contact {name} not found.")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()


class ContactListDialog(QDialog):
    def __init__(self, contacts):
        super().__init__()

        self.setWindowTitle("Contact List")
        self.setGeometry(200, 200, 400, 300)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 380, 280)
        self.display_contacts(contacts)

    def display_contacts(self, contacts):
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)

        header_labels = ["Name", "Phone Number", "Email", "Address"]
        self.table_widget.setColumnCount(len(header_labels))
        self.table_widget.setHorizontalHeaderLabels(header_labels)

        if isinstance(contacts, dict):
            contacts = contacts.items()

        for name, details in contacts:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)

            self.table_widget.setItem(row_position, 0, QTableWidgetItem(name))
            self.table_widget.setItem(
                row_position, 1, QTableWidgetItem(details["phone_number"])
            )
            self.table_widget.setItem(
                row_position, 2, QTableWidgetItem(details["email"])
            )
            self.table_widget.setItem(
                row_position, 3, QTableWidgetItem(details["address"])
            )


class ContactBookGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.contact_book = ContactBook()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Contact Book")
        self.label.setStyleSheet("font-size: 18px; color: #333; margin-bottom: 10px;")
        layout.addWidget(self.label)

        self.add_button = QPushButton("Add Contact")
        self.add_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.add_button.clicked.connect(self.add_contact)
        layout.addWidget(self.add_button)

        self.view_button = QPushButton("View Contact List")
        self.view_button.setStyleSheet("background-color: #3498db; color: white;")
        self.view_button.clicked.connect(self.view_contact_list)
        layout.addWidget(self.view_button)

        self.search_button = QPushButton("Search Contact")
        self.search_button.setStyleSheet("background-color: #e74c3c; color: white;")
        self.search_button.clicked.connect(self.search_contact)
        layout.addWidget(self.search_button)

        self.update_button = QPushButton("Update Contact")
        self.update_button.setStyleSheet("background-color: #f39c12; color: white;")
        self.update_button.clicked.connect(self.update_contact)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete Contact")
        self.delete_button.setStyleSheet("background-color: #c0392b; color: white;")
        self.delete_button.clicked.connect(self.delete_contact)
        layout.addWidget(self.delete_button)

        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.form_layout.addRow("Name:", self.name_input)

        self.phone_input = QLineEdit()
        self.form_layout.addRow("Phone Number:", self.phone_input)

        self.email_input = QLineEdit()
        self.form_layout.addRow("Email:", self.email_input)

        self.address_input = QLineEdit()
        self.form_layout.addRow("Address:", self.address_input)

        layout.addLayout(self.form_layout)

        self.setLayout(layout)
        self.setWindowTitle("Contact Book")

    def add_contact(self):
        name = self.name_input.text()
        phone_number = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        if name and phone_number and email and address:
            self.contact_book.add_contact(name, phone_number, email, address)
            self.clear_input_fields()
        else:
            self.show_message("Input Error", "Please fill in all fields.")

    def view_contact_list(self):
        contacts = self.contact_book.view_contact_list()
        dialog = ContactListDialog(contacts)
        dialog.exec_()

    def search_contact(self):
        keyword, ok_pressed = QInputDialog.getText(
            self, "Search Contact", "Enter name or phone number:"
        )
        if ok_pressed:
            results = self.contact_book.search_contact(keyword)
            self.display_contacts(results)

    def update_contact(self):
        name = self.name_input.text()
        phone_number = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        if name:
            self.contact_book.update_contact(name, phone_number, email, address)
            self.clear_input_fields()
        else:
            self.show_message(
                "Input Error", "Please enter the name of the contact to update."
            )

    def delete_contact(self):
        name = self.name_input.text()
        if name:
            self.contact_book.delete_contact(name)
            self.clear_input_fields()
        else:
            self.show_message(
                "Input Error", "Please enter the name of the contact to delete."
            )

    def display_contacts(self, contacts):
        # Displaying contacts in the main window is optional.
        pass

    def clear_input_fields(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()


def main():
    app = QApplication(sys.argv)

    # Set a formal color scheme
    app.setStyle("Fusion")

    window = ContactBookGUI()
    window.setGeometry(100, 100, 600, 400)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
