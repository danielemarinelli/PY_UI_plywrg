from playwright.sync_api import Page

class RegisterPage:
    def __init__(self, page: Page):  # all locators will be inside the constructor
        self.page = page
        self.first_name_field = page.locator("#input-firstname")
        self.last_name_field = page.locator("#input-lastname")
        self.email_field = page.locator("#input-email")
        self.phone_field = page.locator("#input-telephone")
        self.pw_field = page.locator("#input-password")
        self.pw_confirm_field = page.locator("#input-confirm")
        self.privacy_policy_radio_btn = page.locator("input[type='checkbox']")
        self.continue_btn = page.locator("input[type=submit]")
        self.register_displayed = page.locator("#content h1")


    # ===== Action Methods =====
    # Each method represents a user interaction on the page

    def insert_firstname(self, name):
        """Insert first name"""
        try:
            self.first_name_field.fill(name)
        except Exception as e:
            print(f" Exception while filling 'first name field': {e}")
            raise


    def insert_lastname(self, last_name):
        """Insert last name"""
        try:
            self.last_name_field.fill(last_name)
        except Exception as e:
            print(f" Exception while filling 'last name': {e}")
            raise

    def insert_email(self, email):
        """Insert Email"""
        try:
            self.email_field.fill(email)
        except Exception as e:
            print(f" Exception while filling 'Email': {e}")
            raise

    def insert_telephone(self,phone_number):
        """Insert Telephone"""
        try:
            self.phone_field.fill(phone_number)
        except Exception as e:
            print(f" Exception while filling 'telephone': {e}")
            raise

    def insert_password(self,pw):
        """Insert password"""
        try:
            self.pw_field.fill(pw)
        except Exception as e:
            print(f" Exception while filling 'password': {e}")
            raise

    def insert_password_confirmation(self,pw):
        """Insert password second time"""
        try:
            self.pw_confirm_field.fill(pw)
        except Exception as e:
            print(f" Exception while filling 'confirmation password': {e}")
            raise

    def agree_policy(self):
        """Agree policy clicking on radio button"""
        try:
            self.privacy_policy_radio_btn.click()
        except Exception as e:
            print(f" Exception while clicking 'privacy policy': {e}")
            raise

    def click_continue_btn(self):
        """click continue button"""
        try:
            self.continue_btn.click()
        except Exception as e:
            print(f" Exception while clicking 'continue': {e}")
            raise


    def verify_msg_displayed(self):
        """Register Account must be displayed"""
        try:
            msg = self.register_displayed.inner_text()
            print(msg)
            return msg
        except Exception as e:
            print(f" Exception while checking 'displayed label': {e}")
            raise