
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
        self.post_code = page.locator("#input-postcode")
        self.country = page.locator("#input-country")
        self.region = page.locator("#input-zone")
        self.continue_btn = page.locator("input[type='submit']")
        self.confirmation_msg = page.locator("#account-address").locator("div").nth(0)
        self.edit_address_book_entry = page.locator(":text-is('Edit')")
        self.delete_address_book_entry = page.locator("a:has-text('Delete')").nth(1)
        self.new_address_book_btn = page.get_by_text("New Address")


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

    def insert_all_info_needed(self,fname,lname,address,city,zipcode,country,region):
        try:
            self.first_name.fill("")  # clear field
            self.first_name.fill(fname)
            self.last_name.fill("")  # clear field
            self.last_name.fill(lname)
            self.address1.fill("")  # clear field
            self.address1.fill(address)
            self.city.fill("")  # clear field
            self.city.fill(city)
            self.post_code.fill("")  # clear field
            self.post_code.fill(zipcode)
            self.country.select_option(label=country)
            self.region.select_option(label=region)
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

    def click_edit_address_btn(self):
        try:
            self.edit_address_book_entry.click()
        except Exception as e:
            print(f"Unable to click Edit button: {e}")
            raise e


    def click_delete_address_btn(self):
        try:
            self.delete_address_book_entry.click()
        except Exception as e:
            print(f"Unable to click Delete button: {e}")
            raise e


    def click_new_address_btn(self):
        try:
            self.new_address_book_btn.click()
        except Exception as e:
            print(f"Unable to click New Address button: {e}")
            raise e