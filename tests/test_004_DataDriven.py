
import time
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.myaccount_page import MyAccountPage
from playwright.sync_api import expect
from utilities.data_from_file_util import read_json_data, read_csv_data, read_excel_data

#Load/read the data from the test data files

csv_data=read_csv_data("testdata/logindata.csv")      # reading data from .csv file and returns it as List format
json_data=read_json_data("testdata/logindata.json")   # reading data from .json file and returns it as List format
excel_data=read_excel_data("testdata/logindata.xlsx") # reading data from .xlsx file and returns it as List format


#@pytest.mark.parametrize("testName,email,password,expected",json_data) #must specify the HEADERS/KEYS in the csv/json/xlsx file
#@pytest.mark.parametrize("testName,email,password,expected",csv_data)
@pytest.mark.parametrize("testName,email,password,expected",excel_data)
@pytest.mark.datadriven   # datadriven custom markers are needed for grouping and are present in the pytest.ini file
def test_login_data_driven(page,testName,email,password,expected):  # pass page + the 4 parameters to the function
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page=MyAccountPage(page)

    home_page.click_myAccount()
    home_page.click_login()

    login_page.insert_email(email)
    login_page.insert_password(password)
    login_page.click_login_btn()
    time.sleep(3)

    if expected=="success":    #the header expected is used to validate the test
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000) # valid credentials --> login ok --> test pass!
    else:
        expect(login_page.warning()).to_be_visible(timeout=3000)    # invalid credentials --> login ko --> test pass!
