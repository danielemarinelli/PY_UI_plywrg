
# =====================
# This class represents the "My Account" page of the application.
# It follows the Page Object Model (POM) pattern to separate
# the page locators and actions from the actual test cases.

from playwright.sync_api import Page

class MyAccountPage:
    def __init__(self, page: Page):  # all locators will be inside the constructor
        """
        Constructor to initialize the Playwright Page instance
        and define all locators present on the My Account page.
        """
        self.page = page

        # ===== Locators =====
        # Identifying elements on the My Account page.
        self.myAccount_label = page.locator("h2:has-text('My Account')")
        self.myOrders_label = page.get_by_text("My Orders")
        self.logout_btn = page.get_by_text("Logout").nth(1)

        # ===== Page Validation Methods =====

    def get_my_account_page_heading(self):
        """
        Returns the locator for the 'My Account' page heading.
        Can be used in test assertions to verify page visibility.
        """
        try:
            return self.myAccount_label
        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
            return None

    def get_my_orders_page_heading(self):
        """
        Returns the locator for the 'My Account' page heading.
        Can be used in test assertions to verify page visibility.
        """
        try:
            return self.myOrders_label
        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
            return None


# ===== Logout Action =====

    def click_logout(self):
        """
        Clicks on the 'Logout' link to log out the user.
        Returns an instance of the LogoutPage class
        to allow chained navigation in tests.

        """
        try:
            self.logout_btn.click()
            return LogoutPage(self.page)
        except Exception as e:
            print(f"Unable to click Logout link: {e}")
            raise e  # Re-raise the exception to fail the test intentionally
