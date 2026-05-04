"""
Test Case: User Login Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify Login with Invalid Credentials
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter an invalid email address and password.
5. Click on the "Login" button.
6. Verify that an error message appears indicating invalid credentials.

Expected Result:
----------------
An error message should be displayed, and the user should not be logged in.


Test Case 2: Verify Login with Valid Credentials
------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Verify that the "My Account" page is displayed after successful login.

Expected Result:
----------------
The "My Account" page should appear, confirming a successful login.
"""

import time
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.myaccount_page import MyAccountPage
from config import Config  # Configuration file holding valid/invalid credentials

def test_user_login_invalid_credentials(page):
    """
    Automated Test Case: Verify that a user can't login with an invalid credentials
    """

    # --- Step 1: URL is started with conftest.py file
    # --- Step 2: Create Page Object Instances ---
    home_page = HomePage(page)

    # --- Step 3: Navigate to Login Page ---
    home_page.click_myAccount()
    home_page.click_login()

    # --- Step 4: Insert invalid user and password (fetched from Config.py file) ---
    login = LoginPage(page)
    login.insert_email(Config.invalid_email)
    login.insert_password(Config.invalid_password)
    login.click_login_btn()

    # --- Step 5: Verify that an error message appears indicating invalid credentials
    err_msg = login.warning()
    # text changes, so better not to perform verifications in text displayed
    #expect(err_msg).to_have_text("Warning: No match for E-Mail Address and/or Password.")
    expect(err_msg).to_be_visible(timeout=2000)
    time.sleep(2)


def test_user_login_valid_credentials(page):
    """
    Automated Test Case: Verify that a user can login with valid credentials
    """

    # --- Step 1: URL is started with conftest.py file
    # --- Step 2: Create Page Object Instances ---
    home_page = HomePage(page)
    my_acc = MyAccountPage(page)

    # --- Step 3: Navigate to Login Page ---
    home_page.click_myAccount()
    home_page.click_login()

    # --- Step 4: Insert invalid user and password (fetched from Config.py file) ---
    login = LoginPage(page)
    login.insert_email(Config.valid_email)
    login.insert_password(Config.valid_password)
    login.click_login_btn()

    # --- Step 5: Verify that the "My Account" page is displayed after successful login
    # Wait for the page to load completely after login
    time.sleep(3)
    expect(my_acc.get_my_account_page_heading()).to_be_visible(timeout=2000)  # ones logged My Account left label must be visible
    expect(my_acc.get_my_orders_page_heading()).to_be_visible()     # ones logged My Orders left abel must be visible






