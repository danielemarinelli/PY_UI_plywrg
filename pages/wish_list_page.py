# =====================
# This class represents the "My Wish List" page of the application.
# It follows the Page Object Model (POM) pattern to separate
# the page locators and actions from the actual test cases.

from playwright.sync_api import Page


class WishListPage:
    def __init__(self, page: Page):
        self.page = page
        self.header_wish_list = page.locator("h2:has-text('My Wish List')")
        self.wish_list_table = page.locator("table.table.table-bordered.table-hover")
        self.remove_product_icon = page.locator(".fa.fa-times")
        self.confirmation_msg_after_remove_products = page.locator(".alert.alert-success.alert-dismissible")
        self.empty_wish_list_displayed = page.get_by_text("Your wish list is empty.")
        self.continue_btn = page.locator("a.btn.btn-primary")


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

    def get_products_in_wishlist(self):
        """
        Returns the list of products in the wish list
        """
        try:
            rows = self.wish_list_table.locator("tr")
            #print(rows.count())
            prod_list=[]
            all_row_data = rows.all()
            for row in all_row_data[1:]:  # slicing the table and staring from row 1, print only Product Name column
                second_col = row.locator('td').nth(1).all_inner_texts()
                for text in second_col:
                    prod_list.append(text)  #list will contain the two products selected for wish_list
                #print(prod_list)
            return prod_list
        except Exception as e:
            print(f"Error fetching row count table: {e}")
            return None

    def get_total_price_products_in_wishlist(self):
        """
        Returns the total price of products in the wish list
        """
        try:
            rows = self.wish_list_table.locator("tr")  # tables rows locators
            # print(rows.count())
            prod_prices_list = []
            tot_price = 0
            all_row_data = rows.all()
            for row in all_row_data[1:]:  # slicing the table and staring from row 1, print only Price column
                fifth_col_unit_prices = row.locator('td').nth(4).all_inner_texts()
                #print(fifth_col_unit_prices)
                for price_text in fifth_col_unit_prices:
                    #print(price_text)
                    tot_price= tot_price + float(price_text.replace("$", ""))
                    prod_prices_list.append(price_text.replace("$",""))  # list will contain the two product prices in wish_list

            tp = "$"+str(tot_price).replace(".0","")
            return tp
        except Exception as e:
            print(f"Error fetching row count table: {e}")
            return None


    def get_row_count(self):
        """
        Returns the numbers of rows in the wish list page
        """
        try:
            rows = self.wish_list_table.locator("tr")
            print("rows --> ",rows.count())
            return rows.count()
        except Exception as e:
            print(f"Error fetching row count table: {e}")
            raise


    def remove_products_from_wishlist(self):
        """
        Removes products from wish list
        """
        try:
            self.remove_product_icon.nth(1).click()
            self.remove_product_icon.nth(1).click()
        except Exception as e:
            print(f"Error fetching row count table: {e}")
            raise


    def get_confirmation_msg_wish_list_updated_after_removing_products(self):
        """
        Returns the green confirmation message of wish list modification after remove products in form of locator , to do validations.

        """
        try:
            return self.confirmation_msg_after_remove_products
        except Exception as e:
            print(f"Error while getting confirmation message after removing products: {e}")
            return None


    def empty_wish_list_msg(self):
        """
        Returns the message of the empty wish list in form of locator , to do validations.

         """
        try:
            return self.empty_wish_list_displayed
        except Exception as e:
            print(f"Error while getting empty wish list message after removing all products: {e}")
            raise

    def user_perform_click_to_continue(self):
        """Click on the 'Continue' button after removing all products from wish list"""
        try:
            self.continue_btn.click()
        except Exception as e:
            print(f" Exception while clicking 'Continue': {e}")
            raise
