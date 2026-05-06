# =====================
# This class represents the "My Wish List" page of the application.
# It follows the Page Object Model (POM) pattern to separate
# the page locators and actions from the actual test cases.

from playwright.sync_api import Page


class WishListPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_wish_list = page.locator("h2:has-text('My Wish List')")

    def get_wish_list_page_header(self):
        """
        Returns the header element of the wish list page, if it exists.
        Useful for verifying that the user is on the correct page.
        """
        try:
            return self.header_wish_list
        except Exception as e:
            print(f"Error fetching wish list page header: {e}")
            return None


