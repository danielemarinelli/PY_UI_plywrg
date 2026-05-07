"""
Test Case: User WishList Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify WishList Page
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Search IPOD  from the search bar and click the len
7. Click on the heart icon of the product
8. Verify that the wish list message appears
9. Click on MyAccount link on the top page
10. From the dropdown click on 'my account'
11. Click on the "Wish List" link in the right sidebar.
12. Verify that the products selected are displayed
13. Verify the total price of products is as expected
14. Remove the item from the wish list and verify the message displayed
15. Verify the empty wish list message
16. Click on the "Continue" button.

Expected Result:
----------------
The user should be able to select a product and insert and cancel it from the wish list .
"""

import time
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.myaccount_page import MyAccountPage
from config import Config  # Configuration file holding valid/invalid credentials
from pages.wish_list_page import WishListPage
from pages.product_search_page import ProductSearchPage


# these custom markers are needed for grouping and are present in the pytest.ini file
@pytest.mark.regression
@pytest.mark.sanity
def test_user_wishlist(page):
    """
    Automated Test Case: Verify that a user can log out
    """

    # --- Step 1: URL is started with conftest.py file
    # --- Step 2: Create Page Object Instances ---
    home_page = HomePage(page)
    my_acc = MyAccountPage(page)
    product_search_page = ProductSearchPage(page)
    wl = WishListPage(page)

    # --- Step 3: Navigate to Login Page ---
    home_page.click_myAccount()
    home_page.click_login()

    # --- Step 4: Insert valid user and password (fetched from Config.py file) ---
    login = LoginPage(page)
    login.insert_email(Config.valid_email)
    login.insert_password(Config.valid_password)
    # step 5:
    login.click_login_btn()
    # step 6:
    home_page.enter_product_name(Config.wish_list_product_search)
    home_page.click_search()
    # step 7:
    product_search_page.product_in_wish_list(Config.wish_list_product1)
    # step 8:
    expect(product_search_page.get_confirmation_msg_wish_list()).to_be_visible()
    # repeat step 7 for second product:
    product_search_page.product_in_wish_list(Config.wish_list_product2)
    # repeat step 8 for second product:
    expect(product_search_page.get_confirmation_msg_wish_list()).to_be_visible()
    # step 9:
    product_search_page.click_myAccount_link()
    # step 10:
    product_search_page.click_myAccount_dropdown()
    # step 11:
    my_acc.select_wish_list()
    # step 12:
    expect(wl.get_wish_list_page_header()).to_have_text("My Wish List")
    products_selected_for_wl = wl.get_products_in_wishlist()
    assert products_selected_for_wl == [Config.wish_list_product1, Config.wish_list_product2]
    # step 13:
    assert wl.get_total_price_products_in_wishlist() == Config.total_price_prod_in_wish_list
    time.sleep(3)
    # step 14:
    wl.get_row_count()
    wl.remove_products_from_wishlist()
    time.sleep(3)
    expect(wl.get_confirmation_msg_wish_list_updated_after_removing_products()).to_be_visible(timeout=2000)
    # step 15:
    expect(wl.empty_wish_list_msg()).to_have_text("Your wish list is empty.")
    # step 16:
    wl.user_perform_click_to_continue()
    expect(my_acc.get_my_account_page_heading()).to_be_visible(timeout=2000)







