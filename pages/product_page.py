from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):  # all locators will be inside the constructor
        self.page = page