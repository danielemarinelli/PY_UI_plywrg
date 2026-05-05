"""
Test Case: User Logout Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify Logout Page
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Click on the "Logout" link in the right sidebar.
7. Verify that the "Logout" page is displayed after successful logout.
8. Click on the "Continue" button.

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
from pages.logout_page import LogoutPage
from config import Config  # Configuration file holding valid/invalid credentials

# these custom markers are needed for grouping and are present in the pytest.ini file
@pytest.mark.regression
def test_user_logout(page):
    """
    Automated Test Case: Verify that a user can log out
    """

    # --- Step 1: URL is started with conftest.py file
    # --- Step 2: Create Page Object Instances ---
    home_page = HomePage(page)
    my_acc = MyAccountPage(page)
    logout = LogoutPage(page)

    # --- Step 3: Navigate to Login Page ---
    home_page.click_myAccount()
    home_page.click_login()

    # --- Step 4: Insert valid user and password (fetched from Config.py file) ---
    login = LoginPage(page)
    login.insert_email(Config.valid_email)
    login.insert_password(Config.valid_password)
    login.click_login_btn()

    # --- Step 6: Click the Logout button
    # Wait for the page to load completely after login
    time.sleep(3)
    my_acc.click_logout()
    lo = logout.get_logout_heading_msg()

    # --- Step 7: Validation
    time.sleep(1)
    expect(lo).to_be_visible(timeout=2000)
    expect(lo).to_have_text("You have been logged off your account. It is now safe to leave the computer.")
    expect(logout.get_continue_button()).to_be_visible()

    # --- Step 8: Click on 'Continue' button

    logout.click_continue()
    time.sleep(1)






