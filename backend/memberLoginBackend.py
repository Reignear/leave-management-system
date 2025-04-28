from PyQt5 import QtWidgets
from UI.memberLoginPage import Ui_memberLoginWindow
from backend.memberDashboardBackend import MemberMainDashboard
from utils import get_db_connection

class MemberLoginPage(QtWidgets.QMainWindow):
    def __init__(self, welcome_page):
        super().__init__()
        self.ui = Ui_memberLoginWindow()
        self.ui.setupUi(self)

        # Reference to welcome page
        self.welcome_page = welcome_page
        self.member_dashboard = None

        # Connect buttons
        self.ui.memberBackBTN.clicked.connect(self.welcome_page.go_back_to_welcome)
        self.ui.MemberLoginBTN.clicked.connect(self.verify_member_login)

    def verify_member_login(self):
        username = self.ui.MemberUsername.text().strip()
        password = self.ui.MemberPassword.text().strip()
        print(f"[LOGIN] Username: {username} | Password: {password}")

        employee_data = self.login_member(username, password)
        if employee_data:
            print("[LOGIN] Database login successful.")
            self.show_member_dashboard(employee_data)
        else:
            print("[LOGIN] Database login failed.")
            self.show_error_message("Invalid username or password.")


    def login_member(self, username, password):
        try:
            print("[DB] Connecting to database...")
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Employee WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            print(f"[DB] Query result: {result}")
            if result:
                return {
                    "employee_id": result[0],
                    "firstname": result[1],
                    "middlename": result[2],
                    "lastname": result[3],
                    "suffix": result[4],
                    "province": result[5],
                    "city": result[6],
                    "baranggay": result[7],
                    "zipcode": result[8],
                    "username": result[9],
                    "email": result[10],
                    "password": result[11],
                    "sick_leaves": result[12],
                    "casual_leaves": result[13],
                    "paid_leaves": result[14],
                }
            else:
                return None
        except Exception as e:
            print(f"[ERROR] Login DB error: {e}")
            QtWidgets.QMessageBox.critical(self, "Database Error", f"An error occurred:\n{e}")
            return None
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass


    def show_member_dashboard(self, employee_data):
        print("[DASHBOARD] Initializing MemberMainDashboard")
        self.member_dashboard = MemberMainDashboard(self.welcome_page, employee_data)
        self.member_dashboard.show()
        print("[DASHBOARD] Shown successfully")
        self.hide()

    def show_error_message(self, message):
        QtWidgets.QMessageBox.critical(self, "Login Failed", message)
