"""
Test Case: Address Book Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify user can add address book entry and delete it
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Click on left link: 'Modify your address book entries'.
7. Fill all the mandatory fields
8. Click 'Continue' button
9. Verify confirmation message
10. Click on Delete button.

Expected Result:
----------------
The user should be able to add address book and erase it

"""

import time
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.myaccount_page import MyAccountPage
from config import Config  # Configuration file holding valid/invalid credentials


def test_user_login_valid_credentials(page):
    """
    Automated Test Case: Verify that a user can add address book entry and delete it
    """

    # --- Step 1: URL is started with conftest.py file
    # --- Step 2: Create Page Object Instances ---
    home_page = HomePage(page)
    my_acc = MyAccountPage(page)

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

    time.sleep(3)





