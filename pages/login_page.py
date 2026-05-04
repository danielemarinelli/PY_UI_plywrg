from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):  # all locators will be inside the constructor
        self.page = page
        self.email_field = page.locator("#input-email")
        self.pw_field = page.locator("#input-password")
        self.login_btn = page.locator("input[type=submit]")
        self.warning_msg = page.locator(".alert")


    # ===== Action Methods =====
    # Each method represents a user interaction on the page

    def insert_email(self, email):
        """Insert email in the corresponding field"""
        try:
         self.email_field.fill(email)
        except Exception as e:
            print(f" Exception while filling 'email address': {e}")
            raise


    def insert_password(self,password):
        """Insert password in the corresponding field"""
        try:
            self.pw_field.fill(password)
        except Exception as e:
            print(f" Exception while filling 'password': {e}")
            raise

    def click_login_btn(self):
        """Click on the 'Login' button after inserting the credentials"""
        try:
            self.login_btn.click()
        except Exception as e:
            print(f" Exception while clicking 'Login': {e}")
            raise

    def warning(self):
        """Warn the user if invalid credentials"""
        try:
            return self.warning_msg
        except Exception as e:
            print(f" Exception while fetching 'Warning message': {e}")
            raise