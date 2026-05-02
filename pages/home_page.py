from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):  # all locators will be inside the constructor
        self.page = page
        self.myAccount_btn = page.locator(".hidden-xs").nth(2)  # MyAccount link
        self.register_link = page.get_by_text("Register")
        self.login_link = page.get_by_text("Login")
        self.search_field = page.locator("input[name='search']")
        self.btn_search = page.locator('#search button[type="button"]')

    # ===== Action Methods =====
    # Each method represents a user interaction on the page

    def click_myAccount(self):
        """Click on the 'My Account' link."""
        try:
            self.myAccount_btn.click()
        except Exception as e:
            print(f" Exception while clicking 'My Account': {e}")
            raise


    def click_registerForm(self):
        """Click on the 'Register' link under My Account."""
        try:
            self.register_link.click()
        except Exception as e:
            print(f" Exception while clicking 'Register': {e}")
            raise

    def click_login(self):
        """Click on the 'Login' link under My Account."""
        try:
            self.login_link.click()
        except Exception as e:
            print(f" Exception while clicking 'Login': {e}")
            raise
