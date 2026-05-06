# =====================
# This class represents the "My Wish List" page of the application.
# It follows the Page Object Model (POM) pattern to separate
# the page locators and actions from the actual test cases.

from playwright.sync_api import Page


class WishListPage:
    def __init__(self, page: Page):
        self.page = page




