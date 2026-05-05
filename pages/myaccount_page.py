
# =====================
# This class represents the "My Account" page of the application.
# It follows the Page Object Model (POM) pattern to separate
# the page locators and actions from the actual test cases.

from playwright.sync_api import Page

from pages.logout_page import LogoutPage


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
        self.address_book_entry = page.locator("a:has-text('Modify your address book entries')")
        # locators to perform 'Edit Address' action
        self.first_name = page.locator("#input-firstname")
        self.last_name = page.locator("#input-lastname")
        self.address1 = page.locator("#input-address-1")
        self.city = page.locator("#input-city")
        self.country = page.locator("#input-country")
        self.region = page.locator("#input-zone")
        self.continue_btn = page.locator("input[type='submit']")
        self.confirmation_msg = page.locator("#account-address").locator("div").nth(0)
        self.delete_address_book_entry = page.locator("a:has-text('Delete')")


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

# ===== Insert Address Book Action =====

    """ Fill all the mandatory fields for Book Address"""
    def click_address_book(self):
        try:
            self.address_book_entry.click()
        except Exception as e:
            print(f"Unable to click Address Book link: {e}")
            raise e

    def insert_all_address_needed(self):
        try:
            self.first_name.fill("Phil")
            self.last_name.fill("Simpson")
            self.address1.fill("123 Main Street")
            self.city.fill("Roma")
            self.country.select_option("Italy")
            self.region.select_option("Pesaro e Urbino")
        except Exception as e:
            print(f"Unable to fill the Address Book fields: {e}")
            raise e


    def click_continue_btn(self):
        try:
            self.continue_btn.click()
        except Exception as e:
            print(f"Unable to click Continue button: {e}")
            raise e

    def get_confirmation_msg_for_address_book(self):
        try:
            return self.confirmation_msg
        except Exception as e:
            print(f"Unable to get confirmation message: {e}")
            raise e

    def click_delete_address_btn(self):
        try:
            self.delete_address_book_entry.click()
        except Exception as e:
            print(f"Unable to click Delete button: {e}")
            raise e

