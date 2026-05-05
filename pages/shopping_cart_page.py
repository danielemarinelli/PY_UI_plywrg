from playwright.sync_api import Page

class ShoppingCartPage:
    """
        Page Object Model for the Shopping Cart Page.
        This class contains web element locators and reusable methods
        to interact with the shopping cart page.
        """
    def __init__(self, page: Page):  # all locators will be inside the constructor
        self.page = page
        self.header = page.locator('#content h1')
        self.btn_checkout = page.locator("a.btn.btn-primary")
        # Locator for the total price in the cart summary section
        self.lbl_total_price = page.locator(
            "//*[@id='content']/div[2]/div/table//strong[text()='Total:']//following::td")


        # ===== Action Methods =====
    # Each method represents a user interaction on the page

    def check_label_page(self):
        """Check the 'Shopping Cart' label page."""
        try:
            self.header
        except Exception as e:
            print(f" Exception while checking 'Shopping Cart' label: {e}")
            raise

    def get_total_price(self):
        """
        Returns the total price element from the shopping cart.

        :return: Locator representing the total price element, or None if not found.
        """
        try:
            return self.lbl_total_price
        except Exception as e:
            print(f"Unable to retrieve total price: {e}")
            return None

    """  Check out functionality is not implemented
    def click_checkout(self):
        Click on the 'Checkout' button on Shopping Cart
        Clicks on the "Checkout" button and navigates to the Checkout Page.

        return --> Instance of the CheckoutPage class
        
        try:
            self.btn_checkout.click()
                return CheckoutPage(self.page)
            except Exception as e:
                print(f"Error clicking on checkout button: {e}")
                return None
"""





