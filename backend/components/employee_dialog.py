from PyQt5 import QtWidgets
from UI.viewEmployeeDialog import Ui_EmployeeDialog
from UI.removeConfirmationDialog import Ui_removeConfirmationDialog
from utils import get_db_connection

def show_employee_dialog(parent, employee_id, populate_team_callback):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT employee_id, firstname, middlename, lastname, suffix, province, city, baranggay, zipcode, username, email, sickLeaves, casualLeaves, paidLeaves
            FROM Employee
            WHERE employee_id = %s
        """
        cursor.execute(query, (employee_id,))
        employee = cursor.fetchone()

        if employee:
            view_employee_dialog = QtWidgets.QDialog(parent)
            ui = Ui_EmployeeDialog()
            ui.setupUi(view_employee_dialog)

            # Fill the fields correctly
            full_name = f"{employee[1]} {employee[2]} {employee[3]}".replace("None", "").strip()
            full_address = f"{employee[5]}, {employee[6]}, {employee[7]}, {employee[8]}"

            ui.label_2.setText(full_name)  # Full Name
            ui.label_3.setText(employee[9])  # Username
            ui.label_5.setText(employee[10])  #emial
            ui.label_7.setText(full_address)# Full Address

            # Leave Details (Sick, Casual, Paid)
            ui.label_12.setText(str(employee[11]))  # Sick Leaves
            ui.label_13.setText(str(employee[12]))  # Casual Leaves
            ui.label_14.setText(str(employee[13]))  # Paid Leaves

            # Enlarge the leave numbers
            enlarged_font_style = "font-size: 100px; font-weight: bold;"
            ui.label_12.setStyleSheet(enlarged_font_style)
            ui.label_13.setStyleSheet(enlarged_font_style)
            ui.label_14.setStyleSheet(enlarged_font_style)

            # Connect the Remove Button (pass employee_id)
            ui.removeEmployeeBTN.clicked.connect(lambda: show_remove_confirmation(view_employee_dialog, employee_id, populate_team_callback))

            view_employee_dialog.setModal(True)
            view_employee_dialog.exec_()
        else:
            QtWidgets.QMessageBox.warning(parent, "Not Found", "Employee not found.")

    except Exception as e:
        print(f"[ERROR] Showing employee dialog: {e}")
        QtWidgets.QMessageBox.critical(parent, "Error", f"Failed to load employee:\n{e}")

    finally:
        cursor.close()
        conn.close()

def show_remove_confirmation(parent, employee_id, populate_team_callback):
    view_remove_confirmation = QtWidgets.QDialog(parent)
    ui = Ui_removeConfirmationDialog()
    ui.setupUi(view_remove_confirmation)

    # When Cancel is clicked
    ui.confirmationCancelBTN.clicked.connect(view_remove_confirmation.reject)

    # When Remove is clicked
    ui.confirmationRemoveBTN.clicked.connect(lambda: attempt_remove_employee(ui, view_remove_confirmation, parent, employee_id, populate_team_callback))

    view_remove_confirmation.setModal(True)
    view_remove_confirmation.exec_()

def attempt_remove_employee(ui, confirmation_dialog, parent, employee_id, populate_team_callback):
    password_entered = ui.confirmationLineEdit.text().strip()

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if password matches any manager's password
        cursor.execute("SELECT * FROM Manager WHERE password = %s", (password_entered,))
        manager = cursor.fetchone()

        if manager:
            # FIRST: Delete all leaves of this employee
            cursor.execute("DELETE FROM LeaveApplication WHERE employee_id = %s", (employee_id,))
            print(f"[DB] Deleted related LeaveApplications for employee_id {employee_id}")

            # THEN: Delete the employee
            cursor.execute("DELETE FROM Employee WHERE employee_id = %s", (employee_id,))
            conn.commit()

            QtWidgets.QMessageBox.information(parent, "Success", "Employee removed successfully.")
            confirmation_dialog.accept()
            parent.accept()

        else:
            QtWidgets.QMessageBox.warning(parent, "Incorrect Password", "The password you entered is incorrect.")

    except Exception as e:
        print(f"[ERROR] Removing employee: {e}")
        QtWidgets.QMessageBox.critical(parent, "Error", f"Failed to remove employee:\n{e}")

    finally:
        cursor.close()
        conn.close()
        populate_team_callback()
