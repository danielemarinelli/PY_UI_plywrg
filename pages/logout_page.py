
from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page: Page):  # all locators will be inside the constructor
        """
        Constructor to initialize the Playwright Page instance
        and define all locators present on the Logout page.
        """
        self.page = page

        # ===== Locators =====
        # Identifying elements on the My Account page.
        self.logout_msg_label = page.locator("#content p").nth(0)
        self.continue_btn = page.locator(".btn.btn-primary")

    def get_logout_heading_msg(self):
        """
        Returns the locator for the 'Logout' page heading.
        Can be used in test assertions to verify page visibility.
        """
        try:
            return self.logout_msg_label
        except Exception as e:
            print(f"Error returning Logout page heading: {e}")
            return None



    def click_continue(self):
        """
        Click the 'Continue' button after logging out.
        This typically redirects the user back to the Home Page.
        """
        try:
            self.continue_btn.click()
        except Exception as e:
            print(f" Exception while clicking 'Continue' button: {e}")
            raise

    def get_continue_button(self):
        """
        Return the Continue button locator.
        Useful for checking its visibility or state in test assertions.

        Example:
            expect(logout_page.get_continue_button()).to_be_visible()
        """
        try:
            return self.continue_btn
        except Exception as e:
            print(f" Exception while fetching 'Continue' button locator: {e}")
            return None


