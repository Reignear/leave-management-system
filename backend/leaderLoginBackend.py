from PyQt5 import QtWidgets
from UI.leaderLoginPage import Ui_leaderLoginWindow
from backend.leaderDashboardBackend import LeaderMainDashboard
from utils import get_db_connection

class LeaderLoginPage(QtWidgets.QMainWindow):
    def __init__(self, welcome_page):
        super().__init__()
        self.ui = Ui_leaderLoginWindow()
        self.ui.setupUi(self)

        self.welcome_page = welcome_page
        self.leader_dashboard = None

        self.ui.leaderBackBTN.clicked.connect(self.welcome_page.go_back_to_welcome)
        self.ui.LeaderLoginBTN.clicked.connect(self.verify_manager_login)

    def verify_manager_login(self):
        username = self.ui.LeaderUsername.text().strip()
        password = self.ui.LeaderPassword.text().strip()
        print(f"[LOGIN] Username: {username} | Password: {password}")

        if self.login_manager(username, password):
            print("[LOGIN] Database login successful.")
            self.show_leader_dashboard()
        else:
            print("[LOGIN] Database login failed.")
            self.show_error_message("Invalid username or password.")

    def login_manager(self, username, password):
        try:
            print("[DB] Connecting to database...")
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Manager WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            print(f"[DB] Query result: {result}")
            return result is not None
        except Exception as e:
            print(f"[ERROR] Login DB error: {e}")
            QtWidgets.QMessageBox.critical(self, "Database Error", f"An error occurred:\n{e}")
            return False
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    def show_leader_dashboard(self):
        print("[DASHBOARD] Initializing LeaderMainDashboard")
        self.leader_dashboard = LeaderMainDashboard(self.welcome_page)
        self.leader_dashboard.show()
        print("[DASHBOARD] Shown successfully")
        self.hide()

    def show_error_message(self, message):
        QtWidgets.QMessageBox.critical(self, "Login Failed", message)
