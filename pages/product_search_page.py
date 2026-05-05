from playwright.sync_api import Page
from pages.product_page import ProductPage

class ProductSearchPage:
    """
    Page Object Model class for the Search Results Page.
    This class contains locators and methods to interact with and verify
    products displayed after performing a search.
    """
    def __init__(self, page: Page):  # all locators will be inside the constructor
        self.page = page
        self.all_products = page.locator(".caption a")  # List of all product links shown in the search results
        self.search_btn_ = page.locator("#button-search")
        # Header that appears on the search results page
        self.search_page_header = page.locator("#content h1", has_text="Search -")

        # ===== Page Header =====

    def get_search_results_page_header(self):
        """
        Returns the header element of the search results page, if it exists.
        Useful for verifying that the user is on the correct page.
        """
        try:
            return self.search_page_header
        except Exception as e:
            print(f"Error fetching search results page header: {e}")
            return None

    def search_button_visible(self):
        """blu search button on the left must be displayed on the search page"""
        try:
            return self.search_btn_    # return the locator where we can do verification
        except Exception as e:
            print(f" Exception while checking 'search button on page': {e}")
            raise

    # ===== Product Verification =====

    def is_product_present(self, product_name):
        """
        Checks whether a specific product is displayed on the search results page.

        param --> product_name: Name of the product to search for
        return --> Product element if it exists, otherwise None (not found)
        """
        try:
            count = self.all_products.count()
            for i in range(count):
                product = self.all_products.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    return product
        except Exception as e:
            print(f"Error while checking product is displayed: {e}")
        return None

        # ===== Product Selection =====

    def select_product(self, product_name):
            """
            Selects a product from the search results by its name and navigates to the Product Page.

            param  --> product_name: Name of the product to select
            return --> Instance of ProductPage if the product is found, otherwise None
            """
            try:
                count = self.all_products.count()
                for i in range(count):
                    product = self.all_products.nth(i)
                    title = product.text_content()
                    if title and title.strip() == product_name:
                        product.click()
                        return ProductPage(self.page)
                print(f"Product not found: {product_name}")
            except Exception as e:
                print(f"Error while selecting product: {e}")
            return None

            # ===== Product Count =====

    def get_product_count(self):
        """
        Returns the products found in the search results.

        return --> All locators of the products found
        """
        try:
            return self.all_products
        except Exception as e:
            print(f"Error while getting product count: {e}")
            return None
