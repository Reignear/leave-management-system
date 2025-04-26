# team_page.py
from backend.components.employee_dialog import show_employee_dialog
from utils import get_db_connection
from PyQt5 import QtWidgets, QtCore

def show_team(self):
    self.ui.dashboardStackedWidget.setCurrentWidget(self.ui.teamPage)

def show_add_employee(self):
    view_add_employee = QtWidgets.QDialog(self)
    ui = self.Ui_AddEmployeeDialog()
    ui.setupUi(view_add_employee)

    ui.addBTN.clicked.connect(lambda: self.save_new_employee(ui, view_add_employee))

    view_add_employee.setModal(True)
    view_add_employee.exec_()

def save_new_employee(self, ui, dialog):
    firstname = ui.addFirstname.text().strip()
    middlename = ui.addMiddlename.text().strip()
    lastname = ui.addLastname.text().strip()
    suffix = ui.addSuffix.text().strip()
    province = ui.addProvince.text().strip()
    city = ui.addCity.text().strip()
    barangay = ui.addBarangay.text().strip()
    zipcode = ui.addZipCode.text().strip()
    username = ui.addUsername.text().strip()
    email = ui.addEmail.text().strip()
    password = ui.addPassword.text().strip()

    if not (firstname and lastname and username and email and password):
        QtWidgets.QMessageBox.warning(self, "Input Error", "Please fill in all required fields.")
        return

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Employee (firstname, middlename, lastname, suffix, province, city, baranggay, zipcode, username, email, password, sickLeaves, casualLeaves, paidLeaves)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 5, 5, 5)
        """
        cursor.execute(query, (firstname, middlename, lastname, suffix, province, city, barangay, zipcode, username, email, password))
        conn.commit()

        QtWidgets.QMessageBox.information(self, "Success", "New employee added successfully.")
        dialog.accept()
        self.populate_team_tab()

    except Exception as e:
        print(f"[ERROR] Failed to add employee: {e}")
        QtWidgets.QMessageBox.critical(self, "Error", f"Failed to add employee:\n{e}")

    finally:
        cursor.close()
        conn.close()

def populate_team_tab(self):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT employee_id, firstname, middlename, lastname, email FROM Employee"
        cursor.execute(query)
        employees = cursor.fetchall()

        # Clear previous widgets
        for i in reversed(range(self.teamGridLayout.count())):
            widget_to_remove = self.teamGridLayout.itemAt(i).widget()
            self.teamGridLayout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

        row = 0
        col = 0
        for index, emp in enumerate(employees):
            employee_id, firstname, middlename, lastname, email = emp
            full_name = f"{firstname} {middlename} {lastname}".replace("None", "").strip()
            first_letter = firstname[0].upper() if firstname else "?"


            team_card = QtWidgets.QGroupBox()
            team_card.setFixedSize(361, 291)
            team_card.setStyleSheet("""
                QGroupBox {
                    border-style: solid;
                    border-radius: 10px;
                    background-color: white;
                }
            """)

            top_background = QtWidgets.QWidget(team_card)
            top_background.setGeometry(QtCore.QRect(0, 0, 361, 71))
            top_background.setStyleSheet("""
                background-color: #51158C;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            """)

            letter_bg = QtWidgets.QWidget(team_card)
            letter_bg.setGeometry(QtCore.QRect(110, 20, 141, 101))
            letter_bg.setStyleSheet("""
                background-color: white;
                border-radius: 20px;
            """)

            letter_inner = QtWidgets.QWidget(letter_bg)
            letter_inner.setGeometry(QtCore.QRect(10, 10, 120, 80))
            letter_inner.setStyleSheet("""
                background-color: #B163FF;
                border-radius: 10px;
            """)

            letter_label = QtWidgets.QLabel(letter_inner)
            letter_label.setGeometry(QtCore.QRect(10, 5, 100, 60))
            letter_label.setText(first_letter)
            letter_label.setAlignment(QtCore.Qt.AlignCenter)
            letter_label.setStyleSheet("font-size: 36pt; color: black; font-weight: bold;")

            name_label = QtWidgets.QLabel(team_card)
            name_label.setGeometry(QtCore.QRect(0, 120, 361, 41))
            name_label.setAlignment(QtCore.Qt.AlignCenter)
            name_label.setText(full_name)
            name_label.setStyleSheet("font-size: 14pt; font-weight: bold;")

            email_label = QtWidgets.QLabel(team_card)
            email_label.setGeometry(QtCore.QRect(0, 170, 361, 20))
            email_label.setAlignment(QtCore.Qt.AlignCenter)
            email_label.setText(email if email else "No Email")
            email_label.setStyleSheet("font-size: 10pt;")

            phone_label = QtWidgets.QLabel(team_card)
            phone_label.setGeometry(QtCore.QRect(0, 200, 361, 20))
            phone_label.setAlignment(QtCore.Qt.AlignCenter)
            phone_label.setText("Phone: N/A")
            phone_label.setStyleSheet("font-size: 10pt;")

            view_button = QtWidgets.QPushButton("View", team_card)
            view_button.setGeometry(QtCore.QRect(130, 240, 100, 30))
            view_button.setStyleSheet("""
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                font-size: 10pt;
            """)
            view_button.clicked.connect(lambda checked, eid=employee_id: show_employee_dialog(self, eid))
            
            self.teamGridLayout.addWidget(team_card, row, col)

            col += 1
            if col >= 3:
                col = 0
                row += 1

    except Exception as e:
        print(f"[ERROR] Loading team list: {e}")

    finally:
        cursor.close()
        conn.close()
    def show_employee_details(self, employee_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Employee WHERE employee_id = %s"
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()

            if employee:
                details = f"""
                ID: {employee[0]}
                Name: {employee[1]} {employee[2]} {employee[3]}
                Suffix: {employee[4]}
                Province: {employee[5]}
                City: {employee[6]}
                Barangay: {employee[7]}
                Zip Code: {employee[8]}
                Username: {employee[9]}
                Email: {employee[10]}
                """

                QtWidgets.QMessageBox.information(self, "Employee Details", details)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Employee not found.")

        except Exception as e:
            print(f"[ERROR] Showing employee details: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load details:\n{e}")

        finally:
            cursor.close()
            conn.close()
