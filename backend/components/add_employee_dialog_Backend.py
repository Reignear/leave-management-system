from PyQt5 import QtWidgets
from UI.addEmployeeDialog import Ui_AddEmployeeDialog
from utils import get_db_connection

def show_add_employee(parent, populate_team_callback):
    view_add_employee = QtWidgets.QDialog(parent)
    ui = Ui_AddEmployeeDialog()
    ui.setupUi(view_add_employee)

    ui.addBTN.clicked.connect(lambda: save_new_employee(ui, view_add_employee, populate_team_callback))

    view_add_employee.setModal(True)
    view_add_employee.exec_()

def save_new_employee(ui, dialog, populate_team_callback):
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
        QtWidgets.QMessageBox.warning(None, "Input Error", "Please fill in all required fields.")
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

        QtWidgets.QMessageBox.information(None, "Success", "New employee added successfully.")
        dialog.accept()

        populate_team_callback()  # Refresh team grid

    except Exception as e:
        print(f"[ERROR] Failed to add employee: {e}")
        QtWidgets.QMessageBox.critical(None, "Error", f"Failed to add employee:\n{e}")

    finally:
        cursor.close()
        conn.close()
