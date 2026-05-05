"""
Test Case: Address Book Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify user can edit and existing address book entry
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Click on left link: 'Modify your address book entries'.
7. Click on Edit button and fill all the mandatory fields
8. Click 'Continue' button
9. Verify confirmation message


Expected Result:
----------------
The user should be able to edit an address book

"""


"""
Test Case: Add New Address Book Functionality

===========================================
Test Steps
===========================================

Test Case 2: Verify user can add a new address book entry
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Click on left link: 'Modify your address book entries'.
7. Click on New Address button and fill all the mandatory fields
8. Click 'Continue' button
9. Verify confirmation message
10. Delete Address book


Expected Result:
----------------
The user should be able to add a new address book

"""

import time
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.myaccount_page import MyAccountPage
from config import Config  # Configuration file holding valid/invalid credentials


def test_user_edit_address_book(page):
    """
    Automated Test Case: Verify that a user can edit address book entry
    """

    # --- Step 1: URL is started with conftest.py file
    # --- Step 2: Create Page Object Instances ---
    home_page = HomePage(page)
    my_acc = MyAccountPage(page)

    # Data from Config.py file
    fn = Config.first_name
    ln = Config.last_name
    address = Config.address
    city = Config.city
    zipcode = Config.zipcode
    country = Config.country
    region = Config.region

    # --- Step 3: Navigate to Login Page ---
    home_page.click_myAccount()
    home_page.click_login()

    # --- Step 4: Insert valid user and password (fetched from Config.py file) ---
    login = LoginPage(page)
    login.insert_email(Config.valid_email)
    login.insert_password(Config.valid_password)
    # --- Step 5:
    login.click_login_btn()

    # --- Step 6
    my_acc.click_address_book()
    # --- Step 7
    my_acc.click_edit_address_btn()
    my_acc.insert_all_info_needed(fn,ln,address,city,zipcode,country,region)
    time.sleep(2)
    # --- Step 8
    my_acc.click_continue_btn()
    # --- Step 9 Validation
    expect(my_acc.get_confirmation_msg_for_address_book()).to_be_visible(timeout=2000)
    time.sleep(3)



def test_user_add_address_book_and_deletes_it(page):
    """
    Automated Test Case: Verify that a user can add address book entry and delete it
    """

    # --- Step 1: URL is started with conftest.py file
    # --- Step 2: Create Page Object Instances ---
    home_page = HomePage(page)
    my_acc = MyAccountPage(page)

    # Data from Config.py file
    fn = Config.first_name1
    ln = Config.last_name1
    address = Config.address1
    city = Config.city1
    zipcode = Config.zipcode1
    country = Config.country1
    region = Config.region1

    # --- Step 3: Navigate to Login Page ---
    home_page.click_myAccount()
    home_page.click_login()

    # --- Step 4: Insert valid user and password (fetched from Config.py file) ---
    login = LoginPage(page)
    login.insert_email(Config.valid_email)
    login.insert_password(Config.valid_password)
    # --- Step 5:
    login.click_login_btn()

    # --- Step 6
    my_acc.click_address_book()
    # --- Step 7
    my_acc.click_new_address_btn()
    my_acc.insert_all_info_needed(fn,ln,address,city,zipcode, country,region)
    time.sleep(2)
    # --- Step 8
    my_acc.click_continue_btn()
    # --- Step 9 Validation
    expect(my_acc.get_confirmation_msg_for_address_book()).to_be_visible(timeout=2000)
    time.sleep(3)
    # --- Step 10:
    my_acc.click_delete_address_btn()   # delete the address created previously















