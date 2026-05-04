"""
Test Case: User Registration Functionality

===========================================
Test Steps
===========================================

1. Open the application in the browser.
2. Navigate to the "My Account" menu and click on "Register".
3. Enter user details:
   - First Name
   - Last Name
   - Email
   - Telephone Number
   - Password and Confirm Password
4. Accept the Privacy Policy checkbox.
5. Click on the "Continue" button.
6. Verify that the account creation confirmation message is displayed.

Expected Result:
----------------
After submitting valid details, the system should display the message:
"Your Account Has Been Created!"
"""

import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utilities.random_data_util import RandomDataUtil


@pytest.mark.sanity
@pytest.mark.regression
def test_user_registration(page):
    """
    Automated Test Case: Verify that a new user can successfully register an account.
    """

    # --- Step 1: Create Page Object Instances ---
    home_page = HomePage(page)
    registration_page = RegisterPage(page)

    # --- Step 2: Navigate to Registration Page ---
    home_page.click_myAccount()
    home_page.click_registerForm()

    # --- Step 3: Generate Random Test Data ---
    # Using RandomDataUtil to generate random user details
    random_data = RandomDataUtil()
    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    phone = random_data.get_phone_number()
    password = random_data.get_password()

    # --- Step 4: Fill Registration Form ---
    registration_page.insert_firstname(first_name)
    registration_page.insert_lastname(last_name)
    registration_page.insert_email(email)
    registration_page.insert_telephone(phone)
    registration_page.insert_password(password)
    registration_page.insert_password_confirmation(password)

    # --- Step 5: Accept Privacy Policy and Submit ---
    registration_page.agree_policy()
    registration_page.click_continue_btn()

    # --- Step 6: Verify Account Creation Confirmation ---
    confirmation_msg = registration_page.verify_msg_displayed()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")
